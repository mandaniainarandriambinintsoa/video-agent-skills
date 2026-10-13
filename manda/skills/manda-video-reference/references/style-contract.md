# Reference, preview and acceptance records

Adapted from Melvynx/video-agent-skills `video-steal` and its learnings at
3c897e82fa8992ebd09ffcc3c65c5d22b0de2edd (MIT; see distributed LICENSE).
We retain measurement and comparison, not its installers, integrations or
Remotion templates. Use the already installed HyperFrames/media/audio tools.

## reference-analysis.json

Record `sources` with URL or relative local path, file SHA-256 when accessible,
rights notes and timestamped observations. Each observation records category
(layout, typography, motion, transition, rhythm, sound), evidence, measurement
method, confidence and acceptance criterion. Record unavailable material and
`audioAudition` as performed or unavailable, with actual method and limitations.
No fabricated metrics or claims of complete-frame coverage.

## preview.json

The creator records relative MP4 path, its SHA-256, actual duration, the style
reference file SHA-256, represented beat/transition, audio status and comparison
report path. Preview duration is at most five seconds unless explicitly changed.
Do not fabricate delivery.json for an incomplete full-video job.

## creative-approval.json

Only the operator writes this after an explicit user response:

```json
{
  "decision": "approved",
  "previewSha256": "actual 64-character digest",
  "styleReferenceSha256": "actual 64-character digest",
  "approvedAt": "actual ISO timestamp",
  "source": "reference to the user approval message",
  "scope": "specific film or explicitly approved reusable style"
}
```

The creator and reviewer verify both hashes against local files before a full
render/pass. Do not treat a generic authorization to install skills or start
work as creative approval. Rejection yields timestamped changes and a revised
preview, not an automatically approved new style. Preserve previous evidence.

## Current runtime integration

The existing MCP has create/status/delivery tools; it does not implement a
dedicated preview-approval endpoint or an awaiting-approval state. This release
adds an instruction-level gate, not a security boundary in the runtime.
For a new style, run reference/preview work as an isolated control-plane task
first. An existing full-film task lacking approval must stop with
`qa/creative-gate.json` (reason, missing evidence, next action), not attempt a
full render. Its current generic blocked status needs operator interpretation.
The operator carries approved artifacts into the full-film worktree and resumes
the same task only after reconciliation. Do not ask users to invent checkpoints,
alter protected job state, or repeatedly create new jobs to bypass a block.

A preview may be delivered separately as a clearly labelled review artifact by
the operator. It is never represented as a finished or publishable film.
