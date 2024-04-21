import os
from pandasai import Agent
import pandas as pd
from pandasai.llm import OpenAI
from dotenv import load_dotenv

load_dotenv()

API_KEY = os.getenv('API_KEY')

# Sample DataFrames
sales_by_country = pd.DataFrame({
    "country": ["United States", "United Kingdom", "France", "Germany", "Italy", "Spain", "Canada", "Australia", "Japan", "China"],
    "sales": [5000, 3200, 2900, 4100, 2300, 2100, 2500, 2600, 4500, 7000],
    "deals_opened": [142, 80, 70, 90, 60, 50, 40, 30, 110, 120],
    "deals_closed": [120, 70, 60, 80, 50, 40, 30, 20, 100, 110]
})


# By default, unless you choose a different LLM, it will use BambooLLM.
# You can get your free API key signing up at https://pandabi.ai (you can also configure it in your .env file)
# Instantiate a LLM
llm = OpenAI(api_token=API_KEY)

if __name__ == '__main__':
    agent = Agent(sales_by_country, config = {'llm': llm})
    print(agent.chat('Which are the top 5 countries by sales?'))