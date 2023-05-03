import logging
from concurrent.futures import ThreadPoolExecutor

import requests

from cf_pages_delete_previews import config

log = logging.getLogger(__name__)
session = requests.Session()

def get_projects(cf_config:type[config.Configuration]):
    projectList = []
    projects = session.get(
        cf_config.account_url + "/pages/projects", headers=cf_config.headers, timeout=5)
    if projects.ok:
        for project in projects.json()["result"]:
            projectItem = dict(filter(lambda item: item[0] in ['name','id'], project.items()))
            projectList.append(projectItem)
        return projectList
    return None

def filter_projects(projectList:list,project_filter=config.ProjectFilter)->list:
    '''Return a list of projects that match the filter criteria.

    Args:
        projectList (list): A list of projects.
        project_filter (ProjectFilter): A filter object.

    Returns:
        list: A list of projects that match the filter criteria.
    '''
    if project_filter.projects is not None:
        project_filter = list(project_filter.projects.split(','))
        projects = filter(lambda item: item.get('name') in project_filter, projectList)
        return projects

    if project_filter.projectids is not None:
        project_filter = list(project_filter.projectids.split(','))
        projects = filter(lambda item: item.get('id') in project_filter, projectList)
        return projects
    # if no filter is specified, return all projects
    return projectList

def get_deployments(project_name,cf_config:type[config.Configuration]):
    deployments = session.get(
        cf_config.account_url + "/pages/projects/" + project_name + "/deployments", headers=cf_config.headers, timeout=5)
    return deployments.json()

def delete_eligible(deployment):
    if deployment.get("environment") == "production":
        return False
    if deployment.get("aliases") is None and deployment.get("environment")=="preview":
        return True
    return None

def delete_single_revision(deployment:str, project, project_identifier, args):
    what_if = "Would take action: " if vars(args).get("whatif") else ""

    log.info("%sDeleting deployment \'%s\' from project \'%s\'..." %
    (what_if, deployment["id"], project_identifier))

    delete_endpoint = cf_config.account_url + "/pages/projects/" + \
        project["name"] + "/deployments/" + deployment["id"]

    if not vars(args).get("whatif"):
        delete_request = session.delete(
            delete_endpoint, headers=cf_config.headers, timeout=5)

        if delete_request.json()["success"] == True:
            log.info(
                "Delete request for deployment '%s' was successful.", deployment["id"])
        else:
            log.error("Delete request for deployment '%s' was not successful.  Additional information from the request is included below.", deployment["id"])
            log.error(delete_request.json())

def delete_project_revisions(project, cf_config:type[config.Configuration], args):
    # although project_identifier allows redacting project name, it is still mandatory for api calls.
    project_identifier = project["id"] if vars(args).get("redact") else project["name"]

    log.info("Started working on project %s with options: %s" % (project_identifier, vars(args)))

    deployments = get_deployments(project["name"],cf_config)
    for deployment in filter(delete_eligible, deployments["result"]):
        with ThreadPoolExecutor(max_workers=3) as executor:
            job = executor.submit(delete_single_revision, deployment, project, project_identifier, args)

    if vars(args).get("whatif"):
        log.info("What if scenario: No action taken.")
