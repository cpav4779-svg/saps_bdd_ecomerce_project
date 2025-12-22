import logging
import time
import traceback
from behave import given,when,then
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from features.pageobjects.ProductPage import ProductPage
from features.utilities import configReader
from features.utilities.logUtil import Logger
log=Logger(__name__,file_level=logging.INFO)

@given(u'Navigate to the url Login to website')
def step_impl(context):
    context.prodpage=ProductPage(context.driver)
    context.prodpage.open("url")
    context.prodpage.implicit_wait(10)
    context.prodpage.clickOnContinueShoppingLink("continue_shopping_xpath")

@when(u'Enter "{product_name}" in the search box and click on enter')
def step_impl(context,product_name):
    context.prodpage.enterProductName("search_box_xpath",product_name)
    context.prodpage.clickOnSearchBox("search_box_click_xpath")

@when(u'Fetch all the options and get whose price is less and ratings are high')
def step_impl(context):
    WebDriverWait(context.driver,20).until((
        EC.presence_of_all_elements_located((By.XPATH, configReader.readConfig("locators", "title_product_xpath")))))
    products=context.prodpage.fetch_list_of_product_elements("title_product_xpath")
    print(len(products))
    ratings=context.prodpage.fetch_list_of_rating_elements("rating_product_xpath")
    delivery_dates=context.prodpage.fetch_list_of_delivery_date_elements("deliver_date_product_xpath")
    prices=context.prodpage.fetch_list_of_prices_elements("price_product_xpath")
    addcarts=context.prodpage.fetch_list_of_addcart_elements("add_cart_xpath")
    try:
        product_data=[]
        for product,ratings,deliverydate,price,addcart in zip(products,ratings,delivery_dates,prices,addcarts):
            context.driver.execute_script("arguments[0].scrollIntoView({block: 'center'});", product)
            print(f"product name is >> {product.text} \nrating is >> {ratings.text} \ndelivery date {deliverydate.text} \n"
                  f"price is >> {price.text} \n\n")
            product_data.append({"product_name": product.text,
                                 "rating": ratings.text,
                                 "price": price.text,
                                 "cart": addcart})
    except Exception as e:
        print(e)
        print(traceback.format_exc())
        log.logger.exception(f"Exception occurred: {e}, traceback: {traceback.format_exc()}")
    else:
        print(product_data)
        context.min_price_max_rating = min(
            (p for p in product_data if p['rating'] == max(prod['rating'] for prod in product_data)),
            key=lambda x: x['price'])


@when(u'Fetch less cost machine and add it to cart')
def step_impl(context):
    print(f"printing min price {context.min_price_max_rating['price']} with highest "
          f"ratings {context.min_price_max_rating['rating']} and product name is "
          f"{context.min_price_max_rating['product_name']}")

@when(u'Click on cart button')
def step_impl(context):
    try:
        cart_el = context.min_price_max_rating['cart']
        context.driver.execute_script("arguments[0].scrollIntoView({block: 'center'});", cart_el)
        WebDriverWait(context.driver, 20).until(EC.element_to_be_clickable((By.XPATH, configReader.readConfig("locators", "cart_xpath"))))
        cart_el.click()
    except Exception as e:
        print(e)
        print(traceback.format_exc())


@then(u'verify the item is added to the cart')
def step_impl(context):
    time.sleep(10)
    context.driver.refresh()
    try:
        # Scroll to the top of the page
        context.driver.execute_script("window.scrollTo(0, 0);")
        WebDriverWait(context.driver,10).until(EC.visibility_of_element_located((
            By.XPATH,configReader.readConfig("locators", "cart_xpath"))))
        count = context.prodpage.find_cart_count("cart_xpath")
        log.logger.info(f"printing no. of product added to cart {count.text}")
        print("printing no. of product added to cart",count.text)
        assert count.text == "1"
    except Exception as e:
        print(traceback.format_exc(), e)

