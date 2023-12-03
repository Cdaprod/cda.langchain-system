from fastapi import APIRouter
from ..utils.openai_calls import call_openai_with_script

router = APIRouter()

@router.post("/generate-text")
async def generate_text(prompt: str):
    generated_text = call_openai_with_script(prompt)
    return {"generated_text": generated_text}
