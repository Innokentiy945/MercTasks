from selenium.webdriver.common.by import By

from TaskTwo.Pages.BasePage import BasePage


class SearchPageLocators:
    searchLine = (By.XPATH, "//input[@type='search']")
    searchButton = (By.ID, "search-box__searchbutton")


class ItemsPageLocators:
    itemOne = (By.XPATH, "//*[@id='search-results']/div[2]/div[1]")
    itemTwo = (By.XPATH, "//*[@id='search-results']/div[3]/div[1]")
    addToCard = (By.XPATH, "//span[@class='range-revamp-btn__label']")
    closeModal = (By.XPATH, "//button[@class='rec-btn rec-btn--icon-primary-inverse rec-modal__close']")


class BasketPageLocators:
    goToBasket = (By.XPATH, "//li[@class='hnf-header__shopping-cart-link']")
    basketList = (By.XPATH, "//div[@class='productlist']")


class SearchHelper(BasePage):

    def goSearching(self):
        search_field = self.find_element(SearchPageLocators.searchLine)
        return search_field.click()

    def enterQuery(self, word):
        return self.find_element(SearchPageLocators.searchLine).send_keys(word)

    def clickSearchButton(self):
        return self.find_element(SearchPageLocators.searchButton).click()


class ItemOneHelper(BasePage):
    def getItemOne(self):
        return self.find_element(ItemsPageLocators.itemOne).click()

    def addToCard(self):
        return self.find_element(ItemsPageLocators.addToCard).click()

    def closeModal(self):
        return self.find_element(ItemsPageLocators.closeModal).click()


class ItemTwoHelper(BasePage):
    def getItemTwo(self):
        return self.find_element(ItemsPageLocators.itemTwo).click()

    def addToCard(self):
        return self.find_element(ItemsPageLocators.addToCard).click()


class BasketHelper(BasePage):
    def goToBusket(self):
        return self.find_element(BasketPageLocators.goToBasket).click()

    def verifyItemsInBusket(self):
        return self.find_element(BasketPageLocators.basketList).is_displayed()
