import streamlit as st

# Sample risk calculation functions (to be implemented according to your guidelines)
def calculate_cardio_risk(age, systolic_bp, smoker, cholesterol):
    if smoker and systolic_bp > 140:
        return "High"
    return "Moderate"

def calculate_diabetes_risk(bmi, age, family_history, fasting_glucose, hba1c):
    if fasting_glucose > 126 or hba1c > 6.5:
        return "High"
    return "Moderate"

def calculate_copd_risk(smoking_years, age, fev1, exacerbations_last_year):
    if smoking_years > 20 and exacerbations_last_year > 2:
        return "High"
    return "Moderate"

def calculate_asthma_risk(frequency_of_symptoms, nighttime_symptoms, inhaler_use, fev1, eosinophil_count):
    if frequency_of_symptoms > 4 or nighttime_symptoms > 2:
        return "High"
    return "Moderate"

# AI Assistant Function with Evidence-Based Protocols
def ai_assistant_response(results):
    protocols = {
        "Cardiovascular": {
            "High": (
                "1. **Lifestyle Modifications**: Implement a heart-healthy diet (e.g., DASH diet), exercise regularly (at least 150 minutes/week), "
                "and achieve a healthy weight. \n"
                "2. **Medication Management**: Consider starting antihypertensive medication, statins, and possibly antiplatelet therapy based on risk factors per AHA guidelines. \n"
                "3. **Monitoring**: Regular blood pressure and lipid profile checks every 3-6 months."
            ),
            "Moderate": (
                "1. **Lifestyle Changes**: Encourage a balanced diet rich in fruits, vegetables, and whole grains. \n"
                "2. **Follow-Up**: Reassess risk factors annually and monitor blood pressure and cholesterol. \n"
                "3. **Education**: Provide resources on smoking cessation and stress management."
            )
        },
        "Diabetes": {
            "High": (
                "1. **Dietary Changes**: Refer to a registered dietitian for personalized meal planning. Focus on low glycemic index foods. \n"
                "2. **Medication**: Start metformin and consider additional agents based on patient-specific factors. \n"
                "3. **Monitoring**: Tight glucose control (HbA1c < 7%) with quarterly checks and regular foot, eye, and kidney assessments as per ADA guidelines."
            ),
            "Moderate": (
                "1. **Dietary Modifications**: Recommend regular meals with balanced carbohydrates. \n"
                "2. **Exercise**: Encourage at least 150 minutes of moderate activity per week. \n"
                "3. **Follow-Up**: Monitor HbA1c every 6 months and educate on recognizing symptoms of hypoglycemia."
            )
        },
        "COPD": {
            "High": (
                "1. **Smoking Cessation**: Immediate cessation program and consider pharmacotherapy (e.g., varenicline). \n"
                "2. **Pulmonary Rehabilitation**: Referral to a program that includes exercise training, health education, and breathing techniques. \n"
                "3. **Medications**: Long-acting bronchodilators and inhaled corticosteroids as per GOLD guidelines. \n"
                "4. **Monitoring**: Regular follow-up every 3 months to assess lung function and exacerbation management."
            ),
            "Moderate": (
                "1. **Smoking Cessation**: Strongly advise against smoking and consider resources for quitting. \n"
                "2. **Medications**: Prescribe short-acting bronchodilators as needed. \n"
                "3. **Education**: Provide inhaler technique education and action plan for exacerbations."
            )
        },
        "Asthma": {
            "High": (
                "1. **Personalized Asthma Action Plan**: Develop and provide education on how to use rescue inhalers effectively. \n"
                "2. **Controller Medications**: Initiate daily inhaled corticosteroids or leukotriene receptor antagonists. \n"
                "3. **Follow-Up**: Regular visits every 1-3 months until asthma is well controlled, then reassess every 3-6 months."
            ),
            "Moderate": (
                "1. **Education**: Teach the patient about recognizing and avoiding triggers. \n"
                "2. **Medication**: Assess the need for daily medication based on symptom frequency. \n"
                "3. **Monitoring**: Use peak flow meters to monitor lung function at home."
            )
        }
    }

    combined_response = []
    for condition, risk in results.items():
        if condition in protocols:
            combined_response.append(f"{condition} ({risk} Risk):\n{protocols[condition][risk]}")
    
    return "\n\n".join(combined_response)

# Educational Resource Links
def get_educational_resources(condition):
    resources = {
        "Cardiovascular": "https://medlineplus.gov/cardiovasculardiseases.html",
        "Diabetes": "https://medlineplus.gov/diabetes.html",
        "COPD": "https://medlineplus.gov/copd.html",
        "Asthma": "https://medlineplus.gov/asthma.html",
    }
    return resources.get(condition, None)

# Initialize Streamlit app
st.title("Chronic Care Management Tool")
st.write("This application helps assess risks for various chronic conditions and provides personalized care plans.")

# Initialize session state for results
if 'results' not in st.session_state:
    st.session_state['results'] = {}

# Risk Assessment Tabs
tab1, tab2, tab3, tab4, tab5 = st.tabs(["Cardiovascular Risk", "Diabetes Risk", "COPD Risk", "Asthma Risk", "Unified Care Plan", "AI Assistant"])

