import streamlit as st
import joblib
import pandas as pd
import numpy as np
import pickle
from os.path import dirname, join, realpath


# add banner image
st.header("MOBILE MONEY AND FINANCIAL INCLUSION IN TANZANIA")
st.image("images/logo.jpg")


# form to collect information
my_form = st.form(key="financial_inclusion_form")


@st.cache
# # function to transform Yes and No options
def func(value):
    if value == "Yes":
        return 1
    else:
        return 0

#function to transform Male and Female options
def func2(value):
    if value == "Male":

        return 1
    else:
        return 0

def func3(value):
    if value == "Married":
        return 1
    elif value == "Divorced":
        return 2
    elif value == "Widowed":
        return 3
    else:
        return 4 

def func4(value):
    if value == "No formal education":
        return 1
    elif value == "Some primary":
        return 2
    elif value == "Primary completed":
        return 3
    elif value == "Post primary technical training":
        return 4
    elif value == "Some secondary":
        return 5
    elif value =="University or other higher education":
        return 6
    else:
        return 7    

def func5(value):
    if value == "You personally own the land/plot where you live":
        return 1
    elif value == "You own the land/plot together with someone else":
        return 2
    elif value == "A household member owns the land/plot":
        return 3
    elif value == "The land/plot is rented":
        return 4
    elif value == "You do not own or rent the land":
        return 5
   
    else:
        return 6   

def func9(value):
    if value == "not applicable":
        return -1
    elif value == "Government":
        return 1
    elif value == "Private company/business":
        return 2
    elif value == "Individual who owns his own business":
        return 3
    elif value == "Small scale farmer":
        return 4
    elif value == "Commercial farmer":
        return 5
    elif value == "Work for individual/household e.g. security guard, maid etc.":
        return 6
    else:
        return 7   

def func10(value):
    if value == "not applicable":
        return -1
    elif value == "Crops/produce I grow":
        return 1
    elif value == "Products I get from livestock":
        return 2
    elif value == "Livestock":
        return 3
    elif value == "Fish you catch yourself/aquaculture":
        return 4
    elif value == "Things you buy from others agricultural products":
        return 5
    elif value == "Things you buy from others non-agricultural products":
        return 6
    elif value =="Things you make (clothes, art, crafts)":
        return 7
    elif value == "Things you collect from nature (stones, sand, thatch, herbs)":
        return 8
    elif value == "Things you process (honey, dairy products, flour)":
        return 9          
    else:
        return 10        


def func11(value):
    if value == "not applicable":
        return -1
    elif value == "Personal services (hairdressers, massage, etc.)":
        return 1
    elif value == "Telecommunications/IT":
        return 2
    elif value == "Financial services":
        return 3
    elif value == "Transport":
        return 4
    elif value == "Hospitality Accommodation, restaurants, etc.":
        return 5
    elif value == "Information/research":
        return 6
    elif value =="Technical mechanic, etc.":
        return 7
    elif value == "Educational/child care":
        return 8
    elif value == "Health services traditional healer etc.":
        return 9    

    elif value == "Legal services":
        return 10

    elif value ==  "Security":
        return 11              
    else:
        return 12         

def func13(value):
    if value == "not applicable":
        return -1
    elif value == "Yesterday/today":
        return 1
    elif value == "In the past 7 days":
        return 2
    elif value == "In the past 30 days":
        return 3
    elif value == "In the past 90 days":
        return 4
    elif value =="More than 90 days ago but less than 6 months ago":
        return 5
          
    else:
        return 6      


def func15(value):
    if value == "not applicable":
        return -1
    elif value == "Yesterday/today":
        return 1
    elif value == "In the past 7 days":
        return 2
    elif value == "In the past 30 days":
        return 3
    elif value == "In the past 90 days":
        return 4
    elif value =="More than 90 days ago but less than 6 months ago":
        return 5
          
    else:
        return 6    



