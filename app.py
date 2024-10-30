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

# AI Assistant Function for Healthcare Provider Guidance
def ai_assistant_response(condition, risk):
    if condition == "Cardiovascular":
        if risk == "High":
            return (
                "### Cardiovascular Recommendations\n"
                "- **Management**: Initiate lifestyle changes including a heart-healthy diet (e.g., DASH diet), regular physical activity (150 minutes/week), and weight management.\n"
                "- **Pharmacotherapy**: Consider starting antihypertensive agents and statins based on individual patient risk profiles, following AHA/ACC guidelines.\n"
                "- **Follow-Up**: Schedule follow-ups every 3-6 months to monitor blood pressure, cholesterol levels, and overall cardiovascular health.\n"
                "- **Resources**: [AHA Guidelines](https://www.heart.org/en/professional/quality-improvement/aha-quality-improvement-guidelines)\n"
                "- **Clinical Studies**: Refer to studies supporting lifestyle interventions and medication efficacy in high-risk patients."
            )
        else:
            return (
                "### Cardiovascular Recommendations\n"
                "- **Management**: Encourage heart-healthy lifestyle changes, such as reducing sodium intake and increasing physical activity.\n"
                "- **Monitoring**: Assess risk factors annually, with a focus on blood pressure and cholesterol levels.\n"
            )

    elif condition == "Diabetes":
        if risk == "High":
            return (
                "### Diabetes Recommendations\n"
                "- **Management**: Implement a structured diabetes management plan that includes dietary modifications (e.g., Mediterranean diet) and regular glucose monitoring.\n"
                "- **Pharmacotherapy**: Consider starting Metformin and assess the need for additional agents as per ADA guidelines.\n"
                "- **Follow-Up**: Schedule follow-ups every 3 months to adjust treatment based on glucose levels and HbA1c.\n"
                "- **Resources**: [ADA Standards of Medical Care](https://www.diabetes.org/clinical-resources/standards-of-care)\n"
                "- **Clinical Studies**: Review recent studies on the effectiveness of lifestyle interventions and medications."
            )
        else:
            return (
                "### Diabetes Recommendations\n"
                "- **Management**: Advise on lifestyle changes focusing on increased physical activity and dietary modifications to reduce sugar intake.\n"
                "- **Monitoring**: Regular monitoring of glucose levels and annual HbA1c testing."
            )

    elif condition == "COPD":
        if risk == "High":
            return (
                "### COPD Recommendations\n"
                "- **Management**: Initiate smoking cessation programs and pulmonary rehabilitation immediately. Consider bronchodilators and inhaled corticosteroids based on GOLD guidelines.\n"
                "- **Follow-Up**: Schedule follow-ups every 1-3 months to monitor lung function and exacerbation history.\n"
                "- **Resources**: [GOLD Guidelines](https://goldcopd.org/gold-reports/)\n"
                "- **Clinical Studies**: Look into studies emphasizing the role of smoking cessation in reducing COPD progression."
            )
        else:
            return (
                "### COPD Recommendations\n"
                "- **Management**: Encourage smoking cessation and prescribe bronchodilators as needed. Educate patients on recognizing early signs of exacerbation.\n"
                "- **Follow-Up**: Schedule biannual follow-ups to assess lung function and treatment effectiveness."
            )

    elif condition == "Asthma":
        if risk == "High":
            return (
                "### Asthma Recommendations\n"
                "- **Management**: Optimize medication adherence by prescribing inhaled corticosteroids and developing a comprehensive asthma action plan. Ensure proper inhaler technique.\n"
                "- **Follow-Up**: Schedule visits every 1-3 months to reassess asthma control and adjust medication as needed.\n"
                "- **Resources**: [AAFA Guidelines](https://www.aafa.org)\n"
                "- **Clinical Studies**: Review evidence on the benefits of adherence to inhaled therapies in reducing exacerbations."
            )
        else:
            return (
                "### Asthma Recommendations\n"
                "- **Management**: Reinforce the importance of adherence to maintenance therapy and review the asthma action plan regularly.\n"
                "- **Follow-Up**: Schedule follow-ups every 3-6 months to monitor asthma control."
            )

