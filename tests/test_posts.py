import re
import unittest
from pathlib import Path

class TestBlogPostLinks(unittest.TestCase):
    def setUp(self):
        repo_root = Path(__file__).resolve().parents[1]
        posts_js = repo_root / 'blog' / 'posts.js'
        with posts_js.open() as f:
            self.content = f.read()
        self.hrefs = re.findall(r'href:\s*"([^"]+)"', self.content)

    def test_html_files_exist(self):
        repo_root = Path(__file__).resolve().parents[1]
        for href in self.hrefs:
            path = repo_root / href
            self.assertTrue(path.exists(), f"Missing file: {href}")

if __name__ == '__main__':
    unittest.main()
