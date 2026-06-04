def build_context(results):

    context = []

    for idx, r in enumerate(results):

        chunk = f"""
[Context {idx+1}]
Page: {r['metadata']['page']}

{r['document']}
"""

        context.append(chunk)

    return "\n".join(context)