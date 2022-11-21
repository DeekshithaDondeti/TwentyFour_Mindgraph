import pickle
import pandas as pd
import streamlit as st

st.title("Data Storytelling")

st.subheader('Problem Statement: Standardizing a way to find the eligible candidates for each position in Student council.')

l1 = ['Target Market', 'Market Size', 'Market Segmentation', 'Demographics', 'Pyschographics', 'Strengths and Weaknesses', 'Market Trends']
l2 = ['University Management, to help them with selecting the student council.','Universities will be our market! So the market size is huge.','-','Universities with Medium to High turnover.','Universities who want to pick the deserved candidates (Universities operating in holistic manner).',' strengths: Gives priority to deserved candidates; Weakness: Doesnt give opportunities to new students.','Standardizing procedures to remove human bais.']
df = pd.DataFrame(list(zip(l1,l2)),columns =[' ', ''])
st.table(df)

st.title("Eligible candidates for student council (ranked based on event participation)")

profile= pickle.load(open('profile.pkl','rb'))
profiles ={}
profilenames = profile['Name'].values
profileprofile = profile['json'].values
for i in range(len(profilenames)):
    profiles[profilenames[i]] = profileprofile[i]

general= pickle.load(open('general.pkl','rb'))
general=general['Name'].values[0:15]
option1=st.selectbox('Eligible Candidates for General Secretary',general)
if st.button('Check profile1'):
    st.write(profiles[option1])

club1sec= pickle.load(open('club1sec.pkl','rb'))
club1sec=club1sec['Name'].values[0:15]
option2=st.selectbox('Eligible Candidates for club 1 President',club1sec)
if st.button('Check profile2'):
    st.write(profiles[option2])

club2sec= pickle.load(open('club2sec.pkl','rb'))
club2sec=club2sec['Name'].values[0:15]
option3=st.selectbox('Eligible Candidates for club 2 Secretary',club2sec)
if st.button('Check profile3'):
    st.write(profiles[option3])
#
club3sec= pickle.load(open('club3sec.pkl','rb'))
club3sec=club3sec['Name'].values[0:15]
option4=st.selectbox('Eligible Candidates for club 3 Secretary',club3sec)
if st.button('Check profile4'):
    st.write(profiles[option4])

cultsec= pickle.load(open('cultsec.pkl','rb'))
cultsec=cultsec['Name'].values[0:15]
option5=st.selectbox('Eligible Candidates for Cultural Secretary',cultsec)
if st.button('Check profile5'):
    st.write(profiles[option5])
