import pytest
from playwright.sync_api import expect
from tests.pages.telegram_page import TelegramPage


@pytest.fixture(scope="function")
def open_bot(telegram_authenticated_page):
    """
    Фикстура открывает бота в Telegram Web через поиск.
    """
    bot_username = "@ttracker_stage_bot"
    telegram_page = TelegramPage(telegram_authenticated_page)


    # Открываем Telegram Web
    telegram_authenticated_page.goto("https://web.telegram.org/k/#@ttracker_stage_bot")
    telegram_authenticated_page.wait_for_load_state("domcontentloaded")

    telegram_page.close_error_modal()

    # Ждем загрузки страницы перед взаимодействием
    telegram_authenticated_page.wait_for_timeout(2000)

    # Получаем поле поиска и ожидаем его появления
    search_input = telegram_authenticated_page.locator("input[placeholder='Search']")
    expect(search_input).to_be_visible(timeout=5000)

    # Фокусируемся на поле и вводим имя бота
    search_input.click()
    telegram_authenticated_page.wait_for_timeout(500)
    search_input.fill(bot_username)

    # Ждем обновления списка результатов
    telegram_authenticated_page.wait_for_timeout(3000)

    # Локатор для конкретного бота (по точному тексту)
    first_result = telegram_authenticated_page.locator(f"text={bot_username}").first

    # Если Playwright не находит по тексту, пробуем общий поиск по кнопкам
    if not first_result.is_visible():
        first_result = telegram_authenticated_page.locator("div[role='button']").first

    # Ожидаем появления бота в списке
    expect(first_result).to_be_visible(timeout=10000)

    # Кликаем по найденному боту (принудительно, если надо)
    first_result.click(force=True)

    # Ждём открытия чата
    chat_input = telegram_authenticated_page.locator("div#editable-message-text")
    expect(chat_input).to_be_visible(timeout=10000)

    yield telegram_authenticated_page




