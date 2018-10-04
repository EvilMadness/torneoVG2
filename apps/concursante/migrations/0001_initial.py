# Generated by Django 2.1.1 on 2018-10-04 20:11

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('carrera', '0001_initial'),
        ('personaje', '0001_initial'),
        ('escuela', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Concursante',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=30)),
                ('apaterno', models.CharField(max_length=30)),
                ('amaterno', models.CharField(max_length=30)),
                ('nickname', models.CharField(max_length=20)),
                ('password', models.CharField(max_length=100)),
                ('email', models.CharField(max_length=30)),
                ('id_carrera', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='carrera.Carrera')),
                ('id_escuela', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='escuela.Escuela')),
                ('id_personaje', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='personaje.Personaje')),
            ],
        ),
    ]
