# Generated by Django 3.2.8 on 2022-01-03 16:22

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('products', '0002_auto_20211107_2337'),
    ]

    operations = [
        migrations.CreateModel(
            name='AddFavourites',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
            ],
        ),
        migrations.CreateModel(
            name='Favourites',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
                ('watches', models.ManyToManyField(related_name='favourites', through='favourites.AddFavourites', to='products.Product')),
            ],
        ),
        migrations.AddField(
            model_name='addfavourites',
            name='favourites',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='favourites.favourites'),
        ),
        migrations.AddField(
            model_name='addfavourites',
            name='watches',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='products.product'),
        ),
    ]