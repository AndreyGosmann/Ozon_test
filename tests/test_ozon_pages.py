from pages.ozon_pages import *
from tests.test_data import *
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time


def test_horizontal_menu(selenium):
    page = MainPage(selenium)
    horizontal_menu = page.horizontal_menu
    for i in range(len(horizontal_menu)):
        for j in horizontal_menu_list:
            assert j in horizontal_menu[i].text


def test_sidebar_menu(selenium):
    page = MainPage(selenium)
    sidebar_menu = page.side_bar
    for i in range(len(sidebar_menu)):
        for j in sidebar_list:
            assert j in sidebar_menu[i].text


def test_navigation(selenium):
    page = MainPage(selenium)
    navigation = page.navigation
    for i in range(len(navigation)):
        for j in navigation_list:
            assert j in navigation[i].text


def test_actions_link(selenium):
    page = MainPage(selenium)
    page.actions_horizontal_menu.click()
    actions = WebDriverWait(selenium, 10).until(EC.presence_of_element_located((By.XPATH, '//div[@class="a0k9"]')))
    assert 'Акции и спецпредложения' in actions.text
    assert page.get_relative_link() == '/info/actions/'


def test_top_fashion_link(selenium):
    page = MainPage(selenium)
    page.top_fashion_horizontal_menu.click()
    top_fashion = WebDriverWait(selenium, 10).until(EC.presence_of_element_located((By.XPATH, '//h1')))
    assert 'TOP Fashion' in top_fashion.text
    assert page.get_relative_link() == '/highlight/top-fashion/'


def test_brand_link(selenium):
    page = MainPage(selenium)
    page.brand_horizontal_menu.click()
    brand = WebDriverWait(selenium, 10).until(EC.presence_of_element_located((By.XPATH, '//h1')))
    assert 'Все бренды' in brand.text
    assert page.get_relative_link() == '/brand/'


def test_seller_link(selenium):
    page = MainPage(selenium)
    page.seller_horizontal_menu.click()
    seller = WebDriverWait(selenium, 10).until(EC.presence_of_element_located((By.XPATH, '//div[@class="cl9"]')))
    assert 'Все магазины' in seller.text
    assert page.get_relative_link() == '/seller/'


def test_book_link(selenium):
    page = MainPage(selenium)
    page.book_horizontal_menu.click()
    book = WebDriverWait(selenium, 10).until(EC.presence_of_element_located((By.XPATH, '//h1')))
    assert 'Книги' in book.text
    assert page.get_relative_link() == '/category/knigi-16500/'


def test_certificates_link(selenium):
    page = MainPage(selenium)
    page.certificates_horizontal_menu.click()
    certificates = WebDriverWait(selenium, 10).until(EC.presence_of_element_located((By.XPATH, '//h1')))
    assert 'Электронный подарочный сертификат Миллион подарков (3000)' in certificates.text
    assert page.get_relative_link() == '/context/detail/id/135382627/'


def test_electronics_link(selenium):
    page = MainPage(selenium)
    page.electronics_horizontal_menu.click()
    electronics = WebDriverWait(selenium, 10).until(EC.presence_of_element_located((By.XPATH, '//h1')))
    assert 'Электроника' in electronics.text
    assert page.get_relative_link() == '/category/elektronika-15500/'


def test_clothes_and_footwear_link(selenium):
    page = MainPage(selenium)
    page.clothes_and_footwear_horizontal_menu.click()
    clothes_and_footwear = WebDriverWait(selenium, 10).until(EC.presence_of_element_located((By.XPATH, '//h1')))
    assert 'Одежда, обувь и аксессуары' in clothes_and_footwear.text
    assert page.get_relative_link() == '/category/odezhda-obuv-i-aksessuary-7500/'


def test_children_products_link(selenium):
    page = MainPage(selenium)
    page.children_products_horizontal_menu.click()
    children_products = WebDriverWait(selenium, 10).until(EC.presence_of_element_located((By.XPATH, '//h1')))
    assert 'Детские товары' in children_products.text
    assert page.get_relative_link() == '/category/detskie-tovary-7000/'


def test_house_and_garden_link(selenium):
    page = MainPage(selenium)
    page.house_and_garden_horizontal_menu.click()
    house_and_garden = WebDriverWait(selenium, 10).until(EC.presence_of_element_located((By.XPATH, '//h1')))
    assert 'Дом и сад' in house_and_garden.text
    assert page.get_relative_link() == '/category/dom-i-sad-14500/'


def test_ozon_travel_link(selenium):
    page = MainPage(selenium)
    page.ozon_travel_horizontal_menu.click()
    ozon_travel = WebDriverWait(selenium, 10).until(EC.presence_of_element_located((By.XPATH, '//h1')))
    assert 'OZON Travel' in ozon_travel.text
    assert page.get_relative_link() == '/travel'


