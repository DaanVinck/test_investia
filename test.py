import os
from dotenv import load_dotenv
from supabase import create_client, Client

# 1. Laad .env in
load_dotenv()

# 2. Haal variabelen op
url = os.environ.get("SUPABASE_URL")
key = os.environ.get("SUPABASE_KEY")

# --- DEBUGGING START ---
# Controleer of de variabelen wel echt geladen zijn
if not url or not key:
    print("FOUT: SUPABASE_URL of SUPABASE_KEY niet gevonden in .env bestand!")
else:
    # Verwijder eventuele onzichtbare spaties of extra aanhalingstekens
    url = url.strip().replace('"', '').replace("'", "")
    key = key.strip().replace('"', '').replace("'", "")
    
    print(f"DEBUG: Verbinding maken met URL: {url}") # Check of dit eruit ziet als https://xyz...
# --- DEBUGGING EIND ---

try:
    supabase: Client = create_client(url, key)
    print("Supabase client succesvol aangemaakt.")
except Exception as e:
    print(f"Fout bij aanmaken client: {e}")