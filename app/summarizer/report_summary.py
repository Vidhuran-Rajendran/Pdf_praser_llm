import ollama
from app.query.sql_query import run_sql

def summarize_report():

    rows = run_sql("""
    SELECT content
    FROM engineering_chunks
    LIMIT 100
    """)

    combined = "\n".join(r[0] for r in rows)
    prompt = f"""

Summarize this engineering report.

Focus on:
- brake system
- temperature observations
- important metrics
- test conditions

Report Content:
{combined}

"""

    response = ollama.chat(model="qwen2.5",messages=[{"role": "user","content": prompt}])

    return response["message"]["content"]