# Generated by Django 3.2.15 on 2022-08-18 17:34

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0002_login'),
    ]

    operations = [
        migrations.CreateModel(
            name='Teacher',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('teach', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='teach', to='accounts.register')),
            ],
        ),
        migrations.DeleteModel(
            name='Login',
        ),
    ]
