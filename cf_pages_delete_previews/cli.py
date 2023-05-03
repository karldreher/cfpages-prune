"""Console script for cf_pages_delete_previews."""
import argparse
import logging
import sys

from cf_pages_delete_previews import config, lib

log = logging.getLogger(__name__)
def main():
    """Console script for cf_pages_delete_previews."""
    argparser = argparse.ArgumentParser()
    # while it looks strange and out of order, args must be in the order you want them to appear in --help
    ex_group_redact = argparser.add_mutually_exclusive_group()
    ex_group_redact.add_argument("--projects","--project",action="store",required=False,help="Comma-delimited list of project names where revisions should be deleted.  Default: All projects")
    argparser.add_argument("--projectids","--projectid",action="store",required=False,help="Comma-delimited list of project IDs where revisions should be deleted.  Default: All projects")
    ex_group_redact.add_argument("--redact", action="store_true", default=False, required=False,
                        help="When \"--redact\" is used, project names will be replaced with IDs in log output.  Cannot be used in conjunction with --projects.")
    argparser.add_argument("--whatif", "--dry-run", action="store_true", default=False, required=False,
                        help="When \"--whatif\" or \"--dry-run\" is used, delete action will be skipped.")


    args = argparser.parse_args()
    cf_config = config.Configuration()
    projectFilter = config.ProjectFilter(args)

    projects = lib.get_projects(cf_config)
    if projects.__len__()!=0:
        for project in lib.filter_projects(projects,projectFilter):
            lib.delete_project_revisions(project, cf_config, args)
    else:
        log.error("No projects found")

if __name__ == "__main__":
    sys.exit(main())  # pragma: no cover
