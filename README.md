# Sites Worker ESM starter

Use this starter for a static microsite, click counter, or simple internal UI whose state is browser-scoped. It has no dependencies and needs no install.

Edit `worker/index.js`, then publish through the Sites hosting workflow with this starter's build and validation in `commands`.

The build copies only `worker/index.js` and `.openai/hosting.json`. Do not add standalone asset files. Embed any essential raster bytes in `worker/index.js` and serve or reference them as a data URL.

Pass these argument arrays as `commands`:

```json
[
  ["bash", "scripts/build.sh"],
  ["node", "scripts/validate-artifact.mjs"]
]
```

The deterministic build produces:

```text
dist/
├── .openai/
│   └── hosting.json
└── server/
    └── index.js
```

`dist/server/index.js` is an ES module with a default export containing `fetch(request, env, ctx)`. Edit `worker/index.js`, not the generated file under `dist/`.

## Family / professional administration

The owner portal now includes separate household namespaces (Clement and Ghana foundation by default), individually assigned role scopes, editable agreement drafts, professional responsibility records, a balanced journal ledger, and a transaction request desk. Unassigned users receive a neutral portal without the owner's seeded family / trust information. Every API checks the current assignment server-side. A document is shared only when assigned a work-area category and the person has both document and category access. Existing Clement storage is preserved and migrated on the owner's next save; original file references remain available under the same authorization.

The access register does not send invitations or change Sites sharing. The production site stays owner-private until the owner authorizes named people. An office role is distinct from a signed professional or fiduciary appointment and from external account authority.

## Ledger and external transactions

Accounts record legal holder, currency, restrictions and reconciliation evidence. Journal lines use integer minor units (two decimals). Journals balance separately by currency and are append-only through the API; corrections use reversals. Source transaction IDs are unique within a workspace. A transaction request requires an independent finance approver. No execution endpoint is enabled. A manually evidenced external completed result can post its linked journal atomically with the request update; the result remains operator-reported, not API-confirmed.

Global SOLN Reserve is not connected. The reserve page provides a workspace-scoped JSON exchange schema, previewed file import and duplicate detection. This is the app's exchange format, not an asserted reserve API format. A verified endpoint / schema, authenticated permissions, account mapping, signed response checks, idempotency and sandbox reconciliation are required before live execution or posting results to the reserve.

## Source and checks

`src/base.html` retains the original owner interface. `src/office.js`, `src/agreement-templates.json` and `src/backend.js` implement the additional controls. `python scripts/assemble.py` generates `worker/index.js` with separate owner and member HTML. `bash scripts/build.sh` assembles and packages the worker. Run `node scripts/test-office.mjs` and `node scripts/validate-artifact.mjs` after building.

The automated checks exercise household denial, minimum document scopes, legacy migration, read / edit / approval restrictions, revocation, origin checks, immutable journals, balanced / duplicate entries, independent transaction review, disabled external execution, linked manual-result posting, and both interfaces. They use simulated storage and identities; real-user acceptance and external reserve testing remain operating-readiness work.
