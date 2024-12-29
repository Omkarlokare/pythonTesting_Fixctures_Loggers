import logging

def test_loggingDemo():

    logger = logging.getLogger(__name__)

    filehandler = logging.FileHandler('logfile.log')
    formatter = logging.Formatter("%(asctime)s :%(levelname)s : %(name)s : %(message)s")
    filehandler.setFormatter(formatter)

    logger.addHandler(filehandler)  # filehandler object

    logger.setLevel(logging.CRITICAL)
    logger.debug("A debug statement is executed")
    logger.info("Information statement")
    logger.warning("Something in is warning mode")
    logger.error("A major error has happened")
    logger.critical("Critical issue happened")
