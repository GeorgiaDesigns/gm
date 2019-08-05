# Generated by Django 2.1.7 on 2019-07-05 20:39

import django.contrib.gis.db.models.fields
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mapas', '0003_estados_sociodemografiarmc'),
    ]

    operations = [
        migrations.CreateModel(
            name='EscolasParticualresSp',
            fields=[
                ('gid', models.AutoField(primary_key=True, serialize=False)),
                ('geom', django.contrib.gis.db.models.fields.MultiPointField(blank=True, dim=3, null=True, srid=4326)),
                ('name', models.CharField(blank=True, max_length=254, null=True)),
                ('cnpj', models.CharField(blank=True, max_length=254, null=True)),
                ('nome_fanta', models.CharField(blank=True, max_length=254, null=True)),
                ('data_abert', models.CharField(blank=True, max_length=254, null=True)),
                ('cnae', models.CharField(blank=True, max_length=254, null=True)),
                ('descricao_field', models.CharField(blank=True, db_column='descricao_', max_length=254, null=True)),
                ('natureza_j', models.CharField(blank=True, max_length=254, null=True)),
                ('descrica_1', models.CharField(blank=True, max_length=254, null=True)),
                ('end_numero', models.CharField(blank=True, max_length=254, null=True)),
                ('endereco', models.CharField(blank=True, max_length=254, null=True)),
                ('bairro', models.CharField(blank=True, max_length=254, null=True)),
                ('ddd1', models.CharField(blank=True, max_length=254, null=True)),
                ('fone1', models.CharField(blank=True, max_length=254, null=True)),
                ('ddd2', models.CharField(blank=True, max_length=254, null=True)),
                ('fone2', models.CharField(blank=True, max_length=254, null=True)),
                ('ddd3', models.CharField(blank=True, max_length=254, null=True)),
                ('fone3', models.CharField(blank=True, max_length=254, null=True)),
                ('ddd4', models.CharField(blank=True, max_length=254, null=True)),
                ('fone4', models.CharField(blank=True, max_length=254, null=True)),
                ('ddd5', models.CharField(blank=True, max_length=254, null=True)),
                ('fone5', models.CharField(blank=True, max_length=254, null=True)),
                ('email1', models.CharField(blank=True, max_length=254, null=True)),
                ('email2', models.CharField(blank=True, max_length=254, null=True)),
                ('matriz', models.CharField(blank=True, max_length=254, null=True)),
                ('porte', models.CharField(blank=True, max_length=254, null=True)),
                ('faturament', models.CharField(blank=True, max_length=254, null=True)),
                ('quantidade', models.CharField(blank=True, max_length=254, null=True)),
                ('quantida_1', models.CharField(blank=True, max_length=254, null=True)),
            ],
            options={
                'db_table': 'escolas_particualres_sp',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='FarmaciasRmc',
            fields=[
                ('gid', models.AutoField(primary_key=True, serialize=False)),
                ('name', models.CharField(blank=True, max_length=254, null=True)),
                ('cnpj', models.CharField(blank=True, max_length=254, null=True)),
                ('nomefantas', models.CharField(blank=True, max_length=254, null=True)),
                ('endereco', models.CharField(blank=True, max_length=254, null=True)),
                ('bairro', models.CharField(blank=True, max_length=254, null=True)),
                ('numero', models.CharField(blank=True, max_length=254, null=True)),
                ('complement', models.CharField(blank=True, max_length=254, null=True)),
                ('cep', models.CharField(blank=True, max_length=254, null=True)),
                ('datasituac', models.CharField(blank=True, max_length=254, null=True)),
                ('situacaoca', models.CharField(blank=True, max_length=254, null=True)),
                ('dataabertu', models.CharField(blank=True, max_length=254, null=True)),
                ('regulament', models.CharField(blank=True, max_length=254, null=True)),
                ('natureza', models.CharField(blank=True, max_length=254, null=True)),
                ('cnae', models.CharField(blank=True, max_length=254, null=True)),
                ('setor', models.CharField(blank=True, max_length=254, null=True)),
                ('cidade', models.CharField(blank=True, max_length=254, null=True)),
                ('estado', models.CharField(blank=True, max_length=254, null=True)),
                ('regiao', models.CharField(blank=True, max_length=254, null=True)),
                ('idade', models.CharField(blank=True, max_length=254, null=True)),
                ('simplesnac', models.CharField(blank=True, max_length=254, null=True)),
                ('inscricaoe', models.CharField(blank=True, max_length=254, null=True)),
                ('cnaesecund', models.CharField(blank=True, max_length=254, null=True)),
                ('cnaesecu_1', models.CharField(blank=True, max_length=254, null=True)),
                ('cnaesecu_2', models.CharField(blank=True, max_length=254, null=True)),
                ('cnaesecu_3', models.CharField(blank=True, max_length=254, null=True)),
                ('cnaesecu_4', models.CharField(blank=True, max_length=254, null=True)),
                ('cnaesecu_5', models.CharField(blank=True, max_length=254, null=True)),
                ('cnaesecu_6', models.CharField(blank=True, max_length=254)),
                ('geom', django.contrib.gis.db.models.fields.MultiPointField(blank=True, null=True, srid=4326)),
            ],
            options={
                'db_table': 'farmacias_rmc',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='RestaurantesCampinas',
            fields=[
                ('gid', models.AutoField(primary_key=True, serialize=False)),
                ('name', models.CharField(blank=True, max_length=254, null=True)),
                ('description', models.CharField(blank=True, max_length=254, null=True)),
                ('geom', django.contrib.gis.db.models.fields.MultiPointField(blank=True, null=True, srid=4326)),
            ],
            options={
                'db_table': 'restaurantes_campinas',
                'managed': False,
            },
        ),
        migrations.DeleteModel(
            name='Empresas',
        ),
    ]
