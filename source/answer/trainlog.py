from logging import getLogger, StreamHandler, Formatter, DEBUG


def mylogger(modname=__name__):
    logger = getLogger(modname)
    logger.setLevel(DEBUG)
    
    stream = StreamHandler()
    stream.setLevel(level=DEBUG)
    formatter = Formatter(
        "[%(asctime)s]:(%(levelname)s): %(filename)s:%(lineno)d - %(message)s"
        )
    stream.setFormatter(formatter)
    logger.addHandler(stream)
    
    return logger