from app.models import Message

from sqlmodel import select
from sqlalchemy.ext.asyncio import AsyncSession
from fastapi.exceptions import HTTPException
from fastapi import status
from typing import List

async def list_messages(session: AsyncSession) -> List[Message]:
    messages = await session.execute(select(Message))
    return messages.scalars().all()

async def create_message(session: AsyncSession, content: str) -> Message:
    message = Message(message=content)
    session.add(message)
    await session.commit()
    await session.refresh(message)
    return message

async def retrieve_message(session: AsyncSession, message_id: int) -> Message:
    message = await session.get(Message, message_id)
    if not message:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Message not found.")
    return message

async def destroy_message(session: AsyncSession, message_id: int) -> Message:
    message = await session.get(Message, message_id)
    if not message:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Message not found.")
    await session.delete(message)
    await session.commit()
    return message