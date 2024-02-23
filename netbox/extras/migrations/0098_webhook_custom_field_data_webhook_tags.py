# Generated by Django 4.1.10 on 2023-08-01 16:32

from django.db import migrations, models
import taggit.managers
import utilities.json


class Migration(migrations.Migration):

    dependencies = [
        ('extras', '0097_customfield_remove_choices'),
    ]

    operations = [
        migrations.AddField(
            model_name='webhook',
            name='custom_field_data',
            field=models.JSONField(blank=True, default=dict, encoder=utilities.json.CustomFieldJSONEncoder),
        ),
        migrations.AddField(
            model_name='webhook',
            name='tags',
            field=taggit.managers.TaggableManager(through='extras.TaggedItem', to='extras.Tag'),
        ),
    ]