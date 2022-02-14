# Generated by Django 3.2 on 2022-02-14 13:04

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="LeaveRequest",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("name", models.CharField(max_length=200)),
                ("start_date", models.DateField()),
                ("end_date", models.DateField()),
                (
                    "type_of_leave",
                    models.CharField(
                        choices=[("NO", "Normal"), ("SI", "Sickleave")],
                        default="NORMAL",
                        max_length=2,
                    ),
                ),
            ],
        ),
    ]
