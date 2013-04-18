"""Configuration options for the converter app"""
from __future__ import absolute_import

from django.utils.translation import ugettext_lazy as _

from smart_settings.api import register_settings

from .literals import DEFAULT_LIBREOFFICE_PATH

register_settings(
    namespace=u'converter',
    module=u'converter.settings',
    settings=[
        {'name': u'IM_CONVERT_PATH', 'global_name': u'CONVERTER_IM_CONVERT_PATH', 'default': u'/usr/bin/convert', 'description': _(u'File path to imagemagick\'s convert program.'), 'exists': True},
        {'name': u'IM_IDENTIFY_PATH', 'global_name': u'CONVERTER_IM_IDENTIFY_PATH', 'default': u'/usr/bin/identify', 'description': _(u'File path to imagemagick\'s identify program.'), 'exists': True},
        {'name': u'GM_PATH', 'global_name': u'CONVERTER_GM_PATH', 'default': u'/usr/bin/gm', 'description': _(u'File path to graphicsmagick\'s program.'), 'exists': True},
        {'name': u'GM_SETTINGS', 'global_name': u'CONVERTER_GM_SETTINGS', 'default': u''},
        {'name': u'GRAPHICS_BACKEND', 'global_name': u'CONVERTER_GRAPHICS_BACKEND', 'default': u'converter.backends.python', 'description': _(u'Graphics conversion backend to use.  Options are: converter.backends.imagemagick, converter.backends.graphicsmagick and converter.backends.python.')},
        {'name': u'LIBREOFFICE_PATH', 'global_name': u'CONVERTER_LIBREOFFICE_PATH', 'default': DEFAULT_LIBREOFFICE_PATH, 'exists': True, 'description': _(u'Path to the libreoffice program.')},
        
        #{'name': u'OCR_OPTIONS', 'global_name': u'CONVERTER_OCR_OPTIONS', 'default': u'-colorspace Gray -depth 8 -resample 200x200'},
        #{'name': u'HIGH_QUALITY_OPTIONS', 'global_name': u'CONVERTER_HIGH_QUALITY_OPTIONS', 'default': u'-density 400'},
        #{'name': u'PRINT_QUALITY_OPTIONS', 'global_name': u'CONVERTER_PRINT_QUALITY_OPTIONS', 'default': u'-density 500'},
    ]
)