import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import pickle
from sklearn.metrics import confusion_matrix
from sklearn.metrics import roc_curve, auc
import plotly.graph_objects as go
import plotly.express as px
from sklearn.metrics import accuracy_score, precision_score, recall_score, f1_score, roc_auc_score

st.set_page_config(page_title="Model Monitoring", layout="wide")

'''
# Model Overview
'''

with open('xgboost_rating_pipe_local.pkl', 'rb') as file:
    model = pickle.load(file)
with open('xgboost_nr_pipe_local.pkl', 'rb') as file:
    model_nr = pickle.load(file)


df_test = pd.read_parquet('POC_2.parquet.gzip')
X_test = df_test.drop(columns=['is_correct'])
y_test = df_test['is_correct']

y_test_pred_pkl = model.predict(X_test)
y_test_pred_proba_pkl = model.predict_proba(X_test)[:, 1]

y_test_pred_nr = model_nr.predict(X_test)
y_test_pred_proba_nr = model_nr.predict_proba(X_test)[:, 1]

fpr_with, tpr_with, _ = roc_curve(y_test, y_test_pred_proba_pkl)
roc_auc_with = auc(fpr_with, tpr_with)

fpr_nr, tpr_nr, _ = roc_curve(y_test, y_test_pred_proba_nr)
roc_auc_nr = auc(fpr_nr, tpr_nr)

fig = go.Figure()

# Add ROC curve
fig.add_trace(go.Scatter(
    x=fpr_with, y=tpr_with,
    mode='lines',
    name=f'XGBoost Classifier w/ Rating (AUC = {roc_auc_with:.2f})',
    line=dict(color='darkorange', width=2)
))

fig.add_trace(go.Scatter(
    x=fpr_nr, y=tpr_nr,
    mode='lines',
    name=f'XGBoost Classifier w/o Rating (AUC = {roc_auc_nr:.2f})',
    line=dict(color='blue', width=2, dash='dash')
))

# Add diagonal line
fig.add_trace(go.Scatter(
    x=[0, 1], y=[0, 1],
    mode='lines',
    name='Uniform Classifier',
    line=dict(color='navy', width=2, dash='dash')
))

# Update layout
fig.update_layout(
    title='Receiver Operating Characteristic (ROC) Curve',
    xaxis_title='False Positive Rate',
    yaxis_title='True Positive Rate',
    xaxis=dict(range=[0.0, 1.0]),
    yaxis=dict(range=[0.0, 1.05]),
        legend=dict(
        # x=0.5,  # x position of the legend
        y=-0.3,  # y position of the legend
        xanchor='center',  # Anchor the x position to the center
        yanchor='top',     # Anchor the y position to the top
        orientation='h'    # Horizontal orientation
    ),
    height=500,
)


xgboost = model.named_steps['classifier']
importance = xgboost.feature_importances_
numeric_features= ['upid_rating', 'uuid_rating', 'rating_diff', 'level', 'user_grade']
categorical_features = ['difficulty']
feature_names = numeric_features+ list(model.named_steps['preprocessor'].transformers_[1][1].get_feature_names_out(categorical_features))
# new df for feature importance
feature_importance_df = pd.DataFrame({
    'Feature': feature_names,
    'Importance': importance
}).sort_values(by='Importance', ascending=False)

fig2 = go.Figure()

fig2.add_trace(go.Bar(
    x=feature_importance_df['Importance'],
    y=feature_importance_df['Feature'],
    orientation='h'
))

# Update layout
fig2.update_layout(
    title='Feature Importance for Model w/ Rating',
    xaxis_title='Feature Importance',
    yaxis_title='Feature',
    yaxis=dict(autorange='reversed'),  # Invert y-axis to match Matplotlib plot
    height=500,  # Set figure height
    width=800   # Set figure width
)


cm_nr = confusion_matrix(y_test, y_test_pred_nr)
fig3 = px.imshow(
    cm_nr,
    text_auto=True,
    color_continuous_scale='Blues',
    labels=dict(x='Predicted Labels', y='True Labels', color='Count'),
    title='Confusion Matrix w/o Rating',
)

fig3.update_layout(
    xaxis_title='Predicted Labels',
    yaxis_title='True Labels',
    coloraxis_showscale=False
)

cm_with = confusion_matrix(y_test, y_test_pred_pkl)
# Plot confusion matrix with Plotly
fig4 = px.imshow(
    cm_with,
    text_auto=True,
    color_continuous_scale='Blues',
    labels=dict(x='Predicted Labels', y='True Labels', color='Count'),
    title='Confusion Matrix w/ Rating',
)

fig4.update_layout(
    xaxis_title='Predicted Labels',
    yaxis_title='True Labels',
    coloraxis_showscale=False
)


col1, col2 = st.columns(2)

with col1:
        st.plotly_chart(fig, use_container_width=True)
        st.plotly_chart(fig3, use_container_width=True)
with col2:
        st.plotly_chart(fig2, use_container_width=True)
        st.plotly_chart(fig4, use_container_width=True)



'''
### Model Monitoring
'''

df_metrics = pd.read_parquet('train_performance.parquet.gzip')
accuracy_ = accuracy_score(y_test, y_test_pred_pkl)
precision_ = precision_score(y_test, y_test_pred_pkl)
recall_ = recall_score(y_test, y_test_pred_pkl)
f1_ = f1_score(y_test, y_test_pred_pkl)

df_metrics['July 2019 Performance'] = [accuracy_, precision_, recall_, f1_, roc_auc_with]

st.table(df_metrics)
st.caption('Currently, for this proof-of-concept, Model Report is only for Arithmetic')