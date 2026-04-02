from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from api.routes import movie
from api.routes import payment
from core.startup import run_startup

app = FastAPI(
    title="Cinema Machine AIoT API",
    description="Hệ thống API cho máy bán vé tự động",
    version="0.0.1"
)

# Cho phép gọi API từ web/mobile app bên ngoài (CORS)
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # trong production nên cố định domain
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.on_event("startup")
def startup_event():
    run_startup()

app.include_router(movie)
app.include_router(payment)

@app.get("/")
def root():
    return {"message": "Welcome to Cinema Machine API System"}