# Generated by Django 3.2.9 on 2021-12-04 11:30

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='FormDetailsModel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('field_name', models.CharField(max_length=100)),
                ('Type', models.CharField(choices=[('Text', 'Text'), ('Single select', 'Single select'), ('Number', 'Number'), ('Date', 'Date')], max_length=50)),
                ('options', models.CharField(blank=True, max_length=50, null=True)),
                ('mandatory', models.BooleanField()),
            ],
        ),
        migrations.CreateModel(
            name='UploadCsv',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('csv', models.FileField(upload_to='csv/')),
                ('form_name', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='FormModel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('form_name', models.CharField(max_length=100, verbose_name='Name of the Form')),
                ('form', models.ManyToManyField(to='myapp.FormDetailsModel')),
            ],
            options={
                'verbose_name': 'form_name_and_details',
            },
        ),
    ]
