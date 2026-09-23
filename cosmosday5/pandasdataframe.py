import math, pandas as pd 
data = {
    "Name": ["Alice", "Bob", "Charlie", "David"],
    "score": [85, 92, 78, 90]
}
df = pd.DataFrame(data)
top_scorer = df.loc[df['score'].idxmax()]
