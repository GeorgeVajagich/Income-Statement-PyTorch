import pandas as pd
import numpy as np
import requests
import streamlit as st
import plotly # library for plotting
import plotly.express as px # library for plotting

# getting key
key=pd.read_csv(r"C:\Users\Geord\OneDrive\Desktop\Economics_Stuff\financeKey.txt",header=None)[0][0]

# extracting data from the internet as a json file
ticker="AAPL"
URL=("https://financialmodelingprep.com/api/v3/income-statement/"+ticker+"?apikey="+key)
data = requests.get(URL).json()

#  function that extracts data from the internet as a json file then turns the json file into pandas dataframe

def createdf(ticker):
    URL=("https://financialmodelingprep.com/api/v3/income-statement/"+ticker+"?apikey="+key)
    data = requests.get(URL).json()
    # turning json file into pandas dataframe
    df=pd.DataFrame(data)
    return(df)


# creating function to prints revenue over the past 4 years and revenue growth over the past 1 year for a given stock
def revenue(ticker):
    stock=createdf(ticker)
    return(stock["revenue"])

# function to show last 4 years of revenue growth
def past4growth(ticker):
    stock=createdf(ticker)
    print(ticker)
    print(stock["revenue"][0]/stock["revenue"][1])
    print(stock["revenue"][1]/stock["revenue"][2])
    print(stock["revenue"][2]/stock["revenue"][3])
    print(stock["revenue"][3]/stock["revenue"][4])

# function to show median revenue growth
def mediangrowth(ticker):
    stock=createdf(ticker)
    print(ticker)
    g1=(stock["revenue"][0]/stock["revenue"][1])
    g2=(stock["revenue"][1]/stock["revenue"][2])
    g3=(stock["revenue"][2]/stock["revenue"][3])
    g4=(stock["revenue"][3]/stock["revenue"][4])
    data = np.array([g1,g2,g3,g4])
    print(np.median(data))
    return(np.median(data))

# creating function to project next 5 years of revenue
def futurerevenue(ticker):
    stock=createdf(ticker)
    rate=mediangrowth(ticker)
    start=int(stock["revenue"][0])
    print(start*rate)
    print(start*rate**2)
    print(start*rate**3)
    print(start*rate**4)
    print(start*rate**5)


st. set_page_config(layout="wide")

t=st.chat_input('Ticker')
t=str(t)
try:
    fig = px.scatter(x=[1,2,3,4],y=[1,2,3,4])


    st.write(t)
    st.write(revenue(t))
    st.write("median revenue growth")
    st.write(mediangrowth(t))
    st.plotly_chart(fig)
except:
    pass