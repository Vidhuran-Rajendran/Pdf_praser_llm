import pandas as pd


def propagate_semantic_rows(df):

    if len(df.columns) == 0:
        return df

    first_col = df.iloc[:, 0]

    propagated = []

    previous_value = None

    for val in first_col:

        val_str = str(val).strip()

        # ✅ semantic parent row
        if (
            val_str.lower() not in
            ["", "nan", "none"]
        ):

            previous_value = val

            propagated.append(val)

        else:

            propagated.append(previous_value)

    df.iloc[:, 0] = propagated

    return df