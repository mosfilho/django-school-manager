# -*- encoding: utf-8 -*-
from django.db import models
from filer.fields.image import FilerImageField
from django.contrib.sites.models import Site

LOGRADOURO_CHOICES = (
    ('0', 'Aeroporto'), 
    ('1', 'Alameda'), 
    ('2', 'Area'), 
    ('3', 'Avenida'), 
    ('4', 'Campo'), 
    ('5', 'Chácara'), 
    ('6', 'Colônia'), 
    ('7', 'Condomínio'), 
    ('8', 'Conjunto'), 
    ('9', 'Cistrito'), 
    ('10', 'Esplanada'), 
    ('11', 'Estação'), 
    ('12', 'Estrada'), 
    ('13', 'Favela'), 
    ('14', 'Feira'), 
    ('15', 'Jardim'), 
    ('16', 'Ladeira'), 
    ('17', 'Lago'), 
    ('18', 'Lagoa'), 
    ('19', 'Largo'), 
    ('20', 'Loteamento'), 
    ('21', 'Morro'), 
    ('22', 'Núcleo'), 
    ('23', 'Parque'), 
    ('24', 'Passarela'), 
    ('25', 'Pátio'), 
    ('26', 'Praça'), 
    ('27', 'Quadra'), 
    ('28', 'Recanto'), 
    ('29', 'Residencial'), 
    ('30', 'Rodovia'), 
    ('31', 'Rua'), 
    ('32', 'Setor'), 
    ('33', 'Sítio'), 
    ('34', 'Travessa'), 
    ('35', 'Trecho'), 
    ('36', 'Trevo'), 
    ('37', 'Vale'), 
    ('38', 'Vereda'), 
    ('39', 'Via'), 
    ('40', 'Viaduto'), 
    ('41', 'Viela'), 
    ('42', 'Vila')
)

# Create your models here.
class MetaDados(models.Model):
	site = models.ForeignKey(Site)
	logo_navegador = FilerImageField(blank = True, null = True)
	description = models.CharField(max_length = 155, blank = True, null = True)
	twitter_site = models.CharField(max_length = 20, blank = True, null = True)
	facebook_id = models.CharField(max_length = 50, blank = True, null = True)
	google_profile = models.CharField(max_length = 100, blank = True, null = True)

	def __unicode__(self):
		return self.site.name
'''
class Sede(models.Model):
	nome = models.CharField(max_length = 50)
	logradouro = models.CharField(max_length = 2, choices = LOGRADOURO_CHOICES)
    endereco = models.CharField(max_length = 100, verbose_name = u'Endereço')
    numero = models.IntegerField(verbose_name = u'Número')
    bairro = models.CharField(max_length = 50)
    cidade = models.CharField(max_length = 25)
    sigla_uf = models.CharField(max_length = 2)
'''
