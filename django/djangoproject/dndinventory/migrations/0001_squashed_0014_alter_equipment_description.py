# Generated by Django 4.2.11 on 2024-04-12 15:08

import datetime
from django.conf import settings
import django.core.validators
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    replaces = [('dndinventory', '0001_initial'), ('dndinventory', '0002_alter_equipmentproperty_options_item_custom_price_and_more'), ('dndinventory', '0003_alter_equipment_options_item_custom_category_and_more'), ('dndinventory', '0004_inventory_name'), ('dndinventory', '0005_alter_equipment_price_alter_equipment_weight_and_more'), ('dndinventory', '0006_character_user'), ('dndinventory', '0007_alter_character_user'), ('dndinventory', '0008_item_quantity'), ('dndinventory', '0009_alter_weapon_damage_die'), ('dndinventory', '0010_alter_item_options_item_order'), ('dndinventory', '0011_alter_inventory_name_and_more'), ('dndinventory', '0012_alter_equipment_weight_alter_item_custom_weight'), ('dndinventory', '0013_equipment_description'), ('dndinventory', '0014_alter_equipment_description')]

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Character',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='Equipment',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('category', models.CharField(max_length=100)),
                ('name', models.CharField(max_length=100)),
                ('price', models.DecimalField(decimal_places=2, default=0, max_digits=8)),
                ('weight', models.DecimalField(decimal_places=1, default=0, max_digits=4)),
            ],
            options={
                'verbose_name_plural': 'Equipment',
            },
        ),
        migrations.CreateModel(
            name='Inventory',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('character', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='dndinventory.character')),
                ('name', models.CharField(default='Inventory', max_length=40, unique=True)),
            ],
            options={
                'verbose_name_plural': 'Inventories',
            },
        ),
        migrations.CreateModel(
            name='Weapon',
            fields=[
                ('equipment', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, primary_key=True, serialize=False, to='dndinventory.equipment')),
                ('die_rolls', models.SmallIntegerField(default=1, validators=[django.core.validators.MaxValueValidator(2), django.core.validators.MinValueValidator(0)])),
                ('damage_die', models.SmallIntegerField(default=6, validators=[django.core.validators.MaxValueValidator(12), django.core.validators.MinValueValidator(2), django.core.validators.StepValueValidator(limit_value=2)])),
                ('strength', models.BooleanField(default=False)),
                ('dexterity', models.BooleanField(default=False)),
            ],
        ),
        migrations.CreateModel(
            name='EquipmentProperty',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('property', models.CharField(max_length=20)),
                ('value', models.CharField(max_length=20, null=True)),
                ('equipment', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='dndinventory.equipment')),
            ],
            options={
                'verbose_name_plural': 'Equipment Properties',
            },
        ),
        migrations.CreateModel(
            name='Item',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date_acquired', models.DateTimeField(blank=True, default=datetime.datetime.now)),
                ('equipment', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='dndinventory.equipment')),
                ('inventory', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='dndinventory.inventory')),
                ('custom_price', models.DecimalField(decimal_places=4, max_digits=8, null=True)),
                ('custom_weight', models.DecimalField(decimal_places=1, max_digits=4, null=True)),
                ('custom_category', models.CharField(max_length=100, null=True)),
                ('custom_name', models.CharField(max_length=100, null=True)),
            ],
        ),
        migrations.AddConstraint(
            model_name='equipment',
            constraint=models.UniqueConstraint(fields=('category', 'name'), name='unique_category_name'),
        ),
        migrations.AddConstraint(
            model_name='equipmentproperty',
            constraint=models.UniqueConstraint(fields=('equipment', 'property'), name='combination_equipment_property'),
        ),
        migrations.AddField(
            model_name='character',
            name='user',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='item',
            name='quantity',
            field=models.IntegerField(default=1, validators=[django.core.validators.MinValueValidator(1)]),
        ),
        migrations.AlterField(
            model_name='weapon',
            name='damage_die',
            field=models.SmallIntegerField(default=6, validators=[django.core.validators.MaxValueValidator(12), django.core.validators.MinValueValidator(0)]),
        ),
        migrations.AlterModelOptions(
            name='item',
            options={'ordering': ('order',)},
        ),
        migrations.AddField(
            model_name='item',
            name='order',
            field=models.IntegerField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='inventory',
            name='name',
            field=models.CharField(default='Inventory', max_length=40),
        ),
        migrations.AddConstraint(
            model_name='inventory',
            constraint=models.UniqueConstraint(fields=('character', 'name'), name='combination_character_inventory_name'),
        ),
        migrations.AlterField(
            model_name='equipment',
            name='weight',
            field=models.DecimalField(decimal_places=1, default=0, max_digits=8),
        ),
        migrations.AlterField(
            model_name='item',
            name='custom_weight',
            field=models.DecimalField(decimal_places=1, max_digits=8, null=True),
        ),
        migrations.AddField(
            model_name='equipment',
            name='description',
            field=models.CharField(max_length=360, null=True),
        ),
    ]