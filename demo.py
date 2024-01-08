import streamlit as st
st.set_page_config(page_title='Birds')
st.header("Types of Birds")

col1,col2=st.columns(2)
with col1:
  st.subheader("Parrot")
  st.image("https://images.unsplash.com/photo-1552728089-57bdde30beb3?q=80&w=1000&auto=format&fit=crop&ixlib=rb-4.0.3&ixid=M3wxMjA3fDB8MHxzZWFyY2h8Mnx8cGFycm90fGVufDB8fDB8fHww",caption="Parrot",width=300,use_column_width=True)
  st.write("Parrots also known as psittacines")
with col2:
  st.subheader("Blue bird")
  st.image("https://qph.cf2.quoracdn.net/main-qimg-7f9ae22462e89a4cadab85127ad2c3ed-lq",caption="Blue bird",width=300,use_column_width=True)
  st.write("Bluebird also known as Sialia")
with col3:
  st.subheader("Bird Singing")
  st.image("https://media3.giphy.com/media/KfxPezYC20OnSPQK5J/giphy.gif",caption="Blue bird",width=300,use_column_width=True)
  st.write("Birdsn are so beautiful")


