# Generated by Django 4.2.14 on 2024-07-28 14:20

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('flights', '0002_remove_flight_last_updated'),
    ]

    operations = [
        migrations.AlterField(
            model_name='flight',
            name='gate',
            field=models.CharField(max_length=10),
        ),
        migrations.AlterField(
            model_name='flight',
            name='status',
            field=models.CharField(max_length=20),
        ),
        migrations.CreateModel(
            name='Notification',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('recipient', models.CharField(max_length=100)),
                ('channel', models.CharField(choices=[('SMS', 'SMS'), ('Email', 'Email'), ('App', 'App')], max_length=10)),
                ('message', models.TextField()),
                ('sent_at', models.DateTimeField(auto_now_add=True)),
                ('flight', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='flights.flight')),
            ],
        ),
    ]
