from typing import List, Literal

from pydantic import BaseModel, Field

class InputModel(BaseModel):
    type: str = Field(
        default="Lager",
        description="선호하는 맥주의 종류를 입력하세요. 예: Lager, Ale, Stout"
    )
    flavor: str = Field(
        default="Crisp",
        description="선호하는 맥주의 풍미를 입력하세요. 예: Crisp, Rich, Fruity"
    )
    llm_type: Literal['chatgpt', 'huggingface'] = Field(
        alias='Large Language Model Type',
        description='사용할 LLM 종류',
        default='chatgpt'
    )

class OutputModel(BaseModel):
    recommendations: List[str] = Field(
        description="추천 맥주 리스트"
    )

