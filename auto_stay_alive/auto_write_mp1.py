from supabase import create_client, Client
import time
import os

# Gegevens
url = os.environ.get("SUPABASE_URL_MP1")
key = os.environ.get("SUPABASE_KEY_MP1")
supabase: Client = create_client(url, key)

def voer_actie_uit():
    aantal = 5
    count = 0
    while count < aantal:
        try:
            # 1. TOEVOEGEN
            nieuw_item = {
                "ticker": "TEST",
                "ticker": "0"
            }
            insert_res = supabase.table("stock_performance").insert(nieuw_item).execute()
            
            # Haal het ID op van de zojuist toegevoegde regel
            rij_data = insert_res.data[0]
            rij_id = rij_data['id'] # Let op: gebruik 'ID' als je kolom met hoofdletters is
        
    
            # Wacht even (optioneel, om het proces te volgen)
            time.sleep(3)
    
            # 2. VERWIJDEREN
            # We zeggen: verwijder de regel waar 'id' gelijk is aan het rij_id dat we net kregen
            delete_res = supabase.table("stock_performance").delete().eq("id", rij_id).execute()
            
    
        except Exception as e:
            print(f"❌ Er is iets misgegaan: {e}")
        count = count + 1

if __name__ == "__main__":
    voer_actie_uit()
