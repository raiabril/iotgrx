"""
Config class for configuring the test environment.

"""


class Config():

    # View endpoints
    AUTH_URL = 'http://testserver/auth/'
    API_URL = 'http://testserver/api'

    # Frontend test cases
    FRONTEND_URL = 'localhost:8000/api/'

    # Mozilla paths
    WEBDRIVER_PATH = '/usr/local/bin/geckodriver'
    FIREFOX_PROFILE_PATH = '~/.mozilla/firefox/d726tmxj.default/'
