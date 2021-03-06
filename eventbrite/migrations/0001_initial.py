# Generated by Django 2.1.4 on 2018-12-06 11:41

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Event',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(blank=True, max_length=1000, null=True)),
                ('start', models.DateTimeField(blank=True, db_index=True, null=True)),
                ('min_ticket_cost', models.IntegerField(db_index=True, default=0)),
                ('external_id', models.BigIntegerField()),
                ('organizer_name', models.CharField(blank=True, max_length=1000, null=True)),
                ('raw_data', models.TextField()),
            ],
        ),
    ]
