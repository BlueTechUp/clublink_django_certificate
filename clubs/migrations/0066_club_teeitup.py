# -*- coding: utf-8 -*-
# Generated by Django 1.10.3 on 2017-11-06 03:05
from __future__ import unicode_literals

from django.db import migrations, models
from django.contrib.contenttypes.models import ContentType
from django.contrib.auth.models import Permission
from django.contrib.auth.models import Group


def off_prem_group(apps, schema_editor):
    # We can't import the Person model directly as it may be a newer
    # version than this migration expects. We use the historical version.
    Certificate = apps.get_model('certificates', 'Certificate')

    content_type = ContentType.objects.get_for_model(Certificate)

    off_prem_perm, created = Permission.objects.get_or_create(
        name='Can login off premise',
        content_type=content_type,
        codename='can_login_off_premise')

    off_prem_group, created = Group._default_manager.get_or_create(
        name='Off-premise Access')

    off_prem_group.permissions.add(off_prem_perm)


class Migration(migrations.Migration):

    dependencies = [
        ('clubs', '0065_auto_20171105_1420'),
    ]

    operations = [
        migrations.AddField(
            model_name='club',
            name='teeitup',
            field=models.URLField(
                blank=True,
                help_text='What is the TeeItUp url for iframing?',
                null=True),
        ),
        migrations.RunPython(off_prem_group)
    ]