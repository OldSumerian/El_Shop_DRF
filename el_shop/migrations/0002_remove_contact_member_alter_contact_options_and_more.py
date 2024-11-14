# Generated by Django 5.1.3 on 2024-11-14 14:19

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('el_shop', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='contact',
            name='member',
        ),
        migrations.AlterModelOptions(
            name='contact',
            options={'verbose_name': 'контакт', 'verbose_name_plural': 'контакты'},
        ),
        migrations.AlterModelOptions(
            name='product',
            options={'ordering': ['name', 'release_date'], 'verbose_name': 'продукт', 'verbose_name_plural': 'продукты'},
        ),
        migrations.AlterField(
            model_name='contact',
            name='city',
            field=models.CharField(blank=True, max_length=50, null=True, verbose_name='Город'),
        ),
        migrations.AlterField(
            model_name='contact',
            name='country',
            field=models.CharField(blank=True, max_length=50, null=True, verbose_name='Страна'),
        ),
        migrations.AlterField(
            model_name='contact',
            name='email',
            field=models.EmailField(blank=True, max_length=254, null=True, verbose_name='Почта'),
        ),
        migrations.AlterField(
            model_name='contact',
            name='house_number',
            field=models.CharField(blank=True, max_length=10, null=True, verbose_name='Номер дома'),
        ),
        migrations.AlterField(
            model_name='contact',
            name='street',
            field=models.CharField(blank=True, max_length=50, null=True, verbose_name='Улица'),
        ),
        migrations.AlterField(
            model_name='product',
            name='model',
            field=models.CharField(blank=True, max_length=100, null=True, verbose_name='Модель'),
        ),
        migrations.AlterField(
            model_name='product',
            name='name',
            field=models.CharField(blank=True, max_length=150, null=True, verbose_name='Наименование продукта'),
        ),
        migrations.AlterField(
            model_name='product',
            name='selling_price',
            field=models.DecimalField(decimal_places=2, default=0.0, max_digits=12),
        ),
        migrations.CreateModel(
            name='NetElement',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=300, unique=True, verbose_name='Название')),
                ('level', models.IntegerField(choices=[(0, 0), (1, 1), (2, 2)], verbose_name='Уровень в сети')),
                ('debt', models.DecimalField(decimal_places=2, default=0.0, max_digits=12, verbose_name='Задолженность перед поставщиком')),
                ('date_of_creation', models.DateTimeField(auto_now_add=True, verbose_name='Время создания')),
                ('supplier', models.ForeignKey(blank=True, default=None, null=True, on_delete=django.db.models.deletion.SET_DEFAULT, to='el_shop.netelement', verbose_name='Поставщик')),
            ],
            options={
                'verbose_name': 'сетевой элемент',
                'verbose_name_plural': 'сетевые элементы',
                'ordering': ['level'],
                'abstract': False,
            },
        ),
        migrations.AddField(
            model_name='contact',
            name='base_class',
            field=models.OneToOneField(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='el_shop.netelement'),
        ),
        migrations.AlterField(
            model_name='product',
            name='owner',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='el_shop.netelement'),
        ),
        migrations.DeleteModel(
            name='Node',
        ),
    ]
