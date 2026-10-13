# Manda adaptation

Only `manda/skills/` is deployable. Upstream `skills/` is retained for history
and comparison, not loaded or installed. Do not execute its setup commands.
Keep LICENSE and UPSTREAM-README.md. Review upstream changes before copying.

Target: Codex, HyperFrames, existing Orus voice service, independent QA,
private Drive delivery, Metricool through ChatGPT Work. No Remotion or Treg.
Never put credentials, user footage, generated media or private reports in Git.
VPS access uses `meckia-vps`; agents run as codex-dev, never root, without Docker.
One sandboxed render worker. No global permission changes or remote installers.

Check edits with `python manda/scripts/release.py --check` and the installed
skill-creator quick_validate.py for each changed skill. This is a Markdown
distribution; there is no application build or TypeScript test suite.
