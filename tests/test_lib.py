from cf_pages_delete_previews import lib
from cf_pages_delete_previews import config
import argparse
argparser = argparse.ArgumentParser()

class MockArgs():
    def __init__(self,projects:str=None,projectids:str=None):
        self.projects = projects
        self.projectids = projectids

def test_delete_eligible_true():
    # Test if a eligible, deletable deployment will be marked as such.
    assert lib.delete_eligible({"name":"1","deploymentID":"1","aliases":None, "environment":"preview"}) == True


def test_delete_eligible_false():
    # Test that a production deployment will not be set to eligible.
    assert lib.delete_eligible({"name":"1","deploymentID":"1","aliases":"production","environment":"production"}) == False


def test_delete_eligible_none():
    # Test that junk data will not be set as either true nor false.
    assert lib.delete_eligible({"JunkData":True,"Invalid":"probably"}) == None


projects = [{'id': '861469d7-b898-4c6a-8547-e805aad56087', 'name': 'my-cool-project'},
            {'id': '68b8d347-e97f-4043-bf37-d874c32fbce9', 'name': 'myAwesomeProject'},
            {'id': '1328afd3-92f8-4a24-9da7-c6a430176365', 'name': 'TheOtherProject1'},
            {'id': '6558f9a3-045a-4358-821d-5a58c86ae0fd', 'name': 'LeftoverProject'}]

def test_filter_projects_by_name_single():
    single_project = MockArgs("my-cool-project",None)
    assert {'id': '861469d7-b898-4c6a-8547-e805aad56087', 'name': 'my-cool-project'} in lib.filter_projects(projects,single_project)

def test_filter_projects_by_name_multiple():
    multiple_project = config.ProjectFilter(MockArgs("my-cool-project,myAwesomeProject",None))
    assert len(list(lib.filter_projects(projects,multiple_project)))==2
    filteredProjects = lib.filter_projects(projects,multiple_project)
    assert {'id': '861469d7-b898-4c6a-8547-e805aad56087', 'name': 'my-cool-project'} in filteredProjects
    assert {'id': '68b8d347-e97f-4043-bf37-d874c32fbce9', 'name': 'myAwesomeProject'} in filteredProjects
    assert {'id': '1328afd3-92f8-4a24-9da7-c6a430176365', 'name': 'TheOtherProject1'} not in filteredProjects

def test_filter_projects_by_id_single():
    single_project = MockArgs(None,"861469d7-b898-4c6a-8547-e805aad56087")
    assert {'id': '861469d7-b898-4c6a-8547-e805aad56087', 'name': 'my-cool-project'} in lib.filter_projects(projects,single_project)

def test_filter_projects_by_id_multiple():
    multiple_project = MockArgs(None,"861469d7-b898-4c6a-8547-e805aad56087,68b8d347-e97f-4043-bf37-d874c32fbce9,1328afd3-92f8-4a24-9da7-c6a430176365")
    assert len(list(lib.filter_projects(projects,multiple_project)))==3
    filteredProjects = lib.filter_projects(projects,multiple_project)
    assert {'id': '861469d7-b898-4c6a-8547-e805aad56087', 'name': 'my-cool-project'} in filteredProjects
    assert {'id': '68b8d347-e97f-4043-bf37-d874c32fbce9', 'name': 'myAwesomeProject'} in filteredProjects
    assert {'id': '6558f9a3-045a-4358-821d-5a58c86ae0fd', 'name': 'LeftoverProject'} not in filteredProjects
