# Generated by Django 3.2.9 on 2021-11-26 19:13

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('personas', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Domicilio',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('calle', models.CharField(help_text='ej: san martin', max_length=255, null=1)),
                ('nro_calle', models.IntegerField(help_text='ej: 1757', null=1)),
                ('pais', models.CharField(help_text='ej: arg', max_length=255, null=1)),
            ],
        ),
        migrations.AddField(
            model_name='persona',
            name='domicilio',
            field=models.ForeignKey(null=1, on_delete=django.db.models.deletion.SET_NULL, to='personas.domicilio'),
            preserve_default=1,
        ),
    ]
