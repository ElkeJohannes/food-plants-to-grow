# Generated by Django 4.0 on 2021-12-23 19:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('plants', '0003_plant_layer_alter_plant_stock'),
    ]

    operations = [
        migrations.AlterField(
            model_name='plant',
            name='Layer',
            field=models.CharField(choices=[('Large tree', 'Large tree'), ('Medium tree', 'Medium tree'), ('Small tree', 'Small tree'), ('Shrub', 'Shrub'), ('Ground cover', 'Ground cover'), ('Climber', 'Climber'), ('Root', 'Root')], max_length=100),
        ),
    ]