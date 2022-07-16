from django.contrib.auth import get_user_model
from django.db import models


User = get_user_model()


class AbstractTimeStampModel(models.Model):
    """Дата создания"""
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        abstract = True


class Catering(AbstractTimeStampModel):
    """Общественное питание"""
    title = models.CharField(verbose_name='Название общественного питания', max_length=127)
    description = models.TextField(verbose_name='Описание общественного питания')
    logo = models.ImageField(verbose_name='Логотип общ питания', upload_to='./logo_caterings')
    address = models.CharField(verbose_name='Адрес общ питания', max_length=225)

    def __str__(self):
        return self.title

    class Meta:
        db_table = 'catering'
        verbose_name = 'Catering'
        verbose_name_plural = 'Caterings'


class BookCatering(AbstractTimeStampModel):
    """Бронь общ.питания"""
    user = models.ForeignKey(
        verbose_name='Пользователь', to=User,
        on_delete=models.CASCADE, related_name='book_users'
    )
    catering = models.ForeignKey(
        verbose_name='Общ.питание', to=Catering,
        on_delete=models.CASCADE, related_name='book_users'
    )
    date_book = models.DateField(verbose_name='Время брони')
