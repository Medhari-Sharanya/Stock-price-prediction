import warnings
warnings.simplefilter(action='ignore', category=Warning)

import pandas as pd
import numpy as np
import streamlit as st
import plotly.graph_objs as go
import os

# -----------------------------
# Golden Crossover Signal
# -----------------------------
def GoldenCrossverSignal(name, data_point):

    path = f"Data/{name}.csv"

    if not os.path.exists(path):
        st.error("CSV file not found. Please check Data folder.")
        return None, None

    data = pd.read_csv(path)

    data['Date'] = pd.to_datetime(data['Date'])
    data.set_index('Date', inplace=True)

    # Moving averages
    data['20_SMA'] = data['Close'].rolling(window=20).mean()
    data['50_SMA'] = data['Close'].rolling(window=50).mean()

    # Signal
    data['Signal'] = 0
    data.loc[data['20_SMA'] > data['50_SMA'], 'Signal'] = 1
    data['Position'] = data['Signal'].diff()

    # Last N points
    recent = data.tail(data_point)

    df_pos = recent[(recent['Position'] == 1) | (recent['Position'] == -1)].copy()
    df_pos['Position'] = df_pos['Position'].map({1: 'Buy', -1: 'Sell'})

    # -----------------------------
    # Plot
    # -----------------------------
    trace_close = go.Scatter(
        x=data.index,
        y=data['Close'],
        mode='lines',
        name='Close Price'
    )

    trace_20 = go.Scatter(
        x=data.index,
        y=data['20_SMA'],
        mode='lines',
        name='20 SMA'
    )

    trace_50 = go.Scatter(
        x=data.index,
        y=data['50_SMA'],
        mode='lines',
        name='50 SMA'
    )

    buy = data[data['Position'] == 1]

    sell = data[data['Position'] == -1]

    trace_buy = go.Scatter(
        x=buy.index,
        y=buy['Close'],
        mode='markers',
        name='Buy',
        marker=dict(symbol='triangle-up', size=12)
    )

    trace_sell = go.Scatter(
        x=sell.index,
        y=sell['Close'],
        mode='markers',
        name='Sell',
        marker=dict(symbol='triangle-down', size=12)
    )

    fig = go.Figure(
        data=[trace_close, trace_20, trace_50, trace_buy, trace_sell]
    )

    fig.update_layout(
        title=f"{name} Golden Crossover",
        xaxis_title="Date",
        yaxis_title="Price"
    )

    return fig, df_pos


# -----------------------------
# Streamlit App
# -----------------------------
st.title("📈 Golden Crossover Stock Signal")

stock_name = st.text_input(
    "Enter Stock CSV name (without .csv)",
    "TATAMOTORS"
)

data_point = st.number_input(
    "Number of data points",
    min_value=50,
    value=300
)

capital = st.number_input(
    "Initial Capital",
    min_value=1000,
    value=50000
)

# Button
if st.button("Generate Signal"):

    fig, df_pos = GoldenCrossverSignal(stock_name, data_point)

    if fig is not None:
        st.plotly_chart(fig, use_container_width=True)

        st.subheader("Buy / Sell Signals")

        if len(df_pos) > 0:
            st.dataframe(df_pos[['Close', 'Position']].reset_index())
        else:
            st.write("No signals found.")
