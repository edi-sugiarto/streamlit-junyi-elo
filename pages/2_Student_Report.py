import plotly.express as px
import streamlit as st
import pandas as pd
import plotly.graph_objects as go
from plotly.subplots import make_subplots
# import hydralit_components as hc

st.set_page_config(page_title="Student Card", layout="wide")

# @st.cache_data
# def prepare_data():
df_uuid = pd.read_parquet('UserData_named_ID_EN.parquet.gzip')
df_uuid_rating = pd.read_parquet('uuid_rating_named.parquet.gzip')
df_uuid_rating = df_uuid_rating[['alias', 'categories', 'num_activities', 'final_curr']]
df_uuid_rating.columns = ['Name', 'categories', 'Number of Activities', 'Current Rating']
df_user_total_activities = pd.read_parquet('user_total_activities.parquet.gzip')

list_student = df_user_total_activities['alias'].unique().tolist()

    # return df_uuid, df_uuid_rating, list_student, df_poc

# df_uuid, df_uuid_rating, list_student, df_poc = prepare_data()


select_student = st.selectbox('Select student: ', list_student)
df_uuid_rating = df_uuid_rating[df_uuid_rating['Name'] == select_student]
# st.write(df_uuid_rating)
attempt = df_uuid_rating['Number of Activities'].tolist()
# st.write(attempt)

student_info = df_uuid[df_uuid['alias'] == select_student].copy()
student_info['first_login_date_TW'] = pd.to_datetime(student_info['first_login_date_TW'])
student_info['Registered'] = student_info['first_login_date_TW'].dt.date
student_info = student_info[['uuid','user_grade', 'gender', 'user_city', 'Registered','current_consecutive_login_days']]
student_info.columns = ['User ID', 'Education Grade', 'Gender', 'City Origin', 'Registered', 'Current Login Streak']

student_info = student_info.astype('str')
student_T = student_info.transpose()    
student_T.columns = ['Information Details']


'''
## Total Activities
'''
col1, col2, col3 = st.columns(3)
col1.metric("Algebra", attempt[0])
col2.metric("Arithmetic", attempt[1])
col3.metric("Geometry", attempt[2])

text1 = "Learn Algebra" if attempt[0] > 20 else 'Algebra Placement Test'
text2 = "Learn Arithmetic" if attempt[1] > 20 else 'Arithmetic Placement Test'
text3 = "Learn Geometry" if attempt[2] > 20 else 'Geometry Placement Test'

learn1, learn2, learn3 = st.columns(3)
a = learn1.button(text1)
b = learn2.button(text2)
c = learn3.button(text3)

@st.cache_data
def ingest_problem_data(a):
    upid_rating = pd.read_parquet('final_upid_rating.parquet.gzip')
    return upid_rating

def logistic_function(x, L=1, k=1, d=400, ofs=2):
    power10 = 10**(-k*x/d)
    return (L+ofs) / (1 + power10+ofs)

if a and attempt[0] > 20:
    '''
    ***
    ## Problemset Recommendation: Algebra
    '''
    upid_rating = ingest_problem_data('all')
    upid_filter = upid_rating[upid_rating['categories'] == 'Algebra'][['upid', 'categories', 'num_activities', 'accuracy','final_init']].copy()
    upid_filter.columns = ['ID', 'Topic', 'Global Attempt', 'Global Acc', 'Rating']

    rating = df_uuid_rating.loc[df_uuid_rating['categories'] == 'Algebra', 'Current Rating'].values[0]

    upid_filter['diff'] = rating - upid_filter['Rating']
    upid_filter['Expected Solving%'] = 100 * upid_filter['diff'].apply(logistic_function).round(4)
    # upid_alg['abs_diff'] = upid_alg['diff'].abs()
    col_name = ['Topic', 'Global Attempt', 'Global Acc', 'Rating', 'Expected Solving%']
    easy_ = upid_filter[upid_filter['diff'] < 0].sort_values(by='diff', ascending=False)[col_name].head(5)
    hard_ = upid_filter[upid_filter['diff'] >= -120].sort_values(by='diff')[col_name].head(5)
    st.write('Current Rating:', round(rating, 4))
    easy_col, hard_col = st.columns(2)
    with easy_col:
        st.write('### Normal Difficulty Problemset')
        st.write(easy_)
    with hard_col:
        st.write('### Challenging Difficulty')
        st.write(hard_)

