# Generated by Django 3.1.7 on 2021-04-02 14:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ghostpost', '0002_auto_20210402_1434'),
    ]

    operations = [
        migrations.AlterField(
            model_name='ghostpost',
            name='post_type',
            field=models.CharField(choices=[('', '---Select---'), ('Roast', 'Roast'), ('Boast', 'Boast')], max_length=12),
        ),
    ]
