import csv
import logging
import os

from behave.model import Scenario, Step
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait

from features.utilities.logging_config import setup_logging
from features.utilities.report_utils import get_report_path

report_path = get_report_path()
report_log_path = os.path.join(report_path, "test_report.log")
setup_logging(report_log_path)

test_results: list = []


def before_scenario(context, scenario: "Scenario"):
    logging.info("---------------------------------------------")
    logging.info(f"Starting scenario '{scenario.name}'...")
    driver_path = os.environ.get("DRIVER_PATH", None)
    service = Service(executable_path=driver_path)
    headless_option = os.environ.get("HEADLESS", False)
    options = Options()
    if headless_option:
        options.add_argument("--headless=new")
    options.add_argument("--no-sandbox")
    options.add_argument("--disable-dev-shm-usage")

    logging.info("Running webbrowser...")
    context.driver = webdriver.Chrome(service=service, options=options)
    context.driver.maximize_window()
    context.driver.get("https://www.alten.es/")

    wait = WebDriverWait(context.driver, 10)
    button_accept_cookies = wait.until(
        EC.element_to_be_clickable((By.ID, "tarteaucitronPersonalize2"))
    )
    button_accept_cookies.click()

    scenario_directory_name = scenario.name.replace(" ", "_")
    context.scenario_directory = os.path.join(report_path, scenario_directory_name)
    os.makedirs(context.scenario_directory, exist_ok=True)
    context.step_count = 0


def before_step(context, step: "Step"):
    logging.info(f"Running step: {step.keyword} {step.name}...")


def after_step(context, step: "Step"):
    context.step_count += 1
    screenshot_name = (
        f"{context.step_count:02d}_{step.name.replace(' ', '_').replace(':', '')}.png"
    )
    screenshot_path = os.path.join(context.scenario_directory, screenshot_name)
    context.driver.save_screenshot(screenshot_path)


def after_scenario(context, scenario: "Scenario"):
    error_message = ""
    for step in scenario.steps:
        if step.status == "failed":
            logging.error(f"Step '{step.name}' failed. Reason: {step.error_message}")
            error_message = step.error_message

    test_results.append(
        {
            "Nombre de la prueba": scenario.name,
            "Resultado": "Failed" if scenario.status == "failed" else "Passed",
            "Descripción del error": error_message,
        }
    )

    logging.info("Closing webbrowser...")
    context.driver.close()
    context.driver.quit()

    logging.info(f"Finishing scenario '{scenario.name}'...")
    logging.info("---------------------------------------------")


def after_all(context):
    logging.info("All tests are finished!")
    logging.info("Generating report...")

    report_csv_file = os.path.join(report_path, "test_report.csv")

    with open(report_csv_file, mode="w", newline="", encoding="utf-8") as file:
        writer = csv.DictWriter(
            file,
            fieldnames=["Nombre de la prueba", "Resultado", "Descripción del error"],
        )
        writer.writeheader()
        writer.writerows(test_results)

    logging.info(f"Test report written to {report_path}")
