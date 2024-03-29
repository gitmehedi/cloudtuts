# Generated by Django 3.2 on 2021-12-25 14:10

from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('restapps', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='restaurant',
            name='active',
            field=models.BooleanField(default=True),
        ),
        migrations.AlterField(
            model_name='restaurant',
            name='contact',
            field=models.CharField(max_length=14),
        ),
        migrations.CreateModel(
            name='Menu',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200)),
                ('price', models.FloatField()),
                ('current_date', models.DateField(default=django.utils.timezone.now)),
                ('vote_count', models.IntegerField()),
                ('active', models.BooleanField(default=True)),
                ('restaurant', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='restapps.restaurant')),
            ],
        ),
    ]
