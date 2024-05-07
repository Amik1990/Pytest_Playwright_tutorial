
# def test_visit_youtube(page, browser_type):
  #  browser_type.launch(headless=False, slow_mo=6000)
   # page.goto("https://youtube.com")


def test_visit_youtube(page):
    page.goto("https://youtube.com")

# pokud použiju druhou variantu kódu, tak musím napsat do terminálu:
#pytest --browser chromium --headed --slowmo 3000

# otevřeme se mi youtube na 3 sekundy
#Pozor, pokud nenapíšu konkrétní název souboru, tak se provedou všechny příkazy ze souborů s .py
# Proto je dobré specifikovat co přesně chci spustit: pytest test_usage.py --browser chromium --headed --slowmo 3000
