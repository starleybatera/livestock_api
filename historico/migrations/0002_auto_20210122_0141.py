# Generated by Django 3.1.5 on 2021-01-22 01:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('historico', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='historico',
            name='descricao',
            field=models.CharField(max_length=255),
        ),
    ]