# Generated by Django 4.0 on 2022-01-12 14:54

from django.db import migrations
import django_countries.fields


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0003_alter_users_billing_country_and_more'),
    ]

    operations = [
        migrations.RenameField(
            model_name='users',
            old_name='billing_county',
            new_name='county',
        ),
        migrations.RenameField(
            model_name='users',
            old_name='billing_postcode',
            new_name='postcode',
        ),
        migrations.RenameField(
            model_name='users',
            old_name='billing_street_address1',
            new_name='street_name',
        ),
        migrations.RenameField(
            model_name='users',
            old_name='billing_street_address2',
            new_name='street_number',
        ),
        migrations.RenameField(
            model_name='users',
            old_name='billing_town_or_city',
            new_name='town_or_city',
        ),
        migrations.RemoveField(
            model_name='users',
            name='billing_country',
        ),
        migrations.RemoveField(
            model_name='users',
            name='shipping_country',
        ),
        migrations.RemoveField(
            model_name='users',
            name='shipping_county',
        ),
        migrations.RemoveField(
            model_name='users',
            name='shipping_postcode',
        ),
        migrations.RemoveField(
            model_name='users',
            name='shipping_street_address1',
        ),
        migrations.RemoveField(
            model_name='users',
            name='shipping_street_address2',
        ),
        migrations.RemoveField(
            model_name='users',
            name='shipping_town_or_city',
        ),
        migrations.AddField(
            model_name='users',
            name='country',
            field=django_countries.fields.CountryField(blank=True, max_length=2, null=True),
        ),
    ]
