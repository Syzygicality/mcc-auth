from pydantic import BaseModel
from sqlmodel import Field
from typing import List

class CreateMessageSchema(BaseModel):
    message: str = Field()

class MessageSchema(BaseModel):
    id: int
    message: str

class MessageListSchema(BaseModel):
    messages: List[MessageSchema]