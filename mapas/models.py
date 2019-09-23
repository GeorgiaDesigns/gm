from django.contrib.gis.db import models


class RestaurantesCampinas(models.Model):
    gid = models.AutoField(primary_key=True)
    name = models.CharField(max_length=254, blank=True, null=True)
    description = models.CharField(max_length=254, blank=True, null=True)
    timestamp = models.CharField(max_length=24, blank=True, null=True)
    begin = models.CharField(max_length=24, blank=True, null=True)
    end = models.CharField(max_length=24, blank=True, null=True)
    altitudemo = models.CharField(max_length=254, blank=True, null=True)
    tessellate = models.BigIntegerField(blank=True, null=True)
    extrude = models.BigIntegerField(blank=True, null=True)
    visibility = models.BigIntegerField(blank=True, null=True)
    draworder = models.BigIntegerField(blank=True, null=True)
    icon = models.CharField(max_length=254, blank=True, null=True)
    snippet = models.CharField(max_length=254, blank=True, null=True)
    geom = models.MultiPointField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'restaurantes_campinas'


class RmcHoteis(models.Model):
    gid = models.AutoField(primary_key=True)
    cnpj = models.CharField(max_length=254, blank=True, null=True)
    nomefantas = models.CharField(max_length=254, blank=True, null=True)
    endereco = models.CharField(max_length=254, blank=True, null=True)
    bairro = models.CharField(max_length=254, blank=True, null=True)
    numero = models.CharField(max_length=254, blank=True, null=True)
    complement = models.CharField(max_length=254, blank=True, null=True)
    cep = models.CharField(max_length=254, blank=True, null=True)
    latitude = models.CharField(max_length=254, blank=True, null=True)
    longitude = models.CharField(max_length=254, blank=True, null=True)
    datasituac = models.CharField(max_length=254, blank=True, null=True)
    situacaoca = models.CharField(max_length=254, blank=True, null=True)
    dataabertu = models.CharField(max_length=254, blank=True, null=True)
    regulament = models.CharField(max_length=254, blank=True, null=True)
    natureza = models.CharField(max_length=254, blank=True, null=True)
    cnae = models.CharField(max_length=254, blank=True, null=True)
    setor = models.CharField(max_length=254, blank=True, null=True)
    cidade = models.CharField(max_length=254, blank=True, null=True)
    estado = models.CharField(max_length=254, blank=True, null=True)
    regiao = models.CharField(max_length=254, blank=True, null=True)
    idade = models.CharField(max_length=254, blank=True, null=True)
    simplesnac = models.CharField(max_length=254, blank=True, null=True)
    inscricaoe = models.CharField(max_length=254, blank=True, null=True)
    cnaesecund = models.CharField(max_length=254, blank=True, null=True)
    cnaesecu_1 = models.CharField(max_length=254, blank=True, null=True)
    cnaesecu_2 = models.CharField(max_length=254, blank=True, null=True)
    cnaesecu_3 = models.CharField(max_length=254, blank=True, null=True)
    cnaesecu_4 = models.CharField(max_length=254, blank=True, null=True)
    cnaesecu_5 = models.CharField(max_length=254, blank=True, null=True)
    cnaesecu_6 = models.CharField(max_length=254, blank=True, null=True)
    funcionari = models.CharField(max_length=254, blank=True, null=True)
    geom = models.MultiPointField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'rmc_hoteis'


