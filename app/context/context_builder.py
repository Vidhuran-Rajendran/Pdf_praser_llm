def build_structured_context(chunks):

    sections = []
    for idx, chunk in enumerate(chunks):
        block = f"""
[Context {idx+1}]
{chunk}
"""
        sections.append(block)
    return "\n".join(sections)