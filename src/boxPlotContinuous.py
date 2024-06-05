from plotly.subplots import make_subplots
import plotly.graph_objects as go
from src.main_LoadDataFrame import load_data
import globals as gl


def main():
    dataf = load_data()
    print(dataf.describe())

    fig = make_subplots(rows=8, cols=1)

    for i in range(len(gl.continuous_features)):
        fig.add_trace(go.Box(x=dataf[gl.continuous_features[i]], name=gl.continuous_features[i]), row=i + 1, col=1)

    fig.update_layout(height=3000, width=1000)
    fig.show()


main()
