# Generated by Django 3.1.6 on 2021-02-16 01:24

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Player',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('player_id', models.PositiveIntegerField(default=1)),
                ('name', models.CharField(max_length=100)),
                ('sex', models.CharField(choices=[('M', 'M'), ('F', 'F'), ('NA', 'NA')], max_length=9)),
                ('age', models.PositiveIntegerField(null=True)),
                ('height', models.FloatField(null=True)),
                ('weight', models.FloatField(null=True)),
                ('team', models.CharField(max_length=120)),
            ],
        ),
        migrations.CreateModel(
            name='Event',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('noc', models.CharField(max_length=3)),
                ('games', models.CharField(max_length=100)),
                ('year', models.PositiveIntegerField()),
                ('city', models.CharField(max_length=50)),
                ('season', models.CharField(choices=[('Summer', 'Summer'), ('Winter', 'Winter')], max_length=6)),
                ('sport', models.CharField(max_length=50)),
                ('medal', models.CharField(max_length=50)),
                ('winner', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='winner', to='winners.player')),
            ],
        ),
    ]
