# Generated by Django 4.0 on 2022-02-12 19:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('suggestions', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='suggestion',
            name='user',
        ),
        migrations.AddField(
            model_name='suggestion',
            name='upvoters',
            field=models.TextField(blank=True, null=True),
        ),
    ]