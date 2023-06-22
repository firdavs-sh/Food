# Generated by Django 3.0.8 on 2023-02-26 06:57

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='XizmatTuri',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('xizmat_nomi', models.CharField(max_length=200)),
                ('ctime', models.DateTimeField(auto_now_add=True)),
            ],
        ),
        migrations.CreateModel(
            name='XizmatVaqti',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('xizmatvaqti', models.CharField(max_length=200)),
                ('ctime', models.DateTimeField(auto_now_add=True)),
            ],
        ),
        migrations.CreateModel(
            name='Xizmatlar',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('rasm', models.ImageField(upload_to='media/rasmlar')),
                ('xizmat', models.CharField(max_length=200)),
                ('narxi', models.FloatField()),
                ('davomiyligi', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='restaurants.XizmatVaqti')),
                ('xturi', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='restaurants.XizmatTuri')),
            ],
        ),
        migrations.CreateModel(
            name='Restaurant',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=120)),
                ('image', models.ImageField(upload_to='restaurants/')),
                ('categories', models.CharField(max_length=120)),
                ('location', models.CharField(max_length=120)),
                ('narxi', models.IntegerField()),
                ('aloqa', models.CharField(max_length=150)),
                ('details', models.TextField()),
                ('slug', models.SlugField(blank=True, unique=True)),
                ('views', models.IntegerField(blank=True, default=0)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('is_active', models.BooleanField(default=True)),
                ('likes', models.ManyToManyField(blank=True, related_name='post_likes', to=settings.AUTH_USER_MODEL)),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='IshBeruvchi',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('rasm', models.ImageField(upload_to='media/rasmlar')),
                ('xizmat', models.CharField(max_length=200)),
                ('narxi', models.CharField(max_length=200)),
                ('telefon', models.CharField(max_length=12)),
                ('telegram', models.CharField(max_length=50)),
                ('muddat', models.DateField()),
                ('ctime', models.DateTimeField(auto_now_add=True)),
                ('davomiyligi', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='restaurants.XizmatVaqti')),
                ('xturi', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='restaurants.XizmatTuri')),
            ],
        ),
        migrations.CreateModel(
            name='Comment',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('text', models.TextField(max_length=500)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('post', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='comments', to='restaurants.Restaurant')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
