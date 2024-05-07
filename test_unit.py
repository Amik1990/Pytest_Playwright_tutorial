import unittest

import pytest
from playwright.sync_api import Page


class MyTest(unittest.TestCase):
    @pytest.fixture(autouse=True)
    def setup(self, page: Page):
        self.page = page

    def test_foobar(self):
        self.page.goto("https://microsoft.com")
        self.page.get_by_label("Kupte si Surface Laptop Studio").click()
        assert self.page.evaluate("1+1") == 2


# Pokud chci otevřít generátor kódu, tak napíšu: playwright codegen microsoft.com
