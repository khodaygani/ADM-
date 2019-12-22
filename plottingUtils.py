import plotly.graph_objects as go


def plottingOnMaps(nodes, path=False, paths=False, start=False):
    fig = go.Figure(go.Scattermapbox())

    if path:
        lon, lat = list(zip(*list(map(lambda node: (nodes[node][0] / 1000000, nodes[node][1] / 1000000), path))))
        fig.add_trace(go.Scattermapbox(
            mode="markers+lines",
            lon=lon,
            lat=lat,
            marker={'size': 8, "color": "blue"}))

        fig.add_trace(go.Scattermapbox(
            mode="markers",
            lon=[nodes[path[0]][0] / 1000000],
            lat=[nodes[path[0]][1] / 1000000],
            marker={'size': 14, "color": "green"}))

    elif paths:
        for path in paths:
            lon, lat = list(zip(*list(map(lambda node: (nodes[node][0] / 1000000, nodes[node][1] / 1000000), path))))
            fig.add_trace(go.Scattermapbox(
                mode="markers+lines",
                lon=lon,
                lat=lat,
                marker={'size': 8, "color": "blue"}))

        if start:
            fig.add_trace(go.Scattermapbox(
                mode="markers",
                lon=[nodes[path[0]][0] / 1000000],
                lat=[nodes[path[0]][1] / 1000000],
                marker={'size': 14, "color": "green"}))

    fig.update_layout(mapbox_style="open-street-map")
    fig.update_layout(margin={'l': 0, 't': 0, 'b': 0, 'r': 0})

    fig.show()