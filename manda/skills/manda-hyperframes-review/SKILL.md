---
name: manda-hyperframes-review
description: Independently inspect rendered Manda HyperFrames videos and QA evidence before Drive delivery, checking visual collisions, clipping, safe zones, readability, timing and audio limitations. Use only for a video review phase.
---

# Independent rendered-video review

For a full film, read `style-reference.md`, `qa/style-comparison.md`,
`preview.json` and the operator-owned `creative-approval.json`. Verify approval
refers to the actual preview and style hashes and covers this film. Missing or
stale acceptance is `blocked`; passing technical checks never replaces the
user's creative acceptance. Do not write or change approval yourself.
For a preview-only review, report differences for user decision; never claim
the entire film or style has been accepted. Compare actual reference frames
with output at equivalent narrative moments and describe unassessed sound.

You are the reviewer, not the creator. Read the brief and the production skill's
creative reference. Inspect the actual extracted MP4 frames with image-viewing
tools, the timestamp manifest, the media probe, HyperFrames report, geometry
report and relevant source. Do not infer visual quality solely from code or a
creator's summary. If images cannot be viewed, return `blocked`.
Read the production skill's `references/creative-quality.md` as well. Assess
art direction, rhythm, meaningful motion, transition continuity and sound design,
not just collisions. A generic but technically valid film can require revision.

Keep production files unchanged. Write only `qa/review.json`. Do not generate
audio, repair the film, upload, publish, or claim that your review proves the
absence of every possible defect. Repairs are a subsequent creator phase.

Check every scene at start/middle/end and the transitions, including isolated
full-resolution frames where the contact sheet is too small to read. Identify
unintentional overlap, clipped glyphs, missing images/fonts, unsafe positions,
unreadable contrast, long text, mismatched evidence, blank intervals, and a CTA
that disappears too quickly. Distinguish intentional layering from collisions.
Request additional frames for uncertain transitions. A review may not pass when
important intervals are unobserved or the supplied evidence is inconsistent.

Check technical audio evidence and correspondence with narration. Never claim
to have listened if you only read a transcript or loudness measurement. Record
unassessed pronunciation/intonation explicitly in `limitations`.
Read `qa/sound-design.json`, check its MP4 hash, actual local music/SFX stems,
cue correspondence and mix evidence. Missing requested music or perfunctory
sound design calls for `revise` with concrete corrections. Use listening tools
when available; otherwise explicitly mark perceived mix quality as unassessed.
Do not claim an audio audition from numerical checks. Give a short evidence-based
assessment of each creative dimension in `limitations`, and put unresolved
correctable problems in `findings`.

The orchestrator supplies the video SHA-256 and actual evidence paths. Return:

```json
{
  "verdict": "pass",
  "videoSha256": "64 hexadecimal characters supplied for this MP4",
  "inspectedFrames": ["qa/frames/0001.png"],
  "findings": [],
  "limitations": ["Pronunciation has not been assessed by listening."]
}
```

`verdict` is `pass`, `revise`, or `blocked`. Each finding contains `severity`
(`error` or `warning`), `time` in seconds, `description`, and a concrete
`correction`. `pass` requires no unresolved findings and actual inspected images.
Do not invent image paths or copy the example hash. Use the supplied digest.
If a tool or evidence is missing, report `blocked` with the reason.
Return exactly the five documented top-level keys; no `evidenceAssessment`,
scores or extra objects. Reserve `blocked` for a missing dependency or evidence;
use `revise` for issues the creator can fix within the supplied assets and brief.
