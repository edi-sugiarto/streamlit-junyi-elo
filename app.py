import plotly.express as px
import streamlit as st
import pandas as pd
import plotly.graph_objects as go
from plotly.subplots import make_subplots

st.set_page_config(page_title="Student Card", layout="wide")

@st.cache_data
def prepare_data():
    df_uuid = pd.read_parquet('uuid_login.parquet.gzip')
    df_uuid_rating = pd.read_parquet('uuid_rating.parquet.gzip')
    df_uuid_rating = df_uuid_rating[['alias', 'categories', 'num_activities', 'final_curr']]
    df_uuid_rating.columns = ['Name', 'categories', 'Number of Activities', 'Current Rating']
    list_student = df_uuid['alias'].unique().tolist()
    
    df_poc1 = pd.read_parquet('POC_1.parquet.gzip')
    df_poc2 = pd.read_parquet('POC_2.parquet.gzip')
    df_poc = pd.concat([df_poc1, df_poc2], ignore_index=True)
    df_poc['date'] = df_poc['timestamp_TW'].dt.date

    return df_uuid, df_uuid_rating, list_student, df_poc

df_uuid, df_uuid_rating, list_student, df_poc = prepare_data()
select_student = st.selectbox('Select student: ', list_student)
df_uuid_rating = df_uuid_rating[df_uuid_rating['Name'] == select_student]
# st.write(df_uuid_rating)
attempt = df_uuid_rating['Number of Activities'].tolist()

'''
## Total Activities
'''
col1, col2, col3 = st.columns(3)
col1.metric("Algebra", attempt[0])
col2.metric("Arithmetic", attempt[1])
col3.metric("Geometry", attempt[2])

'''***'''
def get_student(select_student):
    student_info = df_uuid[df_uuid['alias'] == select_student].copy()
    student_info['Registered'] = student_info['first_login_date_TW'].dt.date
    student_info = student_info[['uuid','user_grade', 'gender', 'user_city', 'Registered','current_consecutive_login_days']]
    student_info.columns = ['User ID', 'Education Grade', 'Gender', 'City Origin', 'Registered', 'Current Login Streak']
    return student_info

student_info = get_student(select_student)
student_info = student_info.astype('str')
student_T = student_info.transpose()    
student_T.columns = ['Information Details                                                                                   ']

col1, col2 = st.columns(2)
with col1:
    fig = px.bar(df_uuid_rating, x='Current Rating', y='categories',
                        text='categories',
                        color='categories',
                        labels={'Rating':'Current Rating'},
                        width=500, height=325)
    fig.update_traces(textfont_size=16, textangle=0, textposition='inside',insidetextanchor ='start')
    fig.update_yaxes(visible=False)
    fig.update_layout(xaxis_range=[0, 2800])
    fig.update_layout(showlegend=False)
    st.plotly_chart(fig, use_container_width=True)

with col2:
    f'''
    ## User: {select_student}
    '''
    st.write(student_T)
    
# st.write(student_info.head())
user_id = student_info.iloc[0]['User ID']
# st.write(user_id)

df_filter = df_poc[df_poc['uuid'] == user_id].copy()

df_user_hist = df_filter.groupby(['uuid', 'date'], observed=True).agg(
    attempt_count=('uuid_rating', 'size'),
    average_rating=('uuid_rating', 'mean')
).reset_index()

df_user_hist.columns = ['User ID', 'Date', 'Attempt Counts', 'Strength Rating']
# df_user_hist = df_filter.groupby(['uuid', 'date'], observed=True)['uuid_rating'].mean().reset_index()
# df_user_hist = grouped_df[grouped_df['uuid'] == user_id]

df_user_recent = df_user_hist.tail(5).copy()
df_user_recent['Date'] = df_user_recent['Date'].astype('str')
# st.write(df_user_recent)

'''
***
'''
st.write("<h3 style='text-align: center;'>Recent Activity</h3>", unsafe_allow_html=True)

fig = make_subplots(specs=[[{"secondary_y": True}]])
fig.add_trace(
    go.Bar(x=df_user_recent['Date'], y=df_user_recent['Attempt Counts'], name='Attempt Count',
           marker_color='chocolate', marker_line_color='white',
           marker_line_width=1, opacity=1),
    secondary_y=False,
)
fig.add_trace(
    go.Scatter(x=df_user_recent['Date'], y=df_user_recent['Strength Rating'], name='Strength Rating', 
               mode='lines+markers', line=dict(color="chartreuse")),
    secondary_y=True, 
)
fig.update_layout(
    title_text='',
    xaxis_title='Date',
    width=800
)

fig.update_layout(xaxis=dict(type='category'))
fig.update_yaxes(title_text='', secondary_y=False)
fig.update_yaxes(title_text='',secondary_y=True)

st.plotly_chart(fig, use_container_width=True)
