# app.py
import streamlit as st
from agent_utils import get_search_results

st.set_page_config(page_title=" MyPlexity", page_icon="🌐")

st.title("🔍 Ask MyPlexity Anything!")

query = st.text_input("Enter your query:", placeholder="e.g. What are the latest trends in AI!")

if st.button("Search"):
    if query.strip():
        with st.spinner("Searching..."):
            response = get_search_results(query)
        st.success("✅ Here's what I found:")
        st.write(response)
    else:
        st.warning("⚠️ Please enter a query before searching.")
