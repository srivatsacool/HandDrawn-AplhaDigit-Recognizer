import streamlit as st

bg_image = st.sidebar.selectbox(
    label="Any particular number you want to Draw ?",
    options=("Number_0","Number_1","Number_2","Number_3","Number_4","Number_5" , "Number_6","Number_7","Number_8","Number_9"),
)
if bg_image == "Number_4" or bg_image == "Number_5" or bg_image == "Number_9":
    print(f"numbers/{bg_image}.jpg")
    st.image(f"numbers/{bg_image}.jpg")
else:
    print(f"numbers/{bg_image}.png")
    st.image(f"numbers/{bg_image}.png")