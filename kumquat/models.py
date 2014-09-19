from django.db import models
from django.utils.translation import ugettext_lazy as _
from kumquat.utils import DomainNameValidator

class Domain(models.Model):
	name = models.CharField(max_length=255, unique=True, verbose_name=_('Name'), validators=[DomainNameValidator()])

	def __unicode__(self):
		return self.name
