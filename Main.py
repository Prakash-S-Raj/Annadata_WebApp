import numpy as np
import streamlit as st
import pickle as pk
from streamlit_option_menu import option_menu
import Home,Search



st.set_page_config(
    page_title="Annadata",
    page_icon="rice",
)
class AD:
    def __init__(self):
        self.apps=[]
    def add_app(self,title,func):
        self.apps.append({
            "title":title,
            "function":func
        })
    def set_background():
        page_bg_img='''
        <style>
            body{
                background-image:url("bg image.jpg")
                background-size:cover;
            }
        </style>'''
        st.markdown(page_bg_img,unsafe_allow_html=True)
        st.title(':green[Welcome to Annadata] :coconut:')
    def run():
        
        AD.set_background()
        with st.sidebar:
            app=option_menu(
            menu_title=None,
            options=["Home","Search"],
            icons=["house","search"],
            menu_icon="cast",
            default_index=0,
            )
            styles={
                "container":{
                    "padding":"5!important",
                    "icon":{"color":"white","font-size":"23px"},
                    "nav-link":{"color":"white","font-size":"20px"},
                }
            }
        if app=="Home":
                Home.app()
        if app=="Search":
            Search.main()


AD()

AD.run()
        

