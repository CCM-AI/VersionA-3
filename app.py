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

# AI Assistant Function with Evidence-Based Recommendations
def ai_assistant_response(results):
    responses = []

    for condition, risk in results.items():
        if condition == "Cardiovascular":
            if risk == "High":
                responses.append(
                    "### Cardiovascular Risk Management\n"
                    "- **Management**: Implement lifestyle modifications, including a diet rich in fruits, vegetables, whole grains, and lean proteins. Recommend the Mediterranean or DASH diet. Consider starting statins for cholesterol management and antihypertensive medications as per AHA/ACC guidelines. Monitor blood pressure and lipid profiles every 3-6 months.\n"
                    "- **Evidence**: Refer to the 2023 AHA/ACC Guideline on the Primary Prevention of Cardiovascular Disease.\n"
                    "- **Resources**: [AHA Guidelines](https://www.heart.org/en/professional/quality-improvement/aha-quality-improvement-guidelines), [JNC 8 Hypertension Guidelines](https://www.ncbi.nlm.nih.gov/pubmed/24695196)\n"
                )
            elif risk == "Moderate":
                responses.append(
                    "### Cardiovascular Risk Management\n"
                    "- **Management**: Recommend lifestyle changes focusing on reducing sodium intake (<2,300 mg/day) and increasing physical activity (at least 150 minutes/week). Schedule annual follow-ups to monitor risk factors. Consider pharmacotherapy if lifestyle changes are insufficient.\n"
                    "- **Evidence**: Refer to the 2023 AHA/ACC Guideline on the Primary Prevention of Cardiovascular Disease.\n"
                    "- **Resources**: [AHA Guidelines](https://www.heart.org/en/professional/quality-improvement/aha-quality-improvement-guidelines)\n"
                )

        elif condition == "Diabetes":
            if risk == "High":
                responses.append(
                    "### Diabetes Risk Management\n"
                    "- **Management**: Initiate a comprehensive diabetes management plan, including a structured dietary program (e.g., Mediterranean or DASH diet), regular blood glucose monitoring, and pharmacotherapy (Metformin as first-line treatment). Aim for HbA1c < 7%.\n"
                    "- **Evidence**: Follow the American Diabetes Association (ADA) Standards of Medical Care in Diabetes.\n"
                    "- **Resources**: [ADA Standards](https://www.diabetes.org/clinical-resources/standards-of-care)\n"
                )
            elif risk == "Moderate":
                responses.append(
                    "### Diabetes Risk Management\n"
                    "- **Management**: Advise on lifestyle modifications, emphasizing physical activity (150 min/week) and dietary changes to reduce simple sugars and refined carbs. Monitor HbA1c every 6 months.\n"
                    "- **Evidence**: Refer to the ADA Standards of Medical Care in Diabetes for risk stratification.\n"
                    "- **Resources**: [ADA Standards](https://www.diabetes.org/clinical-resources/standards-of-care)\n"
                )

        elif condition == "COPD":
            if risk == "High":
                responses.append(
                    "### COPD Risk Management\n"
                    "- **Management**: Implement a smoking cessation program and refer to pulmonary rehabilitation. Consider the use of long-acting bronchodilators and inhaled corticosteroids. Schedule regular follow-ups every 1-3 months to monitor lung function and exacerbation history.\n"
                    "- **Evidence**: Follow the Global Initiative for Chronic Obstructive Lung Disease (GOLD) guidelines.\n"
                    "- **Resources**: [GOLD Guidelines](https://goldcopd.org/gold-reports/)\n"
                )
            elif risk == "Moderate":
                responses.append(
                    "### COPD Risk Management\n"
                    "- **Management**: Encourage smoking cessation and prescribe bronchodilators as needed. Educate patients on recognizing early signs of exacerbation. Schedule follow-ups every 6 months.\n"
                    "- **Evidence**: Refer to GOLD guidelines for moderate COPD management strategies.\n"
                    "- **Resources**: [GOLD Guidelines](https://goldcopd.org/gold-reports/)\n"
                )

        elif condition == "Asthma":
            if risk == "High":
                responses.append(
                    "### Asthma Risk Management\n"
                    "- **Management**: Optimize medication adherence by prescribing inhaled corticosteroids and educating patients about proper inhaler technique. Develop a comprehensive asthma action plan. Consider referral for allergy testing if indicated.\n"
                    "- **Evidence**: Follow the National Asthma Education and Prevention Program (NAEPP) guidelines.\n"
                    "- **Resources**: [NAEPP Guidelines](https://www.nhlbi.nih.gov/health-topics/asthma)\n"
                )
            elif risk == "Moderate":
                responses.append(
                    "### Asthma Risk Management\n"
                    "- **Management**: Reinforce adherence to maintenance therapy and review the asthma action plan regularly. Monitor peak flow rates and symptoms.\n"
                    "- **Evidence**: Refer to NAEPP guidelines for moderate asthma management.\n"
                    "- **Resources**: [NAEPP Guidelines](https://www.nhlbi.nih.gov/health-topics/asthma)\n"
                )

    return "\n\n".join(responses)

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
    age = st.number_input("Age", min_value=0, max_value=120, value=30)
    systolic_bp = st.number_input("Systolic Blood Pressure", min_value=80, max_value=200, value=120)
    smoker = st.checkbox("Smoker")
    cholesterol = st.number_input("Cholesterol Level", min_value=100, max_value=300, value=180)
    
    if st.button("Calculate Risk"):
        risk = calculate_cardio_risk(age, systolic_bp, smoker, cholesterol)
        st.session_state.results["Cardiovascular"] = risk
        st.success(f"Cardiovascular Risk Level: {risk}")

