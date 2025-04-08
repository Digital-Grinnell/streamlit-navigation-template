# app_pages/switch_page_demo.py
import streamlit as st

def switch_page( ):
    st.title("Using st.switch_page")
    st.write("`st.switch_page` allows you to programmatically switch pages.")
    st.code("""
if st.button("Go to Intro"):
    st.switch_page("app_pages/intro.py")
    """, language="python")
    if st.button("Go to Intro"):
        st.switch_page("app_pages/intro.py")

if __name__ == "__main__":
    switch_page( )

