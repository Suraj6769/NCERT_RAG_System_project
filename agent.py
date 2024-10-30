from vectordb import query_vectordb
from tools import calculator

def handle_user_query(query):
    query = query.lower().strip()

    if "hello" in query:
        return "Hello! How can I assist you today?"

    elif any(keyword in query for keyword in ["add", "subtract", "multiply", "divide"]):
        return calculator(query)

    return query_vectordb(query)
