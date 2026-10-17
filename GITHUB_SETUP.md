# Clement Family Office — GitHub setup

This package contains the complete app source and scripts from deployed commit cf6fc1dba82f1d8c0bc05439109bcccb557b4271, plus these setup notes and a file fingerprint manifest.

Use a PRIVATE repository. The owner interface includes family-specific seeded records and instructions. This package does not export uploaded tax returns, original trust files, other vault uploads, live balances, private storage objects or authentication credentials.

## Repository contents

- src/base.html: existing owner interface and owner-specific seed / migration records.
- src/office.js: professional access UI, eight agreements, ledger, review workflows, file exchange and proposed-team onboarding.
- src/backend.js: server-side workspace authorization, document permissions, ledger validation and transaction request API.
- src/agreement-templates.json: editable professional / operating agreement templates.
- worker/index.js: generated Worker ES module with distinct owner and assigned-user portals.
- scripts/assemble.py: generate the Worker from the source files.
- scripts/make-templates.py: regenerate the initial agreement drafting templates.
- scripts/build.sh: assemble and package the Worker.
- scripts/test-office.mjs: behavioral / authorization / ledger checks.
- scripts/validate-artifact.mjs: validate the deployable Worker artifact.
- .openai/hosting.json: binding / identity for the existing Sites-hosted app.

## Verify the source

Requires Node.js with native fetch / WebCrypto support, Python 3, and Bash. No npm dependency installation is required.

    bash scripts/build.sh
    node scripts/test-office.mjs
    node scripts/validate-artifact.mjs

Do not commit live financial data, vault uploads, credentials, .env files or private keys.

## GitHub and runtime hosting

GitHub is the source repository and can support automated checks. GitHub Pages serves static files; it does not run this Worker, private R2 storage, transaction approval logic or authenticated backend. The existing app remains on its current private Sites host.

Keep the current Sites authentication gateway and R2 BUCKET binding. Do not deploy this Worker as a directly exposed public endpoint that trusts arbitrary oai-authenticated-user-* request headers. A different host requires an independently verified authentication boundary and a deliberate private-storage migration before use.

The Sites deployment helper is supplied by the Sites environment, not by this repository. Ordinary GitHub pushes do not automatically publish to Sites unless a supported connection is separately configured. The .openai manifest is not a standalone Cloudflare deployment configuration.

Global SOLN Reserve live transaction activation and automatic result posting remain disabled pending its actual authenticated interface, account mappings, signed responses and reconciliation tests. The GitHub upload will not activate that connection.

## Connect the destination

The required GitHub destination is DHCSOLN, per the owner’s correction. The connection currently reports loccommunityassociation-dev and authorizes no repositories or GitHub App installations. Connect or authorize the DHCSOLN destination and select a private repository such as DHCSOLN/clement-family-office. Supply its repository link so the prepared files can be uploaded to the correct private destination. No files have been uploaded to loccommunityassociation-dev.

Peachtree Planning is recorded as the first proposed professional team, subject to agreement. No additional user access, fiduciary appointment or bank signing power has been activated.
