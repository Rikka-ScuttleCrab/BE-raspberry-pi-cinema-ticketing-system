from fastapi import FastAPI
from api import public
from api.admin import admin
from api.payment import payment
from core.startup import run_startup
from fastapi.middleware.cors import CORSMiddleware


app = FastAPI(
    title="Cinema Machine AIoT API",
    description="Hệ thống API cho máy bán vé tự động",
    version="0.0.1"
)

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


@app.on_event("startup")
def startup_event():
    run_startup()

app.include_router(public.router)
app.include_router(admin.router)
app.include_router(payment.router)

@app.get("/")
def root():
    return {"message": "Welcome to Cinema Machine API System"}