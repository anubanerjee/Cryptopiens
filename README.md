**Cryptopiens** has been launched with an aim to enhance the performance of cryptocurrencies for the **techie sapiens**. It will provide investors with a complete outlook of the past, present and near future of the cryptocurrency market. It combines 3 actions in a single platform:
1. Provide past trend of different cryptocurrencies
2. Predict their future values
3. Evaluate the optimized time to invest and trade cryptos for maximum possible return in the user specified time period.

Currently, the application supports the following cryptocurrencies.
1. **Bitcoin**
2. **Ethereum**
3. **Dogecoin**
4. **Tether**
5. **Litecoin**
6. **Ripple**

#### A sample prediction of the future:
![alt text](predictSuggest.png)

## Inspiration
Forecast and analysis to minimize losses and in turn maximize gain through investment in cryptocurrencies.

## What it does
Provides a detailed insight into past and present trends, predict future trends and notify users when to trade cryptocurrencies based on user budget and time period of investment.

## How we built it
1. Python using streamlit
2. Historic data of the crypto currencies from yahoo finance
3. Prediction using an open source tool: fbprophet
4. Plots using seaborn library

## Challenges we ran into
1 . Hosting the dynamic application 
2. Google cloud computing machine was too slow for our application. We had to generate the plots from our localhost and add it on the static webpage.

## Accomplishments that we're proud of
1. We are very glad to make Cryptopiens public. 
2. The web application is available for use at https://static.cryptopiens.tech. The github repository contains the code for dynamic usage of the application. 
3. This dynamic version lets the user select their budget, risk allowance, number of quarters, etc. The. user can see the suggestion based on their choices and peek into each crypto currency we support separately.

## What we learned
1. We used a new machine learning time series prediction model in this project, **FbProphet**. The library is open source. We used a github page and linked it with an external domain using a new domain we bought at **domain.com**.

## What's next for Cryptopiens
1. Cryptopiens is soon going to support DeSo. We are waiting for more data availability.
2. The website only has a static page as the host Github pages only support static pages. We are planning to use google cloud hosting and computing to work around this.
3. Cryptopiens is soon going to have an implementation of a graph-based risk measurement tool for crypto sapiens.