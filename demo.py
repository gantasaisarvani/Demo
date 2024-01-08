import streamlit as st
st.set_page_config(page_title='Birds')
st.header("Types of Birds")

col1,col2=st.columns(2)
with col1:
  st.subheader("Parrot")
  st.image("Parrot.jpg",caption="Parrot",width=300,use_column_width=True)
  st.write("Parrots also known as psittacines")
with col2:
  st.subheader("Blue bird")
  st.image("Blue birds.jpg",caption="Blue bird",width=300,use_column_width=True)
  st.write("Bluebird also known as Sialia")
  
