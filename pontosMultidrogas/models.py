from django.contrib.gis.db import models


class FarmasMulti(models.Model):
    gid = models.AutoField(primary_key=True)
    geom = models.MultiPointField(blank=True, null=True)
    objectid = models.BigIntegerField(blank=True, null=True)
    fid_farma_field = models.BigIntegerField(db_column='fid_farma_', blank=True,
                                             null=True)  # Field renamed because it ended with '_'.
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
    fid_munic_field = models.BigIntegerField(db_column='fid_munic_', blank=True,
                                             null=True)  # Field renamed because it ended with '_'.
    nm_municip = models.CharField(max_length=60, blank=True, null=True)
    cd_geocmu = models.CharField(max_length=7, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'farma_multi'
