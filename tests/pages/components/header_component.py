
class HeaderComponent:


    def __init__(self, page):
        self.burger_menu = page.locator('[id="react-burger-menu-btn"]')
        self.title = page.locator("xpath=//div[contains(text(),'Swag Labs')]")
        self.cart = page.locator('data-test="shopping-cart-link"')
        
        




