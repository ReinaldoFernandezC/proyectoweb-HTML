# Generated by Django 4.0.5 on 2022-07-01 04:40

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='categoria',
            fields=[
                ('idCategoria', models.IntegerField(primary_key=True, serialize=False, verbose_name='Id de categoria')),
                ('nombreCategoria', models.CharField(max_length=30, verbose_name='Nombre de la Categoria')),
            ],
        ),
        migrations.CreateModel(
            name='especie',
            fields=[
                ('idEspecie', models.IntegerField(primary_key=True, serialize=False, verbose_name='Id de la especie')),
                ('nombreEspecie', models.CharField(max_length=30, verbose_name='Nombre de la especie')),
            ],
        ),
        migrations.CreateModel(
            name='articulo',
            fields=[
                ('idArticulo', models.IntegerField(max_length=50, primary_key=True, serialize=False, verbose_name='numero de producto')),
                ('Precio', models.IntegerField(max_length=50, verbose_name='Precio ')),
                ('categoria', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='core.categoria')),
                ('especie', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='core.especie')),
            ],
        ),
    ]