def func16(value):
    if value == "not applicable":
        return -1
    elif value == "Never":
        return 1
    elif value == "Daily":
        return 2
    elif value == "Weekly":
        return 3
    elif value == "Monthly":
        return 4
    else:
        return 5   


def func17(value):
    if value == "not applicable":
        return -1
    elif value == "Never":
        return 1
    elif value == "Daily":
        return 2
    elif value == "Weekly":
        return 3
    elif value == "Monthly":
        return 4
    else:
        return 5 



def func18(value):
    if value == "Can read and write":
        return 1
    elif value == "Can read only":
        return 2
    elif value == "Can write only":
        return 3
    elif value == "Can neither read nor write":
        return 4
    
    else:
        return 5 


def func19(value):
    if value == "Can read and write":
        return 1
    elif value == "Can read only":
        return 2
    elif value == "Can write only":
        return 3
    elif value == "Can neither read nor write":
        return 4
    
    else:
        return 5 





 
Q1 = my_form.number_input('Age',min_value=18, max_value=100)

Q2=my_form.selectbox(
    'Gender',
    (
        'Male',
        'Female'
    )
)

Q3=my_form.selectbox(
    'Marital status',
    (
        'Married',
        'Divorced',
        'Widowed',
        'Single/Never Married'
    )
)

Q4=my_form.selectbox(
    'Highest level of education completed?',
    (
        'No Formal Education',
        'Some primary',
        'Primary Completed',
        'Post Primary Technical Training',
        'Some Secondary',
        'University or Other Higher Education',
        'Do Not Know'
    )
)

Q5=my_form.selectbox(
    'Which of the following applies to you? Read out; Single response ',
    (
        'You personally own the land/plot where you live',
        'You own the land/plot together with someone else ',
        'A household member owns the land/plot',
        'The land/plot is rented',
        'You do not own or rent the land',
        'Do Not Know'
    )
)

Q6=my_form.selectbox(
    'Do you personally own land (other than the land you live on) that you have land certificates of ownership for?',
    (
        'Yes',
        'No'
    )
)

Q7=my_form.selectbox(
    'Do you personally own a mobile phone?',
    (
        'Yes',
        'No'
    )
)

Q8=my_form.info('Different people have different ways of getting money, please tell me how you get the money you spend?Multiple mention possible')

Q8_1=my_form.selectbox(
    'Salaries/Wages',
    (
        'Yes',
        'No'
    )
)

Q8_2=my_form.selectbox(
    'Money from trading/selling anything you produce/grow/raise/make/collect with the intention of selling',
    (
        'Yes',
        'No'
    )
)

Q8_3=my_form.selectbox(
    'Money from providing a service i.e. such as transport, hairdressing, processing, hospitality services (food & accommodation) ',
    (
        'Yes',
        'No'
    )
)

Q8_4=my_form.selectbox(
    'Piece work/Casual labor/Occasional jobs',
    (
        'Yes',
        'No'
    )
)

Q8_5=my_form.selectbox(
    'Rental Income',
    (
        'Yes',
        'No'
    )
)

Q8_6=my_form.selectbox(
    'Interest from savings, investments, stocks, unit trusts etc.',
    (
        'Yes',
        'No'
    )
)

Q8_7=my_form.selectbox(
    'Pension',
    (
        'Yes',
        'No'
    )
)

Q8_8=my_form.selectbox(
    'Social welfare money/grant from Government',
    (
        'Yes',
        'No'
    )
)

Q8_9=my_form.selectbox(
    'Rely on someone else/others to give/send me money',
    (
        'Yes',
        'No'
    )
)

Q8_10=my_form.selectbox(
    'Don’t get money someone else pays my expenses',
    (
        'Yes',
        'No'
    )
)

Q8_11=my_form.selectbox(
    'Other',
    (
        'Yes',
        'No'
    )
)

Q9=my_form.selectbox(
    'Only for those who said they get a salary/wages. Who do you work for?',
    (
        'not applicable',
        'Government',
        'Private company/business',
        'Individual who owns his own business',
        'Small scale farmer',
        'Commercial farmer',
        'Work for individual/household e.g. security guard, maid etc.',
        'Other'
    )
)

