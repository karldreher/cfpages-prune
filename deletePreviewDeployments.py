import requests
import os
import argparse

argparser = argparse.ArgumentParser()
argparser.add_argument("--redact", action="store_true", default=False, required=False, help="When \"--redact\" is used, project names will be replaced with IDs in log output.")
argparser.add_argument("--whatif", action="store_true", default=False, required=False, help="When \"--whatif\" is used, delete action will be deferred.")

ACCOUNT_ID = os.environ["ACCOUNT_ID"]
AUTH_EMAIL = os.environ["AUTH_EMAIL"]
API_KEY = os.environ["API_KEY"]

globalHeaders = {
    "content-type": "application/json;charset=UTF-8",
    "X-Auth-Email": AUTH_EMAIL,
    "X-Auth-Key": API_KEY
}

accountUrl = "https://api.cloudflare.com/client/v4/accounts/{0}".format(ACCOUNT_ID)

def getProjects():
    projects = requests.get(accountUrl + "/pages/projects", headers=globalHeaders)
    return projects.json()

def eligibleToDelete(deployment):
    if deployment["environment"] == "production":
        return False
    if deployment["aliases"] == None:
        return True

def deleteProjectRevisions(projectName, args):
    projectIdentifier = project["id"] if vars(args).get("redact") == True else project["name"]
    whatIf = "Would take action: " if vars(args).get("whatif") == True else ""
    
    #although projectIdentifier allows redacting project name, it is still mandatory for api calls.
    projectName = project["name"]

    deployments = requests.get(accountUrl + "/pages/projects/" + projectName + "/deployments", headers=globalHeaders)
    deploymentsToDelete = filter(eligibleToDelete,deployments.json()["result"])

    for deployment in deploymentsToDelete:
        print("{2}Deleting deployment '{0}' from project '{1}'...".format(deployment["id"], projectIdentifier, whatIf))
        deleteEndpoint = accountUrl + "/pages/projects/" + projectName + "/deployments/" + deployment["id"]
        if vars(args).get("whatif") == False:
            deleteRequest = requests.delete(deleteEndpoint, headers=globalHeaders)
            if(deleteRequest.json()["success"] == True):
                print("Delete request for deployment '{0}' was successful.".format(deployment["id"]))
            else:
                print("Delete request for deployment '{0}' was not successful.  Additional information from the request is included below.".format(deployment["id"]))
                print(deleteRequest.json())

if __name__=="__main__":

    args = argparser.parse_args()

    projects = getProjects()
    for project in projects["result"]:
        deleteProjectRevisions(project, args)
    if vars(args).get("whatif") == True:
        print("\nWhat if scenario: No action taken.")
