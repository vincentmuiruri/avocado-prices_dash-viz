# import the required libraries

from dash import Dash
from dash import dcc
from dash import html
import pandas as pd

# reading the dataset
filepath = "D:/Practice Projects/Python/avocado-prices_dash viz/avocado.csv"
data = pd.read_csv(filepath)

# query the dataset to get region of albany
data = data.query("type == 'conventional' and region == 'Albany'")

# convert the 'Date' column to datetime format and sort the data by date
data['Date'] = pd.to_datetime(data['Date'], format='%Y-%m-%d') 

# sort the data by date
data.sort_values('Date', inplace=True)

# print the first few rows of the processed data
print(data.head())

# initialize the Dash app
app = Dash(__name__)

# define the layout of the app
app.layout = html.Div(
    children=[
        html.H1(children="Avocado Analytics", style={'textAlign': 'center'}),
        html.P(
            children="Analyze the behavior of avocado prices and volumes in the US while"
                     " reviewing the number of avocados sold in the US between 2015 and 2018.",
        ),
        dcc.Graph(
            figure={
                "data": [
                    {
                        "x": data["Date"],
                        "y": data["AveragePrice"],
                        "type": "line",
                    }
                ],
                "layout": {"title": "Average Price of Avocados"}
            },
        ),
        dcc.Graph(
            figure={
                "data": [
                    {
                        "x": data["Date"],
                        "y": data["Total Volume"],
                        "type": "line",
                    }
                ],
                "layout": {"title": "Avocados Sold"},
            },
        ),
    ]
)

# run the app locally using built in server
if __name__ == "__main__":
    app.run(debug=True)    # changes on the code will be reflected without restarting the server

