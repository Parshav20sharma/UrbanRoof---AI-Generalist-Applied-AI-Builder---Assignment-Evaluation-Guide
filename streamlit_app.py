import streamlit as st
from app.ai_engine import generate_response

st.set_page_config(page_title="UrbanRoof AI Chatbot")

st.title("UrbanRoof AI Assistant")

# Initialize session state
if "messages" not in st.session_state:
    st.session_state.messages = []

if "user_info_submitted" not in st.session_state:
    st.session_state.user_info_submitted = False


# Step 1 — Collect Name and Location
if not st.session_state.user_info_submitted:

    st.subheader("Enter your details")

    name = st.text_input("Your Name")
    location = st.text_input("Your Location")

    if st.button("Start Chat"):

        if name and location:

            st.session_state.name = name
            st.session_state.location = location
            st.session_state.user_info_submitted = True

            st.rerun()

        else:
            st.warning("Please enter both Name and Location")


# Step 2 — Chat Interface
else:

    st.success(f"Chat started as {st.session_state.name} from {st.session_state.location}")

    # Display previous messages
    for message in st.session_state.messages:

        with st.chat_message(message["role"]):
            st.markdown(message["content"])


    # Chat input box at bottom
    user_input = st.chat_input("Type your message...")

    if user_input:

        # Show user message
        st.session_state.messages.append(
            {"role": "user", "content": user_input}
        )

        with st.chat_message("user"):
            st.markdown(user_input)


        # Generate AI response
        with st.chat_message("assistant"):

            with st.spinner("Thinking..."):

                response = generate_response(
                    st.session_state.name,
                    st.session_state.location,
                    user_input
                )

                st.markdown(response)

        # Save assistant message
        st.session_state.messages.append(
            {"role": "assistant", "content": response}
        )
