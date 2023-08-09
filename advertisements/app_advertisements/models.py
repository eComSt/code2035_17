from django.db import models
from django.contrib import admin
from django.utils.html import format_html
from django.contrib.auth import get_user_model
User = get_user_model()

class Advertisements(models.Model):
    title = models.CharField('Заголовок',max_length=128)
    description = models.TextField('Описание')
    price = models.DecimalField('Цена',max_digits=10,decimal_places=2)
    #99 999 999.99
    auction = models.BooleanField('Торг',help_text = "Отметьте, если торг уместен")
    created_at = models.DateTimeField(auto_now_add = True)
    updated_at = models.DateTimeField(auto_now = True)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    image = models.ImageField('Изображение',upload_to='advertisements/')
    @admin.display(description="дата создания")
    def created_date(self):
        from django.utils import timezone
        if self.created_at.date()==timezone.now().date():
            created_time = self.created_at.time().strftime("%H:%M:%S")
            return format_html('<span style="color: green; font-weight: bold;">Сегодня в {}</span>', created_time)
        return self.created_at.strftime("%d.%m.%Y в %H:%M:%S")
    @admin.display(description="дата обновления")
    def updated_date(self):
        from django.utils import timezone
        if self.updated_at.date()==timezone.now().date():
            created_time = self.updated_at.time().strftime("%H:%M:%S")
            return format_html('<span style="color: red; font-weight: bold;">Сегодня в {}</span>', created_time)
        return self.created_at.strftime("%d.%m.%Y в %H:%M:%S")
    def __str__(self):
        return f"Advertisements:(id={self.id}, title={self.title}, price={self.price})"
    class Meta:
        db_table = 'advertisements'