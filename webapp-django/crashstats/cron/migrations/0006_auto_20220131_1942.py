# Generated by Django 3.2.11 on 2022-01-31 19:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("cron", "0005_auto_20190430_1242"),
    ]

    operations = [
        migrations.AlterField(
            model_name="job",
            name="id",
            field=models.BigAutoField(
                auto_created=True, primary_key=True, serialize=False, verbose_name="ID"
            ),
        ),
        migrations.AlterField(
            model_name="log",
            name="id",
            field=models.BigAutoField(
                auto_created=True, primary_key=True, serialize=False, verbose_name="ID"
            ),
        ),
    ]