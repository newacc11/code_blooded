# Generated by Django 2.2 on 2020-10-30 19:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('study_platform', '0002_auto_20201030_1911'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='class',
            options={'verbose_name': 'Класс', 'verbose_name_plural': 'Классы'},
        ),
        migrations.AddField(
            model_name='class',
            name='title',
            field=models.CharField(default=1, max_length=300),
            preserve_default=False,
        ),
    ]
