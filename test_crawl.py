import unittest
from crawl import normalize_url, get_heading_from_html, get_first_paragraph_from_html


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

    def test_get_heading_from_html(self):
        test_cases = [
            (
                "H1 present",
                "<html><body><h1>Main Heading</h1></body></html>",
                "Main Heading",
            ),
            (
                "H2 fallback",
                "<html><body><h2>Secondary Heading</h2></body></html>",
                "Secondary Heading",
            ),
            (
                "H1 and H2 present",
                "<html><body><h1>Main Heading</h1><h2>Secondary Heading</h2></body></html>",
                "Main Heading",
            ),
            (
                "Neither H1 nor H2 present",
                "<html><body><p>Some text</p></body></html>",
                "",
            ),
            (
                "Empty HTML",
                "",
                "",
            ),
            (
                "Empty H1",
                "<html><body><h1></h1></body></html>",
                "",
            ),
            (
                "Empty H2",
                "<html><body><h2></h2></body></html>",
                "",
            ),
            (
                "Multiple H1 tags",
                "<html><body><h1>First Heading</h1><h1>Second Heading</h1></body></html>",
                "First Heading",
            ),
            (
                "H2 present alongside other tags",
                "<html><body><p>Intro</p><h2>Section Heading</h2><p>Content</p></body></html>",
                "Section Heading",
            ),
        ]

        for i, (test_name, input_html, expected) in enumerate(test_cases, start=1):
            with self.subTest(test_number=i, test_name=test_name):
                actual = get_heading_from_html(input_html)
                self.assertEqual(actual, expected)

    def test_get_first_paragraph_from_html(self):
        test_cases = [
            (
                "First paragraph",
                "<html><body><p>First paragraph</p></body></html>",
                "First paragraph",
            ),
            (
                "Multiple paragraphs",
                "<html><body><p>First paragraph</p><p>Second paragraph</p></body></html>",
                "First paragraph",
            ),
            (
                "Main tag present",
                "<html><body><main><p>Main paragraph</p></main></body></html>",
                "Main paragraph",
            ),
            (
                "Multiple paragraphs inside main",
                "<html><body><main><p>First main paragraph</p><p>Second main paragraph</p></main></body></html>",
                "First main paragraph",
            ),
            (
                "Prefer paragraph inside main",
                "<html><body><p>Paragraph outside main</p><main><p>Paragraph inside main</p></main></body></html>",
                "Paragraph inside main",
            ),
            (
                "Main exists but has no paragraph",
                "<html><body><main><h1>Main heading</h1></main><p>Paragraph outside main</p></body></html>",
                "Paragraph outside main",
            ),
            (
                "No paragraph tag",
                "<html><body><h1>Main Heading</h1><main></main></body></html>",
                "",
            ),
            (
                "Paragraph with surrounding whitespace",
                "<html><body><p>  Hello world  </p></body></html>",
                "Hello world",
            ),
            (
                "Paragraph nested inside main",
                "<html><body><main><div><p>Nested main paragraph</p></div></main></body></html>",
                "Nested main paragraph",
            ),
            (
                "Empty paragraph",
                "<html><body><p></p><p>Second paragraph</p></body></html>",
                "",
            ),
            (
                "Empty HTML",
                "",
                "",
            ),
        ]

        for i, (test_name, input_html, expected) in enumerate(test_cases, start=1):
            with self.subTest(test_number=i, test_name=test_name):
                actual = get_first_paragraph_from_html(input_html)
                self.assertEqual(actual, expected)


if __name__ == "__main__":
    unittest.main()