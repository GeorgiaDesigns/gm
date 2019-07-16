from django.contrib.gis.db import models


class Estados(models.Model):
    geom = models.MultiPolygonField(srid=4674, blank=True, null=True)
    nm_estado = models.CharField(max_length=50, blank=True, null=True)
    nm_regiao = models.CharField(max_length=20, blank=True, null=True)
    cd_geocuf = models.CharField(max_length=2, blank=True, null=True)

    def __str__(self):
        return self.nm_estado

    class Meta:
        managed = False
        db_table = 'estados'


class EscolasParticualresSp(models.Model):
    gid = models.AutoField(primary_key=True)
    geom = models.MultiPointField(dim=3, blank=True, null=True)
    name = models.CharField(max_length=254, blank=True, null=True)
    cnpj = models.CharField(max_length=254, blank=True, null=True)
    nome_fanta = models.CharField(max_length=254, blank=True, null=True)
    data_abert = models.CharField(max_length=254, blank=True, null=True)
    cnae = models.CharField(max_length=254, blank=True, null=True)
    descricao_field = models.CharField(db_column='descricao_', max_length=254, blank=True,
                                       null=True)  # Field renamed because it ended with '_'.
    natureza_j = models.CharField(max_length=254, blank=True, null=True)
    descrica_1 = models.CharField(max_length=254, blank=True, null=True)
    end_numero = models.CharField(max_length=254, blank=True, null=True)
    endereco = models.CharField(max_length=254, blank=True, null=True)
    bairro = models.CharField(max_length=254, blank=True, null=True)
    ddd1 = models.CharField(max_length=254, blank=True, null=True)
    fone1 = models.CharField(max_length=254, blank=True, null=True)
    ddd2 = models.CharField(max_length=254, blank=True, null=True)
    fone2 = models.CharField(max_length=254, blank=True, null=True)
    ddd3 = models.CharField(max_length=254, blank=True, null=True)
    fone3 = models.CharField(max_length=254, blank=True, null=True)
    ddd4 = models.CharField(max_length=254, blank=True, null=True)
    fone4 = models.CharField(max_length=254, blank=True, null=True)
    ddd5 = models.CharField(max_length=254, blank=True, null=True)
    fone5 = models.CharField(max_length=254, blank=True, null=True)
    email1 = models.CharField(max_length=254, blank=True, null=True)
    email2 = models.CharField(max_length=254, blank=True, null=True)
    matriz = models.CharField(max_length=254, blank=True, null=True)
    porte = models.CharField(max_length=254, blank=True, null=True)
    faturament = models.CharField(max_length=254, blank=True, null=True)
    quantidade = models.CharField(max_length=254, blank=True, null=True)
    quantida_1 = models.CharField(max_length=254, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'escolas_particualres_sp'


class RestaurantesCampinas(models.Model):
    gid = models.AutoField(primary_key=True)
    name = models.CharField(max_length=254, blank=True, null=True)
    description = models.CharField(max_length=254, blank=True, null=True)
    geom = models.MultiPointField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'restaurantes_campinas'


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

