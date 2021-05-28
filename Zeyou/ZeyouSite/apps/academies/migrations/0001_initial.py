# Generated by Django 3.2 on 2021-05-21 14:17

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Academy',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(db_index=True, default='', max_length=64)),
                ('source', models.CharField(db_index=True, default='', max_length=64)),
                ('product_type', models.CharField(db_index=True, default='', max_length=64)),
                ('teaching_assistant', models.CharField(db_index=True, default='', max_length=64)),
                ('sales', models.CharField(db_index=True, default='', max_length=64)),
                ('teacher', models.CharField(db_index=True, default='', max_length=64)),
                ('date_of_purchasing', models.DateField(db_index=True, null=True)),
                ('product', models.CharField(db_index=True, default='', max_length=64)),
                ('date_of_lecture', models.DateField(db_index=True, null=True)),
                ('hours_of_lecture', models.IntegerField(default=0)),
                ('price_per_hour', models.IntegerField(default=0)),
                ('price_overall', models.IntegerField(default=0)),
                ('cur_state', models.CharField(db_index=True, default='', max_length=64)),
            ],
        ),
    ]