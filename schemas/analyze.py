from pydantic import BaseModel


class AnalyzeContent(BaseModel):
    ticker: str


class AnalyzeResponse(BaseModel):
    status: str
    content: AnalyzeContent | str

