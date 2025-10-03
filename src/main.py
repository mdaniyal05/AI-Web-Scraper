import streamlit as st
from scrapers.scrape import scrape_website
from helpers.clean_html_body import clean_body_content
from helpers.extract_html_body import extract_body_content
from helpers.split_content import split_content
from llms.parse_content import parse_with_llama3

st.title("AI WEB SCRAPER")

url = st.text_input("Enter a website URL: ")

if st.button("Scrape Website"):
    st.write("Scraping the website....")

    result = scrape_website(url)

    body_content = extract_body_content(result)

    cleaned_content = clean_body_content(body_content)

    st.session_state.content = cleaned_content

    with st.expander("View Content"):
        st.text_area("Content", cleaned_content, height=500)

    if "content" in st.session_state:
        parse_description = st.text_area("Describe what you want to parse?")

        if st.button("Parse Content"):
            if parse_description:
                st.write("Parsing the content....")

                content_chunks = split_content(st.session_state.content)

                result = parse_with_llama3(content_chunks, parse_description)

                st.write(result)
