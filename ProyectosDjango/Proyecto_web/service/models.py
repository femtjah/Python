from django.db import models


class Service(models.Model):
    title=models.CharField(max_length=50)
    content=models.CharField(max_length=50)
    img=models.ImageField(upload_to='service')
    created=models.DateTimeField(auto_now_add=True)
    updated=models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name='servicio'
        verbose_name_plural='servicios'

    def __str__(self):
        return self.title