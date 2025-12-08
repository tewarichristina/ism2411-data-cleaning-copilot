"Cleans a messy sales dataset and outputs a cleaned version."

import pandas as pd

#standardize column names
def clean_column_names(df):
    df = df.copy()
    df.columns = (
        df.columns 
        .str.strip()
        .str.lower()
        .str.replace(' ', '_')
        .str.replace("-", "_")
    )
    return df

#Function that handles missing values in price and qty
def handle_missing_values(df):
    df = df.copy()
    df["price"] = pd.to_numeric(df["price"], errors="coerce")
    df["qty"] = pd.to_numeric(df["qty"], errors ="coerce")
#Drops missing price
    df = df.dropna(subset=["price"])
    df["qty"] = df["qty"].fillna(1)

    return df

def remove_duplicates(df):
    df = df.copy()
    df = df.drop_duplicates()
    return df

def strip_text_columns(df):
    df = df.copy()
    text_columns = df.select_dtypes(include=["object"]).columns
    for col in text_columns:
        df[col] = df[col].str.strip()
    return df

if __name__ == "__main__":
    raw_path = "data/raw/sales_data_raw.csv"
    cleaned_path = "data/processed/sales_data_clean.csv"
    df = pd.read_csv(raw_path)
    df = clean_column_names(df)
    df = handle_missing_values(df)
    df = remove_duplicates(df)
    df = strip_text_columns(df)
    df.to_csv("data/cleaned_customer.csv", index=False)

    print("Data cleaning complete.")
    print(df.head())

