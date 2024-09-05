import logging
import os
from dataclasses import dataclass

log = logging.getLogger(__name__)


@dataclass
class ProjectFilter:
    def __init__(self, args) -> None:
        self.projects = (
            vars(args).get("projects") if vars(args).get("projects") else None
        )
        self.projectids = (
            vars(args).get("projectids") if vars(args).get("projectids") else None
        )


@dataclass
class Configuration:
    def __init__(self):
        self.account_id = os.environ.get("CF_ACCOUNT_ID")
        self.auth_email = os.environ.get("CF_AUTH_EMAIL")
        self.api_key = os.environ.get("CF_API_KEY")
        self.headers = {
            "content-type": "application/json;charset=UTF-8",
            "X-Auth-Email": self.auth_email,
            "X-Auth-Key": self.api_key,
        }

        self.account_url = (
            f"https://api.cloudflare.com/client/v4/accounts/{self.account_id}"
        )

        if not all(list(self.__dict__.values())):
            log.error(
                "One or more values are not set properly.  CF_ACCOUNT_ID, CF_AUTH_EMAIL, and CF_API_KEY must be set as environment variables."
            )
            log.error("Current configuration: %s", redact(self.__dict__))


def redact(config_dict: dict):
    """
    Redact a dictionary to remove api keys from logs.
    """
    # This is an alternative implementation from the reccomended approach,
    # which is to create a custom formatter.
    # This is OK for now.
    new_dict = {}
    for k in config_dict:
        if k == "api_key":
            new_dict["api_key"] = "<REDACTED>"
        elif k == "headers":
            # We don't need this because it is derived from the environment vars.
            pass
        else:
            new_dict[k] = config_dict.get(k)
    return new_dict
