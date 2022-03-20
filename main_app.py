import streamlit as st
import pickle
import numpy as np
import pandas as pd

def Main():

    model = pickle.load(open('Final_Car_Name_Price_Predicting_Model.pkl','rb'))
    
    df=pd.read_csv('car_data.csv')

    
    string = "Car Price Predictor"
    st.set_page_config(page_title=string, page_icon="🚗") 
    st.title("Car Price Predictor 🚗")
    st.markdown("##### Are you planning to sell your car !?\n##### So let's try evaluating the price.. 🤖 ")
    st.image(
            "https://imgd.aeplcdn.com/0x0/n/cw/ec/27032/s60-exterior-right-front-three-quarter-3.jpeg",
            width=400, # Manually Adjust the width of the image as per requirement
        )
    st.write('')
    st.write('')
    
    # brand
    car_name = st.selectbox('In Which Car You have ? ',df['Car_Name'].unique())

    years = st.number_input('In which year car was purchased ?',1990, 2021, step=1, key ='year')
    Years_old = 2021-years

    Present_Price = st.number_input('What is the current ex-showroom price of the car ?  (In ₹lakhs)', 0.00, 50.00, step=0.5, key ='present_price')

    Kms_Driven = st.number_input('What is distance completed by the car in Kilometers ?', 0.00, 500000.00, step=500.00, key ='drived')

    Owner = st.radio("The number of owners the car had previously ?", (0, 1, 3), key='owner')

    Fuel_Type_Petrol = st.selectbox('What is the fuel type of the car ?',df['Fuel_Type'].unique())

    Seller_Type_Individual = st.selectbox('Are you a dealer or an individual ?',df['Seller_Type'].unique())

    Transmission_Mannual = st.selectbox('What is the Transmission Type ?', df['Transmission'].unique())
    
    if st.button('Predict Price'):


        try:
            Model = model  #get_model()
    
            prediction = Model.predict([car_name, Years_old, Present_Price, Kms_Driven, Owner, Fuel_Type_Petrol, Seller_Type_Individual, Transmission_Mannual])
            output = round(prediction[0],2)
    
            if output<0:
    
                st.warning("You will be not able to sell this car !!")
    
            else:
                
                st.success("You can sell the car for {} lakhs 🙌".format(output))
    
        except:
    
            st.warning("Opps!! Something went wrong\nTry again")

if __name__ == '__main__':
    Main()

