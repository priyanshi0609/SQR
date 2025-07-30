from services.llm_service import ask_llm
from services.math_service import solve_math
import re

def is_math(query: str) -> bool:
    math_keywords = ["solve", "equation", "calculate"]
    if any(word in query.lower() for word in math_keywords):
        return True

    math_pattern = r'[\d\s]*[+\-*/^=]+[\d\s]*'
    return bool(re.search(math_pattern, query))

def is_wellness(query: str) -> bool:
    keywords = ["stress", "anxiety", "mental health", "tired", "sleep", "depressed"]
    return any(word in query.lower() for word in keywords)

async def handle_query(query: str) -> str:
    if is_math(query):
        return solve_math(query)
    elif is_wellness(query):
        return "I'm here for you. It’s okay to feel this way. Try taking deep breaths or talking to a friend ❤️"
    else:
        return await ask_llm(query)
