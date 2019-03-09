# Generated by Django 2.0.2 on 2018-03-07 22:36

from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('clubs', '0081_auto_20171227_0033'),
    ]

    operations = [
        migrations.CreateModel(
            name='EventSeries',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created', models.DateTimeField(default=django.utils.timezone.now)),
            ],
        ),
        migrations.AddField(
            model_name='clubevent',
            name='event_series',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.PROTECT, related_name='event_series', to='clubs.EventSeries'),
        ),
    ]
