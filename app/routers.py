from app.database import get_db_session
from app.crud import (
    list_messages,
    create_message,
    retrieve_message,
    destroy_message
)

from app.schemas import MessageSchema, CreateMessageSchema, MessageListSchema

from fastapi import APIRouter, Depends
from sqlalchemy.ext.asyncio import AsyncSession

ping_router = APIRouter(prefix="/ping", tags=["Ping Server"])
message_router = APIRouter(prefix="/message", tags=["Messages"])

@ping_router.get("")
async def ping():
    return {"message": "PONG"}

@message_router.get("", response_model=MessageListSchema)
async def get_message_list(session: AsyncSession = Depends(get_db_session)):
    messages = await list_messages(session)
    return {"messages": messages}

@message_router.post("", response_model=MessageSchema)
async def post_message(user_data: CreateMessageSchema, session: AsyncSession = Depends(get_db_session)):
    return await create_message(session, user_data.message)

@message_router.get("/{message_id}", response_model=MessageSchema)
async def get_message_entry(message_id: int, session: AsyncSession = Depends(get_db_session)):
    return await retrieve_message(session, message_id)

@message_router.delete("/{message_id}", response_model=MessageSchema)
async def delete_message(message_id: int, session: AsyncSession = Depends(get_db_session)):
    return await destroy_message(session, message_id)