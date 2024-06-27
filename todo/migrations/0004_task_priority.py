# Generated by Django 5.0.6 on 2024-06-27 14:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('todo', '0003_task_due_date'),
    ]

    operations = [
        migrations.AddField(
            model_name='task',
            name='priority',
            field=models.CharField(choices=[('H', 'High'), ('M', 'Medium'), ('L', 'Low')], default='M', max_length=1),
        ),
    ]
