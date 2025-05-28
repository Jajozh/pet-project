import re
from datetime import datetime
import time

import allure
import pytest
from playwright.sync_api import expect
from tests.pages.telegram_page import TelegramPage


@pytest.mark.ttracker
@allure.id(2)
@allure.title("Переход по кнопке 'Закупы' и обратно в главное меню")
@allure.feature("Главное меню")
def test_click_purchases_button(telegram_authenticated_page):
    bot_page = TelegramPage(telegram_authenticated_page)

    with allure.step("Кликнуть кнопку 'Закупы'"):
        bot_page.click_button(bot_page.purchases_button)

    with allure.step("Кликнуть кнопку 'Главное меню'"):
        bot_page.click_button(bot_page.main_menu_button)

    with allure.step("Проверить видимость кнопки 'Закупы'"):
        expect(bot_page.purchases_button).to_be_visible()
        assert bot_page.is_button_visible(bot_page.purchases_button), "Кнопка 'Закупы' должна быть видима"


@pytest.mark.ttracker
@allure.id(368)
@allure.title("Переход по кнопке 'Автопостинг' и обратно в главное меню")
@allure.feature("Главное меню")
def test_click_autopost_button(telegram_authenticated_page):
    bot_page = TelegramPage(telegram_authenticated_page)

    with allure.step("Кликнуть кнопку 'Автопостинг'"):
        bot_page.click_button(bot_page.autopost_button)

    with allure.step("Кликнуть кнопку 'Главное меню'"):
        bot_page.click_button(bot_page.main_menu_button)

    with allure.step("Проверить видимость кнопки 'Автопостинг'"):
        expect(bot_page.autopost_button).to_be_visible()
        assert bot_page.is_button_visible(bot_page.autopost_button), "Кнопка 'Автопостинг' должна быть видима"


@allure.id(167)
@allure.title("Переход по кнопке 'Календарь' и обратно в главное меню")
@allure.feature("Главное меню")
def test_click_calendar_button(telegram_authenticated_page):
    bot_page = TelegramPage(telegram_authenticated_page)

    with allure.step("Кликнуть кнопку 'Календарь'"):
        bot_page.click_button(bot_page.calendar_button)

    with allure.step("Кликнуть кнопку 'Главное меню'"):
        bot_page.click_button(bot_page.main_menu_button)

    with allure.step("Проверить видимость кнопки 'Календарь'"):
        expect(bot_page.calendar_button).to_be_visible()
        assert bot_page.is_button_visible(bot_page.calendar_button), "Кнопка 'Календарь' должна быть видима"


@allure.id(168)
@allure.title("Переход по кнопке 'Мои каналы' и обратно в главное меню")
@allure.feature("Главное меню")
def test_click_button_my_channels(telegram_authenticated_page):
    bot_page = TelegramPage(telegram_authenticated_page)

    with allure.step("Кликнуть кнопку 'Мои каналы'"):
        bot_page.click_button(bot_page.my_channels_button)

    with allure.step("Кликнуть кнопку 'Главное меню'"):
        bot_page.click_button(bot_page.main_menu_button)

    with allure.step("Проверить видимость кнопки 'Мои каналы'"):
        expect(bot_page.my_channels_button).to_be_visible()
        assert bot_page.is_button_visible(bot_page.my_channels_button), "Кнопка 'Мои каналы' должна быть видима"


@allure.id(364)
@allure.title("Переход по кнопке 'Подписка' и обратно в главное меню")
@allure.feature("Главное меню")
def test_click_button_subscribe(telegram_authenticated_page):
    bot_page = TelegramPage(telegram_authenticated_page)

    with allure.step("Кликнуть кнопку 'Подписка'"):
        bot_page.click_button(bot_page.subscribe_button)

    with allure.step("Кликнуть кнопку 'Главное меню'"):
        bot_page.click_button(bot_page.main_menu_button)

    with allure.step("Проверить видимость кнопки 'Подписка'"):
        expect(bot_page.subscribe_button).to_be_visible()
        assert bot_page.is_button_visible(bot_page.subscribe_button), "Кнопка 'Подписка' должна быть видима"


@allure.id(365)
@allure.title("Переход по кнопке 'Реферальный кабинет' и обратно в главное меню")
@allure.feature("Главное меню")
def test_click_button_refer(telegram_authenticated_page):
    bot_page = TelegramPage(telegram_authenticated_page)

    with allure.step("Кликнуть кнопку 'Реферальный кабинет'"):
        bot_page.click_button(bot_page.refer_button)

    with allure.step("Кликнуть кнопку 'Главное меню'"):
        bot_page.click_button(bot_page.main_menu_button)

    with allure.step("Проверить видимость кнопки 'Реферальный кабинет'"):
        expect(bot_page.refer_button).to_be_visible()
        assert bot_page.is_button_visible(bot_page.refer_button), "Кнопка 'Реферальный кабинет' должна быть видима"


