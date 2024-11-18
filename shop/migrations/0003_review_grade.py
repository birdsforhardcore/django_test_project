# Generated by Django 5.1.1 on 2024-10-08 04:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0002_alter_product_category_review'),
    ]

    operations = [
        migrations.AddField(
            model_name='review',
            name='grade',
            field=models.CharField(blank=True, choices=[('5', 'Отлично'), ('4', 'Хорошо'), ('3', 'Нормально'), ('2', 'Плохо'), ('1', 'Ужасно')], max_length=20, null=True, verbose_name='Оценка'),
        ),
    ]
