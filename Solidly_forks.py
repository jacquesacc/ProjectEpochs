import datetime as dt
import streamlit as st
import pandas as pd

df = pd.read_csv('https://docs.google.com/spreadsheets/d/1sOR0lH36AGFfhXqzDWCg70KkcxLyqmkZiZIMOFiN3D0/export?format=csv')

now = dt.datetime(dt.datetime.utcnow().year, dt.datetime.utcnow().month, dt.datetime.utcnow().day, dt.datetime.utcnow().hour, dt.datetime.utcnow().minute, dt.datetime.utcnow().second)
days_to_thursday = (3 - now.weekday()) % 7
next_thursday = now + dt.timedelta(days=days_to_thursday)
next_thursday_start = dt.datetime(next_thursday.year, next_thursday.month, next_thursday.day, 0, 0, 0)
remaining_time = next_thursday_start - now

st.title('List of solidly forks')
st.write('Next epoch in : ', remaining_time)

col1, col2, col3 = st.columns([1,1,2])

with col1:
   st.header("Project")

with col2:
   st.header("Epoch")

with col3:
    st.header("Voting page")

for i in range(0, len(df)):
    if df.loc[i:i, 'Project Type'].item() == 'Solidly fork':
        first_epoch = \
            dt.datetime(df.loc[i:i, 'FE_Year'].item(), df.loc[i:i, 'FE_Month'].item(), df.loc[i:i, 'FE_Day'].item(), 0, 0, 0)

        days_since_first_epoch = next_thursday_start - first_epoch

        current_epoch = int(round((days_since_first_epoch.days/7), 0))

        with col1:
            st.write(df.loc[i:i, 'Project'].item())

        with col2:
            st.write(current_epoch)

        with col3:
            st.write(df.loc[i:i, 'Voting page'].item())





