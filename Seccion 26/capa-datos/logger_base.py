import logging as log

# print(log)
# <module 'logging' from 'C:\\Program Files\\Python39\\lib\\logging\\__init__.py'>

#.basicConfig determina el nivel al que se usará "log"
log.basicConfig(level= log.DEBUG, format='%(asctime)s: %(levelname)s [%(filename)s %(lineno)s %(message)s]',
                datefmt='%I:%M:%S %p',
                handlers=[
                    log.FileHandler('capa_datos.txt'),
                    log.StreamHandler()
                ])

if __name__ == "asdasd":
    log.debug(' mensaje a lvl debug')
    log.info(' mensaje a lvl info')
    log.warning(' mensaje a lvl warning')
    log.error(' mensaje a lvl error')
    log.critical(' mensaje a lvl critical')