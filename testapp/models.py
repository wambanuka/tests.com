from django.conf import settings
from django.db import models
from django.utils import timezone

class Test(models.Model):  #модель тест - содержит заголовок, описание, категорию и картинку
    title = models.CharField(max_length=200)
    text = models.TextField()
    category = models.CharField (max_length=200)
    image = models.ImageField(upload_to=None, height_field=None, width_field=None, max_length=100)
   
# метод
 #   def publish(self):
 #       self.published_date = timezone.now()
 #      self.save()

    def __str__(self):
        return self.title
# Create your models here.
#справка
#models.CharField — так мы определяем текстовое поле с ограничением на количество символов.
#models.TextField — так определяется поле для неограниченно длинного текста. Выглядит подходящим для содержимого поста, верно?
#models.DateTimeField — дата и время.
#models.ForeignKey — ссылка на другую модель.