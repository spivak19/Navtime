import pandas as pd
def search(df,SearchWord):
    def search_string(s, search):
        return search in str(s)

    # Search for the string 'al' in all columns
    mask = df.apply(lambda x: x.map(lambda s: search_string(s, SearchWord)))

    # Filter the DataFrame based on the mask
    filtered_df = df.loc[mask.any(axis=1)]

    return filtered_df