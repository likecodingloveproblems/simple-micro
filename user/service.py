import re
from uuid import uuid4
from fastapi import HTTPException
from fastapi import status

from entity import Token, User

def generate_token() -> Token:
    return Token(str(uuid4()))

def get_token(authorization_header: str) -> str:
    PATTERN = r'^Token (.+)'
    match = re.match(PATTERN, authorization_header)
    if match and match.groups():
        return match.groups()[0]
    raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail='authorization header is not valid!'
            )

def authenticate(user: User, users: list[User]) -> Token:
    for u in users:
        if u.username == user.username:
            if u.password == user.password:
                u.token = generate_token()
                return u.token
            else:
                raise HTTPException(
                        status_code=status.HTTP_406_NOT_ACCEPTABLE,
                        detail='Wrong password!')
    raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail='username not found!')


def signup(user: User, users: list[User]):
    for u in users:
        if u.username == user.username:
            raise HTTPException(status_code=status.HTTP_406_NOT_ACCEPTABLE, detail='this is user has signed up!')
    users.append(user)



def update_password(new_user: User, users: list[User]):
    for user in users:
        if user.username == new_user.username:
            user.password = new_user.password
            return
    raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail='user does not exists!')

