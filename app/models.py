from app.enums import AuthStatus

from sqlmodel import SQLModel, Field, Column, Enum
from pydantic import EmailStr
from typing import Optional

class Message(SQLModel, table=True):
    id: Optional[int] = Field(default=None, primary_key=True)
    message: str = Field()

class User(SQLModel, table=True):
    id: Optional[int] = Field(default=None, primary_key=True)
    keycloak_id: str = Field(index=True, nullable=False)
    username: str = Field(nullable=False)
    email: EmailStr = Field(nullable=False, unique=True)
    account_status: AuthStatus = Field(default=AuthStatus.UNAUTHORIZED)

