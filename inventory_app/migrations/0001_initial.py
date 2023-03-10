# Generated by Django 4.1.3 on 2022-12-09 20:48

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='CGW',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Router_Ports', models.CharField(max_length=100)),
                ('Site', models.CharField(max_length=100)),
                ('Router', models.CharField(max_length=100)),
                ('Slot', models.CharField(max_length=100)),
                ('Port_Name', models.CharField(max_length=100)),
                ('Port_Status', models.CharField(max_length=100)),
                ('Negotiated_Speed', models.CharField(blank=True, max_length=100, null=True)),
                ('Bandwidth', models.CharField(max_length=100)),
                ('Optics', models.CharField(blank=True, max_length=100)),
                ('Card', models.CharField(blank=True, max_length=100)),
            ],
            options={
                'verbose_name_plural': 'CGW',
            },
        ),
        migrations.CreateModel(
            name='cSDE',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Router_Ports', models.CharField(max_length=100)),
                ('Site', models.CharField(max_length=100)),
                ('Router', models.CharField(max_length=100)),
                ('Slot', models.CharField(max_length=100)),
                ('Module_Description', models.CharField(max_length=100)),
                ('Port_Name', models.CharField(max_length=100)),
                ('Port_Status', models.CharField(max_length=100)),
                ('Negotiated_Speed', models.CharField(blank=True, max_length=100, null=True)),
                ('Bandwidth', models.CharField(max_length=100)),
                ('Optics', models.CharField(blank=True, max_length=100)),
            ],
            options={
                'verbose_name_plural': 'cSDE',
            },
        ),
        migrations.CreateModel(
            name='DGW',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Router_Ports', models.CharField(max_length=100)),
                ('Site', models.CharField(max_length=100)),
                ('Router', models.CharField(max_length=100)),
                ('Slot', models.CharField(max_length=100)),
                ('Port_Name', models.CharField(max_length=100)),
                ('Port_Status', models.CharField(max_length=100)),
                ('Negotiated_Speed', models.CharField(blank=True, max_length=100, null=True)),
                ('Bandwidth', models.CharField(max_length=100)),
                ('Optics', models.CharField(blank=True, max_length=100)),
                ('Card', models.CharField(blank=True, max_length=100)),
            ],
            options={
                'verbose_name_plural': 'DGW',
            },
        ),
        migrations.CreateModel(
            name='dSDE',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Router_Ports', models.CharField(max_length=100)),
                ('Site', models.CharField(max_length=100)),
                ('Router', models.CharField(max_length=100)),
                ('Slot', models.CharField(max_length=100)),
                ('Module_Description', models.CharField(max_length=100)),
                ('Port_Name', models.CharField(max_length=100)),
                ('Port_Status', models.CharField(max_length=100)),
                ('Negotiated_Speed', models.CharField(blank=True, max_length=100, null=True)),
                ('Bandwidth', models.CharField(max_length=100)),
                ('Optics', models.CharField(blank=True, max_length=100)),
            ],
            options={
                'verbose_name_plural': 'dSDE',
            },
        ),
        migrations.CreateModel(
            name='IGW',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Router_Ports', models.CharField(max_length=100)),
                ('Site', models.CharField(max_length=100)),
                ('Router', models.CharField(max_length=100)),
                ('Slot', models.CharField(max_length=100)),
                ('Module_Description', models.CharField(max_length=100)),
                ('Port_Name', models.CharField(max_length=100)),
                ('Port_Status', models.CharField(max_length=100)),
                ('Negotiated_Speed', models.CharField(blank=True, max_length=100, null=True)),
                ('Bandwidth', models.CharField(max_length=100)),
                ('Optics', models.CharField(blank=True, max_length=100)),
            ],
            options={
                'verbose_name_plural': 'IGW',
            },
        ),
        migrations.CreateModel(
            name='MX',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Router_Ports', models.CharField(max_length=100)),
                ('Site', models.CharField(max_length=100)),
                ('Router', models.CharField(max_length=100)),
                ('Slot', models.CharField(max_length=100)),
                ('Module_Description', models.CharField(max_length=100)),
                ('Port_Name', models.CharField(max_length=100)),
                ('Port_Status', models.CharField(max_length=100)),
                ('Negotiated_Speed', models.CharField(blank=True, max_length=100, null=True)),
                ('Bandwidth', models.CharField(max_length=100)),
                ('Optics', models.CharField(blank=True, max_length=100)),
            ],
            options={
                'verbose_name_plural': 'MX',
            },
        ),
        migrations.CreateModel(
            name='SIGR',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Router_Ports', models.CharField(max_length=100)),
                ('Site', models.CharField(max_length=100)),
                ('Router', models.CharField(max_length=100)),
                ('Slot', models.CharField(max_length=100)),
                ('Module_Description', models.CharField(max_length=100)),
                ('Port_Name', models.CharField(max_length=100)),
                ('Port_Status', models.CharField(max_length=100)),
                ('Negotiated_Speed', models.CharField(blank=True, max_length=100, null=True)),
                ('Bandwidth', models.CharField(max_length=100)),
                ('Optics', models.CharField(blank=True, max_length=100)),
            ],
            options={
                'verbose_name_plural': 'SIGR',
            },
        ),
        migrations.CreateModel(
            name='WAS',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Router_Ports', models.CharField(max_length=100)),
                ('Site', models.CharField(max_length=100)),
                ('Router', models.CharField(max_length=100)),
                ('Slot', models.CharField(max_length=100)),
                ('Module_Description', models.CharField(max_length=100)),
                ('Port_Name', models.CharField(max_length=100)),
                ('Port_Status', models.CharField(max_length=100)),
                ('Negotiated_Speed', models.CharField(blank=True, max_length=100, null=True)),
                ('Bandwidth', models.CharField(max_length=100)),
                ('Optics', models.CharField(blank=True, max_length=100)),
            ],
            options={
                'verbose_name_plural': 'WAS',
            },
        ),
        migrations.CreateModel(
            name='WGR',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Router_Ports', models.CharField(max_length=100)),
                ('Site', models.CharField(max_length=100)),
                ('Router', models.CharField(max_length=100)),
                ('Slot', models.CharField(max_length=100)),
                ('Module_Description', models.CharField(max_length=100)),
                ('Port_Name', models.CharField(max_length=100)),
                ('Port_Status', models.CharField(max_length=100)),
                ('Negotiated_Speed', models.CharField(blank=True, max_length=100, null=True)),
                ('Bandwidth', models.CharField(max_length=100)),
                ('Optics', models.CharField(blank=True, max_length=100)),
            ],
            options={
                'verbose_name_plural': 'WGR',
            },
        ),
        migrations.CreateModel(
            name='WPR',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Router_Ports', models.CharField(max_length=100)),
                ('Site', models.CharField(max_length=100)),
                ('Router', models.CharField(max_length=100)),
                ('Slot', models.CharField(max_length=100)),
                ('Module_Description', models.CharField(max_length=100)),
                ('Port_Name', models.CharField(max_length=100)),
                ('Port_Status', models.CharField(max_length=100)),
                ('Negotiated_Speed', models.CharField(blank=True, max_length=100, null=True)),
                ('Bandwidth', models.CharField(max_length=100)),
                ('Optics', models.CharField(blank=True, max_length=100)),
            ],
            options={
                'verbose_name_plural': 'WPR',
            },
        ),
        migrations.CreateModel(
            name='WRS',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Router_Ports', models.CharField(max_length=100)),
                ('Site', models.CharField(max_length=100)),
                ('Router', models.CharField(max_length=100)),
                ('Slot', models.CharField(max_length=100)),
                ('Module_Description', models.CharField(max_length=100)),
                ('Port_Name', models.CharField(max_length=100)),
                ('Port_Status', models.CharField(max_length=100)),
                ('Negotiated_Speed', models.CharField(blank=True, max_length=100, null=True)),
                ('Bandwidth', models.CharField(max_length=100)),
                ('Optics', models.CharField(blank=True, max_length=100)),
            ],
            options={
                'verbose_name_plural': 'WRS',
            },
        ),
        migrations.CreateModel(
            name='WrsReservations',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('project_number', models.CharField(max_length=100)),
                ('project_name', models.CharField(max_length=100)),
                ('target_date', models.DateField()),
                ('order_date', models.DateField(db_column='order_date', default=django.utils.timezone.now, verbose_name='Ordered At')),
                ('Router_Port_id', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='inventory_app.wrs')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name_plural': 'WrsReservations',
            },
        ),
        migrations.CreateModel(
            name='WprReservations',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('project_number', models.CharField(max_length=100)),
                ('project_name', models.CharField(max_length=100)),
                ('target_date', models.DateField()),
                ('order_date', models.DateField(db_column='order_date', default=django.utils.timezone.now, verbose_name='Ordered At')),
                ('Router_Port_id', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='inventory_app.wpr')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name_plural': 'WprReservations',
            },
        ),
        migrations.CreateModel(
            name='WgrReservations',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('project_number', models.CharField(max_length=100)),
                ('project_name', models.CharField(max_length=100)),
                ('target_date', models.DateField()),
                ('order_date', models.DateField(db_column='order_date', default=django.utils.timezone.now, verbose_name='Ordered At')),
                ('Router_Port_id', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='inventory_app.wgr')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name_plural': 'WgrReservations',
            },
        ),
        migrations.CreateModel(
            name='WasReservations',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('project_number', models.CharField(max_length=100)),
                ('project_name', models.CharField(max_length=100)),
                ('target_date', models.DateField()),
                ('order_date', models.DateField(db_column='order_date', default=django.utils.timezone.now, verbose_name='Ordered At')),
                ('Router_Port_id', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='inventory_app.was')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name_plural': 'WasReservations',
            },
        ),
        migrations.CreateModel(
            name='SigrReservations',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('project_number', models.CharField(max_length=100)),
                ('project_name', models.CharField(max_length=100)),
                ('target_date', models.DateField()),
                ('order_date', models.DateField(db_column='order_date', default=django.utils.timezone.now, verbose_name='Ordered At')),
                ('Router_Port_id', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='inventory_app.sigr')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name_plural': 'SigrReservations',
            },
        ),
        migrations.CreateModel(
            name='MxReservations',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('project_number', models.CharField(max_length=100)),
                ('project_name', models.CharField(max_length=100)),
                ('target_date', models.DateField()),
                ('order_date', models.DateField(db_column='order_date', default=django.utils.timezone.now, verbose_name='Ordered At')),
                ('Router_Port_id', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='inventory_app.mx')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name_plural': 'MxReservations',
            },
        ),
        migrations.CreateModel(
            name='IgwReservations',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('project_number', models.CharField(max_length=100)),
                ('project_name', models.CharField(max_length=100)),
                ('target_date', models.DateField()),
                ('order_date', models.DateField(db_column='order_date', default=django.utils.timezone.now, verbose_name='Ordered At')),
                ('Router_Port_id', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='inventory_app.igw')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name_plural': 'IgwReservations',
            },
        ),
        migrations.CreateModel(
            name='DsdeReservations',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('project_number', models.CharField(max_length=100)),
                ('project_name', models.CharField(max_length=100)),
                ('target_date', models.DateField()),
                ('order_date', models.DateField(db_column='order_date', default=django.utils.timezone.now, verbose_name='Ordered At')),
                ('Router_Port_id', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='inventory_app.dgw')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name_plural': 'DsdeReservations',
            },
        ),
        migrations.CreateModel(
            name='DgwReservations',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('project_number', models.CharField(max_length=100)),
                ('project_name', models.CharField(max_length=100)),
                ('target_date', models.DateField()),
                ('order_date', models.DateField(db_column='order_date', default=django.utils.timezone.now, verbose_name='Ordered At')),
                ('Router_Port_id', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='inventory_app.dgw')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name_plural': 'DgwReservations',
            },
        ),
        migrations.CreateModel(
            name='CsdeReservations',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('project_number', models.CharField(max_length=100)),
                ('project_name', models.CharField(max_length=100)),
                ('target_date', models.DateField()),
                ('order_date', models.DateField(db_column='order_date', default=django.utils.timezone.now, verbose_name='Ordered At')),
                ('Router_Port_id', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='inventory_app.csde')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name_plural': 'CsdeReservations',
            },
        ),
        migrations.CreateModel(
            name='CgwReservations',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('project_number', models.CharField(max_length=100)),
                ('project_name', models.CharField(max_length=100)),
                ('target_date', models.DateField()),
                ('order_date', models.DateField(db_column='order_date', default=django.utils.timezone.now, verbose_name='Ordered At')),
                ('Router_Port_id', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='inventory_app.cgw')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name_plural': 'CgwReservations',
            },
        ),
    ]
