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
    descriptio = models.CharField(max_length=254, blank=True, null=True)
    timestamp = models.CharField(max_length=24, blank=True, null=True)
    begin = models.CharField(max_length=24, blank=True, null=True)
    end = models.CharField(max_length=24, blank=True, null=True)
    altitudemo = models.CharField(max_length=254, blank=True, null=True)
    tessellate = models.BigIntegerField(blank=True, null=True)
    extrude = models.BigIntegerField(blank=True, null=True)
    visibility = models.BigIntegerField(blank=True, null=True)
    draworder = models.BigIntegerField(blank=True, null=True)
    icon = models.CharField(max_length=254, blank=True, null=True)
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
    geom = models.MultiPointField(dim=3, blank=True, null=True)
    name = models.CharField(max_length=254, blank=True, null=True)
    descriptio = models.CharField(max_length=254, blank=True, null=True)
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

    # def __str__(self):
    #     return self

    class Meta:
        managed = False
        db_table = 'sociodemografia_rmc'
