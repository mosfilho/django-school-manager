# -*- encoding: utf-8 -*-
 
from django.db import models
from django.contrib.flatpages.models import FlatPage

# Create your models here.

ACCESS_CHOICES = (
   ('0',u'Público'),
   ('1',u'Usuário de Sistema'),
   ('2',u'Administrador de Sistema')
)

class Menu(FlatPage):
    pagina_pai = models.ForeignKey("self", blank = True, null = True)
    esta_publicado = models.BooleanField(default=False, verbose_name = u"Está publicado")
    nivel_acesso = models.CharField(max_length = 1, choices = ACCESS_CHOICES,
        verbose_name = u"Nível de acesso")

    def save(self, *args, **kwargs):
        super(Menu, self).save(*args, **kwargs)

    def is_child(self):
        if self.pagina_pai:
            return True
        else:
            return False

    def has_child(self):
        if Menu.objects.filter(pagina_pai = self.id, esta_publicado = True).exists():
            return True
        else:
            return False

#    def get_absolute_url(self):
#        if self.is_child():
#            return "%s%s" % (Menu.objects.get(id = self.pagina_pai.id, esta_publicado = True).url[:-1],
#                             Menu.objects.get(id = self.id, esta_publicado = True).url)
#        else:
#            return self.url
