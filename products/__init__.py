__version__ = '0.1.0'
import os
from django.conf import settings

settings.FIXTURE_DIRS += [os.path.join('products', 'fixtures')]
