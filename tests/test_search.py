from app.query.semantic_search import (
    semantic_search
)

results = semantic_search(
    "maximum front pad temperature"
)

print(results)