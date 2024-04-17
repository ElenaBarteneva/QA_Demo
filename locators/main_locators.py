
class MainLocators:
    SHOPPING_CART = ('xpath', '//a[@data-test="shopping-cart-link"]')
    COUNT_ITEMS = ('css selector', 'span[data-test="shopping-cart-badge"]')
    SORTING = ('xpath', '//select[@data-test="product-sort-container"]')
    PRODUCTS = ('xpath', '//div[@data-test="inventory-item"]')
    BURGER_MENU = ('id', 'react-burger-menu-btn')
    LOGOUT = ('xpath', '//a[@data-test="logout-sidebar-link"]')
    ABOUT_LINK = ('xpath', '//a[@data-test="about-sidebar-link"]')
    RESET = ('xpath', '//a[@data-test="reset-sidebar-link"]')
    TITLE = ('xpath', '//span[@data-test="title"]')
    PRODUCT_PRICES = ('xpath', '//div[@data-test="inventory-item-price"]')
