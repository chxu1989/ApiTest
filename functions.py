import random
import string
import hashlib
import yaml
import time
import datetime
from exceptions import ParamsError


def gen_random_string(str_len):
    """
    generate random string with specified length
    """
    return ''.join(random.choice(string.ascii_letters + 
        string.digits) for _ in range(str_len))


def gen_md5(*args):
    """

    """
    return hashlib.md5(''.join(args).encode('utf-8')).hexdigest()


def get_timestapm(str_len=13):
    """
    get timestamp string, length can only between 0 and 16
    """
    if isinstance (str_len, int) and 0 < str_len < 17:
        return str(time.time()).replace(".", "")[:str_len]
    raise ParamsError("timestamp length can only between 0 and 16.")


def get_current_date(fmt="%Y-%m-%d"):
    """
    get current date, default format is %Y-%m-%d
    """
    return datetime.datetime.now().strftime(fmt)


def sleep(n_secs):
    """ 
    sleep n seconds
    """
    time.sleep(n_secs)