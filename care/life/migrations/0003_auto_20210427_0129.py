# Generated by Django 2.2.11 on 2021-04-26 19:59

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('life', '0002_auto_20210427_0038'),
    ]

    operations = [
        migrations.AlterField(
            model_name='lifedata',
            name='district',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='users.District'),
        ),
        migrations.AlterField(
            model_name='lifedata',
            name='state',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='users.State'),
        ),
    ]
