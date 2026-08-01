class ProductPage:
    def __init__(self,page):
        self.page=page
        self.product_title = page.locator('[data-test="inventory-item-name"]')
        self.product_price= page.locator('[data-test="inventory-item-price"]') 
        self.add_to_cart_button = page.locator('[data-test="add-to-cart"]')
        self.back_to_products_button = page.locator('[data-test="back-to-products"]')



    def get_product_title(self):
        return self.product_title.text_content()
    

    def get_product_price(self):
        return self.product_price.text_content()
    
    def click_add_to_cart(self):
        self.add_to_cart_button.click()

    def click_back_to_products(self):
        self.back_to_products_button.click()    






    


        
        

 