from fastapi import FastAPI
import os
from fastapi.responses import FileResponse, HTMLResponse
from fastapi.templating import Jinja2Templates
from starlette.requests import Request

from utils import (
    csv_to_dict,
    replace_message_context_with_html,
    html_str_to_pdf,
    zip_output_pdf_files,
)


app = FastAPI()
templates = Jinja2Templates(directory="templates")


@app.post("/upload")
async def upload_file(request: Request):
    """
    Upload a csv file and print the contents as dictionary
    """
    # delete output folder
    os.system("rm -rf output")
    request_body = await request.form()
    html_content = request_body["html_content"]
    csv_file = await request_body["file"].read()

    html_content = html_content.strip()
    x = csv_to_dict(csv_file)
    processed_csv = [
        {f"{i['name']}": replace_message_context_with_html(html_content, i)} for i in x
    ]
    html_str_to_pdf(processed_csv)
    output_zip = zip_output_pdf_files()
    return FileResponse(output_zip, media_type="application/zip")


@app.get("/", response_class=HTMLResponse)
def get_index(request: Request):
    return templates.TemplateResponse("upload_file.html", {"request": request})
