from selenium.webdriver.remote.webdriver import WebDriver

from .base_page import BasePage


class ContactFormPage(BasePage):
    def __init__(self, driver: "WebDriver"):
        super().__init__(driver)

    @property
    def button_submit(self):
        return self.get_element("xpath", "//*[@id='contact-form']//button")

    @property
    def nav_contact(self):
        return self.get_element("xpath", "//ul[@id='menu-header-es-1']//li[@id='36']/a")

    @property
    def form_contact(self):
        return self.wait_element(
            "xpath", "//div[@id='contacta']//form[@id='contact-form']"
        )

    @property
    def checkbox_terms_and_conditions(self):
        return self.get_element("id", "webfactory-field-7-control")

    @property
    def input_email(self):
        return self.get_element("id", "webfactory-field-3-control")

    @property
    def input_firstname(self):
        return self.get_element("id", "webfactory-field-0-control")

    @property
    def input_lastname(self):
        return self.get_element("id", "webfactory-field-1-control")

    @property
    def input_message(self):
        return self.get_element("id", "webfactory-field-6-control")

    @property
    def label_email_error(self):
        return self.wait_element("id", "webfactory-field-3-control-error")

    @property
    def label_firstname_error(self):
        return self.wait_element("id", "webfactory-field-0-control-error")

    @property
    def label_lastname_error(self):
        return self.wait_element("id", "webfactory-field-1-control-error")

    @property
    def label_message_error(self):
        return self.wait_element("id", "webfactory-field-6-control-error")

    @property
    def label_terms_and_conditions_error(self):
        return self.wait_element("id", "webfactory-field-6-control-error")

    @property
    def label_popup_error(self):
        self.wait_element("class_name", "modal-body")
        return self.get_element("class_name", "modal-body")

    def accept_terms_and_conditions(self):
        self.click_element(self.checkbox_terms_and_conditions)

    def assert_label_error(self, element_key: str, expected_error: str):
        element = self.__getattribute__(f"label_{element_key}_error")
        self.assert_text(element, expected_error)

    def assert_label_popup_error(self, expected_error: str):
        self.assert_popup_text(self.label_popup_error, expected_error)

    def click_on_submit_button(self):
        self.click_element(self.button_submit)

    def type_on_input(self, element_key: str, text: str):
        element = self.__getattribute__(f"input_{element_key}")
        self.type_element(element, text)

    def go_to_contact_form_section(self):
        self.click_element(self.nav_contact)
        self.assert_text(self.form_contact, "Contacta con nosotros", exact=False)
