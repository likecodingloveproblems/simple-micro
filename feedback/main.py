from typing import Annotated
from fastapi import FastAPI, HTTPException, Header, status
import requests
from entity import Feedback

import service

app = FastAPI()

feedbacks = list()


@app.get('/')
def home():
    return "Feedback app is designed to handle users feedbacks"


@app.post('/feedback')
def create_feedback(feedback: Feedback, authorization: Annotated[str | None, Header()] = None):
    username: str | None = None
    response = requests.get('localhost:5000/user', headers={'authorization': authorization if authorization else ''})
    if response.status_code == 200:
        username = response.json().get('username')
    feedback.username = username
    service.create_feedback(feedback, feedbacks)
    

@app.get('/feedback')
def get_user_feedbacks(authorization: Annotated[str | None, Header()] = None) -> list[Feedback]:
    username: str 
    response = requests.get('localhost:5000/user', headers={'authorization': authorization if authorization else ''})
    if response.status_code == 200 and response.json().get('username'):
        username = response.json().get('username')
    else:
        raise HTTPException(
                status_code=status.HTTP_401_UNAUTHORIZED,
                detail='you must be authorized!'
                )
    return service.get_user_feedbacks(username, feedbacks)
