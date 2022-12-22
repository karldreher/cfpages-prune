import logging
import requests
from cf_pages_delete_previews import config

log = logging.getLogger(__name__)


def get_projects(cf_config:type[config.Configuration]):
    projects = requests.get(
        cf_config.account_url + "/pages/projects", headers=cf_config.headers, timeout=5)
    if projects.ok:
        return projects.json()
    return None

def get_deployments(project_name,cf_config:type[config.Configuration]):
    deployments = requests.get(
        cf_config.account_url + "/pages/projects/" + project_name + "/deployments", headers=cf_config.headers, timeout=5)
    return deployments.json()

def delete_eligible(deployment):
    if deployment.get("environment") == "production":
        return False
    if deployment.get("aliases") is None and deployment.get("name"):
        return True
    return None

def delete_project_revisions(project, cf_config:type[config.Configuration], args):
    # although project_identifier allows redacting project name, it is still mandatory for api calls.
    project_identifier = project["id"] if vars(args).get("redact") else project["name"]
    what_if = "Would take action: " if vars(args).get("whatif") else ""

    log.info("Started working on project %s with options: %s" % (project_identifier, vars(args)))

    deployments = get_deployments(project["name"],cf_config)

    for deployment in filter(delete_eligible, deployments["result"]):
        log.info("%sDeleting deployment \'%s\' from project \'%s\'..." %
            (what_if, deployment["id"], project_identifier))

        delete_endpoint = cf_config.account_url + "/pages/projects/" + \
            project["name"] + "/deployments/" + deployment["id"]

        if not vars(args).get("whatif"):
            delete_request = requests.delete(
                delete_endpoint, headers=cf_config.headers, timeout=5)

            if delete_request.json()["success"] == True:
                log.info(
                    "Delete request for deployment '%s' was successful.", deployment["id"])
            else:
                log.error("Delete request for deployment '%s' was not successful.  Additional information from the request is included below.", deployment["id"])
                log.error(delete_request.json())

    if vars(args).get("whatif"):
        log.info("What if scenario: No action taken.")
