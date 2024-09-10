import streamlit as st
import pickle
import string
from nltk.corpus import stopwords
import nltk
from nltk.stem.porter import PorterStemmer
ps=PorterStemmer()
def transform_text(text):
    text=text.lower()
    text=nltk.word_tokenize(text)

    y=[]
    for i in text:
        if i.isalnum():
            y.append(i)
    text=y[:]
    y.clear()
    for i in text:
        if i not in stopwords.words('english') and i not in string.punctuation:
            y.append(i)
    text=y[:]
    y.clear()
    for i in text:
        y.append(ps.stem(i))
    return " ".join(y)

tf=pickle.load(open('vectorizer.pkl','rb'))
model=pickle.load(open('model.pkl','rb'))

st.markdown("""
    <style>
    .appview-container {
        background-color: #d7bde2 ; /* Replace with your preferred color #d7bde2*/
    }
    .sidebar .sidebar-content {
        background-color: #e0e0e0; /* Replace with your preferred color */
    }
    .stTextArea [data-baseweb=base-input] {
        background-image: linear-gradient(#e66465, #9198e5);
        -webkit-text-fill-color: white;
    }
   .stButton button {
    background: linear-gradient(to left, #83a4d4 0%, #b6fbff  0%, #83a4d4  100%);
    color: black;
    border-radius: 12px;
    padding: 8px 20px;
    font-size: 16px;
    cursor: pointer;
    transition-duration: 0.4s;
}

.stButton button:hover {
    background-position: right center;  /* Shift the gradient to the right */
    color: black;
    border: 2px solid black;
}

    # .stTextArea [data-baseweb=base-input] [disabled=""]{
    #     background-image: linear-gradient(45deg, red, purple, red);
    #     -webkit-text-fill-color: gray;
    # }
    </style>
    """,unsafe_allow_html=True)

st.title("Email/SMS Spam Classifier")
input_sms=st.text_area("Enter the Message")


if st.button('Predict'):
    transform_sms=transform_text(input_sms)
    vectr_input=tf.transform([transform_sms])
    result=model.predict(vectr_input)[0]

    if result==1:
        st.header("Spam")
    else:
        st.header("Not Spam")