# Cardiovascular Risk Tab
with tab1:
    st.header("Cardiovascular Risk Assessment")
    age = st.number_input("Age", min_value=18, max_value=120, value=50, key="age")
    systolic_bp = st.number_input("Systolic Blood Pressure (mmHg)", min_value=80, max_value=200, value=120, key="systolic_bp")
    cholesterol = st.number_input("Cholesterol (mg/dL)", min_value=150, max_value=300, value=200, key="cholesterol")
    smoker = st.checkbox("Smoker", key="smoker")

    if st.button("Calculate Cardiovascular Risk"):
        cardio_risk = calculate_cardio_risk(age, systolic_bp, smoker, cholesterol)
        st.write(f"**Cardiovascular Risk Level**: {cardio_risk}")
        st.session_state['results']["Cardiovascular"] = cardio_risk
        
        # Educational Resource Link
        resource_link = get_educational_resources("Cardiovascular")
        st.markdown(f"[Learn more about Cardiovascular Diseases]({resource_link})", unsafe_allow_html=True)

# Diabetes Risk Tab
with tab2:
    st.header("Diabetes Risk Assessment")
    bmi = st.number_input("BMI", min_value=10.0, max_value=50.0, value=25.0, key="bmi_diabetes")
    age_diabetes = st.number_input("Age", min_value=18, max_value=100, value=30, key="age_diabetes")
    family_history = st.checkbox("Family History of Diabetes", key="family_history")
    fasting_glucose = st.number_input("Fasting Glucose (mg/dL)", min_value=50, max_value=300, value=100, key="fasting_glucose")
    hba1c = st.number_input("HbA1c (%)", min_value=4.0, max_value=15.0, value=5.0, key="hba1c")

    if st.button("Calculate Diabetes Risk"):
        diabetes_risk = calculate_diabetes_risk(bmi, age_diabetes, family_history, fasting_glucose, hba1c)
        st.write(f"**Diabetes Risk Level**: {diabetes_risk}")
        st.session_state['results']["Diabetes"] = diabetes_risk

        # Educational Resource Link
        resource_link = get_educational_resources("Diabetes")
        st.markdown(f"[Learn more about Diabetes]({resource_link})", unsafe_allow_html=True)

# COPD Risk Tab
with tab3:
    st.header("COPD Risk Assessment")
    smoking_years = st.number_input("Years Smoked", min_value=0, max_value=100, value=10, key="smoking_years")
    age_copd = st.number_input("Age", min_value=40, max_value=100, value=65, key="age_copd")
    fev1 = st.number_input("FEV1 (%)", min_value=20, max_value=100, value=80, key="fev1_copd")
    exacerbations_last_year = st.number_input("Exacerbations Last Year", min_value=0, max_value=10, value=1, key="exacerbations_last_year")

    if st.button("Calculate COPD Risk"):
        copd_risk = calculate_copd_risk(smoking_years, age_copd, fev1, exacerbations_last_year)
        st.write(f"**COPD Risk Level**: {copd_risk}")
        st.session_state['results']["COPD"] = copd_risk

        # Educational Resource Link
        resource_link = get_educational_resources("COPD")
        st.markdown(f"[Learn more about COPD]({resource_link})", unsafe_allow_html=True)

# Asthma Risk Tab
with tab4:
    st.header("Asthma Risk Assessment")
    frequency_of_symptoms = st.number_input("Symptoms (per week)", min_value=0, max_value=14, value=2, key="frequency_of_symptoms")
    nighttime_symptoms = st.number_input("Nighttime Symptoms (per month)", min_value=0, max_value=10, value=1, key="nighttime_symptoms")
    inhaler_use = st.number_input("Inhaler Use (times/week)", min_value=0, max_value=14, value=2, key="inhaler_use")
    fev1_asthma = st.number_input("FEV1 (%)", min_value=20, max_value=100, value=80, key="fev1_asthma")
    eosinophil_count = st.number_input("Eosinophil Count (cells/µL)", min_value=0, max_value=1000, value=300, key="eosinophil_count")

    if st.button("Calculate Asthma Risk"):
        asthma_risk = calculate_asthma_risk(frequency_of_symptoms, nighttime_symptoms, inhaler_use, fev1_asthma, eosinophil_count)
        st.write(f"**Asthma Risk Level**: {asthma_risk}")
        st.session_state['results']["Asthma"] = asthma_risk

        # Educational Resource Link
        resource_link = get_educational_resources("Asthma")
        st.markdown(f"[Learn more about Asthma]({resource_link})", unsafe_allow_html=True)

# Unified Care Plan Tab
with tab5:
    st.header("Unified Care Plan")
    if st.session_state['results']:
        care_plan = ai_assistant_response(st.session_state['results'])
        st.write("**Personalized Care Plan**:\n" + care_plan)
    else:
        st.write("Please complete risk assessments in previous tabs first.")

# AI Assistant Tab
with tab6:
    st.header("AI Assistant")
    if st.session_state['results']:
        response = ai_assistant_response(st.session_state['results'])
        st.write("**AI Generated Recommendations**:\n" + response)
    else:
        st.write("Please complete risk assessments in previous tabs first.")

# Run the app
if __name__ == "__main__":
    st.write("This app is running and is ready for use!")
