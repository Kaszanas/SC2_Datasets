#%%

import os
from pathlib import Path
import sys
import umap
import umap.plot
import seaborn as sns
import pandas as pd
from IPython.display import display
from sklearn.preprocessing import StandardScaler

sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), "../../..")))

from src.experiments.dim_reduction.groupby_util import groupby_fields_mean

#%%

csv_path = Path("../../../FIXED_sc2egset_csv.csv").resolve().as_posix()
print(csv_path)
#%%
loaded_data = pd.read_csv(csv_path)

#%%
unique_games = loaded_data["game_hash"].nunique()
print(f"Unique games: {unique_games}")
loaded_data.head()

#%%

groupby_fields = ["outcome", "race", "map_name", "player_name"]
drop_fields = ["game_time_gameloop", "gameloop"]
grouped_dataframes = groupby_fields_mean(data=loaded_data, fields=groupby_fields)

# Dropping game time from outcome as it surely does not differentiate players:
dropped_outcome = grouped_dataframes["outcome"].drop(labels=drop_fields, axis=1)
grouped_dataframes["outcome"] = dropped_outcome

# Dropping game hash:
for grouped_field, result_df in grouped_dataframes.items():
    grouped_unique_games = result_df["game_hash"].nunique()
    print(f"Grouped unique games by {grouped_field}: {grouped_unique_games}")
    print(
        f"Unique games grouped by {grouped_field} and grouped games match: {unique_games == grouped_unique_games}"
    )
    dropped_hash = result_df.drop(labels=["game_hash"], axis=1)
    grouped_dataframes[grouped_field] = dropped_hash

#%%

for grouped_field, result_df in grouped_dataframes.items():
    print(f"Grouped field was: {grouped_field}")
    display(result_df.head())

#%%

player_name_df = grouped_dataframes["player_name"]
print(player_name_df["player_name"].nunique())

#%%

umap_collection = {}

for grouped_field, result_df in grouped_dataframes.items():

    display(result_df[grouped_field].head())

    unique_grouped = result_df[grouped_field].unique()

    # Mapping target to digits:
    unique_map_learning = {
        unique_field: str(i) for i, unique_field in enumerate(unique_grouped)
    }
    unique_map_display = {v: k for k, v in unique_map_learning.items()}
    result_df[grouped_field] = result_df[grouped_field].map(unique_map_learning)

    # Standardizing the data:
    without_grouped_field = result_df.loc[:, result_df.columns != grouped_field]
    standardized_data = StandardScaler().fit_transform(without_grouped_field)

    reducer = umap.UMAP(random_state=42)
    reducer.fit(X=standardized_data, y=result_df[grouped_field])
    print(f"UMAP for field {grouped_field}")

    umap_collection[grouped_field] = reducer

    umap.plot.output_file(filename=f"{grouped_field}_interactive_bokeh_plot.html")
    interactive_plot = umap.plot.interactive(
        reducer,
        labels=result_df[grouped_field].map(unique_map_display),
        color_key_cmap="Paired",
        background="black",
    )
    static_plot = umap.plot.points(
        reducer,
        labels=result_df[grouped_field].map(unique_map_display),
        color_key_cmap="Paired",
        background="black",
    )
    umap.plot.show(static_plot)
    umap.plot.output_file(filename=f"{grouped_field}_static_bokeh_plot.html")
    umap.plot.show(interactive_plot)
