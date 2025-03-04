import requests

SCRYFALL_API_URL = "https://api.scryfall.com/cards/"

def fetch_scryfall_data(scryfall_id):
    """Fetches card details from Scryfall API."""
    response = requests.get(f"{SCRYFALL_API_URL}{scryfall_id}")
    if response.status_code == 200:
        data = response.json()
        card_name = data.get("name", "Unknown")
        border_color = data.get("border_color", "Unknown")
        frame_effect = data.get("frame_effects", [0][0])
        
        # Modify name based on border color
        if border_color == "borderless":
            card_name += " (Borderless)"

        if frame_effect == 'extendedart':
            card_name += " (Extended Art)"

        return card_name
    else:
        return "Not Found", "Unknown"