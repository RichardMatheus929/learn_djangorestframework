# Generated by Django 5.0.6 on 2024-05-17 16:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('avaliacoes', '0001_initial'),
        ('core', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='pontoturistico',
            name='avaliacao',
            field=models.ManyToManyField(to='avaliacoes.avaliacoes'),
        ),
    ]
