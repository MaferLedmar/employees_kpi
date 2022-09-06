import streamlit as st
import pandas as pd
import numpy as np
import plotly.express as px


#--- IMPORT DATA ---#
df=pd.read_csv("employee_data.csv")

#--- PAGE CONFIG ---#
st.set_page_config(page_title="Socialize your Knowledge",
                   page_icon=":busts_in_silhouette:")

st.title("Socialize your Knowledge")
st.markdown("_Site that would help and make easier for us to analyze the performance of Socialize your Knowledge employees_")

#--- LOGO ---#
st.sidebar.image("waveslogo.jpg")
st.sidebar.markdown("##")

#--- SIDEBAR FILTERS ---#

gender = st.sidebar.multiselect("Select Gender",
                                options=df['gender'].unique(),
                                default=df['gender'].unique())
st.sidebar.markdown("##")

performance_score= st.sidebar.multiselect("Select the Performance Score",
                                          options=df['performance_score'].unique(),
                                          default=df['performance_score'].unique())
st.sidebar.markdown("##")

marital_status= st.sidebar.multiselect("Select Marital Status",
                                       options=df['marital_status'].unique(),
                                       default=df['marital_status'].unique())

df_selection=df.query(
    "gender == @gender & performance_score == @performance_score & marital_status == @marital_status")

#--- CHARTS ---#

#Chart to visualize the average worked hours by employee gender
avg_hours_gender=(
    df_selection.groupby(by=['gender']).sum()[['average_work_hours']].sort_values(by="average_work_hours"))

fig_hours_gender=px.bar(avg_hours_gender,
                        x=avg_hours_gender.index,
                        y="average_work_hours", 
                        orientation="v",
                        title="Average Worked Hours by Gender",
                        labels=dict(average_work_hours="Total Worked Hours", gender="Gender"),
                        color_discrete_sequence=["#7ECBB4"],
                        template="plotly_white")
fig_hours_gender.update_layout(plot_bgcolor="rgba(0,0,0,0)")

st.plotly_chart(fig_hours_gender)

#Chart to visualize the salary by employee age
age=df_selection['age']
position=df_selection['position']
salary=df_selection['salary']
fig_age=px.scatter(df_selection,
                   x=age,
                   y=salary,
                   color=position,
                   title="Employee Salary by Age",
                   labels=dict(age="Age", salary="Salary", position="Position"),
                   template="plotly_white")
fig_age.update_layout(plot_bgcolor="rgba(0,0,0,0)")

st.plotly_chart(fig_age)

#Chart to visualize the performance score distribution 
name=df_selection['name_employee']
performance=df_selection['performance_score']

fig_distribution_perf=px.bar(df_selection,
                             x=name,
                             y=performance,
                             title="Performance Score Distribution",
                             labels=dict(name_employee="Employee Name", performance_score="Performance Score"),
                             color_discrete_sequence=["#7ECBB4"],
                             template="plotly_white")
fig_distribution_perf.update_layout(plot_bgcolor="rgba(0,0,0,0)")
st.plotly_chart(fig_distribution_perf)

#Chart to visualize the relation between the average worked hours vs the performance score
avg_hours=df_selection['average_work_hours']
perf_score=df_selection['performance_score']
dept=df_selection['department']
salary=df_selection['salary']

fig_perf_work=px.scatter(df_selection,
                         x=perf_score,
                         y=avg_hours,
                         size=salary,
                         color=dept,
                         title="Worked Hours vs. Performance Score",
                         labels=dict(average_work_hours="Average Hours", performance_score="Performance Score",
                                     department="Department", salary="Salary"),
                         template="plotly_white")
fig_perf_work.update_layout(plot_bgcolor="rgba(0,0,0,0)")

st.plotly_chart(fig_perf_work)


#--- CONCLUSION ---#
st.markdown("**Analysis**")
st.markdown("Within this site you are able to filter by gender, performance score, marital status to make a more profund\
            analysis. In general we see that the female population in the company work more hours than men. The employees in the company\
            are between 30-60 years but the salary is given according to the position they have. We can also appreciate that most of the\
            employees have a performance score of 3 and that the worked hours doesn´t influence that score.")






