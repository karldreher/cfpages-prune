# cfpages-prune

This project contains a Python script for deleting preview deployments of **all** Cloudflare Pages projects within an account.  It is intended to be run as a scheduled job, e.g. with Github Actions.

## Build

The project uses Poetry to conduct builds.  When building locally, ensure Poetry is installed:
```bash
pip --install poetry
poetry install
```

## Usage

This tool is easiest to install using Pipx, after which it can be run using a convenient name:
```bash
pipx install git+https://github.com/karldreher/cloudflare-pages-delete-revisions.git
cfpages-prune

```

The tool assumes that the following environment variables are set:

`CF_ACCOUNT_ID`

`CF_AUTH_EMAIL`

`CF_API_KEY`

These values correspond to those found in the Cloudflare account.

When using Github Actions (as is done in `.github/workflows/main.yml`), these three environment variables must be specified as [Secrets within the repository](https://docs.github.com/en/actions/security-guides/encrypted-secrets#creating-encrypted-secrets-for-a-repository).

### Options
Other options which can manipulate usage can be described succinctly using `--help`:

```
> cfpages-prune
usage: cfpages-prune [-h] [--redact] [--whatif]

optional arguments:
  -h, --help  show this help message and exit
  --redact    When "--redact" is used, project names will be replaced with IDs
              in log output.
  --whatif    When "--whatif" is used, delete action will be deferred.
```
