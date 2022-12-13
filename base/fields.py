import string

from django.db import models
#from django.utils.translation import ugettext_lazy as _
from django.utils.translation import gettext_lazy as _


from .utils import key_generator

class UniqueCodeField(models.CharField):
    description = _("Unique character string (up to %(max_length)s)")

    def __init__(self, prefix="", charset=None, *args, **kwargs):
        self.prefix = prefix
        self.charset = charset if charset else string.ascii_uppercase + string.digits
        super(UniqueCodeField, self).__init__(*args, **kwargs)

    def post_save(self, model_instance, add):
        _value = getattr(model_instance, self.attname)
        allowance = 3
        if add and any([_value == "", not _value]):
            code = key_generator(
                size=self.max_length - len(self.prefix) - allowance, chars=self.charset
            )
            f = {f"{self.attname}": code}
            while self.model.objects.filter(**f).exists():
                code = key_generator(
                    size=self.max_length - len(self.prefix) - allowance,
                    chars=self.charset,
                )
                setattr(model_instance, self.attname, f"{self.prefix}{code}")
            return f"{self.prefix}{code}"
        else:
            return super(UniqueCodeField, self).pre_save(model_instance, add)