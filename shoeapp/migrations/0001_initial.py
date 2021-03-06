# Generated by Django 3.0.7 on 2020-06-16 16:12

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Manufacturer',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('website', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='ShoeColor',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('color_name', models.CharField(choices=[('R', 'Red'), ('O', 'Orange'), ('G', 'Green'), ('B', 'Blue'), ('I', 'Indigo'), ('V', 'Violet'), ('W', 'White'), ('BL', 'Black')], default='BL', max_length=2)),
            ],
        ),
        migrations.CreateModel(
            name='ShoeType',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('style', models.CharField(max_length=30)),
            ],
        ),
        migrations.CreateModel(
            name='Shoes',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('size', models.IntegerField(default=0)),
                ('brand', models.CharField(max_length=30)),
                ('name', models.CharField(max_length=50)),
                ('material', models.CharField(max_length=30)),
                ('fasten_type', models.CharField(max_length=30)),
                ('color', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='shoeapp.ShoeColor')),
                ('manufacturer', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='shoeapp.Manufacturer')),
                ('shoe_type', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='shoeapp.ShoeType')),
            ],
        ),
    ]
