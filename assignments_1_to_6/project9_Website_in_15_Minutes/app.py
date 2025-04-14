import streamlit as st
import time

paragraph = """
The quick brown fox jumps over the lazy dog. This sentence contains every 
letter of the English alphabet, making it a popular pangram used for typing 
practice.
"""

# Title and Instructions
st.title("Typing Speed Tester")
st.subheader("Test your typing speed and accuracy!")
st.markdown("Type the following paragraph as quickly and accurately as you can:")
st.markdown(paragraph)

# Initialize session state
if 'start' not in st.session_state:
    st.session_state.start = False
if 'start_time' not in st.session_state:
    st.session_state.start_time = None
if 'end_time' not in st.session_state:
    st.session_state.end_time = None
if 'user_input' not in st.session_state:
    st.session_state.user_input = ""

# Start Test Button
if st.button("Start Test"):
    st.session_state.start = True
    st.session_state.start_time = time.time()
    st.session_state.user_input = ""  # Clear previous input
    st.session_state.end_time = None

# Show input field only when test is started
if st.session_state.start:
    timer_placeholder = st.empty()

    elapsed_time = time.time() - st.session_state.start_time
    minutes = int(elapsed_time // 60)
    seconds = int(elapsed_time % 60)
    st.write(f"⏱️ Time elapsed: **{minutes} minutes {seconds} seconds**")
    st.text_area("Type here:", height=200, max_chars=len(paragraph), key="user_input")

    if st.button("Submit"):
        st.session_state.end_time = time.time()
        st.session_state.start = False  # Stop the test

        # Typing test logic
        def typing_speed_test(original, typed, start_time, end_time):
            time_taken = end_time - start_time
            words_per_minute = (len(typed.split()) / time_taken) * 60

            correct_chars = sum(1 for o, t in zip(original, typed) if o == t)
            accuracy = (correct_chars / len(original)) * 100 if original else 0

            return round(words_per_minute, 2), round(accuracy, 2), round(time_taken, 2)

        wpm, accuracy, time_taken = typing_speed_test(
            paragraph,
            st.session_state.user_input,
            st.session_state.start_time,
            st.session_state.end_time,
        )

        minutes = int(time_taken // 60)
        seconds = int(time_taken % 60)

        st.success("Test completed!")
        st.write(f"🕒 Time taken: **{minutes} minutes {seconds} seconds**")
        st.write(f"⌨️ Your typing speed: **{wpm} WPM**")
        st.write(f"🎯 Your accuracy: **{accuracy}%**")
    
    else:
        time.sleep(1) 
        st.rerun()


# Footer
st.write("\t")
st.markdown("---")
st.markdown("Created with ❤️ by Urooj Sadiq - [Connect on LinkedIn](https://www.linkedin.com/in/urooj-sadiq-a91031212/)")
