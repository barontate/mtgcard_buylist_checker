import streamlit as st
import scryfall

st.title("MTGMate Buylist Checker")



uploaded_file = st.file_uploader("Upload a CSV file of your cards in Manabox format", type=["csv"])

st.write(
    "Let's start building! For help and inspiration, head over to [docs.streamlit.io](https://docs.streamlit.io/)."
)

