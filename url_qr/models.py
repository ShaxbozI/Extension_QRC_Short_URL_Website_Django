from django.db import models

import qrcode
from io import BytesIO
from django.core.files import File 
import base64

class Url_QR(models.Model):
    url_long = models.CharField(max_length = 300)
    url_short = models.CharField(max_length = 150, blank=True)
    qr_code = models.ImageField(upload_to='qr_codes', blank=True)
    create_at = models.DateField(auto_now_add=True)
    
    def save(self, *args, **kwargs):
        # QR kod yaratish
        qr_text = self.url_long
        qr_image = qrcode.make(qr_text, box_size=15)
        
        # File nomini kiritish
        file_name = f'qrc-{self.url_short}.png'
        
        # So'nggi holatini saqlash uchun yangi Image obyekti yaratish
        qr_image_pil = qr_image.get_image()
        stream = BytesIO()
        qr_image_pil.save(stream, format='PNG')
        
        qr_image_data = stream.getvalue()
        qr_image_base64 = base64.b64encode(qr_image_data).decode('utf-8')
        
        # QR kodni saqlas
        self.qr_code.save(file_name, File(stream), save=False)
        stream.close()
        
        super().save(*args, **kwargs)
        
        

