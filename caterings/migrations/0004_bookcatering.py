# Generated by Django 4.0.6 on 2022-07-16 06:25

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('caterings', '0003_alter_catering_options'),
    ]

    operations = [
        migrations.CreateModel(
            name='BookCatering',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('date_book', models.DateField(verbose_name='Время брони')),
                ('catering', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='book_users', to='caterings.catering', verbose_name='Общ.питание')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='book_users', to=settings.AUTH_USER_MODEL, verbose_name='Пользователь')),
            ],
            options={
                'abstract': False,
            },
        ),
    ]
