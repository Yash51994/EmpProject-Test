# Generated by Django 4.1.3 on 2023-02-07 11:25

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('app1', '0002_company_customer_manager_product'),
    ]

    operations = [
        migrations.AddField(
            model_name='customer',
            name='product',
            field=models.ManyToManyField(null=True, related_name='cust', to='app1.product'),
        ),
        migrations.AddField(
            model_name='employee',
            name='company',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='emp', to='app1.company'),
        ),
        migrations.AddField(
            model_name='manager',
            name='company',
            field=models.OneToOneField(null=True, on_delete=django.db.models.deletion.CASCADE, to='app1.company'),
        ),
        migrations.AddField(
            model_name='product',
            name='company',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='prod', to='app1.company'),
        ),
    ]