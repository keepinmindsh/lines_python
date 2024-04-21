import os
import pandas as pd
from pandasai import SmartDataframe
from pandasai.llm import OpenAI
from dotenv import load_dotenv

load_dotenv()

API_KEY = os.getenv('API_KEY')

# Sample DataFrame
df = pd.DataFrame({
    "country": ["United States", "United Kingdom", "France", "Germany", "Italy", "Spain", "Canada", "Australia", "Japan", "China"],
    "gdp": [19294482071552, 2891615567872, 2411255037952, 3435817336832, 1745433788416, 1181205135360, 1607402389504, 1490967855104, 4380756541440, 14631844184064],
    "happy_index": [6.94, 7.16, 6.66, 7.07, 6.38, 6.4, 7.23, 7.22, 5.87, 5.12]
})

# Instantiate a LLM
llm = OpenAI(api_token=API_KEY)

if __name__ == '__main__':
    df = SmartDataframe(df, config={"llm": llm})
    print(df.chat('Which are the 5 happiest countries?'))