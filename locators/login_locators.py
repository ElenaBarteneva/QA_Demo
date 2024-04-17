
class LoginLocators:
    USERNAME_FIELD = ('xpath', '//input[@data-test="username"]')
    PASSWORD_FIELD = ('xpath', '//input[@data-test="password"]')
    LOGIN_BUTTON = ('xpath', '//input[@data-test="login-button"]')
    ERROR_LOGIN = ('css selector', 'h3[data-test="error"]')
    LOGIN_FORM = ('css selector', 'div[data-test="login-container"]')