@allure.id(367)
@allure.title("Переход по кнопке 'Ссылки без статистики' и обратно в главное меню")
@allure.feature("Главное меню")
def test_click_button_no_stats_links(telegram_authenticated_page):
    bot_page = TelegramPage(telegram_authenticated_page)

    with allure.step("Кликнуть кнопку 'Ссылки без статистики'"):
        bot_page.click_button(bot_page.no_stats_links_button)

    with allure.step("Кликнуть кнопку 'Главное меню'"):
        bot_page.click_button(bot_page.main_menu_button)

    with allure.step("Проверить видимость кнопки 'Ссылки без статистики'"):
        expect(bot_page.no_stats_links_button).to_be_visible()
        assert bot_page.is_button_visible(
            bot_page.no_stats_links_button), "Кнопка 'Ссылки без статистики' должна быть видима"


@allure.id(366)
@allure.title("Переход по кнопке 'Подробнее про @rekla' и обратно в главное меню")
@allure.feature("Главное меню")
def test_click_button_more_about(telegram_authenticated_page):
    bot_page = TelegramPage(telegram_authenticated_page)

    with allure.step("Кликнуть кнопку 'Подробнее про @rekla'"):
        bot_page.click_button(bot_page.more_about_button)

    with allure.step("Кликнуть кнопку 'Главное меню'"):
        bot_page.click_button(bot_page.main_menu_button)

    with allure.step("Проверить видимость кнопки 'Подробнее про @rekla'"):
        expect(bot_page.more_about_button).to_be_visible()
        assert bot_page.is_button_visible(
            bot_page.more_about_button), "Кнопка 'Подробнее про @rekla' должна быть видима"


@pytest.mark.ttracker
@allure.id(75)
@allure.title("Закуп в канале по фикс без маркировки")
@allure.feature("Закупы")
def test_create_purchase_fix_price_without_mark(telegram_authenticated_page):
    bot_page = TelegramPage(telegram_authenticated_page)
    expected_message = """Где будем рекламироваться?\n\nМожно указать несколько рекламных площадок в одном сообщении!\n\nКаждая площадка - с новой строки\nПосле площадки указывается цена закупа через тире\n\nПример:\nБлог у Димы https://t.me/+efJdTFFhH3c2MWMy - 2000\nБлог у Васи https://t.me/+efJdTFFhH3c2MWMy - 3000"""

    with allure.step("Кликнуть кнопку 'Закупы'"):
        bot_page.click_button(bot_page.purchases_button)

    with allure.step("Кликнуть кнопку 'Создать Закуп'"):
        bot_page.click_button(bot_page.create_purchases_button)

    with allure.step("Выбрать канал 'Рекла Автотесты пуб'"):
        bot_page.rekla_autotests_button.click()
        expect(bot_page.rekla_autotests_button).to_have_text(re.compile(r"✅\s+Рекла Автотесты пуб"), timeout=5000)  # Таймаут 5 секунд

    with allure.step("Выбрать дату и время"):
        bot_page.click_button(bot_page.not_specified_button.first)
        bot_page.click_button(bot_page.today_button)
        selected_time = bot_page.select_random_time()
        # bot_page.click_button(bot_page.fix_price_button)

    with allure.step("Кликнуть Далее"):
        time.sleep(10)
        bot_page.click_button(bot_page.next_button)
        
    with allure.step("Проверить, что появилось сообщение с инструкцией"):
        message_element = telegram_authenticated_page.get_by_text(expected_message)
        expect(message_element).to_be_visible(), "Ожидаемое сообщение не появилось!"

    with allure.step("Вставить заготовленную ссылку на канал паблишера, отправить"):
        ad_channel = "Test blog https://t.me/autorekla"

        message_input = telegram_authenticated_page.locator("div").filter(
            has_text=re.compile(r"^Message$")).locator("div").first
        expect(message_input).to_be_visible()  # Ждем появления поля ввода
        message_input.click()
        message_input.fill(ad_channel)

        send_button = telegram_authenticated_page.locator(".btn-send-container")  # Локатор кнопки
        expect(send_button).to_be_visible()  # Убедиться, что кнопка видима
        send_button.click()

        with allure.step("Проверить, что появилось сообщение с подтверждением о закупе"):
            today_date = datetime.now().strftime("%d.%m.%Y")

            expected_purchase_message = f"""🔗 Ссылка зашита с помощью @rekla

                                        Рекламная площадка: {ad_channel}
                                        Рекламируемый канал: Рекла Автотесты пуб
                                        Тип ссылки: Открытая
                                        Цена: 1
                                        Дата: {today_date}
                                        Время: {selected_time}
                                    
                                        ⬇️ Пост ниже ⬇️"""

            confirmation_message = telegram_authenticated_page.get_by_text(expected_purchase_message)
            expect(
                confirmation_message).to_be_visible(), "Сообщение о закупе не появилось или содержит неверные данные!"

            with allure.step("Открывается страница Закупов"):
                expect(bot_page.create_purchases_button).to_be_visible()
                assert bot_page.is_button_visible(bot_page.create_purchases_button), "Кнопка 'Закупы' должна быть видима"
