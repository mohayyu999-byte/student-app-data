import streamlit as st

st.set_page_config(
    page_title="AI Learning Roadmap Generator",
    page_icon="🤖"
)

st.title("🤖 AI Learning Roadmap Generator")
st.write("Generate a personalized learning roadmap in English.")

domain = st.text_input(
    "Enter Domain",
    placeholder="e.g. Artificial Intelligence"
)

field = st.text_input(
    "Enter Field",
    placeholder="e.g. Machine Learning"
)

level = st.selectbox(
    "Select Skill Level",
    ["Beginner", "Intermediate", "Advanced"]
)

time = st.text_input(
    "Time to Learn",
    placeholder="e.g. 3 months"
)

if st.button("Generate Roadmap"):

    if not domain or not field or not time:
        st.warning("Please fill in all the required fields.")

    else:
        st.subheader("Your Learning Roadmap")

        st.markdown(f"""
## {domain} — {field}

**Skill Level:** {level}  
**Available Time:** {time}

### 1. Topics to Learn
- Python programming fundamentals
- NumPy and Pandas
- Data cleaning and preprocessing
- Statistics and probability
- Machine learning fundamentals
- Supervised and unsupervised learning
- Model evaluation
- Feature engineering
- Introduction to deep learning
- Model deployment with Streamlit

### 2. Learning Order
**Phase 1:** Python, NumPy, Pandas, and data handling

**Phase 2:** Statistics, probability, and data preprocessing

**Phase 3:** Supervised machine learning

**Phase 4:** Unsupervised learning and model evaluation

**Phase 5:** Introduction to neural networks and deep learning

**Phase 6:** Build and deploy a complete project

### 3. Suggested Duration
For a **3-month plan**:

- Weeks 1–2: Python and data handling
- Weeks 3–4: Statistics and preprocessing
- Weeks 5–7: Machine learning algorithms
- Weeks 8–9: Model evaluation and projects
- Weeks 10–11: Deep learning fundamentals
- Week 12: Final project and deployment

### 4. Practical Projects
- House price prediction
- Student performance prediction
- Customer classification
- Spam message classification
- Customer segmentation using K-Means

### 5. Important Tools
- Python
- NumPy
- Pandas
- Matplotlib
- Scikit-learn
- TensorFlow or PyTorch
- Jupyter Notebook / VS Code
- Git and GitHub
- Streamlit

### 6. Final Project
Build a complete **{field} application**.

The application should:
1. Accept user input.
2. Clean and prepare the data.
3. Load a trained machine learning model.
4. Generate a prediction.
5. Display the result through a Streamlit interface.
6. Be deployed online.

### Recommended Weekly Routine
- **60%** practical coding
- **25%** learning concepts
- **15%** reviewing and documenting projects

This roadmap is designed to be realistic for a {level.lower()} learner and can be adjusted according to your available time.
""")
