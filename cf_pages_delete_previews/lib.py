import os
import logging
import sys
import requests
log = logging.getLogger(__name__)
log.info("Hello Logging")

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
    if projects.ok:
        return projects.json()
    else:
        return None

def get_deployments(project_name):
    deployments = requests.get(
        ACCOUNT_URL + "/pages/projects/" + project_name + "/deployments", headers=globalHeaders)
    return deployments.json()

def delete_eligible(deployment):
    if deployment.get("environment") == "production":
        return False
    if deployment.get("aliases") is None and deployment.get("name"):
        return True
    return None

def delete_project_revisions(project, args):
    # although project_identifier allows redacting project name, it is still mandatory for api calls.
    project_identifier = project["id"] if vars(args).get("redact") else project["name"]
    what_if = "Would take action: " if vars(args).get("whatif") else ""

    log.info("Started working on project %s with options: %s" % (project_identifier, vars(args)))

    deployments = get_deployments(project["name"])
    deployments_to_delete = filter(delete_eligible, deployments["result"])

    for deployment in deployments_to_delete:
        log.info("%sDeleting deployment \'%s\' from project \'%s\'..." %
            (what_if, deployment["id"], project_identifier))

        delete_endpoint = ACCOUNT_URL + "/pages/projects/" + \
            project["name"] + "/deployments/" + deployment["id"]

        if not vars(args).get("whatif"):
            delete_request = requests.delete(
                delete_endpoint, headers=globalHeaders)

            if delete_request.json()["success"] == True:
                log.info(
                    "Delete request for deployment '%s' was successful.", deployment["id"])
            else:
                log.error("Delete request for deployment '%s' was not successful.  Additional information from the request is included below.", deployment["id"])
                log.error(delete_request.json())

    if vars(args).get("whatif"):
        log.info("What if scenario: No action taken.")
