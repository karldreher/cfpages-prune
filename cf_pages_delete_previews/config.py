import os
from dataclasses import dataclass
import logging
log = logging.getLogger(__name__)

@dataclass
class Configuration:
    def __init__(self):
        self.account_id = os.environ.get("CF_ACCOUNT_ID")
        self.auth_email = os.environ.get("CF_AUTH_EMAIL")
        self.api_key = os.environ.get("CF_API_KEY")

        self.headers = {
            "content-type": "application/json;charset=UTF-8",
            "X-Auth-Email": self.auth_email,
            "X-Auth-Key": self.api_key
        }

        self.account_url = "https://api.cloudflare.com/client/v4/accounts/{0}".format(
            self.account_id)

        if not all(list(self.__dict__.values())):
            log.error("One or more values are not set properly.  CF_account_id, CF_auth_email, and CF_api_key must be set as environment variables.")
            log.error("Current configuration: %s",self.__dict__)
