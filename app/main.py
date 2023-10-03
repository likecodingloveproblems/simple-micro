from fastapi import FastAPI
import uvicorn
import os

app = FastAPI()


@app.get("/")
def home():
    return "Home page ;)"


if False and __name__ == "__main__":
    port: int = int(os.environ.get('PORT', 5000))
    log_level = os.environ.get('LOG_LEVEL', 'info')
    uvicorn.run('main:app', port=port, log_level=log_level)
