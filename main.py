import streamlit as st
from transformers import pipeline

left_co, cent_co,last_co = st.columns(3)
with cent_co:
    st.image("assets\whiteB.jpg", width=300, caption="The legend")

# Add a title to your app
st.title("One piece vibe check")

# Create a text input widget
user_input = st.text_area("What u think about one piece?", height=300)

@st.cache_resource
def load_my_pipeline():
    return pipeline("text-classification", model="OnePieceModel", device=0)

pipe = load_my_pipeline()

def predict():
    if(len(user_input.replace(" ","")) < 30):
        st.write("Nahh make sure its > 30 words")
        return
    
    hasil = pipe(user_input)
    
    # Check case
    match str(hasil[0]['label']):
        case "LABEL_2":
            output = ":green[*Bro likes it*] :sunglasses:"
        case "LABEL_1":
            output = ":yellow[*Meh*] :meh:"
        case "LABEL_0":
            output = ":red[*Not real*] :angry:"
        case _:
            output = 'error'

    return output

# Display the input back to the user
if st.button("Submit"):
    output = predict()
    if(output is not None):
        st.write(f"vibe : {output}")
    
    
