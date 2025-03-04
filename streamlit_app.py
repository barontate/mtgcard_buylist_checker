import streamlit as st
from scryfall import fetch_scryfall_data
import pandas as pd
import time
import random

st.title("MTGMate Buylist Checker")



uploaded_file = st.file_uploader("Upload a CSV file of your cards in Manabox format", type=["csv"])

st.write(
    "Let's start building! For help and inspiration, head over to [docs.streamlit.io](https://docs.streamlit.io/)."
)

def process_csv(file):
    """Process the uploaded CSV file, fetch details from Scryfall, and modify the data."""
    df = pd.read_csv(file)
    
    new_data = []
    for _, row in df.iterrows():
        scryfall_id = row['Scryfall ID']
        card_name = row['Name']
        set_name = row['Set name']
        foil = row['Foil']
        quantity = row['Quantity']
        
        card_data = fetch_scryfall_data(scryfall_id)
        if card_data:
            border_color = card_data.get("border_color", "")
            if border_color == "borderless":
                card_name += " (Borderless)"
        
        new_data.append([card_name, set_name, foil, quantity])
    
    return pd.DataFrame(new_data, columns=["Card Name", "Set Name", "Foil", "Quantity"])
    
# Streamlit UI
st.title("MTG Card CSV Processor with Scryfall API")

uploaded_file = st.file_uploader("Upload your CSV file", type=["csv"])

if uploaded_file is not None:
    st.write("Processing file...")
    processed_df = process_csv(uploaded_file)
    
    st.write("### Processed Data:")
    st.dataframe(processed_df)
    
    # Provide download link
    csv = processed_df.to_csv(index=False).encode('utf-8')
    st.download_button("Download Processed CSV", csv, "processed_cards.csv", "text/csv")
