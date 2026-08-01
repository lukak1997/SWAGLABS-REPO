class FooterComponent:
    def __init__(self, page):
        self.page = page
        self.footer = page.locator("footer")
        self.twitter_link = self.footer.locator("a").nth(0)
        self.facebook_link = self.footer.locator("a").nth(1)
        self.linkedin_link = self.footer.locator("a").nth(2)
        self.footer_text = self.footer.locator('[data-test="footer-copy"]')

    def get_twitter_link_href(self):
        return self.twitter_link.get_attribute("href")

    def get_facebook_link_href(self):
        return self.facebook_link.get_attribute("href")

    def get_linkedin_link_href(self):
        return self.linkedin_link.get_attribute("href")

    def get_footer_text(self):
        return self.footer_text.text_content()