Q10=my_form.selectbox(
    'Only for those who said they get money from selling things, what kind of things do you MAINLY sell (get most money from)?',
    (
        'not applicable',
        'Crops/produce I grow',
        'Products I get from livestock',
        'Livestock',
        'Fish you catch yourself/aquaculture',
        'Things you buy from others agricultural products',
        'Things you buy from others non-agricultural products',
        'Things you make (clothes, art, crafts)',
        'Things you collect from nature (stones, sand, thatch, herbs)',
        'Things you process (honey, dairy products, flour)',
        'Other'
    )
)

Q11=my_form.selectbox(
    'Only for those who said they get money from providing a service, what kind of services do you MAINLY provide (get most money from)?',
    (
        'not applicable',
        'Personal services (hairdressers, massage, etc.)',
        'Telecommunications/IT',
        'Financial services ',
        'Transport',
        'Hospitality Accommodation, restaurants, etc.',
        'Information/research',
        'Technical mechanic, etc.',
        'Educational/child care',
        'Health services traditional healer etc.',
        'Legal services','Security','Other, specify'
    )
)

Q12=my_form.selectbox(
    'In the past 12 months, have you sent money to someone in a different place within the country or outside of Tanzania?',
    (
        'Yes',
        'No'
    )
)

Q13=my_form.selectbox(
    'When did you last send money?',
    (
        'not applicable',
        'Yesterday/today',
        'In the past 7 days',
        'In the past 30 days',
        'In the past 90 days',
        'More than 90 days ago but less than 6 months ago',
        '6 months or longer ago'
    )
)

Q14=my_form.selectbox(
    'In the past 12 months, have you received money from someone in a different place within the country or from outside the country?',
    (
        'Yes',
        'No'
    )
)

Q15=my_form.selectbox(
    'When did you last receive money?',
    (
        'not applicable',
        'Yesterday/today',
        'In the past 7 days',
        'In the past 30 days',
        'In the past 90 days',
        'More than 90 days ago but less than 6 months ago',
        '6 months or longer ago'
    )
)

Q16=my_form.selectbox(
    'In the past 12 months, how often did you use mobile money for purchases of goods and/or services?',
    (
        'not applicable',
        'Never',
        'Daily',
        'Weekly',
        'Monthly',
        'Less often than monthly'
    )
)

Q17=my_form.selectbox(
    'In the past 12 months, how often did you use mobile money for paying your bills?',
    (
        'not applicable',
        'Never',
        'Daily',
        'Weekly',
        'Monthly',
        'Less often than monthly'
    )
)

Q18=my_form.selectbox(
    'Literacy in Kiswahili',
    (
        'Can read and write',
        'Can read only',
        'Can write only',
        'Can neither read nor write',
        'Refused to read'
    )
)

Q19=my_form.selectbox(
    'Literacy in English',
    (
        'Can read and write',
        'Can read only',
        'Can write only',
        'Can neither read nor write',
        'Refused to read'
    )
)

#Latitude_and_Longitude==my_form.text_input('Where do you live?')

# Latitude=my_form.number_input('Latitude')

# Longitude=my_form.number_input('Longitude')

mobile_money=my_form.selectbox(
    'Do you use mobile money?',
    (
        'Yes',
        'No'
    )
)

savings=my_form.selectbox(
    'Do you save?',
    (
        'Yes',
        'No'
    )
)

borrowing=my_form.selectbox(
    'Do you borrow?',
    (
        'Yes',
        'No'
    )
)

insurance=my_form.selectbox(
    'Do you have insurance?',
    (
        'Yes',
        'No'
    )
)

#mobile_money_classification=my_form.selectbox('')

submit = my_form.form_submit_button(label="Make Prediction")


# load the model and one-hot-encoder and scaler

