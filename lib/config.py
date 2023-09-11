import logging
from lib.loger import log_operations

log_file_name = ""
log_format = "%(asctime)s %(levelname)s %(funcName)s: %(message)s"
log_level = "INFO"
"""If we were to productionalize this code, we would also account for different log levels for ex:
log_level = {
    'dev': 'DEBUG',
    'uat': 'DEBUG',
    'prod': 'INFO'
}
"""

max_log_size = 25 * 1024 * 1024 #ie. ~25 MBs
log = log_operations(log_file_name, log_level).get_logger()


db_host = "Mysql@localhost:3306"
db_host = ""
db_port = 3306
db_name = ""
db_username = ""
db_password = ""

