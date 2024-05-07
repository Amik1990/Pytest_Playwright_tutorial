
def test_bing(page):
    page.goto("https:/bing.com")
    breakpoint()

#Když chci aktivovat debugger tak musím vždy napsat breakpoint()

#Spuštění:
#pytest test_debug.py --browser chromium --headed
# V terminálu dole se zobrazí zkratka (Pdb). Tam mohu zkoušek příkazy na tlačítka, které jsem vygeneroval přes codegen příkaz
#např:
#page.get_by_label("Enter your search term").click()

# Když chci odejít z debugg modu, tak  napíšu exit


