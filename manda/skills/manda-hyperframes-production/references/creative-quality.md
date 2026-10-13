# Manda creative quality

The user wants authored, lively motion design with a musical bed and synchronized
sound, not merely a technically correct sequence of interface cards. This is a
creative target, not a promise to match a named model or an unseen reference.
Respect an explicit brief that overrides these defaults.

## Direction before code

State a concrete concept: what changes on screen, why it expresses the message,
and what visual device connects the beats. Prefer one distinctive idea to a
collection of effects. Record palette, type roles, texture/material, spatial
hierarchy and motion character. Use actual brand assets where provided.

For each storyboard beat, describe the focal object, transformation, entry/hold/
exit, transition handoff, narration window and sound cue. Avoid three identical
centered panels with replacement text. Vary scale and framing with purpose;
negative space and quiet moments are part of the rhythm. Decorative layers must
support the content rather than disguise a generic layout.

Before full rendering, inspect representative style frames and a short motion
preview. Fix weak hierarchy or indistinct concepts before polishing microdetails.
Do not require a new user approval for each internal preview.

## Motion direction

Use anticipation, acceleration, settling and stagger where the action calls for
them. Tune easing to mass and meaning rather than applying one elastic preset
everywhere. A task card that becomes a response and then a reminder should retain
a visual identity through the transformation. Use masks, shared objects, depth
or camera reframing selectively; do not add arbitrary zooms or 3D to look busy.

Lead the eye through a clear hierarchy. Hold important words long enough to read
at mobile scale. Preserve the brief's minimum text sizes and safe zones. Avoid
constant looping motion competing with the narration. Render-seek determinism
and actual MP4 inspection remain mandatory.

## Music and sound design

Plan an instrumental bed with a deliberate mood, tempo, beginning and ending.
Music must be perceptible in the final mix, especially between phrases, while
speech remains foregrounded. Duck the bed beneath speech; use short fades and
leave room around consonants. Do not apply one very low constant gain and call
that a finished mix. Existing technical peak/loudness limits remain in force.

Choose sounds for actions: a soft movement accent for a card transfer, a short
tactile click for validation, a restrained tonal resolution for completion.
Place onset/peak against the visual event; do not paste the same whoosh on every
entrance. Avoid meme effects, persistent UI beeping and excessive impacts.

Use `media-use` to inspect available reusable assets and record origin, license
and any required attribution. Freeze actual media locally. Reuse suitable
authorized assets first. An original procedural score is allowed if it has a
real rhythmic/harmonic structure and is declared as such; a flat sine drone is
not an acceptable substitute for a requested music bed. Do not invent a license,
download arbitrary copyrighted tracks, access secrets or buy media autonomously.
If no suitable permitted asset is available, report the missing asset instead of
silently omitting music. The orchestrator still exclusively owns TTS generation.

Preserve voice, music and SFX stems. Write `qa/sound-design.json` with:

- `videoSha256`: the hash of the final MP4 assessed;
- `music`: local asset/stem paths, origin/license, time range and mix treatment;
- `effects`: local paths, origin/license, cue time and corresponding action;
- `mixEvidence`: reproducible checks of source presence, timing, nonzero stem
  levels, gain/ducking automation and final integrated loudness/true peak;
- `listening`: whether listening was actually performed, how, and limitations.

These are evidence, not an automatic aesthetic pass. Do not claim listening
from FFprobe, a waveform, source code or a transcript.

## Creative review standard

Assess four things with timecoded evidence: specificity of visual direction,
motion/transition craft, visual rhythm/readability, and music/SFX integration.
Compare against the actual storyboard and brief, not an imaginary reference.
Technical success alone is insufficient. Return `revise` for generic repeated
layouts, unmotivated motion, missing requested music, sounds absent from the
final mix, mismatched cues or a weak ending that can be corrected by the creator.

Use `blocked` only when essential evidence, assets or inspection capability is
missing; explain the exact dependency. Sampling cannot prove every frame, but
adequate samples covering meaningful motion plus real geometry evidence need not
be rejected solely because they are not continuous playback. Escalate precisely
where uncertainty affects the verdict.

If perceptual audio review is unavailable, report it prominently as unassessed.
Do not award a listening verdict or claim professional sound quality based only
on measurements. The final user audition remains the perceptual acceptance test.
Keep fixes bounded to the existing two repair rounds; do not change the approved
story or regenerate narration simply to pursue an aesthetic preference.
