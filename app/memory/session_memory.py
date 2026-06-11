conversation_history = []

def add_message(role, content):
    conversation_history.append({
        "role": role,
        "content": content
    })


def get_history():
    return conversation_history

def clear_history():
    conversation_history.clear()
    
memory_store = {}

def set_last_dvp(dvp):
    memory_store["last_dvp"] = dvp

def get_last_dvp():
    return memory_store.get("last_dvp")
