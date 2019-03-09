# -*- coding: utf-8 -*-
# Generated by Django 1.10.3 on 2017-03-06 08:09
# flake8: noqa
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('clubs', '0019_auto_20170302_1427'),
        ('certificates', '0027_certificatetype_hide_recipient_name'),
    ]

    operations = [
        migrations.AddField(
            model_name='certificate',
            name='club_secondary',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='certificates_secondary', to='clubs.Club'),
        ),
    ]
