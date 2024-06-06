import os

from fastapi import APIRouter

from llm.chat import build
from llm.store import LLMStore
from models.beer_recommendation import InputModel, OutputModel

# Configure API router
router = APIRouter(
    tags=['functions'],
)

NAME = os.path.basename(__file__)[:-3]
store = LLMStore()

@router.post(f'/func/{NAME}')
async def recommend_beer(input: InputModel) -> OutputModel:
    chain = build(
        name=NAME,
        llm=store.get(input.llm_type)
    )
    prompt = f"Based on the preference for {input.type} type and {input.flavor} flavor, recommend some beers."
    response = chain.invoke({'input_context': prompt})

    # Let's assume the LLM returns a comma-separated list of beer recommendations
    recommendations = response
    return OutputModel(recommendations=recommendations)