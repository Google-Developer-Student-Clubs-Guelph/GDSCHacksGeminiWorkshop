##
## Web app that uses streamlit and the gemini api
##
## The user can enter a prompt and the gemini model will
## return a response (then output it to the screen)
##

##
## Before coding:
##
##  1. Create the folder and file structure
##  2. Create the config.json file and add the API key to it
##

##
## Step 1: Install the required libraries and import here
##
## pip install -q -U google-generativeai streamlit IPython
##
import streamlit as st
import google.generativeai as genai
import json

##
## Step 2: Import for our custom `to_markdown` function
##

##
## Step 3: Read the key in the json file
##
config = json.load(open("./config.json"))
api_key: str = config["gemini"]["api_key"]

##
## Step 4: The app title and description
##

##
## Step 5: Set the api key and initialize the model
##
## "gemini-pro" is the model name that we are using
##
genai.configure(api_key=api_key)
model = genai.GenerativeModel("gemini-pro")

##
## Step 6: Create an input field for the user to enter a prompt
##

##
## Step 7: Create a button to submit the prompt and check if it was clicked
##
## This is done using the `st.button` function in an `if` statement
##

##
## Step 8: If the button was clicked, generate a response
##
response = model.generate_content("the prompt variable goes here")
response.resolve()
text = response._result.candidates[0].content.parts[0].text

##
## Step 9: Convert the text to markdown using our custom function
##          and write it to the screen.
##

##
## We're done! Run the app using the command below:
##
## streamlit run src/app.py
##
