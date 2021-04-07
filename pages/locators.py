from selenium.webdriver.common.by import By


class MainPageLocators:

    HORIZONTAL_MENU = (By.XPATH, '//ul[@data-widget="horizontalMenu"]')
    SIDEBAR = (By.XPATH, '//div[@class="c5y6"]')
    NAVIGATION = (By.XPATH, '//ul[@class="c4w4"]')
    TOP_FASHION_HORIZONTAL_MENU = (By.XPATH, '//a[@href="/highlight/top-fashion/"]')
    ACTIONS_HORIZONTAL_MENU = (By.XPATH, '//a[@href="/info/actions/"]')
    BRAND_HORIZONTAL_MENU = (By.XPATH, '//a[@href="/brand/"]')
    SELLER_HORIZONTAL_MENU = (By.XPATH, '//a[@href="/seller/"]')
    BOOK_HORIZONTAL_MENU = (By.XPATH, '//*[@id="layoutPage"]/div[1]/header/div[2]/div/ul/li[6]/a')
    CERTIFICATES_HORIZONTAL_MENU = (By.XPATH, '//a[@href="/context/detail/id/135382627/?perehod=menu"]')
    ELECTRONICS_HORIZONTAL_MENU = (By.XPATH, '//*[@id="layoutPage"]/div[1]/header/div[2]/div/ul/li[8]/a')
    CLOTHES_AND_FOOTWEAR_HORIZONTAL_MENU = (By.XPATH, '//*[@id="layoutPage"]/div[1]/header/div[2]/div/ul/li[9]/a')
    CHILDREN_PRODUCTS_HORIZONTAL_MENU = (By.XPATH, '//*[@id="layoutPage"]/div[1]/header/div[2]/div/ul/li[10]/a')
    HOUSE_AND_GARDEN_HORIZONTAL_MENU = (By.XPATH, '//*[@id="layoutPage"]/div[1]/header/div[2]/div/ul/li[11]/a')
    OZON_TRAVEL_HORIZONTAL_MENU = (By.XPATH, '//a[@href="https://www.ozon.ru/travel?perehod=ozon_menu_header"]')
    OZON_DISCOUNT_HORIZONTAL_MENU = (By.XPATH, '//a[@href="/highlight/discount/"]')
    ENTITY_NAVIGATION = (By.XPATH, '//a[@href="/highlight/ozon-business/?perehod=header"]')
    MOBILE_APP_NAVIGATION = (By.XPATH, '//a[@href="/info/appspromo/"]')
    REFERRAL_NAVIGATION = (By.XPATH, '//a[@href="/referral/?perehod=header"]')
    BUSINESS_NAVIGATION = (By.XPATH, '//a[@href="//business.ozon.ru/?perehod=header"]')
    CERTIFICATES_NAVIGATION = (By.XPATH, '//a[@href="/context/detail/id/135382627/?perehod=header"]')
    POINTS_NAVIGATION = (By.XPATH, '//a[@href="/info/map/"]')
    POSTAMAT_NAVIGATION = (By.XPATH, '//a[@href="/postamat/"]')
    HELP_NAVIGATION = (By.XPATH, '//a[@href="//docs.ozon.ru/common/"]')
    DELIVERY_NAVIGATION = (By.XPATH, '//a[@href="/my/deliveryPriceInfo"]')
    CATALOG = (By.XPATH, '//*[@id="layoutPage"]/div[1]/header/div[1]/div[2]/div/div[1]/button')
    FILTER = (By.XPATH, '//span[@title="Везде"]')
    SEARCH = (By.XPATH, '//input[@placeholder="Искать на Ozon"]')
    SEARCH_BUTTON = (By.XPATH, '//button[@type="submit"]')
    ORDERS_SIDEBAR = (By.XPATH, '//a[@href="/my/orderlist"]/span[@class="a9c6"]')
    FAVOR_SIDEBAR = (By.XPATH, '//a[@href="/my/favorites"]/span[@class="a9c6"]')
    CART_SIDEBAR = (By.XPATH, '//a[@href="/cart"]/span[@class="a9c6"]')


class ElektronikaLocators:

    ELEKTRONIKA_HORIZONTAL_MENU = (By.XPATH, '//div[@class="c6a1"]')
    APPLIANCES_ELEKTRONIKA_HORIZONTAL_MENU = (By.XPATH,
                                              '//div[@class="c6a2"]/a[@href="/category/bytovaya-tehnika-10500/"]')
    SMARTPHONE_ELEKTRONIKA_HORIZONTAL_MENU = (By.XPATH,
                                              '//div[@class="c6a2"]/a[@href="/category/telefony-i-smart-chasy-15501/"]')
    TV_ELEKTRONIKA_HORIZONTAL_MENU = (By.XPATH,
                                      '//div[@class="c6a2"]/a[@href="/category/televizory-i-videotehnika-15527/"]')
    LAPTOP_ELEKTRONIKA_HORIZONTAL_MENU = \
        (By.XPATH, '//div[@class="c6a2"]/a[@href="/category/noutbuki-planshety-i-elektronnye-knigi-8730/"]')
    COMPUTER_ELEKTRONIKA_HORIZONTAL_MENU = \
        (By.XPATH, '//div[@class="c6a2"]/a[@href="/category/kompyutery-i-komplektuyushchie-15690/"]')
    HEADPHONES_ELEKTRONIKA_HORIZONTAL_MENU = \
        (By.XPATH, '//div[@class="c6a2"]/a[@href="/category/audiotehnika-15543/"]')
    GAMES_SOFT_ELEKTRONIKA_HORIZONTAL_MENU = \
        (By.XPATH, '//div[@class="c6a2"]/a[@href="/category/igry-i-soft-13300/"]')


class PromotionsLocators:

    PROMOTION_MENU = (By.XPATH, '//div[@data-widget="actionSwitcher"]')
    ALL_PROMO_PROMOTION_MENU = (By.XPATH, '//a[@href="/info/actions/?filter=actions"]')
    COUPONS_PROMOTION_MENU = (By.XPATH, '//a[@href="/info/actions/?filter=coupons"]')
    SETS_PROMOTION_MENU = (By.XPATH, '//a[@href="/info/actions/?filter=bundles"]')
