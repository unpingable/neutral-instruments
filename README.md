# neutral-instruments

The small, public visual and information-language core shared by the public
instruments at `neutral.zone`. It provides tokens, typography, masthead/footer,
forms, panels, status rails, and public-page guidance. Product-specific
visualizations and workflows remain in their product repositories.

Products vendor a pinned generated snapshot from `dist/`; there is no runtime
or deployment dependency on this repository. A vendored manifest records the
source commit and content hashes, and product CI verifies local bytes without
network access.

The information-order invariant is: **the useful reading or action appears
before the machinery required to audit it; the audit path remains immediately
available and never introduces a qualification that contradicts the reading.**

See [docs/public-pages.md](docs/public-pages.md) and run
`python scripts/verify.py dist/neutral-instruments.manifest.json` to verify a
snapshot.

Current adopters: [Weatherwatch](https://weatherwatch.neutral.zone/),
[Labelwatch](https://labelwatch.neutral.zone/), and
[atproto-acl](https://atproto-acl.neutral.zone/). Each product vendors its own
copy and links back to its product source; this repository is provenance, not a
runtime dependency.

Licensed under MIT, except bundled fonts, which retain their upstream licenses.
See `THIRD_PARTY_NOTICES.md`.
