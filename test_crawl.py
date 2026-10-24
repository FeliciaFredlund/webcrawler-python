import unittest
from crawl import normalize_url


class TestCrawl(unittest.TestCase):
    def test_normalize_url(self):
        test_cases = [
            ("HTTPS scheme", "https://www.boot.dev/blog/path", "www.boot.dev/blog/path"),
            ("Trailing slash", "http://www.boot.dev/blog/path/", "www.boot.dev/blog/path"),
            ("Already normalized URL", "www.boot.dev", "www.boot.dev"),
            ("No scheme", "www.boot.dev/blog/path", "www.boot.dev/blog/path"),
            ("Query parameters", "www.boot.dev/blog/path?query=help", "www.boot.dev/blog/path"),
            ("Port", "https://www.boot.dev:8080/blog/path", "www.boot.dev/blog/path"),
            ("Fragment", "https://www.boot.dev/blog#section", "www.boot.dev/blog"),
            ("Trailing slashes", "www.boot.dev//", "www.boot.dev"),
            ("Extra whitespace", " www.boot.dev/ ", "www.boot.dev"),
            ("Empty input", "", ""),
        ]

        for i, (test_name, input_url, expected) in enumerate(test_cases, start=1):
            with self.subTest(test_number=i, test_name=test_name):
                actual = normalize_url(input_url)
                self.assertEqual(actual, expected)


if __name__ == "__main__":
    unittest.main()