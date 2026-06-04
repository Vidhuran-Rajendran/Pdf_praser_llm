
from app.query.sql_query import (
    run_sql
)

result = run_sql("""

SELECT *
FROM engineering_chunks
LIMIT 10

""")

for r in result:

    print(r)