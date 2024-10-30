import streamlit as st

# Sample risk calculation functions (to be implemented according to your guidelines)
def calculate_cardio_risk(age, systolic_bp, smoker, cholesterol):
    # Example logic for cardiovascular risk calculation
    if smoker and systolic_bp > 140:
        return "High"
    return "Moderate"

def calculate_diabetes_risk(bmi, age, family_history, fasting_glucose, hba1c):
    # Example logic for diabetes risk calculation
    if fasting_glucose > 126 or hba1c > 6.5:
        return "High"
    return "Moderate"

def calculate_copd_risk(smoking_years, age, fev1, exacerbations_last_year):
    # Example logic for COPD risk calculation
    if smoking_years > 20 and exacerbations_last_year > 2:
        return "High"
    return "Moderate"

def calculate_asthma_risk(frequency_of_symptoms, nighttime_symptoms, inhaler_use, fev1, eosinophil_count):
    # Example logic for asthma risk calculation
    if frequency_of_symptoms > 4 or nighttime_symptoms > 2:
        return "High"
    return "Moderate"

# AI Assistant Function
def ai_assistant_response(query, results):
    responses = []

    for condition, risk in results.items():
        if condition == "Cardiovascular":
            if risk == "High":
                responses.append(
                    "### Cardiovascular Risk Management\n"
                    "- **Management**: Initiate lifestyle changes including a heart-healthy diet, regular physical activity, and weight management. Consider pharmacotherapy for blood pressure and cholesterol management as per AHA/ACC guidelines.\n"
                    "- **Follow-Up**: Schedule regular follow-up visits every 3-6 months to monitor blood pressure, cholesterol levels, and overall cardiovascular health.\n"
                    "- **Resources**: [AHA Guidelines](https://www.heart.org/en/professional/quality-improvement/aha-quality-improvement-guidelines)\n"
                )
            elif risk == "Moderate":
                responses.append(
                    "### Cardiovascular Risk Management\n"
                    "- **Management**: Encourage patients to adopt heart-healthy lifestyle changes such as reducing sodium intake, increasing physical activity, and maintaining a healthy weight. Monitor blood pressure and cholesterol regularly.\n"
                    "- **Follow-Up**: Consider annual check-ups to assess risk factors.\n"
                )

        elif condition == "Diabetes":
            if risk == "High":
                responses.append(
                    "### Diabetes Risk Management\n"
                    "- **Management**: Recommend a structured diabetes management plan including dietary modifications (e.g., DASH diet), regular blood glucose monitoring, and potential initiation of pharmacotherapy (e.g., Metformin) based on ADA guidelines.\n"
                    "- **Follow-Up**: Schedule follow-ups every 3 months to adjust treatment based on glucose levels and HbA1c.\n"
                    "- **Resources**: [ADA Standards of Medical Care](https://www.diabetes.org/clinical-resources/standards-of-care)\n"
                )
            elif risk == "Moderate":
                responses.append(
                    "### Diabetes Risk Management\n"
                    "- **Management**: Advise patients on lifestyle changes including increased physical activity and dietary adjustments to reduce sugar and carbohydrate intake.\n"
                    "- **Follow-Up**: Regular monitoring of blood glucose levels and annual HbA1c testing.\n"
                )

        elif condition == "COPD":
            if risk == "High":
                responses.append(
                    "### COPD Risk Management\n"
                    "- **Management**: Immediate initiation of smoking cessation programs and pulmonary rehabilitation. Consider medications such as bronchodilators and corticosteroids as per GOLD guidelines.\n"
                    "- **Follow-Up**: Schedule regular follow-ups every 1-3 months to monitor lung function and exacerbation history.\n"
                    "- **Resources**: [GOLD Guidelines](https://goldcopd.org/gold-reports/)\n"
                )
            elif risk == "Moderate":
                responses.append(
                    "### COPD Risk Management\n"
                    "- **Management**: Encourage smoking cessation and prescribe bronchodilators as needed. Educate patients on recognizing early signs of exacerbation.\n"
                    "- **Follow-Up**: Biannual follow-ups to assess lung function and medication effectiveness.\n"
                )

        elif condition == "Asthma":
            if risk == "High":
                responses.append(
                    "### Asthma Risk Management\n"
                    "- **Management**: Optimize medication adherence by prescribing inhaled corticosteroids and educating patients about proper inhaler technique. Develop a comprehensive asthma action plan.\n"
                    "- **Follow-Up**: Schedule visits every 1-3 months to reassess control and medication needs.\n"
                    "- **Resources**: [AAFA Guidelines](https://www.aafa.org)\n"
                )
            elif risk == "Moderate":
                responses.append(
                    "### Asthma Risk Management\n"
                    "- **Management**: Reinforce the importance of adherence to maintenance therapy and review the asthma action plan regularly.\n"
                    "- **Follow-Up**: Schedule follow-ups every 3-6 months to monitor asthma control.\n"
                )

    return "\n\n".join(responses)

