import pandas as pd

df = pd.read_csv("Condefects-Python.csv")

def select_balanced_rows(df, column_name, sample_size=20):
    difficulty_counts = df[column_name].value_counts()

    proportion_per_difficulty = sample_size // len(difficulty_counts)
    
    sampled_df = pd.DataFrame()

    for difficulty, count in difficulty_counts.items():
        subset = df[df[column_name] == difficulty]
        subset_sample = subset.sample(min(proportion_per_difficulty, len(subset)), random_state=1)
        sampled_df = pd.concat([sampled_df, subset_sample])

    remaining_rows = sample_size - len(sampled_df)
    if remaining_rows > 0:
        additional_rows = df[~df.index.isin(sampled_df.index)].sample(remaining_rows, random_state=1)
        sampled_df = pd.concat([sampled_df, additional_rows])
    
    return sampled_df

sampled_rows = select_balanced_rows(df, 'Difficulty', sample_size=20)

sampled_rows.to_csv('sampled_dataset.csv', index=False)