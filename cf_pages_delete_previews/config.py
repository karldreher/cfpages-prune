import os
import logging
log = logging.getLogger(__name__)

class Configuration:
    def __init__(self):
        self.ACCOUNT_ID = os.environ.get("CF_ACCOUNT_ID")
        self.AUTH_EMAIL = os.environ.get("CF_AUTH_EMAIL")
        self.API_KEY = os.environ.get("CF_API_KEY")

        self.HEADERS = {
            "content-type": "application/json;charset=UTF-8",
            "X-Auth-Email": self.AUTH_EMAIL,
            "X-Auth-Key": self.API_KEY
        }

        self.ACCOUNT_URL = "https://api.cloudflare.com/client/v4/accounts/{0}".format(
            self.ACCOUNT_ID)

        if all(list(self.__dict__.values())) == False:
            log.error("One or more values are not set properly.  CF_ACCOUNT_ID, CF_AUTH_EMAIL, and CF_API_KEY must be set as environment variables.")
            log.error("Current configuration: %s",self.__dict__)
