import streamlit as st
from scrapers.scrape import scrape_website

st.title("AI WEB SCRAPER")

url = st.text_input("Enter a website URL: ")

if st.button("Scrape Website: "):
    st.write("Scraping the website....")

    result = scrape_website(url)

    print(result)
