
from dotenv import load_dotenv 
load_dotenv()
import os
from supabase import create_client, Client

url = os.environ.get("SUPABASE_URL")
key = os.environ.get("SUPABASE_KEY")
supabase = create_client(url, key)

name = "Daansqmfqs"
code = "1234"
email = "daan@example.com"

# Voeg het toe aan de tabel
res = supabase.table("test_investia").insert([{"id": name, "pasword": code, "email": email}]).execute()
data = supabase.table("test_investia").select("id, pasword").execute()

print(data)