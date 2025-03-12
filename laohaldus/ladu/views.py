from django.shortcuts import render
from .models import Toode, ScanLog
import csv
from django.http import JsonResponse, HttpResponse
from reportlab.pdfgen import canvas
from django.contrib.auth.decorators import login_required
from django.shortcuts import get_object_or_404
from .models import Toode

def eksport_pdf(request):
    # Määrame HTTP vastuse PDF-faili tüüpi
    response = HttpResponse(content_type='application/pdf')
    response['Content-Disposition'] = 'attachment; filename="skaneerimise_logi.pdf"'

    # Loome PDF-i
    pdf = canvas.Canvas(response)
    pdf.setFont("Helvetica", 12)
    pdf.drawString(100, 800, "Skaneerimise Logi")
    
    logs = ScanLog.objects.filter(kasutaja=request.user).order_by('-skaneeritud_aeg')
    
    y = 780
    for log in logs:
        pdf.drawString(100, y, f"{log.toode.nimi} | {log.qr_kood} | {log.skaneeritud_aeg} | {log.kasutaja.username}")
        y -= 20

    pdf.showPage()
    pdf.save()

    return response

@login_required
def eksport_csv(request):
    # Määrame HTTP vastuse CSV-tüüpi
    response = HttpResponse(content_type='text/csv')
    response['Content-Disposition'] = 'attachment; filename="skaneerimise_logi.csv"'

    # Loome CSV kirjutaja
    writer = csv.writer(response)
    writer.writerow(['Toode', 'QR-kood', 'Skaneeritud aeg', 'Kasutaja'])

    # Lisame andmed CSV-faili
    logs = ScanLog.objects.filter(kasutaja=request.user).order_by('-skaneeritud_aeg')
    for log in logs:
        writer.writerow([log.toode.nimi, log.qr_kood, log.skaneeritud_aeg, log.kasutaja.username])

    return response

@login_required
def skaneerimise_logi(request):
    logid = ScanLog.objects.filter(kasutaja=request.user).order_by('-skaneeritud_aeg')
    return render(request, 'skaneerimise_logi.html', {'logid': logid})

def qr_scan(request):
    return render(request, 'qr_scan.html')

def skaneeri_qr(request, qr_kood):
    try:
        toode = get_object_or_404(Toode, partii_number=qr_kood)

        # Logime skaneerimise
        ScanLog.objects.create(
            kasutaja=request.user,
            qr_kood=qr_kood,
            toode=toode
        )

        return JsonResponse({
            'toode': toode.nimi,
            'kogus': toode.kogus,
            'aegumiskuupaev': toode.aegumiskuupaev.strftime('%Y-%m-%d')
        })
    except:
        return JsonResponse({'error': 'Toodet ei leitud'}, status=404)

from django.shortcuts import render
from django.utils.timezone import now, timedelta
from django.db.models import Count
from .models import Toode, ScanLog

def home(request):
    viimased_tooted = Toode.objects.order_by('-id')[:5]  # Viimased 5 toodet

    # Statistika viimase 8 tunni kohta
    current_time = now()
    last_8_hours = [current_time - timedelta(hours=i) for i in range(7, -1, -1)]  # Viimased 8 tundi järjestikuselt
    skaneerimised = ScanLog.objects.filter(
        skaneeritud_aeg__gte=last_8_hours[0]
    ).extra({'hour': "strftime('%%H', skaneeritud_aeg)"}).values('hour').annotate(count=Count('id')).order_by('hour')

    # Eeltäidame tühjad tunnid 0-ga
    data = {hour.strftime('%H:00'): 0 for hour in last_8_hours}
    for row in skaneerimised:
        data[f"{row['hour']}:00"] = row['count']

    return render(request, 'home.html', {
        'viimased_tooted': viimased_tooted,
        'scan_data': data
    })


def tooted(request):
    tooted = Toode.objects.all()
    return render(request, 'tooted.html', {'tooted': tooted})
