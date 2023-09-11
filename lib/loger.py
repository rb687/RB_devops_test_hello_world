import logging.handlers as handlers
import logging
import logging.config
import lib.config as config
import sys

class log_operations:
    def __init__(self, logfilename, level):
        self.app_log = logging.getLogger(__name__)
        self.loggingFormat = logging.Formatter(config.log_format)
        # If we were to put this in PROD, we would want rotating logs for a few days and also get the logs
        # sent to Splunk or similar log analyzer tool
        self.file_handler = handlers.RotatingFileHandler(logfilename, maxBytes=config.max_log_size, backupCount=10)
        self.file_handler.setFormatter(self.loggingFormat)

        self.stdout_handler = logging.StreamHandler(sys.stdout)
        self.stdout_handler.setFormatter(self.loggingFormat)


        self.app_log.propagate = False
        self.app_log.addHandler(self.file_handler)
        self.app_log.addHandler(self.stdout_handler)
        self.app_log.setLevel(level)

    def get_logger(self):
        return self.app_log

