from typing import NewType, Optional
from pydantic import BaseModel

Token = NewType('Token', str)

class User(BaseModel):
    username: str
    password: str
    name: Optional[str] = None
    token: str | None = None
