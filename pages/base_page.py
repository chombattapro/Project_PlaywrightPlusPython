BASE_URL = "https://www.saucedemo.com"

class BasePage:
    def __init__(self, page):
        self.page = page
        self.url = BASE_URL

    def open(self):
        if self.url:
            self.page.goto(self.url)
        else:
            raise ValueError("URL not set for this page")



