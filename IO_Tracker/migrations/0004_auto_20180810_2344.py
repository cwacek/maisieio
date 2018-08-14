# Generated by Django 2.0.7 on 2018-08-11 03:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('IO_Tracker', '0003_auto_20180810_2241'),
    ]

    operations = [
        migrations.AddField(
            model_name='io',
            name='poopFlag',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='io',
            name='urineFlag',
            field=models.BooleanField(default=False),
        ),
        migrations.AlterField(
            model_name='io',
            name='input_type',
            field=models.CharField(choices=[('TPN', 'TPN'), ('LIP', 'Lipids'), ('ENT', 'Enteral Feeds'), ('BOT', 'Bottle Feeds'), ('MED', 'Medications'), ('DIA', 'Diaper'), ('EME', 'Emesis'), ('GAS', 'Gastric Output')], default='TPN', max_length=3),
        ),
    ]