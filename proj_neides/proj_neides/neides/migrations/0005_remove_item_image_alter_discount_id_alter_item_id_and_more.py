# Generated by Django 5.1.1 on 2024-11-29 11:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('neides', '0004_item_image'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='item',
            name='image',
        ),
        migrations.AlterField(
            model_name='discount',
            name='id',
            field=models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID'),
        ),
        migrations.AlterField(
            model_name='item',
            name='id',
            field=models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID'),
        ),
        migrations.AlterField(
            model_name='sale',
            name='id',
            field=models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID'),
        ),
    ]