import streamlit as st
import pandas as pd
import numpy as np
import pickle
from sklearn.tree import DecisionTreeClassifier
from sklearn.ensemble import RandomForestClassifier

from sklearn.preprocessing import LabelEncoder

from sklearn.preprocessing import MinMaxScaler
from sklearn.model_selection import train_test_split
from sklearn.metrics import classification_report, confusion_matrix
st.set_page_config(layout="wide")

#Collecter le profil d'entrée

def show_predict_page():
    def client_caract_entree():
        st.header("Deposit Prediction")
        st.subheader("Customer characteristics")
        col1, col2, col3, col4 = st.columns(4)

        #'''----------age-----------'''
        age = col1.slider('Age',18,100)
        #'''----------job-----------------------------------------------------------------------'''

        jobs = ['Unknown', 'Housemaid', 'Services', 'Admin', 'Blue-collar', 'Technician' ,'Retired',
        'Management', 'Unemployed', 'Self-employed', 'Entrepreneur', 'Student']
        numjob = [11, 3,  7,  0,  1,  9,  5,  4, 10,  6,  2,  8]
        job = col4.selectbox('Type of job',jobs)
        index = jobs.index(job)
        job =numjob[index]
        #'''----------aritals----------------------------------------------------------------------'''

        aritals = ['Unknown', 'Married', 'Single', 'Divorced']
        numaritals=[3, 1, 2, 0]
        arital = col3.radio('Marital status',aritals)
        index = aritals.index(arital)
        arital =numaritals[index]

        #'''------------------------education------------------------------------------------------'''
        educations = ['Unknown', 'High School', 'Basic 4Y', 'Basic 6Y', 'Basic 9Y', 'Professional Course',
        'University Degree', 'Illiterate']
        numeducations=[7, 3, 0, 1, 2, 5, 6, 4]
        education = col4.selectbox('Education',educations)
        index = educations.index(education)
        education =numeducations[index]
        #'''-------------------------------default---------------------------------------------------'''
        defaults = ['Unknown', 'No', 'Yes']
        numdefaults = [1, 0, 2]
        default = col3.radio('Has credit in default?',defaults)
        index = defaults.index(default)
        default =numdefaults[index]

        #'''-------------------------------housing---------------------------------------------------'''
        housings = ['Unknown', 'No', 'Yes']
        numhousings = [1, 0, 2]
        housing = col3.radio('Has housing loan?',housings)
        index = housings.index(housing)
        housing =numhousings[index]
        #'''-------------------------------loan---------------------------------------------------'''
        loans = ['Unknown', 'No', 'Yes']
        numloans = [1, 0, 2]
        loan = col3.radio('Has personal loan?',loans)
        index = housings.index(loan)
        loan =numloans[index]

        #'''-------------------------------contact---------------------------------------------------'''
        contacts = ['Telephone', 'Cellular']
        numcontacts = [1, 0]
        contact = col3.radio('Contact communication type',contacts)
        index = contacts.index(contact)
        contact =numcontacts[index]

        #'''-------------------------------month---------------------------------------------------'''
        months = ['Jan','Feb', 'Mar', 'Apr', 'May', 'Jun', 'Jul', 'Aug', 'Sep', 'Oct', 'Nov', 'Dec']
        nummonths = [10, 11, 5, 0, 6, 4, 3, 1, 9, 8, 7, 2]
        month = col4.selectbox('Last contact month of year',months)
        index = months.index(month)
        month =nummonths[index]

        #'''-------------------------------day_of_week---------------------------------------------------'''
        days = ['Mon', 'Tue', 'Wed', 'Thu', 'Fri']
        numdays = [1, 3, 4, 2, 0]
        day = col4.selectbox('Last contact day of the week',days)
        index = days.index(day)
        day =numdays[index]
        #---
        duration = col1.slider('Last contact duration',0,1000)
        campaign = col1.slider('Number of contacts performed during this campaign and for this client',1,100)
        previous = col1.slider('Number of contacts performed before this campaign and for this client',0,7)

        #'''-------------------------------poutcome---------------------------------------------------'''
        poutcomes = ['Nonexistent', 'Failure', 'Success']
        numpoutcomes = [1, 0, 2]
        poutcome = col3.radio('Outcome of the previous marketing campaign',poutcomes)
        index = poutcomes.index(poutcome)
        poutcome =numpoutcomes[index]

        emp = col1.slider('Employment variation rate',-3.4,1.5)
        cons = col1.slider('Consumer price index',92.2,94.9)
        consconf = col1.slider('Consumer confidence index',-50.8,-26.9)
        euribor3m = col1.slider('Euribor 3 month rate',0.1,6.1)
        employed = col1.slider('Number of employees ',0,6000)
    
        data={
        'Age':age,
        'Job':jobs[numjob.index(job)],
        'Arital':aritals[numaritals.index(arital)],
        'Education':educations[numeducations.index(education)],
        'Default':defaults[numdefaults.index(default)],
        'Housing':housings[numhousings.index(housing)],
        'Loan':loans[numloans.index(loan)],
        'Contact':contacts[numcontacts.index(contact)],
        'Month':months[nummonths.index(month)],
        'Day':days[numdays.index(day)],
        'Duration':duration,
        'Campaign':campaign,

        'previous':previous,
        'poutcome':poutcomes[numpoutcomes.index(poutcome)],
        'emp':emp,
        'cons':cons,
        'consconf':consconf,
        'euribor3m':euribor3m,
        'employed':employed
        
        }
        a =	[[age, job,arital,education,default,housing,loan,contact,month,day,duration,campaign,previous,poutcome,emp,cons,consconf,euribor3m,employed]]
        profil_client=pd.DataFrame(data,index=[0])
        return profil_client,a

    input_df,a=client_caract_entree()

    #importer le modèle

    def load_model():
        with open('Model1.pkl', 'rb') as file:
            data = pickle.load(file)
        return data

    datamodel = load_model()




    #Transformer les données d'entrée en données adaptées à notre modèle
    #importer la base de données
    #df=pd.read_csv('train.csv')
    #credit_input=df.drop(columns=['Loan_ID','Loan_Status'])
    #donnee_entree=pd.concat([input_df,credit_input],axis=0)


    #prendre uniquement la premiere ligne
    #donnee_entree=donnee_entree[:1]

    #afficher les données transformées
    st.subheader('Transformed Characteristics')

    st.write(input_df)
    st.subheader('Prediction result')
    y = datamodel.predict(a)
    if y == [[1]]:
        st.write('Deposit')
    else:
        st.write('No')