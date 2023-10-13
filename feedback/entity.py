from pydantic import BaseModel


class Feedback(BaseModel):
    username: str | None = None
    title: str
    description: str
