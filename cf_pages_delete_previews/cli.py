"""Console script for cf_pages_delete_previews."""
import argparse
import sys
import logging
from cf_pages_delete_previews import lib
from cf_pages_delete_previews import config

log = logging.getLogger(__name__)
def main():
    """Console script for cf_pages_delete_previews."""
    argparser = argparse.ArgumentParser()
    argparser.add_argument("--redact", action="store_true", default=False, required=False,
                        help="When \"--redact\" is used, project names will be replaced with IDs in log output.")
    argparser.add_argument("--whatif", action="store_true", default=False, required=False,
                        help="When \"--whatif\" is used, delete action will be skipped.")

    args = argparser.parse_args()
    cf_config = config.Configuration()

    projects = lib.get_projects(cf_config)
    if projects is not None:
        for project in projects["result"]:
            lib.delete_project_revisions(project, cf_config, args)
    else:
        log.error("No projects found")

if __name__ == "__main__":
    sys.exit(main())  # pragma: no cover
