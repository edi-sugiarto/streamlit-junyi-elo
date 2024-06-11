import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import os

# Set page configuration
st.set_page_config(page_title="Project Overview", layout="wide")

# Custom CSS for styling
st.markdown(
    """
    <style>
    .main-header {
        font-size: 40px;
        font-weight: bold;
        background: -webkit-linear-gradient(#003366, #4c7399); /* Gradient from navy to a lighter shade */
        -webkit-background-clip: text;
        -webkit-text-fill-color: transparent;
    }
    .sub-header {
        font-size: 30px;
        font-weight: bold;
        margin-top: 20px;
        background: -webkit-linear-gradient(#003366, #4c7399); /* Gradient from navy to a lighter shade */
        -webkit-background-clip: text;
        -webkit-text-fill-color: transparent;
    }
    .section {
        font-size: 20px;
        background-color: #f0f2f6;
        padding: 10px;
        border-radius: 5px;
        color: #003366; /* Navy blue color */
        margin-bottom: 20px;
    }
    .image-container {
        display: flex;
        justify-content: center;
        align-items: flex-start; /* Align items to the start to ensure they are at the top */
        height: 100%; /* Make sure the container takes up full height */
    }
    .image-container img {
        max-width: 60%; /* Adjust the percentage to make the image smaller */
        border-radius: 5px;
    }
    </style>
    """,
    unsafe_allow_html=True,
)

# Title
st.markdown('<p class="main-header">Automating Exam Question Generation and Learning Recommendation System for Students through Recursive Feedback ELO Rating Calculation</p>', unsafe_allow_html=True)

# Overview
st.markdown('<h1>Overview</h1>', unsafe_allow_html=True)

# Debugging path
image_path = "catur2.jpg"

# Layout with two columns
col1, col2 = st.columns([1, 2])

# Image in the left column
with col1:
    st.image(image_path, caption="Illustration", use_column_width=True)

# Background Section and Using Junyi Academy Dataset Section in the right column
with col2:
    st.markdown('<p class="sub-header">Background</p>', unsafe_allow_html=True)
    st.markdown("""
    <div class="section">
        We are developing a rating system for education. The algorithm is created from scratch with only NumPy, inspired from Chess ELO system. By employing custom reinforcement learning algorithm at student interactions with questions, we are assigning appropriate ratings to both students and questions across various topics. 
    </div>
    """, unsafe_allow_html=True)

    st.markdown("""
    <div class="section">
        With ratings, we will be able to recommend questions that match each student's skill level, maintaining engagement and providing precise feedback to help teachers plan effective strategies. Additionally, the system can also identify top-performing students for international competitions and regions requiring additional resources and support.
    </div>
    """, unsafe_allow_html=True)

    st.markdown('<p class="sub-header">Dataset: Junyi Academy Student Activity</p>', unsafe_allow_html=True)
    st.markdown("""
    <div class="section">
        Using the extensive open-source Junyi Academy dataset, particularly focused on junior high school problems, we adapted the ELO system to evaluate student performance. Logistic functions were employed to estimate the probability of students solving problems, adjusting ratings accordingly. Early results suggest that our adapted ELO-based recommendation system enhances predictive accuracy in determining whether a student can solve a given question.
    </div>
    """, unsafe_allow_html=True)


# Mechanism Section
st.markdown('<p class="sub-header">Mechanism</p>', unsafe_allow_html=True)

data = {
    "Step 1: Rating Initialization": ["First, we initiate rating for both student and problem. The initiation is a guess number. It can be random, uniform, or accuracy-based initiation."],
    "Step 2: Going Through Dataset": ["We are going through the student activity log. For each student activity, we employ a customized logistic function to get solving probability. With this probability and the actual result, we calculate the student's new rating after said activity."],
    "Step 3: Calculate Loss and Minimization": ["After finishing through the entire activity, we obtain upset loss for each student and problem. With this loss, we update the initial rating guess for student and problem, and go back to step 1 until the loss is minimized."],
    "Step 4: Getting Final Rating and Validation": ["The rating and algorithm are then employed on the test dataset and validated with XGboost. The algorithm will be compared to plain XGboost without additional rating information to determine its efficacy."]
}
df = pd.DataFrame(data)
st.table(df.style.hide(axis='index'))

path = 'ML_Diagram.png'
st.image(path, caption="ML Diagram", use_column_width=True)

st.markdown('<p class="sub-header">Key Aspects</p>', unsafe_allow_html=True)

Customized_Logistic_Function = [
    "When student rating is same as problem rating, standard logistic function determine 50% chance of a student solving probability. We modify it to give a 75% chance. This adjustment ensures that the baseline probability reflects the expected score for students attempting problems at their skill level."
]
Growth_and_static_entity = [
    "In Chess, the ELO works on player vs player, in which both player ratings will be updated after each match. In our case, we use a static rating for problem-set and only update student rating after each activity. To obtain this effect, we employ a recursive feedback system to determine the appropriate rating for student and problems."
]
df_key_aspects = pd.DataFrame({
    "Customized Logistic Function": Customized_Logistic_Function,
    "Growth and static entity": Growth_and_static_entity
})
st.table(df_key_aspects.style.hide(axis='index'))