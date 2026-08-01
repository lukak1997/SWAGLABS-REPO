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

    def select_sort_option(self,option):
        if option not in ["Price (low to high)", "Price (high to low)", "Name (A to Z)", "Name (Z to A)"]:
            raise ValueError(f"Invalid sort option: {option}. Valid options are: 'Price (low to high)', 'Price (high to low)', 'Name (A to Z)', 'Name (Z to A)'")
        self.drop_down_button.select_option(option)
        time.sleep(1)  # Wait for the sorting to take effect
            
     
    def get_prices(self,):
        products= self.product_items.all()
        prices = []

        for item in products:
            item_price =item.locator('[data-test="inventory-item-price"]')
            price_text = item_price.text_content()
            prices.append(float(price_text.replace("$", "")))  # Convert price to float for comparison
        return prices
    
    def get_names(self):
        products= self.product_items.all()
        names = []
        for item in products:
            item_name =item.locator('[data-test="inventory-item-name"]')
            name_text = item_name.text_content()
            names.append(name_text)
        return names
    


    def click_product_img(self,desired_title):
        product = self.find_product_by_name(desired_title)
        product_img = product.locator('img')  # Assuming the image is an <img> tag within the product item
        product_img.click()
        
      

             
             
            
     

    







                
























        

        
        









