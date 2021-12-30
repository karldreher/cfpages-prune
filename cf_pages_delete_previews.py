import os
import argparse
import logging
import sys
import requests

logging.Formatter('%(asctime)s %(levelname)s - %(message)s', style='{')
file_handler = logging.FileHandler(filename=__file__ + ".log")
stdout_handler = logging.StreamHandler(sys.stdout)
logging_handlers = [file_handler, stdout_handler]
logging.basicConfig(handlers=logging_handlers, format='%(asctime)s %(levelname)s - %(message)s',
                    level='INFO', datefmt='%Y-%m-%d %I:%M:%S %p')

argparser = argparse.ArgumentParser()
argparser.add_argument("--redact", action="store_true", default=False, required=False,
                       help="When \"--redact\" is used, project names will be replaced with IDs in log output.")
argparser.add_argument("--whatif", action="store_true", default=False, required=False,
                       help="When \"--whatif\" is used, delete action will be deferred.")

ACCOUNT_ID = os.environ["ACCOUNT_ID"]
AUTH_EMAIL = os.environ["AUTH_EMAIL"]
API_KEY = os.environ["API_KEY"]

globalHeaders = {
    "content-type": "application/json;charset=UTF-8",
    "X-Auth-Email": AUTH_EMAIL,
    "X-Auth-Key": API_KEY
}

ACCOUNT_URL = "https://api.cloudflare.com/client/v4/accounts/{0}".format(
    ACCOUNT_ID)

def get_projects():
    projects = requests.get(
        ACCOUNT_URL + "/pages/projects", headers=globalHeaders)
    return projects.json()

def get_deployments(project_name):
    deployments = requests.get(
        ACCOUNT_URL + "/pages/projects/" + project_name + "/deployments", headers=globalHeaders)
    return deployments.json()

def delete_eligible(deployment):
    if deployment["environment"] == "production":
        return False
    if deployment["aliases"] is None:
        return True
    return None

def delete_project_revisions(project, args):
    # although project_identifier allows redacting project name, it is still mandatory for api calls.
    project_identifier = project["id"] if vars(args).get("redact") else project["name"]
    what_if = "Would take action: " if vars(args).get("whatif") else ""

    deployments = get_deployments(project["name"])
    deployments_to_delete = filter(delete_eligible, deployments["result"])

    for deployment in deployments_to_delete:
        logging.info("{2}Deleting deployment '{0}' from project '{1}'...".format(
            deployment["id"], project_identifier, what_if))
        delete_endpoint = ACCOUNT_URL + "/pages/projects/" + \
            project["name"] + "/deployments/" + deployment["id"]

        if not vars(args).get("whatif"):
            delete_request = requests.delete(
                delete_endpoint, headers=globalHeaders)

            if delete_request.json()["success"] == True:
                logging.info(
                    "Delete request for deployment '{0}' was successful.".format(deployment["id"]))
            else:
                logging.error("Delete request for deployment '{0}' was not successful.  Additional information from the request is included below.".format(
                    deployment["id"]))
                logging.error(delete_request.json())


if __name__ == "__main__":

    args = argparser.parse_args()
    logging.info("Started {0} with options: {1}".format(__file__, vars(args)))

    projects = get_projects()
    for project in projects["result"]:
        delete_project_revisions(project, args)
    if vars(args).get("whatif"):
        logging.info("What if scenario: No action taken.")
