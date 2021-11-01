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


def getProjects():
    projects = requests.get("https://api.cloudflare.com/client/v4/accounts/" + ACCOUNT_ID + "/pages/projects", headers=globalHeaders)
    return projects.json()

def eligibleToDelete(deployment):
    if deployment["environment"] == "production":
        return False
    if deployment["aliases"] == None:
        return True

def deleteProjectRevisions(projectName):
    deployments = requests.get("https://api.cloudflare.com/client/v4/accounts/" + ACCOUNT_ID + "/pages/projects/" + projectName + "/deployments", headers=globalHeaders)
    deploymentsToDelete = filter(eligibleToDelete,deployments.json()["result"])

    for deployment in deploymentsToDelete:
        print("Deleting {0} from project '{1}'...".format(deployment["id"],projectName))
        endpoint = "https://api.cloudflare.com/client/v4/accounts/" + ACCOUNT_ID + "/pages/projects/" + projectName + "/deployments/" + deployment["id"]
        deleteRequest = requests.delete(endpoint, headers=globalHeaders)
        if(deleteRequest.json()["success"] == True):
            print("Delete request was successful.")
        else:
            print("Delete request was not successful.  Additional information from the request is included below.")
            print(deleteRequest.json())

if __name__=="__main__":

    projects = getProjects()
    for project in projects["result"]:
        projectName = project["name"]
        deleteProjectRevisions(projectName)
