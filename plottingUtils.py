import plotly.graph_objects as go


def plottingOnMaps(nodes, path=False, paths=False, start=False):  # one function for plot all the functionalities
    fig = go.Figure(go.Scattermapbox())  # creating the object

    if path:  # we have only one path
        # gathering the coordinates of all those nodes
        lon, lat = list(zip(*list(map(lambda node: (nodes[node][0] / 1000000, nodes[node][1] / 1000000), path))))
        # plotting the path
        fig.add_trace(go.Scattermapbox(
            mode="markers+lines",
            lon=lon,
            lat=lat,
            marker={'size': 8, "color": "blue"}))
        # plotting the starting point of the path
        fig.add_trace(go.Scattermapbox(
            mode="markers",
            lon=[nodes[path[0]][0] / 1000000],
            lat=[nodes[path[0]][1] / 1000000],
            marker={'size': 14, "color": "green"}))

    elif paths: # if we have several paths
        for path in paths:  # plotting each path
            # gathering the coordinates of all those nodes
            lon, lat = list(zip(*list(map(lambda node: (nodes[node][0] / 1000000, nodes[node][1] / 1000000), path))))
            # plotting the path
            fig.add_trace(go.Scattermapbox(
                mode="markers+lines",
                lon=lon,
                lat=lat,
                marker={'size': 8, "color": "blue"}))

        if type(start) == list:  # if we have several starting points
            # gathering the coordinates of all those nodes
            lon, lat = list(zip(*list(map(lambda node: (nodes[node][0] / 1000000, nodes[node][1] / 1000000), start))))
            # plotting their points
            fig.add_trace(go.Scattermapbox(
                mode="markers",
                lon=lon,
                lat=lat,
                marker={'size': 14, "color": "green"}))
        if type(start) == int:  # if we have only one starting pont for all those paths
            # plotting the point
            fig.add_trace(go.Scattermapbox(
                mode="markers",
                lon=[nodes[start][0] / 1000000],
                lat=[nodes[start][1] / 1000000],
                marker={'size': 14, "color": "green"}))

    # getting the map
    fig.update_layout(mapbox_style="open-street-map")
    fig.update_layout(margin={'l': 40, 't': 40, 'b': 40, 'r': 40})

    # plotting finally
    fig.show()
