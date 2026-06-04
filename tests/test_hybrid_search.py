from app.query.hybrid_search import hybrid_search

results = hybrid_search(
    "front pad maximum temperature"
)

print("\n=== SEMANTIC ===\n")
print(results["semantic_results"])

print("\n=== KEYWORD ===\n")
print(results["keyword_results"])
