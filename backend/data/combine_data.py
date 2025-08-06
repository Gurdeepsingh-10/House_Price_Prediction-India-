# Gonna combine the data from multiple cities into a single DataFrame
# But to Identify the city of origin, I will add a new column 'City' to each DataFrame 
# Ei ta e ektu tricky chilo decide kora je kibhabe combine korbo but its the best but pore chap hobe for deployment



import pandas as pd
import os

data_dir = os.path.join("data","raw")
cities = ["Delhi", "Mumbai", "Pune"]
all_dataframes = []

for city in cities:
    file_path = os.path.join(data_dir, f"{city}.csv")
    print(f"Reading data from: {file_path}")
    df = pd.read_csv(file_path)
    df['City'] = city  
    all_dataframes.append(df)

combined_df = pd.concat(all_dataframes, ignore_index=True)

print("Combined DataFrame:")
print(combined_df.head())

output_path = os.path.join("data", "processed", "combined_data.csv")
os.makedirs(os.path.dirname(output_path), exist_ok=True)
combined_df.to_csv(output_path, index=False)

print(f"\nCombined data saved to: {output_path}")