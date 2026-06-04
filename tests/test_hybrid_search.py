from app.query.hybrid_search import (
    hybrid_search
)

results = hybrid_search(
    "front pad maximum temperature"
)

print("\n=== RESULTS ===\n")

for r in results:

    print("SOURCE:", r["source"])
    print("PAGE:", r["metadata"]["page"])
    print("RERANK:", r["rerank_score"])

    print(r["document"])

    print("\n-------------------\n")
