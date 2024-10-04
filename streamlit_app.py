import streamlit as st

m = st.markdown("""
<style>
.counter-text {
        font-size: 24px;
        color: black;
        font-weight: bold;
        margin: auto;
        display: block;
        text-align:center;
        margin-top:-130px;
    }
div.stButton > button:first-child {
    background-color: #007bff;;
    color: white;
    height: 3em;
    width: 12em;
    border-radius:10px;
    border:3px solid #000000;
    font-size:20px;
    font-weight: bold;
    margin: auto;
    display: block;
}
</style>""", unsafe_allow_html=True)



# Initialize the counter in session state if it doesn't exist
st.session_state.counter = st.session_state.get('counter', 0)


# Button to increment the counter
if st.button("Increase Counter"):
    st.session_state.counter += 1

st.markdown(f'<div class="counter-text">Counter:{st.session_state.counter}</div>', unsafe_allow_html=True)
