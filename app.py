# import streamlit as st
# import subprocess

# def run_command(input_text):
#     command = f'python main.py --transcribe --play'
#     subprocess.run(command, shell=True)

# def main():
#     st.title("Audio Generation")
#     input_text = st.text_area("Enter text", height=200)
#     if st.button("Submit"):
#         run_command(input_text)
#         st.success("Audio generated successfully!")

# if __name__ == '__main__':
#     main()

import streamlit as st
import subprocess

def run_command(input_text):
    with open('input_streamlit.txt', 'w') as file:
        file.write(input_text)
    command = 'python main.py --transcribe --play'
    subprocess.run(command, shell=True)

def main():
    st.title("Audio Generation")
    input_text = st.text_area("Enter text", height=200)
    if st.button("Submit"):
        run_command(input_text)
        st.success("Audio generated successfully!")

if __name__ == '__main__':
    main()
