import requests
import os

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

def deleteProjectRevisions(projectName):
    deployments = requests.get(accountUrl + "/pages/projects/" + projectName + "/deployments", headers=globalHeaders)
    deploymentsToDelete = filter(eligibleToDelete,deployments.json()["result"])

    for deployment in deploymentsToDelete:
        print("Deleting deployment '{0}' from project '{1}'...".format(deployment["id"], projectName))
        deleteEndpoint = accountUrl + "/pages/projects/" + projectName + "/deployments/" + deployment["id"]
        deleteRequest = requests.delete(deleteEndpoint, headers=globalHeaders)
        if(deleteRequest.json()["success"] == True):
            print("Delete request for deployment '{0}' was successful.".format(deployment["id"]))
        else:
            print("Delete request for deployment '{0}' was not successful.  Additional information from the request is included below.".format(deployment["id"]))
            print(deleteRequest.json())

if __name__=="__main__":

    projects = getProjects()
    for project in projects["result"]:
        projectName = project["name"]
        deleteProjectRevisions(projectName)
