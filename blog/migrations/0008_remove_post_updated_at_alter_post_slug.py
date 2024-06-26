# Generated by Django 5.0.6 on 2024-06-16 19:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0007_alter_post_categories'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='post',
            name='updated_at',
        ),
        migrations.AlterField(
            model_name='post',
            name='slug',
            field=models.SlugField(blank=True, editable=False, error_messages={'unique': 'A post with this slug already exists.'}, unique=True),
        ),
    ]
