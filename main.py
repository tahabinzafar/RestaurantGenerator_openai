# Import Streamlit library for building web apps
import streamlit as st

# Import helper for generating restaurant names and menu items
import langchain_helper

# Set the title of the web app
st.title("Restaurant Name Generator")

# Create a sidebar with a dropdown menu to select a cuisine
cuisine = st.sidebar.selectbox("Pick a Cuisine", ("British", "Pakistani", "Indian", "Italian", "Mexican", "Arabic", "American"))

# Check if a cuisine is selected
if cuisine:
    
    # Generate restaurant name and menu items based on the selected cuisine
    response = langchain_helper.generate_restaurant_name_and_items(cuisine)
    
    # Display the generated restaurant name as a header
    st.header(response['restaurant_name'].strip())
    
    # Split and display the generated menu items
    menu_items = response['menu_items'].strip().split(",")
    st.write("**Menu Items**")
    for item in menu_items:
        st.write("-", item)
