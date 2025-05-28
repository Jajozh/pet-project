import pytest

from tests.data.asserts import Assertions
from tests.pages.telegram_page import TelegramPage


@pytest.fixture
def telegram_bot_ready(telegram_authenticated_page):
        telegram_page = TelegramPage(telegram_authenticated_page)
        assertions = Assertions(telegram_authenticated_page)

        telegram_page.start_bot()

        return telegram_page, assertions

