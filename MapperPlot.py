import numpy as np
import pandas as pd
import plotly
from gtda.mapper import(
    CubicalCover,
    make_mapper_pipeline,
    Projection,
    plot_static_mapper_graph,
    plot_interactive_mapper_graph,
    MapperInteractivePlotter
)
from sklearn.cluster import DBSCAN
from sklearn.preprocessing import MinMaxScaler
from sklearn.preprocessing import StandardScaler

def PlotMapper(df, n_intervals, overlap, columns = None, plot_dim=2):

    if columns == None:
        columns = df.columns
    # use no projection function just the raw data
    filter_func = Projection()
    # Define cover
    cover = CubicalCover(n_intervals=n_intervals, overlap_frac=overlap)
    # Choose clustering algorithm - default is DBSCAN
    clusterer = DBSCAN()

    # Initialise pipeline
    pipe = make_mapper_pipeline(
        filter_func=filter_func,
        cover=cover,
        clusterer=clusterer,
        verbose=False,
        n_jobs=1,
    )

    # use every column
    pipe.set_params(filter_func=Projection(columns=list(columns)))
    fig = plot_static_mapper_graph(pipe, df, layout_dim = plot_dim, color_data=df)
    fig.show(config={'scrollZoom': True})
    return

###########################################################################
# Read in data and change parameters for the Mapper plot in the lines below
###########################################################################

df = pd.read_csv("ohio_drugdeaths.csv")

# features = ['unemployment_rate', 'PCT_poverty']
print("Building Mapper Graph...")
PlotMapper(df, n_intervals = 6, overlap = .25, plot_dim=2)
