# Local production lessons

These are Manda defaults derived from Content Studio productions, not universal
platform specifications. A project's explicit approved brief can refine them.

For a vertical 1080 x 1920 film:

- Important elements begin at y=150 or lower; principal title around y=220.
- Keep the bottom 400 pixels free of essential content; captions end by y=1520.
- Logos and CTAs preferably end before y=1320 when captions are present.
- Keep 60 pixels on the left; reserve roughly 150 on the right in the lower
  half for social-platform controls. Inspect the intended platform overlay.
- Captions use at most two or three lines; do not duplicate every spoken phrase
  when the animated typography already communicates it.

Narration is supported by visual transformations, not an endless transcript.
Start with a clear curiosity or concrete business problem, develop consequence,
show a useful resolution or real evidence, then a short CTA. Introduce new
information or a meaningful transformation roughly every 1–3 seconds while
preserving reading time. A contrast break or pause can renew attention.

Use one accent consistently. Manda IA defaults to its violet identity when no
different brand direction is supplied. Inspiration from another film is not
permission to copy its media, screenshots, soundtrack, or compositions.

Sound and timing lessons:

- Orus is the preferred French voice, subject to current provider support.
  Do not silently substitute a model or voice when unavailable.
- Validate a voice pilot and reuse its cached bytes. Cache identity includes
  text, model, voice, instructions, format, and conversion version.
- A timed-out paid POST may already be billed: do not retry automatically.
- Use FFprobe durations, keep phrase pauses explicit, and preserve a separate
  narration track. Do not claim word alignment based on character ratios.
- A passing audio measurement is not proof of natural pronunciation. If no
  listening-capable reviewer assessed it, state that limitation.

Validation lessons:

- Generic text checks missed illustrated panels colliding during transitions;
  explicit pair tests and actual-frame inspection were necessary.
- Tests must consider inherited opacity/visibility and intentional containment;
  overlapping backgrounds are not automatically defects.
- Include transition boundaries, CTA, last frame, and long text in evidence.
- Review maintainability warnings explicitly. Never call a render fully clean
  just because errors are absent while unresolved warnings remain.

Provenance inspected on 2026-10-12: `content-studio/VIDEO_PRODUCTION_RULES.md`,
`docs/hyperframes-motion-pipeline.md`, `videos/manda-ia-trois-questions/tools/`,
and `videos/meckia-launch/BRIEF.md`. These lessons exclude the retired Remotion
project and the historical CapCut dashboard workflow.
