
class HeaderComponent:


    def __init__(self, page):
        self.burger_menu = page.locator('[id="react-burger-menu-btn"]')
        self.title = page.locator("xpath=//div[contains(text(),'Swag Labs')]")
        self.cart = page.locator('[data-test="shopping-cart-link"]')



    def count_items_in_cart(self):
        item_count = 0
        if self.cart.text_content() == '':
            return item_count
        else:
            item_count = int(self.cart.text_content())
            return item_count
            
         
    def click_cart_icon(self):
        self.cart.click()




