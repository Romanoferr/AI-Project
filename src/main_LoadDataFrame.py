import pandas as pd

'''
Data Set Information:
    Gender: Feature, Categorical, "Gender"
    Age : Feature, Continuous, "Age"
    Height: Feature, Continuous
    Weight: Feature Continuous
    family_history_with_overweight: Feature, Binary, " Has a family member suffered or suffers from overweight? "
    FAVC : Feature, Binary, " Do you eat high caloric food frequently? "
    FCVC : Feature, Integer, " Do you usually eat vegetables in your meals? "
    NCP : Feature, Continuous, " How many main meals do you have daily? "
    CAEC : Feature, Categorical, " Do you eat any food between meals? "
    SMOKE : Feature, Binary, " Do you smoke? "
    CH2O: Feature, Continuous, " How much water do you drink daily? "
    SCC: Feature, Binary, " Do you monitor the calories you eat daily? "
    FAF: Feature, Continuous, " How often do you have physical activity? "
    TUE : Feature, Integer, " How much time do you use technological devices such as cell phone, videogames, television, computer and others? "
    CALC : Feature, Categorical, " How often do you drink alcohol? "
    MTRANS : Feature, Categorical, " Which transportation do you usually use? "
    NObeyesdad : Target, Categorical, "Obesity level"
    
'''


def load_data():
    data = pd.read_csv('../dataset/ObesityDataSet_raw_and_data_sinthetic.csv')
    dataframe = pd.DataFrame(data)
    print(dataframe)
    print(dataframe.dtypes)

    return dataframe


if __name__ == '__main__':
    load_data()
