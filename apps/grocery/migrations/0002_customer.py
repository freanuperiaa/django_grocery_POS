# Generated by Django 2.1.7 on 2019-03-04 14:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('grocery', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Customer',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(max_length=50)),
                ('last_name', models.CharField(max_length=50)),
                ('address', models.CharField(blank=True, max_length=200)),
                ('gender', models.CharField(blank=True, choices=[('M', 'male'), ('F', 'female'), ('NONB', 'non-binary'), ('PNS', 'prefer not to say')], max_length=30)),
                ('mem_type', models.CharField(choices=[('Plt', 'Platinum'), ('Gold', 'Gold'), ('Silver', 'Silver')], max_length=30)),
                ('trxn_made', models.PositiveIntegerField(default=0)),
                ('mem_date', models.DateField()),
            ],
        ),
    ]
