# -*- encoding: utf-8 -*-

from django.db import models
from filer.fields.image import FilerImageField
from django.contrib.auth.models import User

# Create your models here.

class EstruturaConteudo(models.Model):
    nome = models.CharField(max_length = 40)
    slug = models.SlugField(max_length = 55, blank = True, null = True,
        help_text = u'Identificador na URL. É gerado automaticamente ao salvar este conteúdo')
    esta_publicado = models.BooleanField(default = True)

    class Meta:
        abstract = True
        ordering = ['nome']
    
    def __unicode__(self):
        return self.nome
 
    def get_abolsute_url(self):
        return self.url
    
class Tipo_Conteudo (EstruturaConteudo):
    class Meta:
        verbose_name = u'Tipo de Conteúdo'
        verbose_name_plural = u'Tipos de Conteúdo'
    pass

class Galeria_Imagem (EstruturaConteudo):
    class Meta:
        verbose_name = u'Galeria de Imagem'
        verbose_name_plural = u'Galerias de Imagem'
    pass

class Imagem(models.Model):
    galeria = models.ForeignKey(Galeria_Imagem)
    imagem = FilerImageField()

    class Meta:
        verbose_name = u'Imagem'
        verbose_name_plural = u'Imagens'

class Conteudo(models.Model):
    tipo = models.ForeignKey(Tipo_Conteudo)
    titulo = models.CharField(max_length = 130)
    texto = models.TextField()
    galeria = models.ForeignKey(Galeria_Imagem, blank = True, null = True)
    esta_publicado = models.BooleanField(default = False)
    autor = models.ForeignKey(User, related_name = 'autor', editable = False)
    editor = models.ForeignKey(User, related_name = 'editor', editable = False)
    data_criacao = models.DateTimeField(auto_now = True, verbose_name = u'Data da Criação')
    data_edicao = models.DateTimeField(editable = False, verbose_name = u'Data da Edição', blank = True, null = True)
    slug = models.SlugField(max_length = 200, blank = True, null = True, 
        help_text = u'Identificador na URL. É gerado automaticamente ao salvar este conteúdo.')

    class Meta:
        verbose_name = u'Conteúdo'
        verbose_name_plural = u'Conteúdos'

    def __unicode__(self):
        return self.titulo

################################################## SIGNALS ###########################################################

from django.db.models import signals
from django.template.defaultfilters import slugify

def conteudo_pre_save(signal, instance, sender, **kwargs):
   """Este signal gera um slug automaticamente. Ele verifica se ja existe um conteudo com o mesmo 
      slug e acrescenta um numero ao final para evitar duplicidade"""
   if not instance.slug:
       slug = slugify(instance.titulo)
       novo_slug = slug
       contador = 0
       while Conteudo.objects.filter(slug=novo_slug).exclude(id=instance.id).count() > 0:
           contador += 1
           novo_slug = '%s-%d'%(slug, contador)
       instance.slug = novo_slug

def tipo_conteudo_pre_save(signal, instance, sender, **kwargs):
   if not instance.slug:
       slug = slugify(instance.nome)
       novo_slug = slug
       contador = 0
       while Tipo_Conteudo.objects.filter(slug=novo_slug).exclude(id=instance.id).count() > 0:
           contador += 1
           novo_slug = '%s-%d'%(slug, contador)
       instance.slug = novo_slug

def galeria_pre_save(signal, instance, sender, **kwargs):
   if not instance.slug:
       slug = slugify(instance.nome)
       novo_slug = slug
       contador = 0
       while Galeria_Imagem.objects.filter(slug=novo_slug).exclude(id=instance.id).count() > 0:
           contador += 1
           novo_slug = '%s-%d'%(slug, contador)
       instance.slug = novo_slug

signals.pre_save.connect(conteudo_pre_save, sender=Conteudo)
signals.pre_save.connect(tipo_conteudo_pre_save, sender=Tipo_Conteudo)
signals.pre_save.connect(galeria_pre_save, sender=Galeria_Imagem)
