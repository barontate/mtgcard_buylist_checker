import streamlit as st
from scryfall import process_csv
    
# Streamlit UI
st.title("MTG Card CSV Processor for use with Buylist Search")

uploaded_file = st.file_uploader("Upload your CSV file in the Manabox format", type=["csv"])



if uploaded_file is not None:
    st.write("Processing file...")
    processed_df = process_csv(uploaded_file)
    
    st.write("### Processed Data:")
    st.dataframe(processed_df)
    
    # Provide download link
    csv = processed_df.to_csv(index=False).encode('utf-8')
    st.download_button("Download Processed CSV", csv, "processed_cards.csv", "text/csv")

st.write("This app should correctly append the border treatment to any card name so that it will search correctly on the MTGMate buy list.")

st.write("TODO: add support for etched foils")