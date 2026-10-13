# Production contract

The job orchestrator writes the brief and invokes separate planning, composition,
and review sessions. Do not ask the user to copy prompts between applications.

`narration.json`:

```json
{
  "segments": [
    { "id": "hook", "text": "Votre première phrase." },
    { "id": "resolution", "text": "Votre deuxième phrase." }
  ]
}
```

Use 1–30 segments, unique lowercase IDs with hyphens, 1–1500 characters per
segment and at most 12000 characters total. Narration contains spoken content,
not stage instructions. Provider/model configuration belongs to the service.

The voice service supplies `voice-meta.json` containing model, voice, and a
`segments` array with `id`, `text`, `path`, `duration`, and content hash. Paths are
relative to this worktree. Compose against the delivered audio; do not change it.

Final outputs live under `renders/` and `qa/`. Supply `delivery.json`:

```json
{
  "video": "renders/final.mp4",
  "voice": "assets/audio/voiceover.wav",
  "width": 1080,
  "height": 1920,
  "fps": 30,
  "duration": 40.5,
  "scenes": [
    { "id": "hook", "start": 0, "end": 4.5 },
    { "id": "resolution", "start": 4.5, "end": 40.5 }
  ],
  "checks": {
    "hyperframes": "qa/hyperframes.json",
    "geometry": "qa/geometry.json"
  }
}
```

The numbers above illustrate the schema, not a required story or duration.
Scene boundaries must cover the film and reflect its real montage. The geometry
report records selectors, sampling method, timings, exceptions, and findings;
do not supply a bare `passed: true` with no evidence.

The orchestrator verifies the final MP4 and writes `qa/media.json`, extracted
frames and their timestamps. A separate reviewer reads the brief, checks,
source composition, and actual frames; only that session writes `qa/review.json`.
The orchestrator binds QA to the actual video SHA-256 before upload. Any change
after review invalidates delivery. Drive links are returned only after upload
and metadata verification succeed. The uploader never makes files public.

Blocked/missing audio, failed checks, missing frames, uncertain visual review,
or missing Drive access must remain visible statuses. Never relabel them ready.
