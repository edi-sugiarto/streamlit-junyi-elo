import streamlit as st

# Set the page configuration
st.set_page_config(
    page_title="Acknowledgements",
    page_icon=":tada:",
    layout="wide",
    initial_sidebar_state="auto",
)

# Custom CSS for the updated theme
st.markdown(
    """
    <style>
    .main-header {
        font-size: 40px;
        font-weight: bold;
        background: -webkit-linear-gradient(#003366, #4c7399); /* Gradient from navy to a lighter shade */
        -webkit-background-clip: text;
        -webkit-text-fill-color: transparent;
        text-align: center;
        margin-bottom: 20px;
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
    .quote {
        font-size: 20px;
        background-color: #ffffff;
        padding: 20px;
        border-left: 5px solid #007BFF;
        border-radius: 5px;
        margin: 20px 0;
        text-align: center;
    }
    .quote p.arabic {
        font-size: 30px;
        color: #003366;
    }
    .contact {
        display: flex;
        align-items: center;
        justify-content: center;
        margin-top: 20px;
    }
    .contact img {
        width: 50px;
        margin-right: 10px;
    }
    .contact a {
        font-size: 1.2em;
        color: #007BFF;
        text-decoration: none;
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
    .developer-card {
        background-color: #ffffff;
        border: 2px solid #003366;
        border-radius: 10px;
        padding: 20px;
        margin: 10px;
        text-align: center;
        box-shadow: 0 4px 8px rgba(0, 0, 0, 0.1);
    }
    .developer-name {
        font-size: 25px;
        font-weight: bold;
        color: #003366;
    }
    .developer-role {
        font-size: 18px;
        font-weight: bold;
        color: #003366;
        margin-top: 10px;
    }
    .developer-description {
        font-size: 16px;
        color: #333333;
        margin-top: 10px;
    }
    .social-icons {
        margin-top: 10px;
    }
    .social-icons img {
        width: 20px; /* Smaller icon size */
        height: 20px; /* Maintain aspect ratio */
        margin: 0 5px;
    }
    </style>
    """,
    unsafe_allow_html=True
)

# Title of the app
st.markdown("<div class='main-header'>Acknowledgements</div>", unsafe_allow_html=True)

# Create two columns for the main content and inspiration
col1, col2 = st.columns([3, 1])

# Introduction text in the first column
with col1:
    st.markdown("""
    <div class='section'>
    Thank you for using our application. We appreciate your visit and would like to acknowledge the following individuals and organizations for their contributions and support.
    </div>
    """, unsafe_allow_html=True)

    # Combined Acknowledgements for Individuals and Organizations
    st.markdown("<div class='sub-header'>Individuals and Organizations</div>", unsafe_allow_html=True)
    st.markdown("""
    <div class='section'>
    - Class Manager at Dibimbing: For their excellent management and support.<br>
    - Mentors: For their invaluable guidance and direction.<br>
    - Classmates at Dibimbing DS24: For their camaraderie and support.<br>
    - Dibimbing.id: For providing the platform and resources necessary for our growth and success.
    </div>
    """, unsafe_allow_html=True)

    # Special Thanks
    st.markdown("<div class='sub-header'>Special Thanks</div>", unsafe_allow_html=True)
    st.markdown("""
    <div class='section'>
    A special thanks to our families and friends for their continuous encouragement and support.
    </div>
    """, unsafe_allow_html=True)

    # Developers Involved
    st.markdown("<div class='sub-header'>Developers</div>", unsafe_allow_html=True)
    
    # Create two columns for developers
    dev_col1, dev_col2 = st.columns(2)
    
    with dev_col1:
        st.markdown("""
        <div class='developer-card'>
            <div class='developer-name'>Edi Sugiarto</div>
            <div class='developer-role'>Project Leader<br>Machine Learning Developer</div>
            <div class='developer-description'>
                Machine learning developer and researcher. Three years of experience in engineering and data field. Compiled various projects ranging from reactor modeling, defect improvement, and customer segmentation.
            </div>
            <div class='social-icons'>
                <a href='https://www.linkedin.com/in/edi-sugiarto/' target='_blank'>
                    <img src='https://cdn-icons-png.flaticon.com/512/174/174857.png' alt='LinkedIn'>
                </a>
                <a href='https://github.com/edi-sugiarto' target='_blank'>
                    <img src='https://cdn-icons-png.flaticon.com/512/25/25231.png' alt='GitHub'>
                </a>
            </div>
        </div>
        """, unsafe_allow_html=True)
    
    with dev_col2:
        st.markdown("""
        <div class='developer-card'>
            <div class='developer-name'>Alin A. Adyana</div>
            <div class='developer-role'>Team Member<br>Business and Government Consultant</div>
            <div class='developer-description'>
                Policy consultant for EITI Indonesia. She has over four years of experience in data-driven writing and data analysis, accompanied with Master of Management degree from Universitas Indonesia.
            </div>
            <div class='social-icons'>
                <a href='https://www.linkedin.com/in/alina-ady/' target='_blank'>
                    <img src='https://cdn-icons-png.flaticon.com/512/174/174857.png' alt='LinkedIn'>
                </a>
                <a href='https://github.com/linschq' target='_blank'>
                    <img src='https://cdn-icons-png.flaticon.com/512/25/25231.png' alt='GitHub'>
                </a>
            </div>
        </div>
        """, unsafe_allow_html=True)


# Quotes in the second column
with col2:
    st.markdown("<div class='sub-header'>Inspiration</div>", unsafe_allow_html=True)
    st.markdown("""
    <div class='quote'>
    <p class='arabic'>فَإِنَّ مَعَ الْعُسْرِ يُسْرًا</p>
    <p class='arabic'>إِنَّ مَعَ الْعُسْرِ يُسْرًا</p>
    <p><i>"So verily, with the hardship, there is relief. Verily, with the hardship, there is relief."</i></p>
    <p>QS Al-Inshirah 5-6</p>
    </div>
    """, unsafe_allow_html=True)

# Footer
st.markdown("""
<div class='section contact'>
<img src='https://upload.wikimedia.org/wikipedia/commons/8/8c/Gmail_Icon_%282013-2020%29.svg' alt='Gmail'>
<a href='mailto:edi.sugi1996@gmail.com'>Click to email us</a>
</div>
""", unsafe_allow_html=True)

st.markdown("""
<div class='section'>
<p>Developed by: <a href='https://edi-sugiarto.github.io' target='_blank'>By the numbers</a></p>
</div>
""", unsafe_allow_html=True)