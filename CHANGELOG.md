# CHANGELOG

## v1.2.1 (2024-09-05)

### Fix

* fix: misc fixes (#33)

* chore: manually update versions

* fix: semantic release

* feat: add type hints

* ci: enable pylint

* ci: drop in ruff

* ci: split up jobs

* ci: fix name

* lint: ruff fixes

* lint: ruff fixes ([`f7ac139`](https://github.com/karldreher/cfpages-prune/commit/f7ac139fe4c568e5a166a1d53526863573186d92))

## v1.2.0 (2024-09-04)

### Build

* build(deps): bump certifi from 2022.12.7 to 2023.7.22 (#30)

Bumps [certifi](https://github.com/certifi/python-certifi) from 2022.12.7 to 2023.7.22.
- [Commits](https://github.com/certifi/python-certifi/compare/2022.12.07...2023.07.22)

---
updated-dependencies:
- dependency-name: certifi
  dependency-type: indirect
...

Signed-off-by: dependabot[bot] &lt;support@github.com&gt;
Co-authored-by: dependabot[bot] &lt;49699333+dependabot[bot]@users.noreply.github.com&gt; ([`9b0ee61`](https://github.com/karldreher/cfpages-prune/commit/9b0ee61f1c92bcb91ae91b47b11f752d747ed122))

### Feature

* feat: add new options (#31)

* feat: add list option

* feat: configure logging with env

* ci: bump actions versions

* feat: add option to force delete

* test: update pytest and silence warnings

* chore: bump deps

* chore: lock poetry

* fix: file

* fix: syntax

* fix: syntax

* test: fix test

* ci: update python-semantic-release

* ci: fix syntax

* docs: update docs

* ci: how on earth did codeql get enabled

* Revert &#34;ci: how on earth did codeql get enabled&#34;

This reverts commit df036582912ddb59c04c49dc9db0b3defb273309.

* ci: fix release preview

* ci: fix syntax

* fix: breaking changes

* ci: remove preview

* fix: remove option

* fix: remove deprecated options ([`e243322`](https://github.com/karldreher/cfpages-prune/commit/e243322451ca1206cfb2c0d8950433a1ef8ee7a6))

### Fix

* fix: semantic release (#32)

* build: add config settings

* Revert &#34;ci: remove preview&#34;

This reverts commit 289f7f1f7ccd16f03a1d72aa7c7828274a18e5a2.

* fix: ref

* fix: token

* ci: add verbosity ([`840bd17`](https://github.com/karldreher/cfpages-prune/commit/840bd174b2893203c84f42814f24217385214c3f))

## v1.1.0 (2023-05-03)

### Feature

* feat: Concurrency and code improvement (#29)

* feat: concurrent operation

* chore: isort

* refactor: filter_projects

* refactor: rename project_list

* refactor: get_projects

* fix: include cf_config

* refactor: redact ([`fdbacb3`](https://github.com/karldreher/cfpages-prune/commit/fdbacb3fcf78b8cafcd886483da8b1a706c7806b))

## v1.0.0 (2023-02-25)

### Breaking

* feat: specify projects  (#28)

* feat: modify get_projects for portability of return

* feat: Project parameter

* feat: Parameter for projectIDs

* feat: mutually exclusive groups

* feat: docs update

BREAKING CHANGE: Several non-backwards compatible changes were made in this update.

* feat: retire personal config

BREAKING CHANGE: Making the project more adaptable for general use

* test: expose more detail with pytest run ([`5fb3abb`](https://github.com/karldreher/cfpages-prune/commit/5fb3abbd916e68c6511582bbae8dabb0cb0645e4))

### Ci

* ci: retire release workflow (#27) ([`f1b81a7`](https://github.com/karldreher/cfpages-prune/commit/f1b81a7cb70619b56c76f0d8361e29d194d7e15a))

## v0.3.0 (2023-02-21)

### Ci

* ci: fix (#25) ([`cba72ac`](https://github.com/karldreher/cfpages-prune/commit/cba72aca7b6392cf1c17a0e29a3b55096e2b0fa3))

* ci: fix token (#24) ([`1ab32b9`](https://github.com/karldreher/cfpages-prune/commit/1ab32b9791912dcb646ffcf3202f7dc630af6f1f))

### Feature

* feat: dry run alias (#26)

* feat: allow using dry-run as well as whatif

* docs: update docs ([`73cfef5`](https://github.com/karldreher/cfpages-prune/commit/73cfef5879b543f1f40bd98fc9f4d4127fbbbdce))

## v0.2.2 (2023-02-21)

### Ci

* ci: more precisely ascertain latest tag (#22) ([`2a16641`](https://github.com/karldreher/cfpages-prune/commit/2a16641b8137db38afb070fb9c46702b5489bec5))

* ci: release (#21)

* ci: release on tag

* ci: fix secret

* fix: ci ([`356b6e8`](https://github.com/karldreher/cfpages-prune/commit/356b6e8dba98655c4d95145b7fd4c0ba25f44b52))

### Fix

* fix: secrets leakage (#23)

* fix: limit secrets exposure in logging

* test: add a test for redaction

* fix: return

* fix: tests ([`fd7e98f`](https://github.com/karldreher/cfpages-prune/commit/fd7e98fbde7bb0fe584a8cfff594d0ff67f5e2a2))

## v0.2.1 (2023-02-20)

### Fix

* fix: semver version_toml (#20) ([`dd15865`](https://github.com/karldreher/cfpages-prune/commit/dd158650f0e6791da28e3e6cf6354e4bf393c17f))

## v0.2.0 (2023-02-19)

### Chore

* chore: update semver version (#16) ([`1a43dbd`](https://github.com/karldreher/cfpages-prune/commit/1a43dbd0b70e23814a1ec201548f0fa658c32fda))

* chore: pin workflow (#14) ([`a971dc3`](https://github.com/karldreher/cfpages-prune/commit/a971dc360e956e7cd39282e873eef80532c28edc))

### Ci

* ci: fetch-depth 0 (#18) ([`4b8c430`](https://github.com/karldreher/cfpages-prune/commit/4b8c430205292908fa63c3c81216c8c94651d9ca))

* ci: pin runner version (#15)

* ci: pin workflows

* fix: version ([`f3f08bf`](https://github.com/karldreher/cfpages-prune/commit/f3f08bf8eca3f5b6b726f8017f017a6693961c8b))

### Feature

* feat: sessions (#19)

* ci: fetch-depth 0

* feat: sessionize requests

* ci: preview semantic version on PR

* fix: fetch-depth ([`c8d44ab`](https://github.com/karldreher/cfpages-prune/commit/c8d44abdf65de7c32ba29b57479d8567ded2fd85))

### Unknown

* Fix: cf api (#17)

* fix: api response

* fix: tests

* fix: attempt to repair mangled version ([`96ec960`](https://github.com/karldreher/cfpages-prune/commit/96ec960afbc0f99774fdb754e6bcf76258cfe783))

## v0.1.0 (2022-12-22)

### Ci

* ci: fix semantic release (#13) ([`a339e00`](https://github.com/karldreher/cfpages-prune/commit/a339e00f4888cb1cd215a3e2b2e4b3b9d93df08f))

* ci: fix poetry install (#12)

* ci: fix poetry install

* ci: fix poetry install ([`1cf6d55`](https://github.com/karldreher/cfpages-prune/commit/1cf6d555399cb23396a92bca8802dc46d9819ede))

### Feature

* feat: new config module (#11)

* ci: Better workflow

* feat: add config module

* lint: quality suggestions

* lint: quality suggestions

* ci: fix python-setup ([`7381601`](https://github.com/karldreher/cfpages-prune/commit/73816017e0cb2d0b599e8afc9e3b7a2fa1bc9e97))

## v0.0.1 (2022-12-21)

### Breaking

* feat!: changing the name of the cli ([`c63f496`](https://github.com/karldreher/cfpages-prune/commit/c63f496354109b1907e25af727edd11699410e1f))

### Build

* build: semver release ([`4c5fca4`](https://github.com/karldreher/cfpages-prune/commit/4c5fca49006e0192d856cfe67e738bf375f041b4))

* build: adopt poetry groups ([`2e3660f`](https://github.com/karldreher/cfpages-prune/commit/2e3660f66df10b1c93e101ecd171a8aab8d2a6aa))

* build: update python dependencies and add pyenv file ([`6e221c4`](https://github.com/karldreher/cfpages-prune/commit/6e221c461731c1e8b772e4939236c29744455176))

### Chore

* chore: commit lockfile ([`0a2a24e`](https://github.com/karldreher/cfpages-prune/commit/0a2a24e233124fd264e304dbd1704c271e0127ae))

* chore: remove unused import ([`3b560b0`](https://github.com/karldreher/cfpages-prune/commit/3b560b0435a611561be29c5c0e32052c5f534d02))

* chore: update gitignore ([`fa57b17`](https://github.com/karldreher/cfpages-prune/commit/fa57b171cf044e3bff83b8eb8b1d2e9a5518c404))

### Ci

* ci: add test pipeline ([`ad01fff`](https://github.com/karldreher/cfpages-prune/commit/ad01fffe3d1f1419f2d1aa1b657dd939c0db5c4f))

* ci: update workflow with new name ([`aebd63b`](https://github.com/karldreher/cfpages-prune/commit/aebd63b5962579cb4df7c60fb559433cc9ba8924))

### Documentation

* docs: update instructions for API Keys ([`9b2e5ff`](https://github.com/karldreher/cfpages-prune/commit/9b2e5ff5441b4b243d5e67b6c1bf93b6e8f65ac6))

* docs: make help more clear ([`e3c2ffe`](https://github.com/karldreher/cfpages-prune/commit/e3c2ffe892b4273c1138aae8e33bba258398264a))

### Feature

* feat: change variable names to avoid collision ([`3395a00`](https://github.com/karldreher/cfpages-prune/commit/3395a0066b4b70645bafbea20743301ee862d4b0))

* feat: centralize logging config and improve failure handling ([`cb25599`](https://github.com/karldreher/cfpages-prune/commit/cb255991e2897af08af3d6ba29afbe34b6f370cb))

### Fix

* fix: semver (#10) ([`4cdb09d`](https://github.com/karldreher/cfpages-prune/commit/4cdb09d7ca6bf233386e22b25ca92bea69f32a2f))

* fix: release ref (#9)

* fix: release ref

* fix: cache

* fix: cache version

* fix: remove cache ([`c4f0bf7`](https://github.com/karldreher/cfpages-prune/commit/c4f0bf7a69f17a1f7662b4411241566e07773325))

* fix: workflow syntax (#8)

* fix: workflow syntax

* fix: poetry version

* fix: install dev deps

* test: remove empty test file

* test: add environment to pytest

* fix: address environment variable names

* fix: address environment variable names ([`a0cda8c`](https://github.com/karldreher/cfpages-prune/commit/a0cda8c18a10699d8e493706bd2769f3c961cdba))

### Refactor

* refactor: minor changes from pylint ([`4b9d1b0`](https://github.com/karldreher/cfpages-prune/commit/4b9d1b009e9ebace1e280ab45d56af6e0093ca00))

### Unknown

* Merge pull request #7 from karldreher/develop

refactor: added tests, new name, and packaging improvements ([`a1b742f`](https://github.com/karldreher/cfpages-prune/commit/a1b742f70c1adc28faa1f37b9c6efaf837094901))

* update gitignore ([`24a2960`](https://github.com/karldreher/cfpages-prune/commit/24a2960b0f3d10f953f6ee33b18c27d13a3884bf))

* improve functionality from tests ([`cf2c0a4`](https://github.com/karldreher/cfpages-prune/commit/cf2c0a4f05c61906c82d5a6615b6f3d0d55306c0))

* add some tests ([`8d0e2e7`](https://github.com/karldreher/cfpages-prune/commit/8d0e2e7f68a2e5b21f62b05d8ebdf58e56df8881))

* Merge pull request #6 from karldreher/develop

Develop ([`b4042d9`](https://github.com/karldreher/cfpages-prune/commit/b4042d921b4b04f6f59fef20e4c2b65dd3a7e63a))

* Update main.yml ([`d981643`](https://github.com/karldreher/cfpages-prune/commit/d981643ff1dccbb98e3d9d37c5cb0bd1e28c0471))

* Prepare for pulling to main ([`6de64ff`](https://github.com/karldreher/cfpages-prune/commit/6de64ff6b64a41bffbdbaa5c36b9a78677bfdfad))

* Merge pull request #5 from karldreher/develop

More mature packaging ([`069d1a9`](https://github.com/karldreher/cfpages-prune/commit/069d1a9cad51fe30348321bcbb98cde6e88bd20f))

* Don&#39;t checkout, because we don&#39;t need it ([`71dbd92`](https://github.com/karldreher/cfpages-prune/commit/71dbd92871ce1f8c29d11b2ec2f3b7e18ec5f2f8))

* Turn on redacted mode ([`2426523`](https://github.com/karldreher/cfpages-prune/commit/242652311ceefe5336787211069c9e4593444b48))

* rookie mistake ([`b3459f9`](https://github.com/karldreher/cfpages-prune/commit/b3459f9f409b2a5edfa98ae9cd218599ef27171a))

* Merge pull request #4 from karldreher/packaging

More mature packaging using Poetry ([`11faf42`](https://github.com/karldreher/cfpages-prune/commit/11faf424b4ab2355377c419dd7dfd9e4c3be112b))

* Incorporate packaged install into Actions ([`0b33b87`](https://github.com/karldreher/cfpages-prune/commit/0b33b87c25b7f44bdb6a1be8688f0bbd55b09686))

* minor logging improvement ([`78bb652`](https://github.com/karldreher/cfpages-prune/commit/78bb65284d20abde656c0df8ac9215b83e507b13))

* fixed logging issue ([`555a4c9`](https://github.com/karldreher/cfpages-prune/commit/555a4c9412f758a75e04bf6fe297ef0e90615974))

* fixed some imports ([`ebbf91d`](https://github.com/karldreher/cfpages-prune/commit/ebbf91d1135cb9d22c46c395130167d8c271996f))

* Update pyproject.toml ([`b1ec64e`](https://github.com/karldreher/cfpages-prune/commit/b1ec64e78fbbd5706fe66fdcc28fe7c397ce8866))

* add pyproject.toml ([`ea2d322`](https://github.com/karldreher/cfpages-prune/commit/ea2d3224df46ca213f99aece88e696176f77c5bb))

* Update .gitignore ([`123892f`](https://github.com/karldreher/cfpages-prune/commit/123892f4235d097360deecfd5136d47ec846ac85))

* Add MIT License ([`f2a64ef`](https://github.com/karldreher/cfpages-prune/commit/f2a64ef7a89df1fa11beeb76a48cc8d579ef841d))

* changes to structure to prepare for packaging ([`6ce6882`](https://github.com/karldreher/cfpages-prune/commit/6ce6882884f30d5e558ff658531795d87588b6d4))

* moved ([`bebd7ae`](https://github.com/karldreher/cfpages-prune/commit/bebd7ae88f446c6f921c9deca256cb4228a67a6d))

* renamed ([`15b2505`](https://github.com/karldreher/cfpages-prune/commit/15b2505d95a04037ede40c26a7dfe8cb4060931e))

* Merge pull request #3 from karldreher/develop

Develop ([`6709835`](https://github.com/karldreher/cfpages-prune/commit/670983573d4b7bf7c668047028fad4befc935a1b))

* refactored get_deployment ([`f1012d6`](https://github.com/karldreher/cfpages-prune/commit/f1012d6e221e9b4b2b6b92287274bd4136e9cac4))

* how did this ever work ([`510fe82`](https://github.com/karldreher/cfpages-prune/commit/510fe82796fd5a641f30df8c0d9288156d9df868))

* Merge pull request #2 from karldreher/develop

Develop ([`1697ada`](https://github.com/karldreher/cfpages-prune/commit/1697adac8f74d092d01a71226cb9aaa6a6762b0b))

* Better style improvements from pylint

pylint made me 6.09 times as good of a python programmer today! ([`18aea92`](https://github.com/karldreher/cfpages-prune/commit/18aea92615d2ac544ad1979ef9ae818dbd89b05c))

* implement better logging ([`aa65802`](https://github.com/karldreher/cfpages-prune/commit/aa658025f5f072012d5a9a1b6d1b7d701268a220))

* Merge pull request #1 from karldreher/develop

added options ([`8392ebe`](https://github.com/karldreher/cfpages-prune/commit/8392ebef8ee026d1db463f3e2cfbb9f5fea8b0c4))

* added options ([`acddfe4`](https://github.com/karldreher/cfpages-prune/commit/acddfe492dc3b2f48aa3500b83fc8bc19eed22e4))

* consistent messages ([`f1a54b9`](https://github.com/karldreher/cfpages-prune/commit/f1a54b96e98d90bfa0a5a3ba5642a4540298aeb6))

* refactor accountUrl ([`7ca4569`](https://github.com/karldreher/cfpages-prune/commit/7ca45696c2e73411f0cf04af5ea6e7dfbd8e7ce5))

* improved logging ([`740852e`](https://github.com/karldreher/cfpages-prune/commit/740852e6bd331be7d469a261c14f16549a411bab))

* Update main.yml ([`cb9ddb9`](https://github.com/karldreher/cfpages-prune/commit/cb9ddb9ba8bcba5b55aa3633b18cd9a75b8a2e1f))

* exclude current production pages to suppress errors ([`c060cf9`](https://github.com/karldreher/cfpages-prune/commit/c060cf9d52166a6e1427d2d6edbd20947e8084c6))

* Add cron schedule ([`d32dd3a`](https://github.com/karldreher/cfpages-prune/commit/d32dd3acf2d0e42ec4e308dde26cc3347078e856))

* add secrets in actions env ([`266f947`](https://github.com/karldreher/cfpages-prune/commit/266f947d5f93970a7fa9629b3b66bd3d2c062a50))

* Create main.yml ([`1feba9d`](https://github.com/karldreher/cfpages-prune/commit/1feba9dca6829c7bd8ad12f4254959f50952fe06))

* obtain secrets from environment ([`30edeab`](https://github.com/karldreher/cfpages-prune/commit/30edeab40f0c947b4d15d4fe7d80a5fd43c8e256))

* initial commit ([`8049d73`](https://github.com/karldreher/cfpages-prune/commit/8049d73d0ebf6a866c8f9e3a18e4eb2f642ac192))

* Initial commit ([`7f99e77`](https://github.com/karldreher/cfpages-prune/commit/7f99e778a244aad13b3bd2b8e7c4c7d8d105c969))
