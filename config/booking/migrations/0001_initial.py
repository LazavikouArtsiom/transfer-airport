# Generated by Django 3.1.4 on 2020-12-21 16:07

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Booking',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
                ('phone', models.CharField(max_length=20)),
                ('email', models.CharField(max_length=30)),
                ('city', models.IntegerField(choices=[(1, 'Могилёв'), (2, 'Шклов'), (3, 'Бобруйск'), (4, 'Гомель'), (5, 'Орша')], default=1, max_length=20)),
                ('airport', models.IntegerField(choices=[(1, 'а/п Борисполь')], default=1)),
                ('count', models.IntegerField(default=1)),
                ('order_date', models.DateField()),
                ('is_back', models.BooleanField(default=True)),
                ('back_date', models.DateField()),
                ('notes', models.CharField(max_length=255)),
            ],
        ),
    ]
