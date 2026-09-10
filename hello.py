import os
import time

from dotenv import load_dotenv
from google import genai
from google.genai.errors import ServerError

load_dotenv()

client = genai.Client(api_key=os.environ["GOOGLE_API_KEY"])

for i in range(3):
    try:
        response = client.models.generate_content(
            model="gemini-flash-latest",
            contents="こんにちは",
        )

        print(response.text)
        print("接続成功")
        break

    except ServerError as e:
        print("サーバーが混雑しています。再試行します。")
        time.sleep(5)