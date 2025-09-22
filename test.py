from dotenv import load_dotenv
import os

load_dotenv()

url = os.environ.get("SUPABASE_URL")
print("SUPABASE_URL:", url)