# Create patient-friendly care plan based on risk levels
def patient_friendly_care_plan(results):
    care_plan = []

    for condition, risk in results.items():
        care_steps = f"### Care Plan for {condition} - Risk Level: {risk}\n"
        
        if risk == "High":
            care_steps += (
                "- **Step 1**: Schedule an appointment with your healthcare provider within the next week.\n"
                "- **Step 2**: Start a heart-healthy diet, focusing on fruits, vegetables, whole grains, and lean proteins. Here’s a helpful [video on heart-healthy diets](https://www.youtube.com/watch?v=example1).\n"
                "- **Step 3**: Increase your physical activity to at least 150 minutes of moderate exercise per week. Here’s a [guide to starting exercise](https://www.youtube.com/watch?v=example2).\n"
                "- **Step 4**: Monitor your blood pressure and cholesterol levels as advised. Use this [blood pressure log template](https://example.com/log-template).\n"
                "- **Step 5**: Join a support group or online community for motivation. Here’s a list of resources: [Support Groups](https://example.com/support-groups).\n"
            )
        elif risk == "Moderate":
            care_steps += (
                "- **Step 1**: Schedule a follow-up appointment within the next month.\n"
                "- **Step 2**: Implement dietary changes focusing on reducing sodium and sugar intake. Check out this [diet tips video](https://www.youtube.com/watch?v=example3).\n"
                "- **Step 3**: Aim for at least 30 minutes of exercise most days of the week. Here’s a [simple exercise routine](https://www.youtube.com/watch?v=example4).\n"
                "- **Step 4**: Track your weight and blood pressure at home. Use this [tracking app](https://example.com/app).\n"
                "- **Step 5**: Learn more about your condition through these [educational resources](https://example.com/education).\n"
            )
        else:
            care_steps += (
                "- **Step 1**: Schedule an annual check-up with your healthcare provider.\n"
                "- **Step 2**: Maintain a balanced diet and active lifestyle. Here’s a [general health tips video](https://www.youtube.com/watch?v=example5).\n"
                "- **Step 3**: Monitor your health regularly, including blood pressure and weight. Consider using a [health app](https://example.com/app).\n"
                "- **Step 4**: Stay informed about your health condition through reliable sources. Here are some [trusted websites](https://example.com/trusted-websites).\n"
            )
        
        care_plan.append(care_steps)

    return "\n\n".join(care_plan)

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

        # Educational Resources
        st.write("### Educational Resources for Healthcare Providers")
        st.write("- [AHA Guidelines on Cardiovascular Disease Management (PDF)](https://www.heart.org/-/media/Files/Health-Topics/Hypertension/2022-Hypertension-Clinical-Practice-Guidelines-Executive-Summary.pdf)")

# Diabetes Risk Tab
with tab2:
    st.header("Diabetes Risk Assessment")
    bmi = st.number_input("BMI", min_value=10.0, max_value=50.0, value=25.0, key="bmi")
    age = st.number_input("Age", min_value=18, max_value=120, value=50, key="diabetes_age")
    family_history = st.checkbox("Family History of Diabetes", key="family_history")
    fasting_glucose = st.number_input("Fasting Glucose (mg/dL)", min_value=50, max_value=300, value=100, key="fasting_glucose")
    hba1c = st.number_input("HbA1c (%)", min_value=4.0, max_value=15.0, value=5.5, key="hba1c")

    if st.button("Calculate Diabetes Risk"):
        diabetes_risk = calculate_diabetes_risk(bmi, age, family_history, fasting_glucose, hba1c)
        st.write(f"**Diabetes Risk Level**: {diabetes_risk}")
        st.session_state['results']["Diabetes"] = diabetes_risk
        st.write(ai_assistant_response("Diabetes", diabetes_risk))

        # Educational Resources
        st.write("### Educational Resources for Healthcare Providers")
        st.write("- [ADA Standards of Medical Care in Diabetes (PDF)](https://diabetesjournals.org/care/article/43/Supplement_1/S1/Standards-of-Medical-Care-in-Diabetes-2020)")

# COPD Risk Tab
with tab3:
    st.header("COPD Risk Assessment")
    smoking_years = st.number_input("Years of Smoking", min_value=0, max_value=50, value=10, key="smoking_years")
    age = st.number_input("Age", min_value=18, max_value=120, value=50, key="copd_age")
    fev1 = st.number_input("FEV1 (%)", min_value=20, max_value=100, value=80, key="fev1")
    exacerbations_last_year = st.number_input("Exacerbations in Last Year", min_value=0, max_value=10, value=1, key="exacerbations")

    if st.button("Calculate COPD Risk"):
        copd_risk = calculate_copd_risk(smoking_years, age, fev1, exacerbations_last_year)
        st.write(f"**COPD Risk Level**: {copd_risk}")
        st.session_state['results']["COPD"] = copd_risk
        st.write(ai_assistant_response("COPD", copd_risk))

        # Educational Resources
        st.write("### Educational Resources for Healthcare Providers")
        st.write("- [GOLD Guidelines for the Management of COPD (PDF)](https://goldcopd.org/wp-content/uploads/2020/11/GOLD-2020-Report-Updated-2020-11-12-3.pdf)")

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
        st.write(ai_assistant_response("Asthma", asthma_risk))

        # Educational Resources
        st.write("### Educational Resources for Healthcare Providers")
        st.write("- [AAFA Asthma Management Guidelines (PDF)](https://aafa.org/media/2356/aafa-asthma-management-guidelines-2020.pdf)")

# Unified Care Plan Tab
with tab5:
    st.header("Unified Care Plan")
    if st.session_state['results']:
        st.write("### Suggested Patient-Friendly Care Plan")
        patient_care_plan = patient_friendly_care_plan(st.session_state['results'])
        st.write(patient_care_plan)

# Footer Section
st.write("---")
st.header("Feedback and Support")
st.write("We value your feedback! Please let us know how we can improve this application or if you need further assistance.")
feedback = st.text_area("Your Feedback:", height=100)
if st.button("Submit Feedback"):
    st.success("Thank you for your feedback!")
