
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('categoryname', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='Vehicle',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('parkingnumber', models.CharField(max_length=20)),
                ('vehiclecompany', models.CharField(max_length=50)),
                ('regno', models.CharField(max_length=10)),
                ('ownername', models.CharField(max_length=50)),
                ('ownercontact', models.CharField(max_length=15)),
                ('pdate', models.DateField()),
                ('intime', models.CharField(max_length=50)),
                ('outtime', models.CharField(max_length=50)),
                ('parkingcharge', models.CharField(max_length=50)),
                ('remark', models.CharField(max_length=500)),
                ('status', models.CharField(max_length=20)),
                ('category', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='vehicle.Category')),
            ],
        ),
    ]
