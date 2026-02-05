from fastapi import FastAPI
from fastapi.staticfiles import StaticFiles

app = FastAPI()

# staticフォルダ配下を、そのままWebで配信
app.mount("/", StaticFiles(directory="static", html=True), name="static")
