# -*- coding: utf-8 -*-
# Generated by Django 1.10.6 on 2017-04-01 05:42
from __future__ import unicode_literals

import django.core.validators
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='CookedAt',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date', models.DateTimeField()),
                ('rating', models.IntegerField(validators=[django.core.validators.MaxValueValidator(5), django.core.validators.MinValueValidator(1)])),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
            ],
        ),
        migrations.CreateModel(
            name='Direction',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('step', models.IntegerField()),
                ('timer', models.TimeField()),
                ('description', models.TextField()),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
            ],
        ),
        migrations.CreateModel(
            name='Ingredient',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=800)),
                ('amount', models.CharField(max_length=100)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
            ],
        ),
        migrations.CreateModel(
            name='Recipe',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=800, unique=True)),
                ('preparation_time', models.FloatField(blank=True, null=True)),
                ('cooking_time', models.FloatField(blank=True, null=True)),
                ('cuisine', models.CharField(choices=[('Ame', 'American'), ('Chi', 'Chinese'), ('Ind', 'Indian'), ('Ita', 'Italian'), ('Fre', 'French'), ('Gre', 'Greek'), ('Med', 'Mediterranean'), ('Mex', 'Mexican'), ('Nor', 'Nordic'), ('Tur', 'Turkish'), ('Ban', 'Bangladesh'), ('Oth', 'Other')], default='Oth', max_length=3)),
                ('meal', models.CharField(choices=[('Mai', 'Main Course'), ('Sna', 'Snacks'), ('Bre', 'Breakfast'), ('Sid', 'Side Dished'), ('Des', 'Dessert'), ('Cak', 'Caking and Baking'), ('Dri', 'Drinks'), ('Oth', 'Other')], default='Oth', max_length=3)),
                ('video', models.URLField(blank=True, null=True)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('direction', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='recipe.Direction')),
                ('ingredient', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='recipe.Ingredient')),
            ],
        ),
        migrations.AddField(
            model_name='cookedat',
            name='recipe',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='recipe.Recipe'),
        ),
    ]