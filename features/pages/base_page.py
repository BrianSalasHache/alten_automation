from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webdriver import WebDriver
from selenium.webdriver.remote.webelement import WebElement
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait


class BasePage:
    def __init__(self, driver: "WebDriver"):
        self.driver = driver

    def assert_text(self, element: "WebElement", expected_txt: str, **kwargs):
        exact = kwargs.get("exact", True)
        self.scroll_to_element(element, **kwargs)

        if exact:
            assert (
                expected_txt == element.text
            ), f"Expected {expected_txt} but got '{element.text}'"
        else:
            assert (
                expected_txt in element.text
            ), f"Expected '{expected_txt}' is not in '{element.text}'"

    def assert_popup_text(self, element: "WebElement", expected_txt: str):
        assert (
            expected_txt == element.text
        ), f"Expected {expected_txt} but got '{element.text}'"

    def click_element(self, element: "WebElement", **kwargs):
        self.scroll_to_element(element, **kwargs)
        element.click()

    def get_reference(self, locator_type: str, locator_value: str) -> tuple[str, str]:
        locator_types = {
            "id": By.ID,
            "name": By.NAME,
            "class_name": By.CLASS_NAME,
            "link_text": By.LINK_TEXT,
            "xpath": By.XPATH,
            "css": By.CSS_SELECTOR,
        }

        locator_type_value = locator_types.get(locator_type)
        if locator_type_value is None:
            raise ValueError(f"Invalid locator type: {locator_type}")
        return locator_type_value, locator_value

    def wait_element(self, locator_type: str, locator_value: str) -> "WebElement":
        ref = self.get_reference(locator_type, locator_value)
        wait = WebDriverWait(self.driver, 10)
        element = wait.until(EC.presence_of_element_located(ref))
        return element

    def get_element(self, locator_type: str, locator_value: str) -> "WebElement":
        ref = self.get_reference(locator_type, locator_value)
        return self.driver.find_element(*ref)

    def type_element(self, element: "WebElement", text: str, **kwargs):
        self.scroll_to_element(element, **kwargs)
        element.send_keys(text)

    def scroll_to_element(self, element: "WebElement", **kwargs):
        padding = kwargs.get("padding", 200)
        actions = ActionChains(self.driver)
        actions.scroll_to_element(element).scroll_by_amount(0, padding).perform()
