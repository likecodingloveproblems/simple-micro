from typing import Iterable
from entity import Feedback


def create_feedback(feedback: Feedback, feedbacks: list[Feedback]):
    feedbacks.append(feedback)

def get_user_feedbacks(username: str, feedbacks) -> Iterable[Feedback]:
    return filter(lambda feedback: feedback.username == username, feedbacks)
