import requests
import pandas as pd

SCRYFALL_API_URL = "https://api.scryfall.com/cards/"

def fetch_scryfall_data(scryfall_id):
    """Fetches card details from Scryfall API."""
    response = requests.get(f"{SCRYFALL_API_URL}{scryfall_id}")
    if response.status_code == 200:
        data = response.json()
        card_name = data.get("name", "Unknown")
        border_color = data.get("border_color", "Unknown")
        frame_effect = data.get("frame_effects", [0])
        
        # Modify name based on border color
        if border_color == "borderless":
            card_name += " (Borderless)"

        if frame_effect == ['extendedart']:
            card_name += " (Extended Art)"

        if frame_effect == ['showcase']:
            card_name += " (Showcase)"
        

        return card_name
    else:
        return "Not Found", "Unknown"


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
        
        card_name = fetch_scryfall_data(scryfall_id)
        
        new_data.append([card_name, set_name, foil, quantity])
    
    return pd.DataFrame(new_data, columns=["Card Name", "Set Name", "Foil", "Quantity"])