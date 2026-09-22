import streamlit as st
from gradio_client import Client

st.set_page_config(
    page_title="AI Learning Roadmap Generator",
    page_icon="🤖"
)

@st.cache_resource
def load_client():
    return Client("abidlabs/en2fr")

client = load_client()

st.title("🤖 AI Learning Roadmap Generator")
st.write("Generate a personalized learning roadmap using AI.")

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

        prompt = f"""
Create a learning roadmap for:

Domain: {domain}
Field: {field}
Skill Level: {level}
Available Time: {time}

Include:

1. Topics to learn
2. Learning order
3. Duration for each phase
4. Practical projects
5. Important tools
6. Final project

Make the roadmap realistic and beginner-friendly.
"""

        with st.spinner("Generating your roadmap..."):

            try:
                result = client.predict(
                    prompt,
                    api_name="/predict"
                )

                st.subheader("Your Learning Roadmap")
                st.markdown(str(result))

            except Exception as e:
                st.error("There was an error connecting to the AI model.")
                st.write(e)
