from typing import Optional
from pydantic import BaseModel, Field
from datetime import datetime

class UserCreate(BaseModel):
    username: str
    email: str
    password: str
    role: str = "reviewer"

class User(BaseModel):
    id: int
    username: str
    email: str
    role: str
    created_at: datetime
    updated_at: datetime

    class Config:
        orm_mode = True

class ContractCreate(BaseModel):
    title: str
    content: str
    user_id: int

class Contract(BaseModel):
    id: int
    title: str
    content: str
    version: int
    user_id: int
    created_at: datetime
    updated_at: datetime

    class Config:
        orm_mode = True

class CommentCreate(BaseModel):
    contract_id: int
    text: str

class Comment(BaseModel):
    id: int
    contract_id: int
    user_id: int
    text: str
    created_at: datetime
    updated_at: datetime

    class Config:
        orm_mode = True
