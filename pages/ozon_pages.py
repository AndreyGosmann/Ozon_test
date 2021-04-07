from pages.base_page import BasePage
from pages.locators import *
import os


class MainPage(BasePage):

    def __init__(self, driver, timeout=10):
        super().__init__(driver, timeout)
        url = os.getenv("MAIN_URL") or 'https://www.ozon.ru/'
        driver.get(url)

        self.horizontal_menu = driver.find_elements(*MainPageLocators.HORIZONTAL_MENU)
        self.side_bar = driver.find_elements(*MainPageLocators.SIDEBAR)
        self.navigation = driver.find_elements(*MainPageLocators.NAVIGATION)
        self.top_fashion_horizontal_menu = driver.find_element(*MainPageLocators.TOP_FASHION_HORIZONTAL_MENU)
        self.actions_horizontal_menu = driver.find_element(*MainPageLocators.ACTIONS_HORIZONTAL_MENU)
        self.brand_horizontal_menu = driver.find_element(*MainPageLocators.BRAND_HORIZONTAL_MENU)
        self.seller_horizontal_menu = driver.find_element(*MainPageLocators.SELLER_HORIZONTAL_MENU)
        self.book_horizontal_menu = driver.find_element(*MainPageLocators.BOOK_HORIZONTAL_MENU)
        self.certificates_horizontal_menu = driver.find_element(*MainPageLocators.CERTIFICATES_HORIZONTAL_MENU)
        self.electronics_horizontal_menu = driver.find_element(*MainPageLocators.ELECTRONICS_HORIZONTAL_MENU)
        self.clothes_and_footwear_horizontal_menu = driver.find_element(*MainPageLocators.
                                                                        CLOTHES_AND_FOOTWEAR_HORIZONTAL_MENU)
        self.children_products_horizontal_menu = driver.find_element(*MainPageLocators.
                                                                     CHILDREN_PRODUCTS_HORIZONTAL_MENU)
        self.house_and_garden_horizontal_menu = driver.find_element(*MainPageLocators.HOUSE_AND_GARDEN_HORIZONTAL_MENU)
        self.ozon_travel_horizontal_menu = driver.find_element(*MainPageLocators.OZON_TRAVEL_HORIZONTAL_MENU)
        self.ozon_discount_horizontal_menu = driver.find_element(*MainPageLocators.OZON_DISCOUNT_HORIZONTAL_MENU)
        self.entity_navigation_menu = driver.find_element(*MainPageLocators.ENTITY_NAVIGATION)
        self.mobile_app_navigation_menu = driver.find_element(*MainPageLocators.MOBILE_APP_NAVIGATION)
        self.referral_navigation_menu = driver.find_element(*MainPageLocators.REFERRAL_NAVIGATION)
        self.business_navigation_menu = driver.find_element(*MainPageLocators.BUSINESS_NAVIGATION)
        self.certificates_navigation_menu = driver.find_element(*MainPageLocators.CERTIFICATES_NAVIGATION)
        self.points_navigation_menu = driver.find_element(*MainPageLocators.POINTS_NAVIGATION)
        self.postamat_navigation_menu = driver.find_element(*MainPageLocators.POSTAMAT_NAVIGATION)
        self.help_navigation_menu = driver.find_element(*MainPageLocators.HELP_NAVIGATION)
        self.delivery_navigation_menu = driver.find_element(*MainPageLocators.DELIVERY_NAVIGATION)
        self.catalog = driver.find_element(*MainPageLocators.CATALOG)
        self.filter_menu = driver.find_element(*MainPageLocators.FILTER)
        self.search = driver.find_element(*MainPageLocators.SEARCH)
        self.search_button = driver.find_element(*MainPageLocators.SEARCH_BUTTON)
        self.orders_sidebar_menu = driver.find_element(*MainPageLocators.ORDERS_SIDEBAR)
        self.favor_sidebar_menu = driver.find_element(*MainPageLocators.FAVOR_SIDEBAR)
        self.cart_sidebar_menu = driver.find_element(*MainPageLocators.CART_SIDEBAR)


class ElektronikaPage(BasePage):

    def __init__(self, driver, timeout=10):
        super().__init__(driver, timeout)
        url = os.getenv("ELEKTRONIKA_URL") or 'https://www.ozon.ru/category/elektronika-15500/'
        driver.get(url)

        self.elektronika_horizontal_menu = driver.find_elements(*ElektronikaLocators.ELEKTRONIKA_HORIZONTAL_MENU)
        self.appliances_elektronika_horizontal_menu = driver.find_element(*ElektronikaLocators.
                                                                          APPLIANCES_ELEKTRONIKA_HORIZONTAL_MENU)
        self.smartphione_elektronika_horizontal_menu = driver.find_element(*ElektronikaLocators.
                                                                           SMARTPHONE_ELEKTRONIKA_HORIZONTAL_MENU)
        self.tv_elektronika_horizontal_menu = driver.find_element(*ElektronikaLocators.TV_ELEKTRONIKA_HORIZONTAL_MENU)
        self.laptop_elektronika_horizontal_menu = driver.find_element(*ElektronikaLocators.
                                                                      LAPTOP_ELEKTRONIKA_HORIZONTAL_MENU)
        self.computer_elektronika_horizontal_menu = driver.find_element(*ElektronikaLocators.
                                                                        COMPUTER_ELEKTRONIKA_HORIZONTAL_MENU)
        self.headphones_elektronika_horizontal_menu = driver.find_element(*ElektronikaLocators.
                                                                          HEADPHONES_ELEKTRONIKA_HORIZONTAL_MENU)
        self.games_soft_elektronika_horizontal_menu = driver.find_element(*ElektronikaLocators.
                                                                          GAMES_SOFT_ELEKTRONIKA_HORIZONTAL_MENU)


class PromotionsPage(BasePage):

    def __init__(self, driver, timeout=10):
        super().__init__(driver, timeout)
        url = os.getenv("PROMOTIONS_URL") or 'https://www.ozon.ru/info/actions/'
        driver.get(url)

        self.promotion_menu = driver.find_elements(*PromotionsLocators.PROMOTION_MENU)
        self.all_promo_promotion_menu = driver.find_element(*PromotionsLocators.ALL_PROMO_PROMOTION_MENU)
        self.coupons_promotion_menu = driver.find_element(*PromotionsLocators.COUPONS_PROMOTION_MENU)
        self.sets_promotion_menu = driver.find_element(*PromotionsLocators.SETS_PROMOTION_MENU)