def test_ozon_discount_link(selenium):
    page = MainPage(selenium)
    page.ozon_discount_horizontal_menu.click()
    WebDriverWait(selenium, 10).until(EC.presence_of_all_elements_located((By.XPATH, '//div[@class="b6e2"]')))
    time.sleep(3)
    assert page.get_relative_link() == '/highlight/discount/'


def test_entity_link(selenium):
    page = MainPage(selenium)
    page.entity_navigation_menu.click()
    WebDriverWait(selenium, 10). \
        until(EC.presence_of_element_located((By.XPATH, '//h4[@class="delivery-landing__info-title font-title"]')))
    assert page.get_relative_link() == '/highlight/ozon-business/'


def test_mobile_app_link(selenium):
    page = MainPage(selenium)
    page.mobile_app_navigation_menu.click()
    WebDriverWait(selenium, 10). \
        until(EC.presence_of_element_located((By.XPATH, '//img[@src="/graphics/action/190722-apps/oval.svg"]')))
    assert page.get_relative_link() == '/info/appspromo/'


def test_referral_link(selenium):
    page = MainPage(selenium)
    page.referral_navigation_menu.click()
    WebDriverWait(selenium, 10). \
        until(EC.presence_of_element_located((By.XPATH, '//div[@class="ref-header-title"]')))
    assert page.get_relative_link() == '/referral/'


def test_business_link(selenium):
    page = MainPage(selenium)
    page.business_navigation_menu.click()
    WebDriverWait(selenium, 10). \
        until(EC.presence_of_element_located((By.XPATH, '//h1')))
    assert page.get_url() == 'business.ozon.ru'


def test_certificates_navigation_link(selenium):
    page = MainPage(selenium)
    page.certificates_navigation_menu.click()
    WebDriverWait(selenium, 10). \
        until(EC.presence_of_element_located((By.XPATH, '//h1')))
    assert page.get_relative_link() == '/context/detail/id/135382627/'


def test_points_link(selenium):
    page = MainPage(selenium)
    page.points_navigation_menu.click()
    WebDriverWait(selenium, 10). \
        until(EC.presence_of_element_located((By.XPATH, '//h1')))
    time.sleep(3)
    assert page.get_relative_link() == '/geo/sankt-peterburg/'


def test_postamat_link(selenium):
    page = MainPage(selenium)
    page.postamat_navigation_menu.click()
    WebDriverWait(selenium, 10). \
        until(EC.presence_of_element_located((By.XPATH, '//*[@id="start"]/div/div/div[5]/div[1]/h2')))
    assert page.get_relative_link() == '/postamat/'


def test_help_link(selenium):
    page = MainPage(selenium)
    page.help_navigation_menu.click()
    WebDriverWait(selenium, 10). \
        until(EC.presence_of_element_located((By.XPATH, '//h1')))
    assert page.get_relative_link() == '/common/'


def test_delivery_link(selenium):
    page = MainPage(selenium)
    page.delivery_navigation_menu.click()
    WebDriverWait(selenium, 10). \
        until(EC.presence_of_element_located((By.XPATH, '//h2[@class="c5r9"]')))
    assert page.get_relative_link() == '/my/deliveryPriceInfo'


def test_catalog(selenium):
    page = MainPage(selenium)
    page.catalog.click()
    catalog = WebDriverWait(selenium, 10). \
        until(EC.presence_of_all_elements_located((By.XPATH,
                                                   '//*[@id="layoutPage"]/div[1]/header/div[1]/div[2]/div/div['
                                                   '2]/div/div[1]/div')))
    for i in range(len(catalog)):
        for j in catalog_list:
            assert j in catalog[i].text


def test_filter(selenium):
    page = MainPage(selenium)
    page.filter_menu.click()
    filter_menu = WebDriverWait(selenium, 10).until(EC.presence_of_all_elements_located((By.XPATH,
                                                                                         '//div[@class="b6u5"]')))
    for i in range(len(filter_menu)):
        for j in filter_list:
            assert j in filter_menu[i].text


def test_elektronica_horizontal_menu(selenium):
    page = ElektronikaPage(selenium)
    horizontal_menu = page.elektronika_horizontal_menu
    for i in range(len(horizontal_menu)):
        for j in electronika_horizontal_menu_list:
            assert j in horizontal_menu[i].text


def test_appliances_link(selenium):
    page = ElektronikaPage(selenium)
    page.appliances_elektronika_horizontal_menu.click()
    time.sleep(5)
    appliances = WebDriverWait(selenium, 10).until(EC.presence_of_element_located((By.XPATH, '//h1')))
    assert 'Бытовая техника' in appliances.text
    assert page.get_relative_link() == '/category/bytovaya-tehnika-10500/'


