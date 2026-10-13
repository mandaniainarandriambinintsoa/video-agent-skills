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

## Runtime integration (MCP 0.2.0)

The runtime automatically creates a representative preview in `preview-N/`,
checks it, freezes it, and uploads a private PREVIEW file to Drive. Its durable
state becomes `awaiting_approval`. The creator never writes approval itself.

ChatGPT Work reads `get_video_preview` and shows the link to the user. After
explicit acceptance, it calls `approve_video_preview` with jobId, unique actionId,
exact previewSha256 and userConfirmed=true. Corrections use
`request_video_revision` with the same jobId, current hash, a unique actionId
and feedback. Repeat the SAME actionId and input after a network timeout.
A new preview invalidates the previous acceptance. Neither tool publishes.

The runtime owns `creative-approval.json`, derived from protected job state.
It verifies frozen preview and style hashes before queuing/composing the full
film and again before final upload. Approval/revision commands are serialized.
Only awaiting approval accepts a new decision. Retries return the existing job.

Waiting and queued decisions survive restart. An interrupted external call or
render remains blocked for reconciliation: never blindly retry a paid request
or task creation. Historical completed videos stay readable without approval.

This gate prevents the orchestrator from commissioning full production without
an approval command. It relies on authenticated ChatGPT Work to obtain the actual
human response; a boolean argument is not an independent human-identity proof.
