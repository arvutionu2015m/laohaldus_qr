# **Projekt: Laohaldussüsteem QR-koodide ja Partii Jälgimisega**  

### **Ülevaade**  
See projekt on **QR-koodidega varustatud laohaldussüsteem**, mis võimaldab hallata **tooteid, partiisid ja aegumiskuupäevi**. Süsteem pakub **skaneerimisvõimalusi, dünaamilist lao jälgimist ja ekspordifunktsioone**. 

---

## **Funktsioonid ja Peamised Omadused**  

### ✅ **Toodete ja Partii Jälgimine**  
- Tooteid saab **lisada, muuta ja kustutada** Django admin-paneelis.  
- Igal tootel on **pilt, QR-kood, partii number ja aegumiskuupäev**.  
- **Automaatne QR-koodi genereerimine**, et lihtsustada partii jälgimist.

### ✅ **QR-koodide Skaneerimine ja Logimine**  
- **Veebipõhine QR-skanner**, mis kasutab **JavaScripti ja `html5-qrcode`** teeki.  
- **Füüsiliste QR-skannerite tugi**, mis registreerib andmed süsteemi.  
- **Skaneerimiste logi**, mis salvestab **kasutaja, QR-koodi ja aja**.

### ✅ **Statistika ja Graafikud**  
- **Viimati lisatud tooted** on nähtavad avalehel.  
- **QR-koodide skaneerimise aktiivsus viimase 8 tunni jooksul** on **Chart.js graafikuna**.  
- **Dünaamilised graafikud**, mis annavad ülevaate skaneerimiste sagedusest.

### ✅ **Andmete Ekspordi Funktsioonid**  
- **Ekspordi CSV** – võimaldab salvestada skaneerimiste logi Exceli jaoks.  
- **Ekspordi PDF** – võimaldab alla laadida logid arhiveerimiseks ja printimiseks.  

---

## **Tehnoloogiad ja Raamistikud**  

- **Backend:** Python, Django, Django-admin  
- **Frontend:** Bootstrap 4, HTML, CSS, JavaScript  
- **Andmebaas:** SQLite (või laiendatav PostgreSQL, MySQL)  
- **Graafikud:** Chart.js  
- **QR-koodide genereerimine:** Python `qrcode` teek  
- **QR-skaneerimine:** `html5-qrcode` JavaScripti teek  
- **Failihaldus:** Meediafailide üleslaadimine Django kaudu  

---

## **Töövoog ja Kasutajakogemus**  

1. **Administraator** logib süsteemi sisse ja lisab **uue toote** (pilt, kogus, partii, QR-kood).  
2. **Lao töötaja** saab skaneerida QR-koodi **mobiilseadme või füüsilise skanneriga**.  
3. Skaneerimise andmed salvestatakse **logisse ja analüüsitakse graafikuna**.  
4. Administraator saab **ekspordida andmeid CSV või PDF-vormingus**.  

---

## **Edasised Täiendused ja Parendused**  
🔹 **Automaatne lao vähendamine pärast skaneerimist**  
🔹 **Mobiiliäpi integreerimine API kaudu**  
🔹 **Teavitused (nt kui toode hakkab aeguma)**  
🔹 **Kasutajaõiguste süsteem erinevatele rollidele**  

---

## **Järeldus**  
See **laohaldussüsteem** on **moodne, kiire ja efektiivne lahendus laoseisu jälgimiseks**. Tänu **QR-koodidele ja dünaamilistele aruannetele** saab **kasutaja reaalajas jälgida varusid, hallata partiisid ja optimeerida lao töövoogu**. 🚀  
