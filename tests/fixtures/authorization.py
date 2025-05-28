import time

import pytest
import json
from pathlib import Path
from playwright.sync_api import expect, TimeoutError
from tests.Locators.buttons import TelegramBotLocators


@pytest.fixture(scope="function")
def telegram_authenticated_page(page):
    # Указываем путь к файлу local_storage.json относительно корня проекта
    storage_path = Path(__file__).resolve().parent.parent.parent / "local_storage.json"

    # Проверяем, существует ли файл
    if not storage_path.exists():
        pytest.fail(f"Файл {storage_path} не найден. Убедитесь, что он существует.")

    # Переходим на Telegram Web
    page.goto("https://web.telegram.org/")

    # Загружаем данные из local_storage.json
    with open(storage_path, "r") as f:
        storage_state = json.load(f)

    # Восстанавливаем состояние localStorage
    page.evaluate(f"""
        const state = {json.dumps(storage_state)};
        for (const [key, value] of Object.entries(state)) {{
            localStorage.setItem(key, value);
        }}
    """)

    # Обновляем страницу, чтобы применить изменения
    page.reload()
    page.goto("https://web.telegram.org/k/")
    page.wait_for_load_state("domcontentloaded", timeout=60000)

    try:
        bot_chat = page.get_by_role(**TelegramBotLocators.MAIN_MENU_BOT_CHAT)
        expect(bot_chat).to_be_visible(timeout=10000)
        expect(bot_chat).to_be_in_viewport()

        for attempt in range(10):
            bot_chat.click(button="right")
            time.sleep(1)  # небольшая пауза, чтобы элемент успел появиться

            delete_chat_button = page.get_by_text(TelegramBotLocators.DELETE_CHAT_BUTTON)
            if delete_chat_button.is_visible():
                break  # если кнопка появилась, выходим из цикла
        else:
            raise TimeoutError("Не удалось открыть контекстное меню после нескольких попыток")

        expect(delete_chat_button).to_be_visible(timeout=10000)
        expect(bot_chat).to_be_in_viewport()
        delete_chat_button.click()

        confirm_button = page.get_by_role(**TelegramBotLocators.CONFIRM_DELETE_BUTTON)
        expect(confirm_button).to_be_visible()
        expect(bot_chat).to_be_in_viewport()
        confirm_button.click()
    except TimeoutError:
        print("Бот отсутствует в списке чатов. Переходим к поиску.")
    except Exception as e:
        print(f"Произошла ошибка при проверке бота: {e}")

    # Поиск и запуск бота
    search_input = page.get_by_placeholder(TelegramBotLocators.SEARCH_INPUT_PLACEHOLDER)
    expect(search_input).to_be_visible()
    search_input.fill(TelegramBotLocators.BOT_CHAT_HAS_TEXT)

    bot_result = page.get_by_text(TelegramBotLocators.BOT_RESULT_TEXT)
    expect(bot_result).to_be_visible()
    bot_result.click()

    start_button = page.get_by_role(**TelegramBotLocators.START_BUTTON)
    expect(start_button).to_be_visible()
    start_button.click()

    return page
