# Generated by Django 2.2.12 on 2020-05-02 11:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("home", "0004_r1"),
    ]

    operations = [
        migrations.CreateModel(
            name="R2",
            fields=[
                (
                    "id",
                    models.AutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("r2", models.BigIntegerField()),
            ],
        ),
    ]
