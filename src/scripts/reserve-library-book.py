import os
from nova_act import NovaAct
from dotenv import load_dotenv

load_dotenv('../../.env')

with NovaAct(use_default_chrome_browser=True, starting_page="https://kcls.org/locations/bellevue//") as nova:
    nova.act("Click on the 'Log in' button")
    nova.act("Click on the green 'Log in/Register' button that appeared just below it after your previous click")
    # Focus on username field and enter via Playwright
    nova.act("Click on the Username field")
    nova.page.keyboard.type(os.getenv('LIBRARY_USERNAME', 'seanhall4217'))
    
    # Focus on password field and enter via Playwright  
    nova.act("Click on the Password field")
    nova.page.keyboard.type(os.getenv('LIBRARY_PASSWORD', '4666'))
    nova.act("Click on the 'Log in' button")

    nova.act("Search for 'The Paper Menagerie'")
    nova.act("Click 'Place Hold' for the book")
    nova.act("Click on the blue 'Place Hold' button that popped up after your previous click. If your action is successful, it will be replaced with a gray 'Cancel Hold' button. If the 'Place Hold' button is still there, you didn't actually register a click on it.")