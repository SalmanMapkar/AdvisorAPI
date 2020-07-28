from django.core.exceptions import ValidationError
from django.utils.translation import ugettext_lazy as _

def EmptyEmailorPassword(value):
    if value is "":
        raise ValidationError(_("Empty fields"))
    return value