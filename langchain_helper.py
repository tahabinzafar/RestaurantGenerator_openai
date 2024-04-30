# Import necessary modules and libraries
from langchain.llms import OpenAI
from langchain.prompts import PromptTemplate
from langchain.chains import LLMChain
from langchain.chains import SequentialChain
from secret_key import openapi_key

import os

# Set OpenAI API key
os.environ['OPENAI_API_KEY'] = openapi_key

# Initialize OpenAI language model
llm = OpenAI(temperature=0.7)

# Define a function to generate restaurant names and menu items based on cuisine
def generate_restaurant_name_and_items(cuisine):

    # Chain 1: Generate a restaurant name based on cuisine
    prompt_template_name = PromptTemplate(
        input_variables=['cuisine'],
        template="I want to open a restaurant for {cuisine} food. Suggest a fancy name for this."
    )

    # Initialize LLMChain for generating restaurant names
    name_chain = LLMChain(llm=llm, prompt=prompt_template_name, output_key="restaurant_name")

    # Chain 2: Generate menu items based on the generated restaurant name
    prompt_template_items = PromptTemplate(
        input_variables=['restaurant_name'],
        template="""Suggest some menu items for {restaurant_name}. Return it as a comma separated string"""
    )

    # Initialize LLMChain for generating menu items
    food_items_chain = LLMChain(llm=llm, prompt=prompt_template_items, output_key="menu_items")

    # Define a sequential chain to execute the chains sequentially
    chain = SequentialChain(
        chains=[name_chain, food_items_chain],  # List of chains to execute sequentially
        input_variables=['cuisine'],  # Input variables required for the chains
        output_variables=['restaurant_name', "menu_items"]  # Output variables returned by the chains
    )

    # Execute the chain with the provided cuisine as input
    response = chain({'cuisine': cuisine})

    # Return the response containing the generated restaurant name and menu items
    return response

# Main block to execute the function with an example cuisine
if __name__ == "__main__":
    print(generate_restaurant_name_and_items("Italian"))
