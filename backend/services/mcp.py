import json
import os
from services.math_service import solve_math
from services.llm_service import ask_llm

def load_protocols():
    with open(os.path.join(os.path.dirname(__file__), "../protocols/protocols.json")) as f:
        return json.load(f)

protocols = load_protocols()

async def route_query(query: str) -> dict:
    query_lower = query.lower()
    for key, data in protocols.items():
        if any(word in query_lower for word in data["intent_keywords"]):
            if data["service"] == "math_service":
                response = solve_math(query)
            elif data["service"] == "llm_service":
                response = await ask_llm(query)
            elif data["service"] == "wellness":
                response = "I'm here for you. Stay strong and take care of your mental well-being."
            else:
                response = "Unknown service"
            return {
                "agent": data["agent"],
                "intent": key,
                "response": response
            }
    
    # Default fallback
    response = await ask_llm(query)
    return {
        "agent": "Fallback LLM",
        "intent": "general",
        "response": response
    }

