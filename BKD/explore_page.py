import numpy
import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import matplotlib.pyplot as plt
import numpy as np
import seaborn as sns


def shorten_categories(categories, cutoff):
    categorical_map = {}
    for i in range(len(categories)):
        if categories.values[i] >= cutoff:
            categorical_map[categories.index[i]] = categories.index[i]
        else:
            categorical_map[categories.index[i]] = 'Other'
    return categorical_map


def clean_experience(x):
    if x ==  'More than 50 years':
        return 50
    if x == 'Less than 1 year':
        return 0.5
    return float(x)


def clean_education(x):
    if 'Bachelor’s degree' in x:
        return 'Bachelor’s degree'
    if 'Master’s degree' in x:
        return 'Master’s degree'
    if 'Professional degree' in x or 'Other doctoral' in x:
        return 'Post grad'
    return 'Less than a Bachelors'


@st.cache
def load_data():
    df = pd.read_csv("bank-additional-full.csv",sep=";")
    df = df[["job", "marital", "education", "housing", "loan", "age", "y"]]
    return df

df = load_data()

def pl():
    fig, ax = plt.subplots()
    sns.countplot(x ='y', data = df, palette = 'viridis')

    plt.title('Deposit Distribution of Bank Customers', fontsize = 16)
    plt.xlabel('Deposit', fontsize = 14)
    plt.ylabel('Total Customers', fontsize = 14)
    plt.xticks(fontsize = 12)

    # Show the plot
    st.pyplot()

def show_explore_page():
    #pl()
    #st.set_option('deprecation.showPyplotGlobalUse', False)
    is_check = st.checkbox("Display Data")
    if is_check:
        st.write(df)

    teams = st.sidebar.multiselect("Enter jobs", df['job'].unique())
    

    variables = st.sidebar.multiselect("Enter the variables", df.columns)
    
    selected_club_data = df[(df['job'].isin(teams))]

    two_clubs_data = selected_club_data[variables]
    club_data_is_check = st.checkbox("Display the data of selected jobs")
    if club_data_is_check:
        st.write(two_clubs_data)
