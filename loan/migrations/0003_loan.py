# Generated by Django 3.2 on 2021-05-10 18:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('loan', '0002_alter_register_mobileno'),
    ]

    operations = [
        migrations.CreateModel(
            name='Loan',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('loanamt', models.IntegerField()),
                ('duration_of_loan', models.IntegerField()),
                ('ROI', models.IntegerField()),
            ],
        ),
    ]
