from app.agent.router import route_query
from app.agent.tools import rag_tool,sql_tool


def run_agent(query):
    route = route_query(query)
    if route == "sql":
        return sql_tool(query)
    else:
        return rag_tool(query)
