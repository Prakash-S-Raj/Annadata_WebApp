import streamlit as st
import numpy as np
import pickle as pk 
#st.title("Search your desired crop")

with open('Crop recommendation.pkl','rb') as file:
    loaded_model=pk.load(file)

def crop_recommendation(input_data):
    i_data=np.asarray(input_data)
    final_data=i_data.reshape(1,-1)
    prediction=loaded_model.predict(final_data)
    return prediction[0]
def main():
    st.subheader(':red[Take your desired crop!] :rose: ')
    styles={
        "padding":"20px",
        "color":"red",
    }
    N=st.text_input('Nitrogen content in the field',placeholder="Nitrogen")
    P=st.text_input('Phosphorous content in the field',placeholder="Phosphorous")
    K=st.text_input('Potassium content in the field',placeholder="Potassium")
    Temperature=st.text_input('Temperature of the crop field',placeholder="Temperature")
    Humidity=st.text_input('Humidity of the field region',placeholder="Humidity")
    pH=st.text_input('ph of the respective crop',placeholder="pH")
    Rainfall=st.text_input('Rainfall near the crop field',placeholder="Rainfall")
    input_file=[N,P,K,Temperature,Humidity,pH,Rainfall]
    recommended=''
    if (st.button('Crop name')):
        recommended=crop_recommendation(input_file)
    
    if st.success(recommended):
        st.title('ಅನ್ನದಾತೋ ಸುಖೀಭವ:')
if __name__=='__main__':
    main()