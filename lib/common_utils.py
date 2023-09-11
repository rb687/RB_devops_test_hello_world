from datetime import datetime, date
from lib.config import log
import lib.config as config
from lib.sql import db_operations
import lib.constants as sql


def connect_to_db():
    db_conn_string = "mysql+pymysql://{username}:{password}@{db_host}:{db_port}/{db_name}".format(
        username=config.db_username,
        password=config.db_password,
        db_host=config.db_host,
        db_port=config.db_port,
        db_name=config.db_name
    )
    db_conn = db_operations(db_conn_string)
    if db_conn.test_conn():
        log.info("DB connection successful")
        return db_conn

    return None

def is_request_valid(req):
    #This function checks if the payload for date of birth update is valid and/or is the DOB format valid
    # We dont want to let the caller
    keys = req.keys()
    if len(keys) > 1:
        log.info("More than one key found in request " + str(keys))
        return False
    elif req.get('dateOfBirth') == None:
        log.info("'dateOfBirth' key not found in request")
        return False
    else:
        return is_dob_valid(req.get('dateOfBirth'))


def is_dob_format_valid(date_of_birth):
    try:
        date_of_birth = datetime.strptime(date_of_birth, "%Y-%m-%d")
        log.info("DOB format is valid")
        return True
    except Exception as err:
        log.warning("Encountered an exception while check if DOB is valid. Error is " + str(err))
        return False


def is_dob_before_today(date_of_birth):
    try:
        past = datetime.strptime(date_of_birth, "%Y-%m-%d")
        present = datetime.now()
        if past.date() < present.date():
            log.info("DOB is before today")
            return True
        else:
            log.info("DOB is not before today")
            return False
    except Exception as err:
        log.critical("Encountered an exception while checking if DOB is older than today. Error is " + str(err))
        return False


def is_dob_valid(date_of_birth):
    if is_dob_format_valid(date_of_birth) and is_dob_before_today(date_of_birth):
        log.info("DOB validation passed")
        return True
    else:
        log.info("DOB validation didnt pass ")
        return False


def update_db(username, date_of_birth):
    try:
        db_conn = connect_to_db()
        if db_conn:
           query = sql.UPDATE_DOB.format(username=username,
                                         dob_insert=date_of_birth,
                                         dob_update=date_of_birth)
           db_conn.execute_sql(query)
    except:
        raise


def is_username_valid(username):
    if username.isalpha():
        return True
    else:
        return False


def get_dob(username):
    try:
        db_conn = connect_to_db()
        if db_conn:
            query = sql.GET_DOB.format(username=username)
            res = db_conn.execute_sql(query)
            res = res.fetchall()
            log.info("Got the DOB for user " + username + " as " + str(res[0][0]))
            return res[0][0]
    except:
        log.error("Error occured while trying to fetch DOB for user " + username)
        raise


def get_dob_message(username):
    date_of_birth_db = get_dob(username)
    date_of_birth = datetime.strptime(date_of_birth_db, "%Y-%m-%d")
    today = date.today()
    date_of_birth = date_of_birth.replace(year=today.year).date()

    present = datetime.now().date()
    num_of_days = (date_of_birth - present).days

    if num_of_days < 0:
        # 365 days in a year + the number of days that has already gone so you want to subtract them and
        # +1 to include today in the calulation
        num_of_days = 365 + num_of_days + 1

    if num_of_days == 0:
        return "Hello, {username}! Happy Birthday!".format(username=username)
    else:
        return "Hello, {username}! Your birthday is in {days} day (s)".format(username=username,
                                                                         days=num_of_days)

    return None


def user_exists(username):
    try:
        db_conn = connect_to_db()
        if db_conn:
            query = sql.USER_EXISTS.format(username=username)
            res = db_conn.execute_sql(query)
            res = res.fetchall()
            log.info("Got the DOB for user " + username + " as " + str(res[0][0]))
            return True
    except:
        log.error("No data found for the " + username)
        return False

