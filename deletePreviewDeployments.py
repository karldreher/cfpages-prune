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

def notAlias(deployment):
    if deployment["aliases"] == None:
        return True

def deleteProjectRevisions(projectName):
    deployments = requests.get("https://api.cloudflare.com/client/v4/accounts/" + ACCOUNT_ID + "/pages/projects/" + projectName + "/deployments", headers=globalHeaders)
    deploymentsToDelete = filter(notAlias,deployments.json()["result"])
    for deployment in deploymentsToDelete:
        endpoint = "https://api.cloudflare.com/client/v4/accounts/" + ACCOUNT_ID + "/pages/projects/" + projectName + "/deployments/" + deployment["id"]
        deleteRequest = requests.delete(endpoint, headers=globalHeaders)
        print(deleteRequest.json())


if __name__=="__main__":

    projects = getProjects()
    for project in projects["result"]:
        projectName = project["name"]
        deleteProjectRevisions(projectName)
