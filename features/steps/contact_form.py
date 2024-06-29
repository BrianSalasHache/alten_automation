from behave import given, then, when

from features.pages.contact_form_page import ContactFormPage


@given("I am in the contact form section")
def go_to_contact_form_section(context):
    context.form_page = ContactFormPage(context.driver)
    context.form_page.go_to_contact_form_section()


@when("I leave the required fields empty")
def leave_required_fields_empty(context):
    pass


@when("I click the submit button")
def click_on_submit_button(context):
    context.form_page.click_on_submit_button()


@then("I should get an error message '{expected_error}'")
def assert_label_errors(context, expected_error):
    context.form_page.assert_label_error("firstname", expected_error)
    context.form_page.assert_label_error("lastname", expected_error)
    context.form_page.assert_label_error("email", expected_error)
    context.form_page.assert_label_error("message", expected_error)
    context.form_page.assert_label_error("terms_and_conditions", expected_error)


@when("in the first name field I type '{firstname}'")
def type_on_input_firstname(context, firstname):
    context.form_page.type_on_input("firstname", firstname)


@when("in the last name field I type '{lastname}'")
def type_on_input_lastname(context, lastname):
    context.form_page.type_on_input("lastname", lastname)


@when("in the email field I type '{email}'")
def type_on_input_email(context, email):
    context.form_page.type_on_input("email", email)


@when("in the message field I type '{message}'")
def type_on_input_message(context, message):
    context.form_page.type_on_input("message", message)


@when("I accept the terms and conditions")
def accept_terms_and_conditions(context):
    context.form_page.accept_terms_and_conditions()


@then("I should get a popup error message '{expected_error}'")
def assert_popup_error_label(context, expected_error):
    context.form_page.assert_label_popup_error(expected_error)
