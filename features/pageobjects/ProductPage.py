from features.pageobjects.BasePage import BasePage


class ProductPage(BasePage):
    def __init__(self,driver):
        super().__init__(driver)

    def open(self,url):
        self.openUrl(url)

    def clickOnContinueShoppingLink(self,locator):
        self.clickElement(locator)

    def clickOnSearchBox(self,locator):
        self.clickElement(locator)

    def enterProductName(self,locator,value):
        self.type(locator, value)

    def explicit_wait(self,time):
        self.explicit_wait_object(time)

    def find_cart_count(self,locator):
        element=self.find_the_element(locator)
        return element

    def fetch_list_of_product_elements(self,locator):
        elements=self.find_the_elements(locator)
        return elements


    def fetch_list_of_rating_elements(self,locator):
        elements=self.find_the_elements(locator)
        return elements

    def fetch_list_of_delivery_date_elements(self,locator):
        elements = self.find_the_elements(locator)
        return elements

    def fetch_list_of_prices_elements(self,locator):
        elements = self.find_the_elements(locator)
        return elements

    def fetch_list_of_addcart_elements(self,locator):
        elements = self.find_the_elements(locator)
        return elements

