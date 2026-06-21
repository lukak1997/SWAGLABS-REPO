
class LoginPage:



    def __init__(self,page):
        self.username_field = page.locator('[data-test="username"]')
        self.password_field = page.locator('[data-test="password"]')
        self.login_button = page.locator('[data-test="login-button"]')

        
    def write_username(self,username):        
        self.username_field.fill(username) 

    def write_password(self,password):        
        self.password_field.fill(password) 


    def click_login(self):        
        self.login_button.click() 
