from typing import Annotated
from fastapi import FastAPI, HTTPException, Header, status
from starlette.status import HTTP_417_EXPECTATION_FAILED

from dto import GetUserResponse, LoginRequestDto, SignupRequestDto, UpdatePasswordRequestDto
from entity import User
import service

app = FastAPI()

users = list()


@app.get('/')
def home():
    return "User app is designed for the authentication and authorization!"


@app.post("/login")
def login(data: LoginRequestDto):
    print(data)
    user = User(**data.model_dump())
    return service.authenticate(user, users)
    


@app.post("/signup")
def signup(data: SignupRequestDto):
    print(data)
    user = User(**data.model_dump())
    service.signup(user, users)


@app.post("/update-password")
def update_password(data: UpdatePasswordRequestDto):
    user = User(**data.model_dump())
    service.update_password(user, users)

@app.get('/user')
def get_user(authorization: Annotated[str, Header()]) -> GetUserResponse:
    token = service.get_token(authorization)
    for user in users:
        if user.token == token:
            return user
    raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail='token is not valid!'
            )

