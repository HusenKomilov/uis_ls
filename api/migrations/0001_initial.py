# Generated by Django 5.0.1 on 2024-01-25 15:22

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Author',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_ad', models.DateTimeField(auto_now_add=True, verbose_name='Yaratilgan vaqt')),
                ('updated_ad', models.DateTimeField(auto_now=True, verbose_name="O'zgartirilgan vaqt")),
                ('title', models.CharField(max_length=150, verbose_name='Muallif ismi')),
                ('image', models.ImageField(upload_to='authors/', verbose_name='Muallif rasmi')),
                ('description', models.TextField(verbose_name='Muallif haqida qisqacha')),
                ('content', models.TextField()),
                ('facebook_url', models.CharField(max_length=300, verbose_name='Facebook manzili')),
                ('twitter_url', models.CharField(max_length=300, verbose_name='Twitter manzili')),
                ('instagram_url', models.CharField(max_length=300, verbose_name='Instagram manzili')),
                ('pinterest_url', models.CharField(max_length=300, verbose_name='Pinterest manzili')),
                ('is_top', models.BooleanField(default=False, verbose_name='Top Muallifligi')),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_ad', models.DateTimeField(auto_now_add=True, verbose_name='Yaratilgan vaqt')),
                ('updated_ad', models.DateTimeField(auto_now=True, verbose_name="O'zgartirilgan vaqt")),
                ('title', models.CharField(max_length=200, verbose_name='Maqolalar kategoriyasi')),
                ('image', models.ImageField(upload_to='category/', verbose_name='Kategoriya rasmi')),
                ('count_post', models.IntegerField(default=0, verbose_name='Boglangan maqolalar soni')),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='ContactUs',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_ad', models.DateTimeField(auto_now_add=True, verbose_name='Yaratilgan vaqt')),
                ('updated_ad', models.DateTimeField(auto_now=True, verbose_name="O'zgartirilgan vaqt")),
                ('content', models.TextField()),
                ('facebook_url', models.CharField(max_length=300, verbose_name='Facebook manzili')),
                ('twitter_url', models.CharField(max_length=300, verbose_name='Twitter manzili')),
                ('instagram_url', models.CharField(max_length=300, verbose_name='Instagram manzili')),
                ('pinterest_url', models.CharField(max_length=300, verbose_name='Pinterest manzili')),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='ContactUsRequest',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_ad', models.DateTimeField(auto_now_add=True, verbose_name='Yaratilgan vaqt')),
                ('updated_ad', models.DateTimeField(auto_now=True, verbose_name="O'zgartirilgan vaqt")),
                ('name', models.CharField(max_length=200)),
                ('email', models.EmailField(max_length=254)),
                ('subject', models.CharField(max_length=250)),
                ('message', models.TextField()),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='FAQ',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_ad', models.DateTimeField(auto_now_add=True, verbose_name='Yaratilgan vaqt')),
                ('updated_ad', models.DateTimeField(auto_now=True, verbose_name="O'zgartirilgan vaqt")),
                ('question', models.CharField(max_length=300)),
                ('answer', models.TextField()),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='Tags',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_ad', models.DateTimeField(auto_now_add=True, verbose_name='Yaratilgan vaqt')),
                ('updated_ad', models.DateTimeField(auto_now=True, verbose_name="O'zgartirilgan vaqt")),
                ('title', models.CharField(max_length=250, verbose_name='Kichik teglar')),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='Post',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_ad', models.DateTimeField(auto_now_add=True, verbose_name='Yaratilgan vaqt')),
                ('updated_ad', models.DateTimeField(auto_now=True, verbose_name="O'zgartirilgan vaqt")),
                ('title', models.CharField(max_length=250)),
                ('image', models.ImageField(upload_to='', verbose_name='post/')),
                ('short_content', models.CharField(max_length=300)),
                ('content', models.TextField()),
                ('published_date', models.DateTimeField(auto_now_add=True)),
                ('read_min', models.CharField(max_length=200)),
                ('is_featured', models.BooleanField(default=False)),
                ('is_popular', models.BooleanField(default=False)),
                ('author', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='posts', to='api.author')),
                ('category', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='posts', to='api.category')),
                ('tags', models.ManyToManyField(related_name='posts', to='api.tags')),
            ],
            options={
                'abstract': False,
            },
        ),
    ]
