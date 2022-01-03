# htmdf
Converts html to pdf with support for variables using [fastApi](https://fastapi.tiangolo.com/).

# Installation
1. Clone this repository.
```
git clone https://github.com/ShreehariVaasishta/htmdf.git
```
2. Go to the root directory of this project and install the dependencies using `pip`. Activate [virtual environment](https://python-guide-cn.readthedocs.io/en/latest/dev/virtualenvs.html) if you use one.
```
pip3 install -r requirements.txt
```
3. Run the app
```
uvicorn main:app --reload
```
# Usage
1. Here we created a html template for certificates. 
2. Added csv with columns which needs to be replaced in the html template.


# Sample
<b>Input Form</b><br/><br/>
![image](https://user-images.githubusercontent.com/37337599/147964589-5ffbd64e-7c75-4b04-bfd9-a964a75f3a5a.png)

<b>Output PDF</b><br/><br/>
![image](https://user-images.githubusercontent.com/37337599/147964737-27ae01e0-afc5-461a-bf9b-efc60eec030e.png)
