# Generated by Django 3.2.4 on 2021-07-10 17:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('stickers', '0007_alter_caixastickers_valor_total'),
    ]

    operations = [
        migrations.CreateModel(
            name='TotalStickers',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('total_vendidos', models.IntegerField()),
            ],
        ),
    ]