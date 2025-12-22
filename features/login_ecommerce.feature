# Created by PavithraB at 19-12-2025
Feature: Ecomerce web application test
  # Enter feature description here

  Scenario: Navigate to website and add products to cart
    Given Navigate to the url Login to website
    When Enter "washing machine LG" in the search box and click on enter
    And Fetch all the options and get whose price is less and ratings are high
    And Fetch less cost machine and add it to cart
    And Click on cart button
    Then verify the item is added to the cart
    
   @sanity
   Scenario: Navigate to website and add products to cart
    Given Navigate to the url Login to website
    When Enter "fridge samsung" in the search box and click on enter
    And Fetch all the options and get whose price is less and ratings are high
    And Fetch less cost machine and add it to cart
    And Click on cart button
    Then verify the item is added to the cart