import streamlit as st 
import pandas as pd
import joblib

model_path = r'E:\VS Code\Grand_Project\notebook\gbgs_model.joblib'
model = joblib.load(model_path)

def main():
    st.title("Credit Risk Assessment")
    html_temp = """
    <div style="background-color:tomato;padding:10px">
    <h2 style="color:white;text-align:center;">Streamlit Credit Risk Assessment App </h2>
    </div>
    """
    with st.sidebar:
        user_name=st.text_input("Enter your name: ")
        if len(user_name)>3:
            st.info(f"Welcome {user_name}")

    st.markdown(html_temp, unsafe_allow_html=True)
    Age = st.number_input("Enter Age")  
    Income = st.number_input("Enter Income")
    Home = st.text_input("Enter Home")
    Emp_length = st.number_input("Enter Employment Length")
    Intent = st.text_input("Enter Loan Intension")
    Amount = st.number_input("Enter Amount")
    Rate = st.number_input("Enter Rate")
    Percent_income = st.number_input("Enter Income Percentage")
    Default = st.text_input("Enter Default") 

    data = {'Age': [Age],
            'Income': [Income],
            'Home': [Home],
            'Emp_length': [Emp_length],
            'Intent': [Intent],
            'Amount': [Amount],
            'Rate': [Rate],
            'Percent_income': [Percent_income],
            'Default': [Default]}
    
    inputs = pd.DataFrame(data)

    if st.button("Predict"):
        if not inputs.empty:
            try:
                prediction = predictions(inputs)[0]
                if prediction == 1:
                    st.success("Dear {} the Credit Risk Assessment's status is {}".format(user_name,prediction))
                else:
                    st.error("Dear {} the Credit Risk Assessment's status is {}".format(user_name,prediction))
            except Exception as e:
                st.error(f"Error during prediction: {e}")
        else:
            st.warning("Please enter valid input values.")

    if st.button("About"):
        st.text("Let's Learn")
        st.text("Built with Streamlit")


def predictions(inputs):
    prediction = model.predict(inputs)
    return prediction

if __name__ == "__main__":
    main()
