
import streamlit as st
import numpy as np

# set the page config
st.set_page_config(page_title='BMI Calculator', page_icon='🏋️', layout='centered')

# add title and description
st.title('BMI Calculator 🏋️')
st.write('Calculate your body mass indece (BMI) to check if you have a healthy body weight.')

# create a two column for input
col1, col2 = st.columns(2)

with col1:
    weight =st.number_input('Enter your weight (kg), min_value=20.0, max_value= 300.0,value=70.0, step=0.1')
with col2:
    height= st.number_input('Enter your heught(cm),min_value=100.0, max_value= 250.0,value=170.0, step=0.1')

# function to calculate BMI
def calculate_bmi(weight,height):
    return weight / ((height/100)**2)

# function of categorize BMI
def get_bmi_category(bmi):
    if bmi < 18.5:
        return 'underweight','warning'
    elif 18.5 <= bmi < 24:
        return 'healthy weight','sucess'
    elif 25 <= bmi < 30:
        return 'overweight','warning'
    elif 30 <= bmi < 35:
        return 'dangerously overweight','warning'
    else:
        return 'obsity'
    

def main():
    #calculate BMI button
    if st.button('calculate BMI'):
        bmi = calculate_bmi(weight,height)
        category,status = get_bmi_category(bmi)

        #display the result of BMI
        st.write("-----")
        st.markdown(f'### your BMI : **{bmi:.1f}**')

        #display the category of BMI
        st.markdown(f'### category: {status} [**{category}**]')

        # display the chart of BMI
        st.write("-----")
        st.write('### Bmi category according to your bmi value')
        st.write('-- underweight: < 18.5')
        st.write('-- Normal weight: 18.5 - 24.9')
        st.write('-- overweight: 25 - 29.9')
        st.write('-- Obesity:  > 30')

        #add a visuialization of BMI
        st.write('### your BMI on the scale :')
        bmi_range = np.arange(15, 30, 0.1)
        current_bmi = float (bmi)

        # create a progress bar line
        progress = (current_bmi -15) / (35 - 15)
        progress = min (max(progress, 0), 1)
        st.progress = (progress)

if __name__ == '__main__':
    main()