# with open(
#     join(dirname(realpath(__file__)), "model/finalized_model.sav"), "rb") as fm :
#     model = joblib.load(fm)

# with open(join(dirname(realpath(__file__)), "preprocessing/MinMaxScaler.sav"), "rb") as m:
#     scaler = joblib.load(m)


# with open(
#     join(dirname(realpath(__file__)), "preprocessing/one-hot-encoder.sav"), "rb") as o:
#     one_hot_encoder = joblib.load(o)


model = pickle.load(open("model/group_07_model2.sav", "rb"))
# scaler = pickle.load(open("preprocessing/MinMaxScaler.sav", "rb"))


# result dictionary
result_dic = {
    0: "no mobile money and no other financial service (saving, borrowing, insurance)",
    1: "no mobile money, but at least one other financial service",
    2: "mobile money only",
    3: "mobile money and at least one other financial service",
   
}


@st.cache
# function to clean and tranform the input
def preprocessing_data(data):

    # For other variables let's use one-hot-encoder
    multi_categorical_variables = [
        "Q3",
        "Q4",
        "Q5",
        "Q9",
        "Q10",
        "Q11",
        "Q13",
        "Q14",
        "Q15",
        "Q16",
        "Q17",
        "Q18",
        "Q19"
    ]

    multi_categorical_data = data[multi_categorical_variables]

    # multi_categorical_data = one_hot_enc.transform(multi_categorical_data)
    data = pd.get_dummies(data, prefix_sep='_', columns = multi_categorical_variables)



    data = data.to_numpy()

    final_data = np.concatenate([data, multi_categorical_data], axis=1)

    # final_data = scaler.transform(final_data)

    return final_data


if submit:

    # collect inputs
    input = {
        "Q1": Q1,
        "Q2": func2(Q2),
        "Q3": func3(Q3),
        "Q4": func4(Q4),
        "Q5": func5(Q5),
        "Q6": func(Q6),
        "Q7": func(Q7),
        "Q8_1": func(Q8_1),
        "Q8_2": func(Q8_2),
        "Q8_3": func(Q8_3),
        "Q8_4": func(Q8_4),
        "Q8_5": func(Q8_5),
        "Q8_6": func(Q8_6),
        "Q8_7": func(Q8_7),
        "Q8_8": func(Q8_8),
        "Q8_9": func(Q8_9),
        "Q8_10": func(Q8_10),
        "Q8_11": func(Q8_11),
        "Q9": func9(Q9),
        "Q10": func10(Q10),
        "Q11": func11(Q11),
        "Q12": func(Q12),
        "Q13": func13(Q13),
        "Q14": func(Q14),
        "Q15": func15(Q15),
        "Q16": func16(Q16),
        "Q17": func17(Q17),
        "Q18": func18(Q18),
        "Q19": func10(Q19),
        "mobile_money": func(mobile_money),
        "savings": func(savings),
        "borrowing": func(borrowing),
        "insurance": func(insurance)

    }

    # Create a DataFrame
    data = pd.DataFrame(input, index=[0])
    
    # st.write(data.shape)
    # clean and transform input
    # transformed_data = preprocessing_data(
    #     data=data
    # )
    
    # perform prediction
    prediction = model.predict(data)
    output = int(prediction[0])

    probas = model.predict_proba(data)
    probability = "{:.2}".format(float(probas[:,output]))

    # Display results of the prediction
    st.header("Results")

    if output == 0:
        st.write("There is a probability of no mobile money and no other financial service is  {}".format(probability))

    elif output == 1:
        st.write("There is a probability of no mobile money but at least one other financial service is  {}".format(probability))

    elif output == 2:
        st.write("There is a probability mobile money only is {}".format(probability))   

    else:
        st.write("There is a probability mobile money and at least one other financial service is  {}".format(probability))    

     

    st.write(" COnclusion, this individual most likely uses  {} ".format(result_dic[output]))

#rl = "https://twitter.com/Davis_McDavid"
st.write("All rights are preserved  ❤️ by Group7")