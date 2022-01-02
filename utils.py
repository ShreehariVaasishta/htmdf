import csv
import pdfkit
import os
from datetime import datetime
from constants import *


def csv_to_dict(file: bytes) -> list:
    """
    Convert a csv file to a list of dictionaries
    """
    data = file.decode("utf-8")
    reader = csv.DictReader(data.splitlines())
    return list(reader)


def replace_message_context_with_html(
    html_content: str, message_context: dict
) -> bytes:
    """
    Replace the message context with html content
    """
    msg = html_content
    for key in message_context:
        msg = msg.replace("{{" + key + "}}", message_context[key])
    return msg


def html_str_to_pdf(html_content: list):
    """
    Convert html content to pdf
    """
    os.makedirs(OUTPUT_FOLDER_NAME, exist_ok=True)
    for content in html_content:
        for key in content:
            _content = content[key]
            curr_datetime = datetime.now().strftime("%b-%d-%Y-%H:%M:%S")
            pdfkit.from_string(
                _content,
                f"{OUTPUT_FOLDER_NAME}/{curr_datetime}-{list(content.keys())[0]}.pdf",
            )
    return True
