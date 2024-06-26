# Generated by Django 4.0.3 on 2024-04-13 20:33

import autoslug.fields
import ckeditor.fields
from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('blog', '0002_alter_category_model_options_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='writing_model',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.ImageField(upload_to='writing_images')),
                ('title', models.CharField(max_length=30)),
                ('content', ckeditor.fields.RichTextField()),
                ('slug', autoslug.fields.AutoSlugField(editable=False, populate_from='title', unique=True)),
                ('categories', models.ManyToManyField(related_name='writing', to='blog.category_model')),
                ('writer', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='writings', to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name': 'writing',
                'verbose_name_plural': 'writings',
                'db_table': 'writing',
            },
        ),
    ]
