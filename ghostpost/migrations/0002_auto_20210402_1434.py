# Generated by Django 3.1.7 on 2021-04-02 14:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ghostpost', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='ghostpost',
            name='post_type',
            field=models.CharField(choices=[('Roast', 'Roast'), ('Boast', 'Boast')], max_length=12),
        ),
    ]