import os 

import streamlit as st 
from langchain.prompts import PromptTemplate
from langchain.chains import LLMChain 
from langchain.utilities import WikipediaAPIWrapper 
from langchain import PromptTemplate, HuggingFaceHub, LLMChain
os.environ["HUGGINGFACEHUB_API_TOKEN"] = 'xxxxxxxxx'

# App framework
st.title('Meal Plan Generator')
prompt = st.text_input('Plug in your dietary restrictions here and a meal plan will be generated!') 

# Prompt templates
food_template = PromptTemplate(
    input_variables = ['restrictions'], 
    template='Generate me a meal plan with these dietary restrictions using the wikipedia as a reference RESTRICTIONS: {restrictions}'
)





# Llms
llm=HuggingFaceHub(repo_id="gpt2-xl", model_kwargs={"temperature":0.7})
plan_chain = LLMChain(llm=llm, prompt=food_template, verbose=True)

wiki = WikipediaAPIWrapper()

# Show stuff to the screen if there's a prompt
if prompt: 
    wiki_research = wiki.run(prompt) 
    plan = plan_chain.run(restrictions=prompt, wikipedia_research=wiki_research)

    st.write(plan) 



    with st.expander('Wikipedia Research'): 
        st.info(wiki_research)
