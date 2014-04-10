from django.db import models
from filer.fields.image import FilerImageField
from django.contrib.sites.models import Site

TWITTER_CARD_CHOICES = (
	('0','summary'),
	('1','photo'),
	('2','video'),
)

# Create your models here.
class Escola(models.Model):
	nome = models.CharField(max_length = 30)
	logo_navegador = FilerImageField()
	site = models.ForeignKey(Site)

class SEO(models.Model):
	site = models.ForeignKey(Site)
	description = models.CharField(max_length = 155)

class SocialTwitter(models.Model):
	twitter_site = models.CharField(max_length = 20)
	facebook_id = models.CharField(max_length = 50)