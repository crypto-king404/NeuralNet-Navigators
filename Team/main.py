import streamlit as st
import vertexai
from vertexai.preview import generative_models
from vertexai.preview.generative_models import GenerativeModel, ChatSession

# Initialize Vertex AI
project = "worksheet-generator-427421"
vertexai.init(project=project)

config = generative_models.GenerationConfig(temperature=0.4)

# Load model with config
model = GenerativeModel("gemini-pro", generation_config=config)

def generate_worksheet(grade_level, topic):
    chat = model.start_chat()
    query = f"Generate a worksheet for {grade_level} level on the topic of {topic}. Include fill-in-the-blank questions and multiple-choice questions."
    response = chat.send_message(query)
    output = response.candidates[0].content.parts[0].text

    return output

def main():
    st.title("Worksheet Generator")
    st.write("Generate a worksheet based on any topic or text.")

    grade_level = st.selectbox('Grade level:', ['Primary', 'Secondary', 'High School', 'University'])
    topic = st.text_input('Topic or text:', 'Machine Learning')

    if st.button('Generate'):
        worksheet = generate_worksheet(grade_level, topic)

        st.markdown(worksheet)

if __name__ == "__main__":
    main()
