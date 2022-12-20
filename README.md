# cfpages-prune

This project contains a Python script for deleting preview deployments of **all** Cloudflare Pages projects within an account.  It is intended to be run as a scheduled job, e.g. with Github Actions.

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

This tool is easiest to install using Pipx, after which it can be run using a convenient name:
```bash
pipx install git+https://github.com/karldreher/cfpages-prune.git
cfpages-prune

```

The tool assumes that the following environment variables are set:

`CF_ACCOUNT_ID` - This corresponds to your Cloudflare Account ID.

`CF_AUTH_EMAIL` - The email address with access to this Cloudflare account.

`CF_API_KEY` - This **MUST** be a Global API key.  This is not a limitation of this tool, but one of the Cloudflare API.  (Pages projects **read** access currently requires this.)


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
  --whatif    When "--whatif" is used, delete action will be skipped.
```