# Diabetes Risk Tab
with tab2:
    st.header("Diabetes Risk Assessment")
    bmi = st.number_input("BMI", min_value=10, max_value=50, value=25)
    age = st.number_input("Age", min_value=0, max_value=120, value=30)
    family_history = st.checkbox("Family History of Diabetes")
    fasting_glucose = st.number_input("Fasting Glucose", min_value=70, max_value=300, value=100)
    hba1c = st.number_input("HbA1c", min_value=4.0, max_value=14.0, value=5.5)
    
    if st.button("Calculate Risk"):
        risk = calculate_diabetes_risk(bmi, age, family_history, fasting_glucose, hba1c)
        st.session_state.results["Diabetes"] = risk
        st.success(f"Diabetes Risk Level: {risk}")

# COPD Risk Tab
with tab3:
    st.header("COPD Risk Assessment")
    smoking_years = st.number_input("Years Smoked", min_value=0, max_value=50, value=10)
    age = st.number_input("Age", min_value=0, max_value=120, value=30)
    fev1 = st.number_input("FEV1 (%)", min_value=0, max_value=100, value=80)
    exacerbations_last_year = st.number_input("Exacerbations Last Year", min_value=0, max_value=10, value=0)
    
    if st.button("Calculate Risk"):
        risk = calculate_copd_risk(smoking_years, age, fev1, exacerbations_last_year)
        st.session_state.results["COPD"] = risk
        st.success(f"COPD Risk Level: {risk}")

# Asthma Risk Tab
with tab4:
    st.header("Asthma Risk Assessment")
    frequency_of_symptoms = st.number_input("Days with Symptoms per Week", min_value=0, max_value=7, value=1)
    nighttime_symptoms = st.number_input("Nights with Symptoms per Month", min_value=0, max_value=30, value=0)
    inhaler_use = st.number_input("Inhaler Use per Week", min_value=0, max_value=14, value=0)
    fev1 = st.number_input("FEV1 (%)", min_value=0, max_value=100, value=80)
    eosinophil_count = st.number_input("Eosinophil Count (cells/uL)", min_value=0, max_value=1000, value=300)
    
    if st.button("Calculate Risk"):
        risk = calculate_asthma_risk(frequency_of_symptoms, nighttime_symptoms, inhaler_use, fev1, eosinophil_count)
        st.session_state.results["Asthma"] = risk
        st.success(f"Asthma Risk Level: {risk}")

# Unified Care Plan Tab
with tab5:
    st.header("Unified Care Plan")
    if st.session_state.results:
        recommendations = ai_assistant_response(st.session_state.results)
        care_plan = patient_friendly_care_plan(st.session_state.results)
        st.subheader("Multidisciplinary Recommendations")
        st.markdown(recommendations)
        st.subheader("Patient-Friendly Care Plan")
        st.markdown(care_plan)
    else:
        st.warning("Please complete the risk assessments first.")
