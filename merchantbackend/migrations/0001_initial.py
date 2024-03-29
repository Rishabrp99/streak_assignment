# Generated by Django 4.1.5 on 2023-01-27 00:24

from django.db import migrations, models
import uuid


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Order',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False, unique=True)),
                ('order_amount', models.IntegerField(blank=True, default=0, null=True)),
                ('order_meta', models.CharField(blank=True, default='', max_length=100, null=True)),
            ],
        ),
    ]
