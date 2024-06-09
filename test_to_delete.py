from selenium import webdriver
from selenium.webdriver.common.by import By


def test_has_text():
    driver = webdriver.Chrome()
    driver.get('https://magento.softwaretestingboard.com/radiant-tee.html#')
    text = driver.find_element(By.XPATH, '//*[@id="description"]/div/div/p[1]').text
    assert text != 0