def test_smartphone_link(selenium):
    page = ElektronikaPage(selenium)
    page.smartphione_elektronika_horizontal_menu.click()
    time.sleep(5)
    smartphone = WebDriverWait(selenium, 10).until(EC.presence_of_element_located((By.XPATH, '//h1')))
    assert 'Телефоны и смарт-часы' in smartphone.text
    assert page.get_relative_link() == '/category/telefony-i-smart-chasy-15501/'


def test_tv_link(selenium):
    page = ElektronikaPage(selenium)
    page.tv_elektronika_horizontal_menu.click()
    time.sleep(5)
    tv = WebDriverWait(selenium, 10).until(EC.presence_of_element_located((By.XPATH, '//h1')))
    assert 'Телевизоры и видеотехника' in tv.text
    assert page.get_relative_link() == '/category/televizory-i-videotehnika-15527/'


def test_laptop_link(selenium):
    page = ElektronikaPage(selenium)
    page.laptop_elektronika_horizontal_menu.click()
    time.sleep(5)
    laptop = WebDriverWait(selenium, 10).until(EC.presence_of_element_located((By.XPATH, '//h1')))
    assert 'Ноутбуки, планшеты и электронные книги' in laptop.text
    assert page.get_relative_link() == '/category/noutbuki-planshety-i-elektronnye-knigi-8730/'


def test_computer_link(selenium):
    page = ElektronikaPage(selenium)
    page.computer_elektronika_horizontal_menu.click()
    time.sleep(5)
    computer = WebDriverWait(selenium, 10).until(EC.presence_of_element_located((By.XPATH, '//h1')))
    assert 'Компьютеры и комплектующие' in computer.text
    assert page.get_relative_link() == '/category/kompyutery-i-komplektuyushchie-15690/'


def test_headphones_link(selenium):
    page = ElektronikaPage(selenium)
    page.headphones_elektronika_horizontal_menu.click()
    time.sleep(5)
    headphones = WebDriverWait(selenium, 10).until(EC.presence_of_element_located((By.XPATH, '//h1')))
    assert 'Аудиотехника' in headphones.text
    assert page.get_relative_link() == '/category/audiotehnika-15543/'


def test_games_soft_link(selenium):
    page = ElektronikaPage(selenium)
    page.games_soft_elektronika_horizontal_menu.click()
    time.sleep(5)
    games_soft = WebDriverWait(selenium, 10).until(EC.presence_of_element_located((By.XPATH, '//h1')))
    assert 'Всё для игр' in games_soft.text
    assert page.get_relative_link() == '/category/igry-i-soft-13300/'


def test_search(selenium):
    page = MainPage(selenium)
    page.search.clear()
    page.search.send_keys('телефон')
    page.search_button.click()
    result = WebDriverWait(selenium, 10). \
        until(EC.presence_of_element_located((By.XPATH, '//div[@class="b6r7"]/strong')))
    assert 'телефон' in result.text


def test_orders_link(selenium):
    page = MainPage(selenium)
    page.orders_sidebar_menu.click()
    orders = WebDriverWait(selenium, 10).until(EC.presence_of_element_located((By.XPATH, '//div[@class="d0c3"]')))
    assert 'Вы не авторизованы' in orders.text
    assert page.get_relative_link() == '/my/orderlist'


def test_favor_link(selenium):
    page = MainPage(selenium)
    page.favor_sidebar_menu.click()
    favor = WebDriverWait(selenium, 10).until(EC.presence_of_element_located((By.XPATH, '//div[@class="a0k9"]')))
    assert 'Избранное' in favor.text
    assert page.get_relative_link() == '/my/favorites'


def test_cart_link(selenium):
    page = MainPage(selenium)
    page.cart_sidebar_menu.click()
    cart = WebDriverWait(selenium, 10).until(EC.presence_of_element_located((By.XPATH, '//h1')))
    assert 'Корзина пуста' in cart.text
    assert page.get_relative_link() == '/cart'


def test_promotion_menu(selenium):
    page = PromotionsPage(selenium)
    promotion_menu = page.promotion_menu
    for i in range(len(promotion_menu)):
        for j in promotion_menu_list:
            assert j in promotion_menu[i].text


def test_all_promo_link(selenium):
    page = PromotionsPage(selenium)
    page.all_promo_promotion_menu.click()
    time.sleep(1)
    assert page.get_link_query() == 'filter=actions'


def test_coupons_link(selenium):
    page = PromotionsPage(selenium)
    page.coupons_promotion_menu.click()
    time.sleep(1)
    assert page.get_link_query() == 'filter=coupons'


def test_sets_link(selenium):
    page = PromotionsPage(selenium)
    page.sets_promotion_menu.click()
    time.sleep(1)
    assert page.get_link_query() == 'filter=bundles'
