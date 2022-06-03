from fastapi import FastAPI, Request
import uvicorn
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates
from fastapi import Request

app = FastAPI()

app.mount("/static", StaticFiles(directory="static"), name="static")

names = {}
names['0'] = 'Rounak'
names['1'] = 'Prabhjyot'
names['2'] = 'Vikrant'


@app.get("/rollno/{roll_no}")
def read_root(roll_no: str, request: Request):
    if roll_no in names:
        return {"studentName": names[roll_no], "rollNo": roll_no}
    else:
        return ''


@app.get("/addrollno/")
def add_rollno(roll: str, name: str):
   names[roll]=name
   return 'Added '+name





uvicorn.run(app, host="0.0.0.0", port=8001, log_level="debug")
