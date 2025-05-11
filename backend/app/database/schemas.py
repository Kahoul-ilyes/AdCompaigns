from pydantic import BaseModel
from datetime import datetime
from typing import Optional

class UserCreate(BaseModel):
    username: str
    password: str

class UserOut(BaseModel):
    id: int
    username: str

    class Config:
        orm_mode = True

class AdCampaignBase(BaseModel):
    name: str
    description: str
    start_date: datetime
    end_date: datetime
    budget: float
    status: bool

class AdCampaignCreate(AdCampaignBase):
    pass

class AdCampaignUpdate(AdCampaignBase):
    pass

class AdCampaignPartialUpdate(BaseModel):
    name: Optional[str] = None
    description: Optional[str] = None
    start_date: Optional[datetime] = None
    end_date: Optional[datetime] = None
    budget: Optional[float] = None
    status: Optional[bool] = None

class AdCampaignOut(AdCampaignBase):
    id: int

    class Config:
        orm_mode = True