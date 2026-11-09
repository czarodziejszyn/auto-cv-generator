from typing import TypeDict


class CVState(TypeDict):
    job_description: str
    extracted_keywords: list[str]
    retrieved_context: str
    draft_cv: str
    critic_feedback: str
    critic_score: int
    iteration_count: int
