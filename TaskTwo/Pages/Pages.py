from selenium.webdriver.common.by import By

from TaskTwo.Pages.BasePage import BasePage


class SearchPageLocators:
    accCookies = (By.XPATH, "//button[@id='onetrust-accept-btn-handler']")
    searchLine = (By.XPATH, "//input[@type='search']")
    searchButton = (By.ID, "search-box__searchbutton")


class ItemsPageLocators:
    goToSort = (By.CSS_SELECTOR, "#content > div > div > div.filters > div > button.filter-button.filter-button--SORT.button.button--secondary.button--small")
    getHighPrices = (By.XPATH, "//div[@class='single-select-filter']//label[@class='single-select-filter__item radio-button']//span[contains(text(), 'Price: high to low')]")
    goToHighPrice = (By.XPATH, "//button[@class='filters__confirm-button button button--dark button--small']")

    item = (By.XPATH, "//*[@id='search-results']//*[@class='serp-grid__item serp-grid__item--product search-grid__item range-revamp-product-compact']")
    addToCard = (By.XPATH, "//span[@class='range-revamp-btn__label']")
    purchaseModal = (By.XPATH, "//button[@class='rec-btn rec-btn--icon-primary-inverse rec-modal__close']")


class BasketPageLocators:
    goToBasket = (By.XPATH, "//li[@class='hnf-header__shopping-cart-link']")
    basketList = (By.XPATH, "//div[@class='product']")


class SearchHelper(BasePage):

    def acceptCookies(self):
        return self.find_element(SearchPageLocators.accCookies).click()

    def goSearching(self):
        return self.find_element(SearchPageLocators.searchLine).click()

    def enterQuery(self, word):
        return self.find_element(SearchPageLocators.searchLine).send_keys(word)

    def clickSearchButton(self):
        return self.find_element(SearchPageLocators.searchButton).click()


class ItemOneHelper(BasePage):

    def sortingPrices(self):
        return  self.find_element(ItemsPageLocators.goToSort).click()

    def getHighPrices(self):
        return self.find_element(ItemsPageLocators.getHighPrices).click()

    def goToHighPrices(self):
        return self.find_element(ItemsPageLocators.goToHighPrice).click()

    def getItemOne(self):
        elements = self.find_elements(ItemsPageLocators.item)
        elemList = list(elements)
        return elemList[0].click()

    def addToCard(self):
        return self.find_element(ItemsPageLocators.addToCard).click()

    def closingModal(self):
        return self.find_element(ItemsPageLocators.purchaseModal).click()


class ItemTwoHelper(BasePage):

    def sortingPrices(self):
        return self.find_element(ItemsPageLocators.goToSort).click()

    def getHighPrices(self):
        return self.find_element(ItemsPageLocators.getHighPrices).click()

    def goToHighPrices(self):
        return self.find_element(ItemsPageLocators.goToHighPrice).click()

    def getItemTwo(self):
        elements = self.find_elements(ItemsPageLocators.item)

        return elements[1].click()

    def addToCard(self):
        return self.find_element(ItemsPageLocators.addToCard).click()


class BasketHelper(BasePage):
    def goToBusket(self):
        return self.find_element(BasketPageLocators.goToBasket).click()

    def verifyItemsInBusket(self):
        itemsInBasket = self.find_elements(BasketPageLocators.basketList)
        return bool(len(itemsInBasket) == 2)
