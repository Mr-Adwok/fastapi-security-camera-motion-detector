from fastapi import FastAPI, Request, WebSocket
from fastapi.responses import StreamingResponse
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates
from pydantic import BaseModel
from src.generate_frames import generate_frames
from fastapi.middleware.cors import CORSMiddleware

from mypy.dmypy_util import send





app = FastAPI()


# app.mount("/static", StaticFiles(directory="/static"), name="static")


templates = Jinja2Templates(directory="src/templates")

# camera = VideoCamera()
motion_detected = False

class MotionAlert(BaseModel):
    motion: bool



@app.get("/")
def dashboard(request: Request):
    return templates.TemplateResponse(
        "dashboard.html",
        {
            "request": request,
            "title": "Security Camera Dashboard"
        }
    )

















# @app.post("/motion_alert")
# def motion_alert(data: MotionAlert):
#     global motion_detected
#     motion_detected = data.motion
#     if data.motion:
#         camera.start_recording()
#     else:
#         camera.stop_recording()
#     return {"status": "recording" if data.motion else "stopped"}

@app.get("/motion_status")
def get_motion_status():
    return {"motion": motion_detected}
