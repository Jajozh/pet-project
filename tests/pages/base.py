from playwright.sync_api import Page, Response
from tests.data.environment import host


class Base:
    def __init__(self, page: Page):
        self.page = page

    def open(self, uri) -> Response | None:
        """Открывает страницу по относительному URL"""
        return self.page.goto(f"{host.get_base_url()}{uri}",
                              wait_until='domcontentloaded')

    def input(self, locator, data: str) -> None:
        """Ввод данных в поле"""
        self.page.locator(locator).fill(data)

    def click(self, locator) -> None:
        """Клик по элементу"""
        self.page.click(locator)

    def get_text(self, element) -> str:
        """Получение текста элемента"""
        return self.page.locator(element).text_content()

    def click_element_by_index(self, selector: str, index: int):
        """Клик по элементу с определенным индексом"""
        self.page.locator(selector).nth(index).click()

    def input_value_by_index(self, selector: str, index: int, data: str):
        """Ввод данных в элемент по индексу"""
        self.page.locator(selector).nth(index).fill(data)

    def click_element_by_text(self, text: str):
        """Клик по кнопке с определенным текстом"""
        button = self.page.get_by_role("button", name=text).last
        button.wait_for(timeout=5000)
        button.click()

    def element_exists(self, text: str) -> bool:
        """Проверяет, существует ли элемент с заданным текстом"""
        return self.page.get_by_role("button", name=text).count() > 0

    def wait_for_element(self, locator: str, timeout=5000):
        """Ожидание видимости элемента"""
        self.page.locator(locator).wait_for(timeout=timeout)
