from dotenv import load_dotenv
import os
load_dotenv()
print(os.getenv("TMDB_API_KEY"))