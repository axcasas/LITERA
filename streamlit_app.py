import streamlit as st
import streamlit_book as stb

# Set wide display
st.set_page_config(layout="wide")

# Set multipage
save_answers = True

stb.set_book_config(menu_title="LITERA",
                    menu_icon="clock",
                    options=[
                            "Intro",   
                            "MCTQ", 
                            ], 
                    paths=[
                            "pages/Intro.py", 
                            "pages/00 MCTQ", 
                            ],
                    icons=[
                            "book", 
                            "code", 
                            ],
                    save_answers=save_answers,
                    )