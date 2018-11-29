import logging.config
import multiprocessing

#bind = "0.0.0.0:8080"
workers = (2 * multiprocessing.cpu_count()) + 1
#logconfig = "./log.conf"
loglevel = 'debug'

LOGGING = {
	'version' : 1,
    'handlers': {
        'file' : {
			'class' : 'logging.handlers.RotatingFileHandler',
			#'formatter' : 'key_value',
			'filename' : 'gunicorn.log',
			'maxBytes' : 1024,
			'backupCount' : 3
		}
	},
	'loggers':{
		'root':{
			'handlers' : ['file']
		}
	}
}

#logging.config.dictConfig(LOGGING)