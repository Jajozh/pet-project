import random
from datetime import datetime, timedelta
from tests.Locators.buttons import TelegramBotLocators  # Импортируем локаторы
from tests.Locators.buttons import TelegramBotLocatorsPurchases  # Импортируем локаторы
from playwright.sync_api import expect, Page
from tests.pages.base import Base


class TelegramPage(Base):
    def __init__(self, page: Page):
        super().__init__(page)
        # Локаторы для кнопок
        self.main_menu_button = self.page.get_by_role(**TelegramBotLocators.BUTTON_MAIN_MENU).last
        self.back_button = self.page.get_by_role(**TelegramBotLocators.BACK_BUTTON).last
        self.purchases_button = self.page.get_by_role(**TelegramBotLocators.BUTTON_PURCHASES).last
        self.autopost_button = self.page.get_by_role(**TelegramBotLocators.BUTTON_AUTOPOST).last
        self.calendar_button = self.page.get_by_role(**TelegramBotLocators.BUTTON_CALENDAR).last
        self.my_channels_button = self.page.get_by_role(**TelegramBotLocators.BUTTON_MY_CHANNELS).last
        self.subscribe_button = self.page.get_by_role(**TelegramBotLocators.BUTTON_SUBSCRIBE).last
        self.refer_button = self.page.get_by_role(**TelegramBotLocators.BUTTON_REFER).last
        self.no_stats_links_button = self.page.get_by_role(**TelegramBotLocators.BUTTON_NO_STATS_LINKS).last
        self.more_about_button = self.page.get_by_role(**TelegramBotLocators.BUTTON_MORE_ABOUT).last
        self.create_purchases_button = self.page.get_by_role(**TelegramBotLocatorsPurchases.BUTTON_CREATE_PURCHASES).last
        self.rekla_autotests_button = self.page.get_by_role(**TelegramBotLocatorsPurchases.BUTTON_REKLA_AUTOTESTS).last
        self.test_creative_button = self.page.get_by_role(**TelegramBotLocatorsPurchases.BUTTON_TEST_CREATIVE).last
        self.creative_name_button = self.page.get_by_role(**TelegramBotLocatorsPurchases.BUTTON_CREATIVE_NAME).last
        self.not_specified_button = self.page.get_by_role(**TelegramBotLocatorsPurchases.BUTTON_NOT_SPECIFIED)
        self.today_button = self.page.get_by_role(**TelegramBotLocatorsPurchases.BUTTON_TODAY).last
        self.next_button = self.page.get_by_role(**TelegramBotLocatorsPurchases.BUTTON_NEXT).last
        self.fix_price_button = self.page.get_by_role(**TelegramBotLocatorsPurchases.BUTTON_FIX_PRICE).last

    def click_button(self, button):
        """Кликает по указанной кнопке."""
        expect(button).to_be_in_viewport()
        expect(button).to_be_visible()
        expect(button).to_be_enabled()
        expect(button).to_be_attached()
        button.click()

    def is_button_visible(self, button):
        """Проверяет, видна ли указанная кнопка."""
        return button.is_visible()

    def select_random_time(self):
        """Выбирает случайное время с шагом в 3 часа, которое позже текущего.
        Если текущее время позже 21:00 — выбирает 21:00."""
        current_time_obj = datetime.now().replace(second=0, microsecond=0)
        
        start_time = datetime.strptime("00:00", "%H:%M")
        time_steps = [start_time + timedelta(hours=3 * i) for i in range(8)]  # 00:00, 03:00, ..., 21:00
        
        future_time_steps = [time for time in time_steps if time > current_time_obj]

        if not future_time_steps:
            # Если текущее время после 21:00 — выбираем 21:00
            random_time_obj = datetime.strptime("21:00", "%H:%M")
        else:
            random_time_obj = random.choice(future_time_steps)

        random_time = random_time_obj.strftime("%H:%M")

        time_button = self.page.get_by_role("button", name=random_time)
        expect(time_button).to_be_visible()
        expect(time_button).to_be_in_viewport()
        time_button.click()

        return random_time