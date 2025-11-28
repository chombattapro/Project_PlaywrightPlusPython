class BasePage:
    base_url = "https://saucedemo.com"

    def __init__(self, page, url=None):
        self.page = page
        self.url = url or self.base_url

    def open(self):
        if self.url:
            self.page.goto(self.url)
        else:
            raise ValueError("URL not set for this page")



