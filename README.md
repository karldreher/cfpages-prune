# cloudflare-pages-delete-revisions

This project contains a Python script for deleting preview deployments of **all** Cloudflare Pages projects within an account.  It is intended to be run as a scheduled job, e.g. with Github Actions.

## Usage

```bash
pip3 install -r requirements.txt
python3 deletePreviewDeployments.py

```
This assumes that the following environment variables are set: 

`ACCOUNT_ID` 

`AUTH_EMAIL` 

`API_KEY` 

When using Github Actions (as is done in `.github/workflows/main.yml`), these three environment variables must be specified as Secrets within the repository.

### Options
Other options which can manipulate usage can be described succinctly using `--help`: 

```
> python deletePreviewDeployments.py --help 
usage: deletePreviewDeployments.py [-h] [--redact] [--whatif]

optional arguments:
  -h, --help  show this help message and exit
  --redact    When "--redact" is used, project names will be replaced with IDs
              in log output.
  --whatif    When "--whatif" is used, delete action will be deferred.
```
