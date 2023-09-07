"""Youtube Video Model"""

from datetime import datetime
from pydantic import BaseModel, field_serializer

class YouTubeVideo(BaseModel):
    date: datetime
    title: str
    views: int
    duration: int
    author: str
    thumbnail: str
    url: str
    video_id: str

    @field_serializer('date')
    def serialize_dt(self, dt: datetime, _info):
        return dt.isoformat()
