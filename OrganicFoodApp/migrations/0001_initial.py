# Generated by Django 5.1 on 2024-09-02 06:49

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Special_Offers',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=253)),
                ('image', models.ImageField(default='', upload_to='pic')),
                ('description', models.TextField()),
                ('rate', models.CharField(max_length=100)),
                ('category', models.CharField(choices=[('all offers', 'all offer'), ('fruits', 'Fruits'), ('vegatables', 'Vegatables')], max_length=50)),
            ],
        ),
    ]
