# cfpages-prune

This project contains a Python script for deleting preview deployments of **any** (up to and including all) Cloudflare Pages projects within an account.  It is intended to be run as a scheduled job, e.g. with Github Actions.

## Build

The project uses Poetry to conduct builds.  When building locally, ensure Poetry is installed:
```bash
pip --install poetry
poetry install
```

If developing locally, it's reccomended that you install the `dev` poetry group:
```bash
poetry install --with=dev
```

## Usage

This tool is designed with CI/CD in mind, and is appropriate for automated, scheduled use.

This tool is easiest to install using Pipx, after which it can be run using a convenient name:
```bash
pipx install git+https://github.com/karldreher/cfpages-prune.git
cfpages-prune

```

The tool assumes that the following environment variables are set:

`CF_ACCOUNT_ID` - This corresponds to your Cloudflare Account ID.

`CF_AUTH_EMAIL` - The email address with access to this Cloudflare account.

`CF_API_KEY` - This **MUST** be a Global API key.  This is not a limitation of this tool, but one of the Cloudflare API.  (Pages projects **read** access currently requires this.)


### Options
Other options which can manipulate usage can be described succinctly using `--help`:

```
> cfpages-prune --help
usage: cfpages-prune [-h] [--list-projects] [--projects PROJECTS] [--projectids PROJECTIDS] [--redact] [--force] [--whatif]

options:
  -h, --help            show this help message and exit
  --list-projects       List all projects and exit. Ignores other arguments.
  --projects PROJECTS, --project PROJECTS
                        Comma-delimited list of project names where revisions should be deleted. Default: All projects
  --projectids PROJECTIDS, --projectid PROJECTIDS
                        Comma-delimited list of project IDs where revisions should be deleted. Default: All projects
  --redact              When "--redact" is used, project names will be replaced with IDs in log output. Cannot be used in
                        conjunction with --projects.
  --force               Force deletion of all revisions, including those in production environments. Use with extreme
                        caution.
  --whatif, --dry-run   When "--whatif" or "--dry-run" is used, delete action will be skipped.
```

### Safety
This tool is designed with **safety** and **privacy** in mind.
As explained by `--help`, the options `--redact` and `--whatif` are designed for DevOps engineers to mask output in a way that can be used in a multitude of environments and secure scenarios, as well as safely test.

### Usage Examples

Delete only projects in `my-cool-project` and `the-awesome-project`:
```
cfpages-prune --projects my-cool-project,the-awesome-project
```

Safely see what operations will be performed on Cloudflare project IDs 206509b1-db55-4674-8a67-ad5089cf81fc and ab2d7740-ebd2-4701-b2ff-dfb3dcbc8d29:
```
cfpages-prune --projectids 206509b1-db55-4674-8a67-ad5089cf81fc,ab2d7740-ebd2-4701-b2ff-dfb3dcbc8d29 --whatif
```
