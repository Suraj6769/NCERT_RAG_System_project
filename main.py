from fastapi import FastAPI, Request
from agent import Agent

app = FastAPI()
agent = Agent()

@app.post("/agent_action")
async def agent_action(request: Request):
    data = await request.json()
    user_query = data.get("query", "")
    
    # Agent decides which action to take
    action_type, result = agent.decide_action(user_query)

    return {
        "action": action_type,
        "result": result
    }

# To run the API: uvicorn main:app --reload
