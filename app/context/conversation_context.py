from app.memory.session_memory import get_history

def build_conversation_context():

    history = get_history()
    context = ""

    for h in history[-6:]:
        context += f"""
{h['role'].upper()}:
{h['content']}
"""
    return context