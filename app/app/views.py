#-*- coding: utf-8 -*-

from rest_framework.viewsets import ModelViewSet
import logging
from app.models import Databases
from app.models import DatabasesSerializer

LOGGING_CONFIG = None
logging.config.dictConfig({
    'version': 1,
    'disable_existing_loggers': False,
    'formatters': {
        'console': {
            # exact format is not important, this is the minimum information
            'format': '%(asctime)s %(name)-12s %(levelname)-8s %(message)s',
        },
    },
    'handlers': {
        'console': {
            'class': 'logging.StreamHandler',
            'formatter': 'console',
        },
    },
    'loggers': {
    # root logger
        '': {
            'level': 'DEBUG',
            'handlers': ['console'],
        },
    },
})

logger = logging.getLogger(__name__)

class DatabasesViewset(ModelViewSet):
    queryset = Databases.objects.all()
    serializer_class = DatabasesSerializer

