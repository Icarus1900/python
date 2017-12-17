import logging

logger = logging.getLogger()  # logger object

fh = logging.FileHandler('log.txt')

sh = logging.StreamHandler()

fm = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s -%(message)s')

fh.setFormatter(fm)  # set format

logger.addHandler(fh)  # direct to file

logger.addHandler(sh)  # direct to screen

logger.debug('debug')

logger.info('info')

logger.warning('warning')

logger.error('error')

logger.critical('critical')