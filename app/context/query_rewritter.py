from app.memory.session_memory import get_history

def rewrite_query(current_query):
    history = get_history()

    # ✅ previous user queries
    previous_queries = [h["content"]for h in history if h["role"] == "user"]

    # ✅ no history
    if not previous_queries:
        return current_query

    previous_query = previous_queries[-1]

    # ✅ avoid duplicate expansion
    if current_query.lower() in previous_query.lower():
        return current_query

    # ✅ contextual rewrite
    rewritten = (previous_query+ " "+ current_query)
    return rewritten