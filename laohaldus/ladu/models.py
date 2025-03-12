import qrcode
from io import BytesIO
from django.core.files.base import ContentFile
from django.db import models
from django.contrib.auth.models import User
from django.utils.timezone import now

class ScanLog(models.Model):
    kasutaja = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, blank=True)
    qr_kood = models.CharField(max_length=255)
    toode = models.ForeignKey('Toode', on_delete=models.CASCADE)
    skaneeritud_aeg = models.DateTimeField(default=now)

    def __str__(self):
        return f"{self.toode.nimi} skaneeritud {self.kasutaja} poolt {self.skaneeritud_aeg}"


class Tootekategooria(models.Model):
    nimi = models.CharField(max_length=255)

    def __str__(self):
        return self.nimi

class Toode(models.Model):
    nimi = models.CharField(max_length=255)
    kategooria = models.ForeignKey(Tootekategooria, on_delete=models.CASCADE)  
    partii_number = models.CharField(max_length=100, unique=True)
    kogus = models.PositiveIntegerField(default=0)
    aegumiskuupaev = models.DateField()
    pilt = models.ImageField(upload_to='toote_pildid/', blank=True, null=True) 
    qr_kood = models.ImageField(upload_to="qr_codes", blank=True, null=True)

    def __str__(self):
        return f"{self.nimi} ({self.partii_number})"

    def save(self, *args, **kwargs):
        if not self.qr_kood:
            qr = qrcode.make(self.partii_number)
            buffer = BytesIO()
            qr.save(buffer, format="PNG")
            filename = f"qr_{self.partii_number}.png"
            self.qr_kood.save(filename, ContentFile(buffer.getvalue()), save=False)
        super().save(*args, **kwargs)
