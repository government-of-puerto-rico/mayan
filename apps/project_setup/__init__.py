from __future__ import absolute_import

from django.utils.translation import ugettext_lazy as _

from navigation.api import register_top_menu

from .links import link_setup_menu

setup_menu = register_top_menu('setup_menu', link=link_setup_menu, position=-2)
