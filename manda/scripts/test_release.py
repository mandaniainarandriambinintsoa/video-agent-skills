"""Release boundary regression tests; never run downloaded skill commands."""
from pathlib import Path
import shutil
import tempfile
import unittest

from release import ROOT, payload


class ReleaseTests(unittest.TestCase):
    def setUp(self):
        self.temp = tempfile.TemporaryDirectory()
        self.addCleanup(self.temp.cleanup)
        self.root = Path(self.temp.name)
        shutil.copytree(ROOT / "manda" / "skills", self.root / "manda" / "skills")
        shutil.copy(ROOT / "LICENSE", self.root / "LICENSE")

    def test_no_upstream_in_payload(self):
        files = payload(self.root)
        self.assertEqual(sum(p.endswith("/LICENSE") for p in files), 3)
        self.assertTrue(all(p.startswith("manda-") for p in files))

    def test_unexpected_skill_rejected(self):
        (self.root / "manda" / "skills" / "video-setup").mkdir()
        with self.assertRaisesRegex(ValueError, "Unexpected"):
            payload(self.root)

    def test_executable_rejected(self):
        (self.root / "manda/skills/manda-video-reference/install.sh").write_text("exit 0")
        with self.assertRaisesRegex(ValueError, "Markdown"):
            payload(self.root)

    def test_escaping_link_rejected(self):
        p = self.root / "manda/skills/manda-video-reference/SKILL.md"
        with p.open("a") as f:
            f.write("\n[secret](../../../../LICENSE)\n")
        with self.assertRaisesRegex(ValueError, "escaping"):
            payload(self.root)


if __name__ == "__main__":
    unittest.main()