# Initialize Streamlit app
st.title("Chronic Care Management Tool")
st.write("This application helps assess risks for various chronic conditions and provides personalized care plans.")

# Initialize session state for results
if 'results' not in st.session_state:
    st.session_state['results'] = {}

# Risk Assessment Tabs
tab1, tab2, tab3, tab4, tab5 = st.tabs(["Cardiovascular Risk", "Diabetes Risk", "COPD Risk", "Asthma Risk", "Unified Care Plan"])

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

# COPD Risk Tab
with tab3:
    st.header("COPD Risk Assessment")
    smoking_years = st.number_input("Years Smoking", min_value=0, max_value=50, value=10, key="smoking_years")
    age_copd = st.number_input("Age", min_value=18, max_value=100, value=30, key="age_copd")
    fev1 = st.number_input("FEV1 (%)", min_value=20, max_value=100, value=80, key="fev1")
    exacerbations_last_year = st.number_input("Exacerbations Last Year", min_value=0, max_value=10, value=1, key="exacerbations_last_year")

    if st.button("Calculate COPD Risk"):
        copd_risk = calculate_copd_risk(smoking_years, age_copd, fev1, exacerbations_last_year)
        st.write(f"**COPD Risk Level**: {copd_risk}")
        st.session_state['results']["COPD"] = copd_risk

# Asthma Risk Tab
with tab4:
    st.header("Asthma Risk Assessment")
    frequency_of_symptoms = st.slider("Frequency of Symptoms (0-7 days/week)", 0, 7, 2, key="frequency_of_symptoms")
    nighttime_symptoms = st.slider("Nighttime Symptoms (0-7 days/week)", 0, 7, 1, key="nighttime_symptoms")
    inhaler_use = st.slider("Inhaler Use (0-7 days/week)", 0, 7, 2, key="inhaler_use")
    fev1_asthma = st.number_input("FEV1 (%) - Asthma", min_value=20, max_value=100, value=80, key="fev1_asthma")
    eosinophil_count = st.number_input("Eosinophil Count (cells/μL)", min_value=0, max_value=1000, value=300, key="eosinophil_count")

    if st.button("Calculate Asthma Risk"):
        asthma_risk = calculate_asthma_risk(frequency_of_symptoms, nighttime_symptoms, inhaler_use, fev1_asthma, eosinophil_count)
        st.write(f"**Asthma Risk Level**: {asthma_risk}")
        st.session_state['results']["Asthma"] = asthma_risk

# Unified Care Plan Tab
with tab5:
    st.header("Unified Care Plan")
    if st.session_state['results']:
        st.write("### Care Plan Based on Risk Levels")
        for condition, risk in st.session_state['results'].items():
            st.write(f"#### {condition} - {risk} Risk")
            if risk == "High":
                st.write(f"- **Management Plan for {condition}**: Intensive management with medication adjustments and close monitoring as per guidelines.")
                st.write("- **Follow-Up**: Regular visits for monitoring vital signs and medication adherence.")
                st.write("- **Expected Outcomes**: Reduced symptoms and improved quality of life.")
            elif risk == "Moderate":
                st.write(f"- **Management Plan for {condition}**: Lifestyle modifications and regular monitoring.")
                st.write("- **Follow-Up**: Bi-monthly check-ups to monitor condition status.")
                st.write("- **Expected Outcomes**: Stabilized condition and prevention of complications.")
            else:
                st.write(f"- **Management Plan for {condition}**: Routine monitoring and preventive measures.")
                st.write("- **Follow-Up**: Annual check-ups to ensure ongoing health maintenance.")
                st.write("- **Expected Outcomes**: Long-term health stability.")

# AI Assistant Tab
with st.expander("AI Assistant (Multidisciplinary Team) for Healthcare Provider Guidance", expanded=True):
    st.header("AI Assistant for Risk Management and Care Guidance")
    query = st.text_input("Ask the AI Assistant about risk management, personalized care, or guidelines:")
    if st.button("Get AI Assistance"):
        if st.session_state['results']:
            ai_response = ai_assistant_response(query, st.session_state['results'])
            st.write(ai_response)
        else:
            st.write("Please complete risk assessments in previous tabs first.")

# Educational Resources Section
st.write("---")
st.header("Educational Resources")
st.write("Here are some trusted resources for chronic disease management:")
st.write("- [American Diabetes Association (ADA)](https://www.diabetes.org)")
st.write("- [American Heart Association (AHA)](https://www.heart.org)")
st.write("- [Global Initiative for Chronic Obstructive Lung Disease (GOLD)](https://goldcopd.org)")
st.write("- [Asthma and Allergy Foundation of America (AAFA)](https://www.aafa.org)")

# Footer Section
st.write("---")
st.header("Feedback and Support")
st.write("We value your feedback! Please let us know how we can improve this application or if you need further assistance.")
feedback = st.text_area("Your Feedback:", height=100)
if st.button("Submit Feedback"):
    st.success("Thank you for your feedback!")
