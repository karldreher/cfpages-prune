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
