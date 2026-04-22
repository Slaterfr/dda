import pandas as pd
from .ingestion import Ingestion


class Transform:

    @staticmethod
    def transform(coin: str = None):

        data = Ingestion.get_marked_data(coin)
        df = pd.DataFrame(data)
        
        df = Transform.clean(df)

        print(df)
        return df

    @staticmethod
    def clean(df):

        df = df.copy()

        # Select relevant columns from the API response
        # Adjust these based on actual API column names
        relevant_cols = [col for col in ["id", "current_price", "market_cap", "total_volume", "last_updated"] 
                        if col in df.columns]
        
        if not relevant_cols:
            print(f"Warning: None of the expected columns found. Available columns: {df.columns.tolist()}")
            return df
        
        df = df[relevant_cols]

        # Convert numeric columns to numeric type
        numeric_cols = [col for col in relevant_cols if col in ["current_price", "market_cap", "total_volume"]]
        for col in numeric_cols:
            df[col] = pd.to_numeric(df[col], errors="coerce")

        # Convert timestamp column if it exists
        if "last_updated" in df.columns:
            df["last_updated"] = pd.to_datetime(df["last_updated"], errors="coerce")

        # Drop rows with missing critical values
        if "id" in df.columns:
            df = df.dropna(subset=["id"])

        return df

    
if __name__ == '__main__':
    Transform.transform()
