import pytest


# Když chci spustit pouze jeden konkrétní browser:
@pytest.mark.only_browser("chromium")
def test_youtube(page):
    page.goto("https://youtube.com")


#pytest test_only_browser.py --browser chromium --browser firefox --browser webkit --headed

# Pokud na konec příkazu napíšu -v, tak se mi zobrazí podrobnější výsledek testu
#pytest test_only_browser.py --browser chromium --browser firefox --browser webkit --headed -v

# Když napíšu do terminálu následující, tak se mi spustí věechny testy ve složce a vytvoří se složka test-results
#pytest --browser chromium --headed --video on