if b and attempt[1] > 20:
    '''
    ***
    ## Problemset Recommendation: Arithmetic
    '''
    upid_rating = ingest_problem_data('all')
    upid_filter = upid_rating[upid_rating['categories'] == 'Arithmetic'][['upid', 'categories', 'num_activities', 'accuracy','final_init']].copy()
    upid_filter.columns = ['ID', 'Topic', 'Global Attempt', 'Global Acc', 'Rating']

    rating = df_uuid_rating.loc[df_uuid_rating['categories'] == 'Arithmetic', 'Current Rating'].values[0]

    upid_filter['diff'] = rating - upid_filter['Rating']
    upid_filter['Expected Solving%'] = 100 * upid_filter['diff'].apply(logistic_function).round(4)
    # upid_alg['abs_diff'] = upid_alg['diff'].abs()
    col_name = ['Topic', 'Global Attempt', 'Global Acc', 'Rating', 'Expected Solving%']
    easy_ = upid_filter[upid_filter['diff'] < 0].sort_values(by='diff', ascending=False)[col_name].head(5)
    hard_ = upid_filter[upid_filter['diff'] >= -120].sort_values(by='diff')[col_name].head(5)
    st.write('Current Rating:', round(rating, 4))
    easy_col, hard_col = st.columns(2)
    with easy_col:
        st.write('### Normal Difficulty Problemset')
        st.write(easy_)
    with hard_col:
        st.write('### Challenging Difficulty')
        st.write(hard_)

if c and attempt[2] > 20:
    '''
    ***
    ## Problemset Recommendation: Geometry
    '''
    upid_rating = ingest_problem_data('all')
    upid_filter = upid_rating[upid_rating['categories'] == 'Geometry'][['upid', 'categories', 'num_activities', 'accuracy','final_init']].copy()
    upid_filter.columns = ['ID', 'Topic', 'Global Attempt', 'Global Acc', 'Rating']

    rating = df_uuid_rating.loc[df_uuid_rating['categories'] == 'Geometry', 'Current Rating'].values[0]

    upid_filter['diff'] = rating - upid_filter['Rating']
    upid_filter['Expected Solving%'] = 100 * upid_filter['diff'].apply(logistic_function).round(4)
    # upid_alg['abs_diff'] = upid_alg['diff'].abs()
    col_name = ['Topic', 'Global Attempt', 'Global Acc', 'Rating', 'Expected Solving%']
    easy_ = upid_filter[upid_filter['diff'] < 0].sort_values(by='diff', ascending=False)[col_name].head(5)
    hard_ = upid_filter[upid_filter['diff'] >= -120].sort_values(by='diff')[col_name].head(5)
    st.write('Current Rating:', round(rating, 4))
    easy_col, hard_col = st.columns(2)
    with easy_col:
        st.write('### Normal Difficulty Problemset')
        st.write(easy_)
    with hard_col:
        st.write('### Challenging Difficulty')
        st.write(hard_)



'''***'''


col1, col2 = st.columns(2)


with col1:
    fig1 = px.bar(df_uuid_rating, x='Current Rating', y='categories',
                        text='categories',
                        color='categories',
                        labels={'Rating':'Current Rating'},
                        width=500, height=325)
    fig1.update_traces(textfont_size=16, textangle=0, textposition='inside',insidetextanchor ='start')
    fig1.update_yaxes(visible=False)
    fig1.update_layout(xaxis_range=[0, 2800])
    fig1.update_layout(showlegend=False)
    st.plotly_chart(fig1, use_container_width=True)

with col2:
    f'''
    ## User: {select_student}
    '''
    st.table(student_T)
    
# st.write(student_info.head())
show_recent = st.button("Show Recent Activity")

@st.cache_data
def ingest_database(a):
    df_poc1 = pd.read_parquet('POC_1.parquet.gzip')
    df_poc2 = pd.read_parquet('POC_2.parquet.gzip')
    df_poc = pd.concat([df_poc1, df_poc2], ignore_index=True)
    df_poc['date'] = df_poc['timestamp_TW'].dt.date
    return df_poc

if show_recent:
    df_poc = ingest_database('all')

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

    # df_user_hist, df_user_recent = get_user_history()
    '''
    ***
    '''
    st.write("<h3 style='text-align: center;'>Recent Activity</h3>", unsafe_allow_html=True)

    fig2 = make_subplots(specs=[[{"secondary_y": True}]])
    fig2.add_trace(
        go.Bar(x=df_user_recent['Date'], y=df_user_recent['Attempt Counts'], name='Attempt Count',
            marker_color='chocolate', marker_line_color='white',
            marker_line_width=1, opacity=1),
        secondary_y=False,
    )
    fig2.add_trace(
        go.Scatter(x=df_user_recent['Date'], y=df_user_recent['Strength Rating'], name='Strength Rating', 
                mode='lines+markers', line=dict(color="chartreuse")),
        secondary_y=True, 
    )
    fig2.update_layout(
        title_text='',
        xaxis_title='Date',
        width=800
    )

    fig2.update_layout(xaxis=dict(type='category'))
    fig2.update_yaxes(title_text='', secondary_y=False)
    fig2.update_yaxes(title_text='',secondary_y=True)

    st.plotly_chart(fig2, use_container_width=True)

    st.caption('Currently, for this proof-of-concept, recent activity is only for Arithmetic')


