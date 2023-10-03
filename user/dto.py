from typing import Optional
from pydantic import BaseModel


class SignupRequestDto(BaseModel):
    username: str
    password: str
    name: Optional[str] = None


class LoginRequestDto(BaseModel):
    username: str
    password: str


class UpdatePasswordRequestDto(BaseModel):
    username: str
    new_password: str


class GetUserResponse(BaseModel):
    username: str

