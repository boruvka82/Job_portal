# Generated by Django 4.0.4 on 2022-05-01 17:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('jobp', '0012_alter_teacher_name'),
    ]

    operations = [
        migrations.AlterField(
            model_name='teacher',
            name='name',
            field=models.CharField(max_length=50),
        ),
    ]
