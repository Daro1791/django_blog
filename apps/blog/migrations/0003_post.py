# Generated by Django 5.0.1 on 2024-01-08 16:52

import ckeditor.fields
import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0002_alter_author_mail'),
    ]

    operations = [
        migrations.CreateModel(
            name='Post',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('title', models.CharField(max_length=100, verbose_name='Title')),
                ('slug', models.CharField(max_length=100, verbose_name='Slug')),
                ('description', models.CharField(max_length=150, verbose_name='Description')),
                ('content', ckeditor.fields.RichTextField()),
                ('image', models.ImageField(upload_to='images/')),
                ('state', models.BooleanField(default=True, verbose_name='Published/Unpublished')),
                ('creation_date', models.DateField(auto_now_add=True, verbose_name='Creation date')),
                ('author', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='blog.author')),
                ('category', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='blog.category')),
            ],
            options={
                'verbose_name': 'Post',
                'verbose_name_plural': 'Posts',
            },
        ),
    ]
