def deduplicate_context(results):
    unique = []
    seen = set()
    
    for r in results:
        if isinstance(r,dict):
            text = str(r.get("document","")).strip()
        else:
            text = str(r).strip()
        
        if text in seen:
            continue
        seen.add(text)
        unique.append(text)
        
    return unique