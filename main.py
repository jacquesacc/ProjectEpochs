import datetime as dt
import streamlit as st

# https://docs.google.com/spreadsheets/d/1sOR0lH36AGFfhXqzDWCg70KkcxLyqmkZiZIMOFiN3D0/edit?usp=sharing


project = ['Thena', 'Ramses', 'SolidLizard']
first_flip = [dt.datetime(2023, 1, 12, 0, 0, 0, tzinfo=dt.timezone.utc), dt.datetime(2023, 3, 23, 0, 0, 0, tzinfo=dt.timezone.utc), dt.datetime(2023, 2, 2, 0, 0, 0, tzinfo=dt.timezone.utc)]

st.title('Time to next epoch for Solidly forks')

col1, col2, col3 = st.columns(3)

with col1:
   st.header("Project")

with col2:
   st.header("Next epoch")

with col3:
   st.header("Time to epoch")

for i in range(0,len(project)):
    epoch = 1
    next_epoch = first_flip[i]
    if next_epoch < dt.datetime.now().astimezone(dt.timezone.utc):
        while next_epoch < dt.datetime.now().astimezone(dt.timezone.utc):
            epoch = epoch + 1
            next_epoch = next_epoch + dt.timedelta(days=7)

        time_to_epoch = next_epoch - dt.datetime(dt.datetime.now().year, dt.datetime.now().month, dt.datetime.now().day, dt.datetime.now().hour, dt.datetime.now().minute, dt.datetime.now().second).astimezone(dt.timezone.utc)

    with col1:
        st.write(project[i])

    with col2:
        st.write(epoch)

    with col3:
        st.write(time_to_epoch)


