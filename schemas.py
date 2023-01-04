from typing import List, Optional
from pydantic import BaseModel

class Event(BaseModel):
    title: str
    start_time: datetime
    end_time: datetime
    