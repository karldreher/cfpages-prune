import os
import logging
import sys
import requests

file_handler = logging.FileHandler(filename='cf_pages_delete_previews' + '.log')
stdout_handler = logging.StreamHandler(sys.stdout)
logging_handlers = [file_handler, stdout_handler]
logging.basicConfig(handlers=logging_handlers, format='%(asctime)s %(levelname)s - %(message)s',
                    level='INFO', datefmt='%Y-%m-%d %I:%M:%S %p')

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
    
    logging.info("Started working on project %s with options: %s" % (project_identifier, vars(args)))

    deployments = get_deployments(project["name"])
    deployments_to_delete = filter(delete_eligible, deployments["result"])

    for deployment in deployments_to_delete:
        logging.info("%sDeleting deployment \'%s\' from project \'%s\'..." %
            (what_if, deployment["id"], project_identifier))
        
        delete_endpoint = ACCOUNT_URL + "/pages/projects/" + \
            project["name"] + "/deployments/" + deployment["id"]

        if not vars(args).get("whatif"):
            delete_request = requests.delete(
                delete_endpoint, headers=globalHeaders)

            if delete_request.json()["success"] == True:
                logging.info(
                    "Delete request for deployment '%s' was successful.", deployment["id"])
            else:
                logging.error("Delete request for deployment '%s' was not successful.  Additional information from the request is included below.", deployment["id"])
                logging.error(delete_request.json())

    if vars(args).get("whatif"):
        logging.info("What if scenario: No action taken.")
