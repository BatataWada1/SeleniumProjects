import logging
import time
class LogGeneration:

    @staticmethod
    def loggen():
        dateTimeStamp = time.strftime('%Y_%m_%d_%H_%M')
        logging.basicConfig(filename=r'..\Logs\nop_run_{0}.log'.format(dateTimeStamp),
                        format='%(asctime)s : %(name)s : %(levelname)-5s : %(message)s' , datefmt='%d-%m-%Y %I:%M:%S %p')
        logger = logging.getLogger()
        logger.setLevel(logging.INFO)
        return logger