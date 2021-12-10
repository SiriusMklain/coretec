# Generated by Django 4.0 on 2021-12-10 13:54

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='ProductCategory',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100, verbose_name='Имя категории')),
                ('brand', models.CharField(max_length=100, verbose_name='Бренд')),
            ],
            options={
                'verbose_name': 'Категория продукции',
                'verbose_name_plural': 'Категории продукции',
                'db_table': 'category_product',
                'ordering': ('name',),
            },
        ),
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=250, verbose_name='Имя комплектуещей')),
                ('quantity', models.IntegerField(verbose_name='Клличество')),
                ('category', models.ForeignKey(db_constraint='name', on_delete=django.db.models.deletion.CASCADE, to='production.productcategory', verbose_name='Категория')),
            ],
            options={
                'verbose_name': 'Комплектующия',
                'verbose_name_plural': 'Комплектующии',
                'db_table': 'product',
                'ordering': ('name',),
            },
        ),
    ]
