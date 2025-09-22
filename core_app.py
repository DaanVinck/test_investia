from dotenv import load_dotenv 
load_dotenv()
import os
from supabase import create_client, Client

url = os.environ.get("SUPABASE_URL")
key = os.environ.get("SUPABASE_KEY")
supabase = create_client(url, key)


#data = supabase.table("test_investia").insert({"id": "Daan", "pasword": "123456", "email": "daan@gmail.com"}).execute()
data = supabase.table("test_investia").select("*").execute()
print(data)