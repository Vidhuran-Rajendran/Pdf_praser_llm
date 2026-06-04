import pandas as pd

from app.parser.table_segmenter import (
    segment_dataframe
)

from app.parser.semantic_propagator import (
    propagate_semantic_rows
)

import pandas as pd


def remove_sparse_columns(df):

    cols_to_keep = []

    total_rows = len(df)

    for col in df.columns:

        values = (
            df[col]
            .astype(str)
            .str.strip()
            .str.lower()
        )

        # ✅ count meaningful cells
        meaningful = values[
            ~values.isin(["", "nan", "none"])
        ]

        meaningful_count = len(meaningful)

        # ✅ keep if at least 30% rows contain data
        if meaningful_count >= max(2, int(total_rows * 0.3)):
            cols_to_keep.append(col)

    return df[cols_to_keep]

def normalize_tables(tables):

    final_tables = []

    for t in tables:

        df = t["df"]
        # df = remove_sparse_columns(df)
        df = df.dropna(axis=1, how="all")

        # ✅ clean only fully empty rows/cols
        df = df.dropna(axis=0, how="all")
       

        # ✅ preserve structure
        df = df.fillna(None)

        # ✅ segment logically
        segments = segment_dataframe(df)

        for idx, seg in enumerate(segments):

            # ✅ semantic propagation
            seg = propagate_semantic_rows(seg)

            final_tables.append({
                "table_id":
                    f"{t['table_id']}_segment_{idx}",

                "page": t["page"],

                "df": seg
            })

    return final_tables