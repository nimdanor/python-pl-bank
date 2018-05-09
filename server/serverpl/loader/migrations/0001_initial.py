# Generated by Django 2.0.4 on 2018-05-03 19:02

from django.db import migrations, models
import django.db.models.deletion
import jsonfield.fields


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('filebrowser', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='PL',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('json', jsonfield.fields.JSONField()),
                ('name', models.CharField(max_length=100)),
                ('rel_path', models.CharField(max_length=360)),
                ('directory', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='filebrowser.Directory')),
            ],
        ),
        migrations.CreateModel(
            name='PLTP',
            fields=[
                ('sha1', models.CharField(max_length=160, primary_key=True, serialize=False)),
                ('json', jsonfield.fields.JSONField()),
                ('name', models.CharField(max_length=50)),
                ('rel_path', models.CharField(max_length=360)),
                ('directory', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='filebrowser.Directory')),
                ('pl', models.ManyToManyField(to='loader.PL')),
            ],
        ),
    ]
