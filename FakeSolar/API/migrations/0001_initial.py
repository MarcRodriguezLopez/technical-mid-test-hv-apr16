# Generated by Django 4.0.4 on 2022-04-16 10:03

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Inspection',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=256)),
                ('inspectorName', models.CharField(max_length=256)),
                ('itemsOk', models.IntegerField()),
                ('issuesWarningCount', models.IntegerField(blank=True, default=0)),
                ('issuesCriticalCount', models.IntegerField(blank=True, default=0)),
                ('company', models.CharField(max_length=256)),
            ],
        ),
    ]
