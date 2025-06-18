from pydantic import BaseModel


class SummaryResponse(BaseModel):
    status: str
    content: str
