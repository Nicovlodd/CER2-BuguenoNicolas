# Generated by Django 4.2.6 on 2023-10-22 18:13

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Entidad',
            fields=[
                ('ID', models.BigAutoField(primary_key=True, serialize=False)),
                ('nombre', models.CharField(max_length=100)),
                ('logo', models.ImageField(upload_to='entidad_logos/')),
            ],
        ),
    ]
