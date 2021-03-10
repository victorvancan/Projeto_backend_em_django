import  uuid
from django.db import models
from stdimage.models import StdImageField
from django.utils.translation import gettext_lazy as _

def get_file_path(_instance, filename):
    ext = filename.split('.')[-1]
    filename = f'{uuid.uuid4()}.{ext}'
    return filename


class Base(models.Model):
    criados = models.DateField(_('criação'), auto_now_add=True)
    modificados = models.DateField(_('modificado'), auto_now=True)
    ativo = models.BooleanField(_ ('ativo?'), default=True)


class Servico(Base):
    ICONE_CHOICES = (
        ('lni-cog', _('Engrenagem')),
        ('lni-status-up', _('Gráfico')),
        ('lni-users', _('Usuários')),
        ('lni-layers', _('Design')),
        ('lni-mobile', _('Mobile')),
        ('lni-rocket', _('Foguete')),
    )
    servicos = models.CharField(_('Serviços'), max_length=100)
    descricao = models.TextField(_('Descrição'), max_length=100)
    icone = models.CharField(_('Icone'), max_length=13, choices=ICONE_CHOICES)

    class meta:
        verbose_name = _('Serviço')
        verbose_name_plural = _('Serviços')

    def __str__(self):
        return self.servicos


class Cargo(Base):
    cargos = models.CharField('Cargo', max_length=100)

    class meta:
        verbose_name = _('Cargo')
        verbose_name_plural = _('Cargos')

    def __str__(self):
        return self.cargos


class Funcionario(Base):
    nome = models.CharField(_('nome'), max_length=100)
    funcao = models.ForeignKey('core.Cargo', verbose_name=_('Cargo'), on_delete=models.CASCADE)
    bio = models.TextField(_('Bio'), max_length=200)
    image = StdImageField(_('Image'), upload_to=get_file_path, variations={'thumb': {'width': 480, 'height': 480, 'crop': True}})
    facebook = models.CharField('Facebook', max_length=100, default='#')
    twitter = models.CharField('Twitter', max_length=100, default='#')
    instagram = models.CharField('Instagram', max_length=100, default='#')


    class Meta:
        verbose_name = _('Funcionário')
        verbose_name_plural = _('Funcionários')

    def __str__(self):
        return self.nome


class Feature(Base):
    ICONE_CHOICES = (
        ('lni-cog', _('Engrenagem')),
        ('lni-laptop-phone', _('note e cel')),
        ('lni-leaf', _('folha')),
        ('lni-layers', _('Design')),
        ('lni-rocket', _('Foguete')),

    )

    features = models.CharField(_('feature'), max_length=100)
    descricao = models.TextField(_('descricao'), max_length=100)
    icon = models.CharField(_('Icon'), max_length=17, choices=ICONE_CHOICES)

    class Meta:
        verbose_name = _('Feature')
        verbose_name_plural = _('Features')

    def __str__(self):
        return self.features
