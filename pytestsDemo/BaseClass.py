import logging


class BaseClass:
    def getLoggerdemo(self):

        logger = logging.getLogger(__name__)

        filehandler = logging.FileHandler('logfile.log')
        formatter = logging.Formatter("%(asctime)s :%(levelname)s : %(name)s : %(message)s")
        filehandler.setFormatter(formatter)

        logger.addHandler(filehandler)  # filehandler object

        logger.setLevel(logging.DEBUG)
        return logger
