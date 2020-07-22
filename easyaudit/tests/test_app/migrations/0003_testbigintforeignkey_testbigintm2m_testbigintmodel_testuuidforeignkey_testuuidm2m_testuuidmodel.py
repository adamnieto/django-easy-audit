# Generated by Django 3.0.6 on 2020-05-14 17:28

from django.db import migrations, models
import django.db.models.deletion
import uuid


class Migration(migrations.Migration):

    dependencies = [
        ('test_app', '0002_auto_20180220_1533'),
    ]

    operations = [
        migrations.CreateModel(
            name='TestBigIntModel',
            fields=[
                ('id', models.BigAutoField(primary_key=True, serialize=False)),
                ('name', models.CharField(default='test data', max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='TestUUIDModel',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False, unique=True)),
                ('name', models.CharField(default='test data', max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='TestUUIDM2M',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False, unique=True)),
                ('name', models.CharField(max_length=50)),
                ('test_m2m', models.ManyToManyField(to='test_app.TestUUIDModel')),
            ],
        ),
        migrations.CreateModel(
            name='TestUUIDForeignKey',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False, unique=True)),
                ('name', models.CharField(max_length=50)),
                ('test_fk', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='test_app.TestUUIDModel')),
            ],
        ),
        migrations.CreateModel(
            name='TestBigIntM2M',
            fields=[
                ('id', models.BigAutoField(primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=50)),
                ('test_m2m', models.ManyToManyField(to='test_app.TestBigIntModel')),
            ],
        ),
        migrations.CreateModel(
            name='TestBigIntForeignKey',
            fields=[
                ('id', models.BigAutoField(primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=50)),
                ('test_fk', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='test_app.TestBigIntModel')),
            ],
        ),
    ]
