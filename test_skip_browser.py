import pytest

#Když budu chtí přeskočit jeden prohlížeč, tak použiju fixture níže:
@pytest.mark.skip_browser("chromium")
def test_youtube(page):
    page.goto("https://youtube.com")


#pytest test_skip_browser.py --browser chromium --browser firefox --browser webkit --headed
