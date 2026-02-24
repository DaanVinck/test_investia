from supabase import create_client, Client
import time

# Gegevens
url = os.environ.get("SUPABASE_URL")
key = os.environ.get("SUPABASE_KEY")
supabase: Client = create_client(url, key)

def voer_actie_uit():
    try:
        # 1. TOEVOEGEN
        nieuw_item = {
            "stock_name": "Test Aandeel",
            "ticker": "TEST"
        }
        insert_res = supabase.table("stock").insert(nieuw_item).execute()
        
        # Haal het ID op van de zojuist toegevoegde regel
        rij_data = insert_res.data[0]
        rij_id = rij_data['id'] # Let op: gebruik 'ID' als je kolom met hoofdletters is
        
        print(f"✅ Toegevoegd: {rij_data['stock_name']} met ID: {rij_id}")

        # Wacht even (optioneel, om het proces te volgen)
        print("Wachten op verwijderen (3 seconden)...")
        time.sleep(3)

        # 2. VERWIJDEREN
        # We zeggen: verwijder de regel waar 'id' gelijk is aan het rij_id dat we net kregen
        delete_res = supabase.table("stock").delete().eq("id", rij_id).execute()
        
        print(f"🗑️ Succesvol verwijderd: Regel met ID {rij_id}")

    except Exception as e:
        print(f"❌ Er is iets misgegaan: {e}")

if __name__ == "__main__":
    voer_actie_uit()
