from time import sleep

import allure

from TaskTwo.Pages.Pages import SearchHelper, ItemOneHelper, ItemTwoHelper, BasketHelper


def custom_wait():
    sleep(10)


@allure.story('Testing e-shop')
@allure.feature('Add two items with highest price to card')
def test_items(set_up):
    main_page = SearchHelper(set_up)
    item_one = ItemOneHelper(set_up)
    item_two = ItemTwoHelper(set_up)
    basket = BasketHelper(set_up)

    main_page.go_to_site()
    main_page.goSearching()
    main_page.enterQuery("BJURSTA")
    main_page.clickSearchButton()

    custom_wait()
    item_one.getItemOne()
    item_one.addToCard()

    main_page.goSearching()
    main_page.enterQuery("BJURSTA")
    main_page.clickSearchButton()

    item_two.getItemTwo()
    item_two.addToCard()
    custom_wait()

    custom_wait()
    basket.goToBusket()
    basket.verifyItemsInBusket()
