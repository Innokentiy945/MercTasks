import allure
from hamcrest import *

from TaskTwo.Pages import Pages
from TaskTwo.Pages.Pages import SearchHelper, ItemOneHelper, ItemTwoHelper, BasketHelper


@allure.story('Testing e-shop')
@allure.feature('Add two items with highest price to card')
def test_items(set_up):
    main_page = SearchHelper(set_up)
    item_one = ItemOneHelper(set_up)
    item_two = ItemTwoHelper(set_up)
    basket = BasketHelper(set_up)
    searchedItem = "BJURSTA"

    main_page.go_to_site()
    main_page.acceptCookies()
    main_page.goSearching()
    main_page.enterQuery(searchedItem)
    main_page.clickSearchButton()

    item_one.sortingPrices()
    item_one.getHighPrices()
    item_one.goToHighPrices()
    item_one.getItemOne()
    item_one.addToCard()

    if Pages.ItemsPageLocators.purchaseModal == True:

        item_one.closingModal()
        main_page.goSearching()
        main_page.enterQuery(searchedItem)
        main_page.clickSearchButton()

        item_two.sortingPrices()
        item_two.getHighPrices()
        item_two.goToHighPrices()
        item_two.getItemTwo()
        item_two.addToCard()

    else:
        main_page.goSearching()
        main_page.enterQuery(searchedItem)
        main_page.clickSearchButton()

        item_two.sortingPrices()
        item_two.getHighPrices()
        item_two.goToHighPrices()
        item_two.getItemTwo()
        item_two.addToCard()

    if Pages.ItemsPageLocators.purchaseModal == True:
        item_one.closingModal()
        basket.goToBusket()
        assert_that(basket.verifyItemsInBusket(), True)

    else:
        basket.goToBusket()
        assert_that(basket.verifyItemsInBusket(), True)

