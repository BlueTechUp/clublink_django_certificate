# -*- coding: utf-8 -*-
# Generated by Django 1.10.3 on 2017-08-22 04:21
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('clubs', '0052_clubeventrsvp_custom_question_answer'),
    ]

    operations = [
        migrations.RenameField(
            model_name='clubeventrsvp',
            old_name='number_of_guests',
            new_name='number_of_adults',
        ),
        migrations.AddField(
            model_name='clubeventrsvp',
            name='number_of_children',
            field=models.IntegerField(default=0),
        ),
    ]
