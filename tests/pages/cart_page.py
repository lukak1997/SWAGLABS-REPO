class CartPage:
    def __init__(self, page):
        self.page = page
        self.page_title = page.locator('[data-test="title"]')
        self.cart_items = page.locator('[data-test="inventory-item"]')
        self.continue_shopping_button = page.locator('[data-test="continue-shopping"]')
        self.checkout_button = page.locator('[data-test="checkout"]')

    def get_item_count(self):
        return len(self.cart_items.all())

    def find_item_by_name(self, desired_title):
        for item in self.cart_items.all():
            item_name = item.locator('[data-test="inventory-item-name"]')
            if item_name.text_content().strip() == desired_title:
                return item
        return None

    def is_item_in_cart(self, desired_title):
        return self.find_item_by_name(desired_title) is not None

    def get_item_names(self):
        item_names = []
        for item in self.cart_items.all():
            item_name = item.locator('[data-test="inventory-item-name"]')
            item_names.append(item_name.text_content().strip())
        return item_names

    def remove_item(self, desired_title):
        item = self.find_item_by_name(desired_title)
        if item is None:
            raise AssertionError(f"Item '{desired_title}' was not found in the cart")
        remove_button = item.locator('[data-test^="remove-"]')
        remove_button.click()

    def click_continue_shopping(self):
        self.continue_shopping_button.click()

    def click_checkout(self):
        self.checkout_button.click()
        



        