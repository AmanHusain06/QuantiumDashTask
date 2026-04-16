import pandas as pd
from dash import Dash, html, dcc, Input, Output
import plotly.express as px

df = pd.read_csv("processed_data.csv")
df["Date"] = pd.to_datetime(df["Date"])

app = Dash(__name__)

app.layout = html.Div(
    style={
        "backgroundColor": "#f8f9fa",
        "minHeight": "100vh",
        "padding": "30px",
        "fontFamily": "Arial, sans-serif"
    },
    children=[
        html.Div(
            style={
                "maxWidth": "1100px",
                "margin": "0 auto",
                "backgroundColor": "white",
                "padding": "30px",
                "borderRadius": "15px",
                "boxShadow": "0 4px 12px rgba(0,0,0,0.1)"
            },
            children=[
                html.H1(
                    "Soul Foods Pink Morsel Sales Dashboard",
                    id="app-header",
                    style={
                        "textAlign": "center",
                        "marginBottom": "10px",
                        "color": "#222"
                    }
                ),

                html.P(
                    "Explore Pink Morsel sales over time and compare regions before and after the January 15, 2021 price increase.",
                    style={
                        "textAlign": "center",
                        "color": "#555",
                        "marginBottom": "30px"
                    }
                ),

                html.Label(
                    "Filter by Region:",
                    style={
                        "fontWeight": "bold",
                        "fontSize": "16px",
                        "display": "block",
                        "marginBottom": "10px"
                    }
                ),

                dcc.RadioItems(
                    id="region-picker",
                    options=[
                        {"label": "All", "value": "all"},
                        {"label": "North", "value": "north"},
                        {"label": "East", "value": "east"},
                        {"label": "South", "value": "south"},
                        {"label": "West", "value": "west"},
                    ],
                    value="all",
                    inline=True,
                    style={"marginBottom": "25px"},
                    labelStyle={
                        "marginRight": "20px",
                        "fontSize": "15px"
                    }
                ),

                dcc.Graph(id="sales-chart")
            ]
        )
    ]
)


@app.callback(
    Output("sales-chart", "figure"),
    Input("region-picker", "value")
)
def update_chart(selected_region):
    filtered_df = df.copy()

    if selected_region != "all":
        filtered_df = filtered_df[filtered_df["Region"] == selected_region]

    daily_sales = (
        filtered_df.groupby("Date", as_index=False)["Sales"]
        .sum()
        .sort_values("Date")
    )

    fig = px.line(
        daily_sales,
        x="Date",
        y="Sales",
        title=f"Pink Morsel Sales Over Time - {selected_region.capitalize()}",
        labels={"Date": "Date", "Sales": "Sales"}
    )

    fig.update_layout(
        plot_bgcolor="white",
        paper_bgcolor="white",
        title_x=0.5
    )

    return fig


if __name__ == "__main__":
    app.run(debug=True)