class FarmaMulti(models.Model):
    gid = models.AutoField(primary_key=True)
    geom = models.MultiPointField(blank=True, null=True)
    objectid = models.BigIntegerField(blank=True, null=True)
    fid_farma_field = models.BigIntegerField(db_column='fid_farma_', blank=True, null=True)  # Field renamed because it ended with '_'.
    nome = models.CharField(max_length=254, blank=True, null=True)
    ddd = models.CharField(max_length=254, blank=True, null=True)
    fone = models.CharField(max_length=254, blank=True, null=True)
    fax = models.CharField(max_length=254, blank=True, null=True)
    titular = models.CharField(max_length=254, blank=True, null=True)
    razao_soci = models.CharField(max_length=254, blank=True, null=True)
    razao_so_1 = models.CharField(max_length=254, blank=True, null=True)
    insc_estad = models.CharField(max_length=254, blank=True, null=True)
    endereco = models.CharField(max_length=254, blank=True, null=True)
    numero = models.CharField(max_length=254, blank=True, null=True)
    bairro = models.CharField(max_length=254, blank=True, null=True)
    cep = models.CharField(max_length=254, blank=True, null=True)
    email = models.CharField(max_length=254, blank=True, null=True)
    farmacia = models.CharField(max_length=254, blank=True, null=True)
    fid_munic_field = models.BigIntegerField(db_column='fid_munic_', blank=True, null=True)  # Field renamed because it ended with '_'.
    nm_municip = models.CharField(max_length=60, blank=True, null=True)
    cd_geocmu = models.CharField(max_length=7, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'farma_multi'


class SociodemografiaRmc(models.Model):
    gid = models.AutoField(primary_key=True)
    geom = models.MultiPolygonField(blank=True, null=True)
    cd_geocodi = models.CharField(max_length=20, blank=True, null=True)
    tipo = models.CharField(max_length=10, blank=True, null=True)
    nm_distrit = models.CharField(max_length=60, blank=True, null=True)
    nm_municip = models.CharField(max_length=60, blank=True, null=True)
    nm_micro = models.CharField(max_length=100, blank=True, null=True)
    nm_meso = models.CharField(max_length=100, blank=True, null=True)
    cod_setor = models.FloatField(blank=True, null=True)
    situacao_s = models.BigIntegerField(blank=True, null=True)
    f25a60anos = models.IntegerField(blank=True, null=True)
    mulheres_2 = models.IntegerField(blank=True, null=True)
    homens_25a = models.IntegerField(blank=True, null=True)
    domicilio_field = models.IntegerField(db_column='domicilio_', blank=True, null=True)
    pessoa_a = models.IntegerField(blank=True, null=True)
    pessoa_b = models.IntegerField(blank=True, null=True)
    pessoa_ab = models.IntegerField(blank=True, null=True)
    ipc_ab = models.FloatField(blank=True, null=True)
    potencial_field = models.FloatField(db_column='potencial_', blank=True, null=True)
    shape_area = models.FloatField(blank=True, null=True)
    densid_dem = models.FloatField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'sociodemografia_rmc'


class FarmaciasRmc(models.Model):
    gid = models.AutoField(primary_key=True)
    name = models.CharField(max_length=254, blank=True, null=True)
    cnpj = models.CharField(max_length=254, blank=True, null=True)
    nomefantas = models.CharField(max_length=254, blank=True, null=True)
    endereco = models.CharField(max_length=254, blank=True, null=True)
    bairro = models.CharField(max_length=254, blank=True, null=True)
    numero = models.CharField(max_length=254, blank=True, null=True)
    complement = models.CharField(max_length=254, blank=True, null=True)
    cep = models.CharField(max_length=254, blank=True, null=True)
    datasituac = models.CharField(max_length=254, blank=True, null=True)
    situacaoca = models.CharField(max_length=254, blank=True, null=True)
    dataabertu = models.CharField(max_length=254, blank=True, null=True)
    regulament = models.CharField(max_length=254, blank=True, null=True)
    natureza = models.CharField(max_length=254, blank=True, null=True)
    cnae = models.CharField(max_length=254, blank=True, null=True)
    setor = models.CharField(max_length=254, blank=True, null=True)
    cidade = models.CharField(max_length=254, blank=True, null=True)
    estado = models.CharField(max_length=254, blank=True, null=True)
    regiao = models.CharField(max_length=254, blank=True, null=True)
    idade = models.CharField(max_length=254, blank=True, null=True)
    simplesnac = models.CharField(max_length=254, blank=True, null=True)
    inscricaoe = models.CharField(max_length=254, blank=True, null=True)
    cnaesecund = models.CharField(max_length=254, blank=True, null=True)
    cnaesecu_1 = models.CharField(max_length=254, blank=True, null=True)
    cnaesecu_2 = models.CharField(max_length=254, blank=True, null=True)
    cnaesecu_3 = models.CharField(max_length=254, blank=True, null=True)
    cnaesecu_4 = models.CharField(max_length=254, blank=True, null=True)
    cnaesecu_5 = models.CharField(max_length=254, blank=True, null=True)
    cnaesecu_6 = models.CharField(max_length=254, blank=True)
    geom = models.MultiPointField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'farmacias_rmc'

