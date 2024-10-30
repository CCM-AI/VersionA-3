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
    # Example response structure, should be replaced with actual AI logic
    responses = {
        "Cardiovascular": "Consider lifestyle modifications, blood pressure monitoring, and medication adjustments as per AHA guidelines.",
        "Diabetes": "Focus on dietary changes, regular glucose monitoring, and HbA1c management based on ADA recommendations.",
        "COPD": "Implement smoking cessation, pulmonary rehabilitation, and inhaler technique assessments.",
        "Asthma": "Ensure adherence to a personalized asthma action plan and regular follow-ups for medication management."
    }
    
    combined_response = []
    for condition in results.keys():
        combined_response.append(f"{condition}: {responses.get(condition, 'No specific guidance available.')}")
    
    return "\n".join(combined_response)

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
    st.header("Unified Care Plan for Patients")
    if st.session_state['results']:
        st.write("### Care Plan Based on Risk Levels")
        for condition, risk in st.session_state['results'].items():
            st.write(f"#### {condition} - {risk} Risk")

            if risk == "High":
                st.write(f"**Your Management Plan for {condition}:**")
                st.write("- **Step 1**: Schedule an appointment with your healthcare provider to discuss treatment options and medications.")
                st.write("- **Step 2**: Follow a tailored diet plan (e.g., low-sodium for heart conditions, low-sugar for diabetes).")
                st.write("- **Step 3**: Engage in regular physical activity, aiming for at least 150 minutes of moderate exercise weekly.")
                st.write("- **Step 4**: Monitor your condition closely with the help of your healthcare team, and keep track of symptoms or changes.")
                st.write("- **Step 5**: Attend follow-up appointments every 1-3 months as recommended.")
                st.write("- **Helpful Resources**: Here are some links to help you understand your condition and management better:")
                st.write("  - [Heart Health Resources](https://www.heart.org/en/health-topics/heart-attack) (for cardiovascular risks)")
                st.write("  - [Diabetes Education](https://www.diabetes.org/diabetes) (for diabetes management)")
                st.write("  - [COPD Support](https://www.copdsupport.com) (for COPD management)")
                st.write("  - [Asthma Management](https://www.aafa.org/asthma/) (for asthma management)")

            elif risk == "Moderate":
                st.write(f"**Your Management Plan for {condition}:**")
                st.write("- **Step 1**: Schedule a regular check-up with your healthcare provider to monitor your condition.")
                st.write("- **Step 2**: Adopt healthy lifestyle changes, including a balanced diet and regular exercise.")
                st.write("- **Step 3**: Keep a symptom diary to track any changes or triggers.")
                st.write("- **Step 4**: Consider joining a support group or educational session for additional help.")
                st.write("- **Helpful Resources**: Explore these links for more information:")
                st.write("  - [Heart Disease Prevention](https://www.heart.org/en/healthy-living) (for cardiovascular risks)")
                st.write("  - [Understanding Diabetes](https://www.diabetes.org/diabetes) (for diabetes management)")
                st.write("  - [Managing COPD](https://www.copd.net) (for COPD management)")
                st.write("  - [Asthma Basics](https://www.aafa.org/asthma-basics/) (for asthma management)")

            else:  # Low Risk
                st.write(f"**Your Management Plan for {condition}:**")
                st.write("- **Step 1**: Continue with your healthy lifestyle practices and regular check-ups.")
                st.write("- **Step 2**: Stay informed about your condition and its management.")
                st.write("- **Helpful Resources**: Check these links to enhance your knowledge:")
                st.write("  - [Heart Health](https://www.heart.org/en/healthy-living) (for cardiovascular wellness)")
                st.write("  - [Diabetes Basics](https://www.diabetes.org) (for diabetes education)")
                st.write("  - [COPD Information](https://www.copd.net) (for COPD awareness)")
                st.write("  - [Asthma Tips](https://www.aafa.org/asthma-tips/) (for asthma management)")

# AI Assistant Tab (remains unchanged)
with st.expander("AI Assistant (Multidisciplinary Team) for Healthcare Provider Guidance", expanded=True):
    st.header("AI Assistant for Risk Management and Care Guidance")
    query = st.text_input("Ask the AI Assistant about risk management, personalized care, or guidelines:")
    if st.button("Get AI Assistance"):
        if st.session_state['results']:
            ai_response = ai_assistant_response(query, st.session_state['results'])
            st.write(ai_response)
        else:
            st.write("Please complete risk assessments in previous tabs first.")
