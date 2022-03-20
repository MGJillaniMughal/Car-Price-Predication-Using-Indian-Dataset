import streamlit as st
import pandas as pd
import pickle

model = pickle.load(open('Linear_Reg_Model.pkl','rb'))

def Main():

    
    df=pd.read_csv('car_data.csv')

    # Create a list of possible values and multiselect menu with them in it.
    car_names = df['Car_Name'].unique()

    Fuel_Type=df['Fuel_Type'].unique()
    owner=df['Owner'].unique()
    transmission=df['Transmission'].unique()
    seller_type=df['Seller_Type'].unique()

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

    car_name=st.selectbox('In Which Car You have ?',car_names,key='car_name')

    years = st.number_input('In which year car was purchased ?',1990, 2021, step=1, key ='year')
    Years_old = 2021-years

    Present_Price = st.number_input('What is the current ex-showroom price of the car ?  (In ₹lakhs)', 0.00, 50.00, step=0.5, key ='present_price')

    Kms_Driven = st.number_input('What is distance completed by the car in Kilometers ?', 0.00, 500000.00, step=500.00, key ='drived')

    Owner = st.radio("The number of owners the car had previously ?",owner, key='owner')

    Fuel_Type_Petrol = st.selectbox('What is the fuel type of the car ?',Fuel_Type, key='fuel')

    # if(Fuel_Type_Petrol=='Petrol'):
    
    #     Fuel_Type_Petrol=1
    #     Fuel_Type_Diesel=0
    
    # elif(Fuel_Type_Petrol=='Diesel'):
    
    #     Fuel_Type_Petrol=0
    #     Fuel_Type_Diesel=1
    
    # else:
    
    #     Fuel_Type_Petrol=0
    #     Fuel_Type_Diesel=0

    Seller_Type_Individual = st.selectbox('Are you a dealer or an individual ?',seller_type, key='dealer')
    
    # if(Seller_Type_Individual=='Individual'):
    
    #     Seller_Type_Individual=1
    
    # else:
    
    #     Seller_Type_Individual=0	

    Transmission_Mannual = st.selectbox('What is the Transmission Type ?', transmission, key='manual')
    
    # if(Transmission_Mannual=='Mannual'):
    
    #     Transmission_Mannual=1
    
    # else:
    
    #     Transmission_Mannual=0

    if st.button("Estimate Price", key='predict'):
    
        try:
            Model = model  #get_model()
    
            prediction = Model.predict([[car_name,Years_old, Present_Price, Kms_Driven, Owner, Fuel_Type_Petrol, Seller_Type_Individual, Transmission_Mannual]])
            output = round(prediction[0],2)
    
            if output<0:
    
                st.warning("You will be not able to sell this car !!")
    
            else:
                
                st.success("You can sell the car for {} lakhs 🙌".format(output))
    
        except:
    
            st.warning("Opps!! Something went wrong\nTry again")

if __name__ == '__main__':
    Main()