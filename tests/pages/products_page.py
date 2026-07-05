import time
class ProductsPage:
    def __init__(self,page):
        self.burger_menu_icon=page.locator('[id="react-burger-menu-btn"]')
        self.title=page.locator(".app_logo")
        self.cart_icon = page.locator('[data-test="shopping-cart-link"]') 
        self.drop_down_button= page.locator('[data-test="product-sort-container"]')
        self.product_items=page.locator('[data-test="inventory-item"]')
        


    def click_menu(self):
        self.burger_menu_icon.click()


    def click_cart_icon(self):
        self.cart_icon.click()  


    def get_product_count(self):
        products= self.product_items.all()
        return len(products)
    
    def find_product_by_name(self,desired_title):
        
        products= self.product_items.all()
        for item in products:
            item_name=item.locator('[data-test="inventory-item-name"]') 
            actual_title = item_name.text_content()
            if actual_title == desired_title:
                return item
             

    def click_add_to_cart_button(self,desired_title):
        item_box = self.find_product_by_name(desired_title)
        button = item_box.locator('[data-test^="add-to-cart"]')
        button.click()

    def click_remove_from_cart_button(self,desired_title):
        item_box = self.find_product_by_name(desired_title)
        button = item_box.locator('[data-test^="remove-sauce-labs"]')
        button.click()

        

        
        









