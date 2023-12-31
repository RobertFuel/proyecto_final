# Generated by Django 4.2.5 on 2023-10-07 11:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tareas', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Curso',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=100)),
            ],
        ),
        migrations.AddField(
            model_name='tarea',
            name='curso',
            field=models.PositiveSmallIntegerField(choices=[(1, 'Inglés'), (2, 'Francés'), (3, 'Español')], default=1),
        ),
    ]
