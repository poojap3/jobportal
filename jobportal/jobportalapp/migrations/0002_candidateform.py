# Generated by Django 3.1.3 on 2021-12-27 14:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('jobportalapp', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='CandidateForm',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('candidate_name', models.CharField(blank=True, max_length=50, null=True)),
                ('candidate_old_company', models.CharField(blank=True, max_length=50, null=True)),
                ('previous_CTC', models.CharField(blank=True, max_length=50, null=True)),
                ('expected_CTC', models.CharField(blank=True, max_length=50, null=True)),
                ('location', models.CharField(blank=True, max_length=50, null=True)),
                ('created', models.DateTimeField(auto_now_add=True, null=True, verbose_name='Created')),
            ],
        ),
    ]