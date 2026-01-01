from django.contrib import admin
from django.contrib.auth.models import Group
from django.utils.translation import gettext_lazy as _

admin.site.site_header = _('EhoLux administracija')
admin.site.site_title = _('EhoLux administracija')
admin.site.index_title = _('EhoLux administracija')

# Unregister Group model
admin.site.unregister(Group)


