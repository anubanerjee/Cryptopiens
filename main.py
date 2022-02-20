# pip3 install pystan=2.19.1.1 streamlit fbprophet yfinance plotly
# http://lethalletham.com/ForecastingAtScale.pdf
import streamlit as st
from datetime import date

import yfinance as yf
from fbprophet import Prophet
from fbprophet.plot import plot_plotly
from plotly import graph_objs as go

st.title('Crypto Price Forecast Application: Cryptopiens.tech')

START = st.date_input("State the starting date", date(2020, 1, 1))
START = START.strftime("%Y-%m-%d")
st.write('The system starts at:', START)
#START = "2021-01-01"
TODAY = date.today().strftime("%Y-%m-%d")

crypto = ('BTC-USD', 'ETH-USD', 'USDT-USD', 'DOGE-USD', 'XRP-USD', 'LTC-USD')
selected_crypto = st.selectbox('Select dataset for prediction', crypto)
#stocks = ('GOOGL', 'AAPL', 'MSFT', 'TSLA', 'FB', 'PFE')
#selected_stock = st.selectbox('Select dataset for prediction', stocks)

n_quarters = st.slider('Quarter of prediction:', 1, 4)
period = n_quarters * 3 * 30

budget = st.number_input('Insert your budget')
st.write('Your budget is: ', budget)

@st.cache
def load_data(ticker):
	data = yf.download(ticker, START, TODAY)
	data.reset_index(inplace=True)
	return data

	
data_load_state = st.text('Loading data...')
data = load_data(selected_crypto)
data_load_state.text('Loading data... done!')

st.subheader('Raw data')
st.write(data.tail())

# Plot raw data
def plot_raw_data():
	fig = go.Figure()
	fig.add_trace(go.Scatter(x=data['Date'], y=data['Open'], name="stock_open"))
	fig.add_trace(go.Scatter(x=data['Date'], y=data['Close'], name="stock_close"))
	fig.layout.update(title_text='Time Series data with Rangeslider', xaxis_rangeslider_visible=True)
	st.plotly_chart(fig)
	
plot_raw_data()

# Predict forecast with Prophet.
df_train = data[['Date','Close']]
df_train = df_train.rename(columns={"Date": "ds", "Close": "y"})

m = Prophet()
m.fit(df_train)
future = m.make_future_dataframe(periods=period)
forecast = m.predict(future)

# Show and plot forecast
st.subheader('Forecast data')
st.write(forecast.tail())
    
st.write(f'Forecast plot for {n_quarters} quarters')
fig1 = plot_plotly(m, forecast)
st.plotly_chart(fig1)

st.write("Forecast components")
fig2 = m.plot_components(forecast)
st.write(fig2)


import seaborn as sb 
import pandas as pd 
import matplotlib.pyplot as plt 
fig3 = plt.figure()


def suggest(crypto):
	forecasts = []
	for coin in crypto:
		data =load_data(coin)
		df_train = data[['Date','Close']]
		df_train = df_train.rename(columns={"Date": "ds", "Close": "y"})
		m = Prophet()
		m.fit(df_train)
		future = m.make_future_dataframe(periods=period)
		forecast = m.predict(future)
		forecast['change'] = forecast['yhat'] = forecast['yhat'] - forecast['yhat'].shift(-1)
		forecasts.append(forecast['yhat'])
		sb.lineplot(x="ds", y="change", data=forecast) 	

suggest(crypto)

plt.ylabel("Change in predicted price") 
plt.legend(labels=crypto)
st.write(fig3)
