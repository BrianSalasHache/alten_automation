import os
from datetime import datetime


def get_report_path():
    now = datetime.now()
    formatted_time = now.strftime("%Y-%m-%d_%H-%M-%S")

    report_path = os.path.join("reports", formatted_time)
    os.makedirs(report_path, exist_ok=True)
    return report_path
