import streamlit as st
from scrapers.scrape import scrape_website
from helpers.clean_html_body import clean_body_content
from helpers.extract_html_body import extract_body_content
from helpers.split_content import split_content

st.title("AI WEB SCRAPER")

url = st.text_input("Enter a website URL: ")

if st.button("Scrape Website: "):
    st.write("Scraping the website....")

    result = scrape_website(url)

    body_content = extract_body_content(result)

    cleaned_content = clean_body_content(body_content)

    st.session_state.dom_content = cleaned_content

    with st.expander("View Content"):
        st.text_area("Content", cleaned_content, height=500)
