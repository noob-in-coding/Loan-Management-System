# Generated by Django 3.2 on 2021-05-13 16:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('loan', '0004_auto_20210513_2127'),
    ]

    operations = [
        migrations.AlterField(
            model_name='loan',
            name='ROI',
            field=models.IntegerField(),
        ),
        migrations.AlterField(
            model_name='loan',
            name='duration_of_loan',
            field=models.IntegerField(),
        ),
        migrations.AlterField(
            model_name='loan',
            name='loanamt',
            field=models.IntegerField(),
        ),
    ]
