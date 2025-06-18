import uvicorn
from fastapi import FastAPI, APIRouter, Body
from fastapi.middleware.cors import CORSMiddleware

from schemas.analyze import AnalyzeResponse
from schemas.summary import SummaryResponse
from core.summarize import summarize
from core.analyze import analyze

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

api = APIRouter(
    prefix="/api/v0"
)


@api.get("/")
async def empty_page():
    return {"main": "page"}


@api.post("/summarize")
async def get_summary_text(
    text: str = Body(..., embed=True)
) -> SummaryResponse:
    try:
        summary = await summarize(text=text)
        return SummaryResponse(
            status="success",
            content=summary,
        )
    except Exception as e:
        return SummaryResponse(
            status="error",
            content=str(e),
        )


@api.post("/analyze")
async def get_analysed_text(
    text: str = Body(...)
) -> AnalyzeResponse:
    try:
        analysis = await analyze(text=text)
        return ...
    except Exception as e:
        return AnalyzeResponse(
            status="error",
            content=str(e),
        )


app.include_router(api)

if __name__ == "__main__":
    uvicorn.run("main:app", host="0.0.0.0", port=8000)