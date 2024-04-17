
class OrderLocators:
    FIRST_NAME_FIELD = ('css selector', 'input[data-test="firstName"]')
    LAST_NAME_FIELD = ('css selector', 'input[data-test="lastName"]')
    ZIP_CODE = ('css selector', 'input[data-test="postalCode"]')
    CONTINUE_BTN = ('css selector', 'input[data-test="continue"]')
    FINISH_BTN = ('css selector', 'button[id="finish"]')
    SUCCESSFULL_ORDER = ('css selector', 'h2[data-test="complete-header"]')
    ERROR_MESSAGE = ('css selector', 'h3[data-test="error"]')