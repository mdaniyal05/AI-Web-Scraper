import streamlit as st
from scrapers.scrape import scrape_website
from helpers.clean_html_body import clean_body_content
from helpers.extract_html_body import extract_body_content
from helpers.split_content import split_content
from llms.parse_content import parse_with_llama3

st.title("AI WEB SCRAPER")

if "content" not in st.session_state:
    st.session_state.content = None
if "parsed_result" not in st.session_state:
    st.session_state.parsed_result = None
if "parse_description" not in st.session_state:
    st.session_state.parse_description = ""


url = st.text_input("Enter a website URL:")


if st.button("Scrape Website"):
    st.write("Scraping the website....")

    result = scrape_website(url)
    body_content = extract_body_content(result)
    cleaned_content = clean_body_content(body_content)

    st.session_state.content = cleaned_content
    st.session_state.parsed_result = None

if st.session_state.content:
    with st.expander("View Content"):
        st.text_area("Content", st.session_state.content, height=500)

    st.session_state.parse_description = st.text_area(
        "Describe what you want to parse?",
        value=st.session_state.parse_description
    )

    if st.button("Parse Content"):
        if st.session_state.parse_description.strip():
            st.write("Parsing the content....")
            content_chunks = split_content(st.session_state.content)
            result = parse_with_llama3(
                content_chunks, st.session_state.parse_description)
            st.session_state.parsed_result = result

if st.session_state.parsed_result:
    st.subheader("Parsed Result")
    st.write(st.session_state.parsed_result)
