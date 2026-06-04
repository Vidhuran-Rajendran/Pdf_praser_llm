import pandas as pd


def get_row_profile(row):

    values = [
        str(x).strip()
        for x in row
    ]

    numeric_count = 0
    text_count = 0
    empty_count = 0

    for v in values:

        if v.lower() in ["", "nan", "none"]:
            empty_count += 1

        elif any(c.isdigit() for c in v):
            numeric_count += 1

        else:
            text_count += 1

    populated = len(values) - empty_count

    return {
        "numeric": numeric_count,
        "text": text_count,
        "empty": empty_count,
        "populated": populated
    }
def segment_dataframe(df):

    segments = []

    current = []

    previous_profile = None

    for _, row in df.iterrows():

        row_values = list(row)

        profile = get_row_profile(row_values)

        # ✅ detect structural discontinuity
        split_condition = False

        if previous_profile:

            diff = abs(
                profile["populated"] -
                previous_profile["populated"]
            )

            # ✅ sudden structure shift
            if diff >= 3:
                split_condition = True

        if split_condition and current:

            segments.append(
                pd.DataFrame(current)
            )

            current = []

        current.append(row_values)

        previous_profile = profile

    if current:
        segments.append(
            pd.DataFrame(current)
        )

    return segments