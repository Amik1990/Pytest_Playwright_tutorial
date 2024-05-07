
def test_youtube(page):
    page.goto("https://youtube.com")

# když chci, aby se mi otevřel chrom, tak napíšu do terminálu následující:
#pytest test_more_browser.py --browser chromium --headed

# Další možnost když chci, aby se postupné spustilo víc prohlížečů:
#pytest test_more_browser.py --browser chromium --browser firefox --browser webkit --headed
