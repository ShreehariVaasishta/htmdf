from typing import Iterable
from fastapi import FastAPI, File
from utils import csv_to_dict, replace_message_context_with_html, html_str_to_pdf

app = FastAPI()


@app.post("/upload")
def upload_file(html_content: str, file: bytes = File(...)):
    """
    Upload a csv file and print the contents as dictionary
    """
    html_content = html_content.strip()
    x = csv_to_dict(file)
    processed_csv = [
        {f"{i['name']}": replace_message_context_with_html(html_content, i)} for i in x
    ]
    return html_str_to_pdf(processed_csv)
    # return processed_csv
