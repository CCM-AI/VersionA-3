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
                "- **Management**: \n"
                "  - Initiate lifestyle changes, including:\n"
                "    - **Diet**: Aim for a diet low in saturated fats (<7% of total calories) and high in fruits, vegetables, and whole grains. Target a daily sodium intake <2,300 mg.\n"
                "    - **Physical Activity**: Minimum 150 minutes of moderate-intensity aerobic exercise per week.\n"
                "  - **Pharmacotherapy**: \n"
                "    - Start antihypertensive agents if BP >140/90 mmHg. Consider statins if LDL ≥ 190 mg/dL or 70-189 mg/dL with a 10-year ASCVD risk ≥ 20%.\n"
                "  - **Targets**: \n"
                "    - Achieve BP <130/80 mmHg and LDL <100 mg/dL within 6 months.\n"
                "  - **Risk Factors to Avoid**: Smoking, excessive alcohol, high-sugar diets, sedentary lifestyle.\n"
                "  - **Follow-Up**: Every 3-6 months to monitor progress.\n"
                "- **Resources**: [AHA Guidelines](https://www.heart.org/en/professional/quality-improvement/aha-quality-improvement-guidelines) | [ASCVD Risk Calculator](https://tools.acc.org/ASCVD/Risk-Estimator-Plus/)\n"
            )
        else:
            return (
                "### Cardiovascular Recommendations\n"
                "- **Management**: \n"
                "  - Encourage lifestyle changes focusing on:\n"
                "    - **Diet**: Maintain sodium intake <2,300 mg, limit saturated fats, increase fiber.\n"
                "    - **Physical Activity**: Encourage at least 150 minutes of moderate activity per week.\n"
                "  - **Monitoring**: Check BP and cholesterol annually.\n"
                "- **Resources**: [AHA Guidelines](https://www.heart.org/en/professional/quality-improvement/aha-quality-improvement-guidelines)\n"
            )

    elif condition == "Diabetes":
        if risk == "High":
            return (
                "### Diabetes Recommendations\n"
                "- **Management**: \n"
                "  - Implement a structured management plan:\n"
                "    - **Diet**: Follow a Mediterranean diet with a focus on whole foods, aiming for <45% of calories from carbohydrates.\n"
                "    - **Physical Activity**: 150 minutes of moderate-intensity exercise per week.\n"
                "  - **Pharmacotherapy**: \n"
                "    - Start Metformin if HbA1c > 6.5%. Add GLP-1 receptor agonists or SGLT2 inhibitors as needed based on individual characteristics.\n"
                "  - **Targets**: \n"
                "    - Aim for HbA1c <7% within 3-6 months; fasting glucose 80-130 mg/dL.\n"
                "  - **Risk Factors to Avoid**: High-sugar diets, sedentary lifestyle, smoking.\n"
                "  - **Follow-Up**: Every 3 months to adjust treatment.\n"
                "- **Resources**: [ADA Standards of Medical Care](https://www.diabetes.org/clinical-resources/standards-of-care) | [Diabetes Education Resources](https://www.diabeteseducator.org)\n"
            )
        else:
            return (
                "### Diabetes Recommendations\n"
                "- **Management**: \n"
                "  - Advise on lifestyle changes:\n"
                "    - **Diet**: Maintain a balanced diet and monitor carbohydrate intake.\n"
                "    - **Physical Activity**: Aim for 30 minutes of moderate exercise most days of the week.\n"
                "  - **Monitoring**: Annual HbA1c testing.\n"
                "- **Resources**: [ADA Standards of Medical Care](https://www.diabetes.org/clinical-resources/standards-of-care)\n"
            )

    elif condition == "COPD":
        if risk == "High":
            return (
                "### COPD Recommendations\n"
                "- **Management**: \n"
                "  - Initiate smoking cessation programs immediately. Use pharmacotherapy as needed (e.g., varenicline).\n"
                "  - **Pharmacotherapy**: Consider long-acting bronchodilators and inhaled corticosteroids.\n"
                "  - **Targets**: \n"
                "    - Achieve FEV1 improvement of at least 15% within 6 months of initiating therapy.\n"
                "  - **Risk Factors to Avoid**: Smoking, air pollution, occupational exposures.\n"
                "  - **Follow-Up**: Every 1-3 months to monitor lung function and exacerbations.\n"
                "- **Resources**: [GOLD Guidelines](https://goldcopd.org/gold-reports/) | [COPD Exacerbation Management Guidelines](https://www.thoracic.org/professionals/care-standards/guidelines/copd-exacerbations.php)\n"
            )
        else:
            return (
                "### COPD Recommendations\n"
                "- **Management**: \n"
                "  - Encourage smoking cessation and prescribe bronchodilators as needed.\n"
                "  - **Monitoring**: Assess lung function annually; track symptoms regularly.\n"
                "- **Resources**: [GOLD Guidelines](https://goldcopd.org/gold-reports/)\n"
            )

    elif condition == "Asthma":
        if risk == "High":
            return (
                "### Asthma Recommendations\n"
                "- **Management**: \n"
                "  - Optimize controller medication (inhaled corticosteroids) and develop a comprehensive asthma action plan.\n"
                "  - **Targets**: \n"
                "    - Achieve symptom control with no more than 2 days of rescue inhaler use per week within 4-8 weeks.\n"
                "  - **Risk Factors to Avoid**: Smoking, allergens (e.g., dust mites, pollen), air pollution.\n"
                "  - **Follow-Up**: Every 1-3 months to reassess control and medication needs.\n"
                "- **Resources**: [AAFA Guidelines](https://www.aafa.org) | [NHLBI Asthma Guidelines](https://www.nhlbi.nih.gov/health-topics/asthma)\n"
            )
        else:
            return (
                "### Asthma Recommendations\n"
                "- **Management**: \n"
                "  - Reinforce adherence to maintenance therapy and review the asthma action plan regularly.\n"
                "  - **Monitoring**: Schedule follow-ups every 3-6 months.\n"
                "- **Resources**: [AAFA Guidelines](https://www.aafa.org)\n"
            )

# Create patient-friendly care plan based on risk levels
def patient_friendly_care_plan(results):
    care_plan = []

    for condition, risk in results.items():
        care_steps = f"### Care Plan for {condition} - Risk Level: {risk}\n"
        
        if risk == "High":
            care_steps += (
                "- **Step 1**: Schedule an appointment with your healthcare provider within the next week.\n"
                "- **Step 2**: Start a heart-healthy diet focusing on fruits, vegetables, whole grains, and lean proteins. Here’s a helpful [video on heart-healthy diets](https://www.youtube.com/watch?v=example1).\n"
                "- **Step 3**: Increase your physical activity to at least 150 minutes of moderate exercise per week. Here’s a [guide to starting exercise](https://www.youtube.com/watch?v=example2).\n"
                "- **Step 4**: Monitor your blood pressure and cholesterol levels as advised. Use this [blood pressure log template](https://example.com/log-template).\n"
                "- **Step 5**: Join a support group or online community for motivation. Here’s a list of resources: [Support Groups](https://example.com/support-groups).\n"
            )
        elif risk == "Moderate":
            care_steps += (
                "- **Step 1**: Follow up with your healthcare provider within the next month.\n"
                "- **Step 2**: Continue a balanced diet and stay active. Consider keeping a food diary.\n"
                "- **Step 3**: Aim to get at least 30 minutes of exercise most days.\n"
                "- **Step 4**: Monitor your symptoms and report any changes to your provider.\n"
                "- **Step 5**: Educate yourself about your condition using reliable sources like the [CDC](https://www.cdc.gov) or [Mayo Clinic](https://www.mayoclinic.org).\n"
            )

        care_plan.append(care_steps)

    return "\n".join(care_plan)

# Streamlit app
st.title("Chronic Disease Risk Assessment Tool")

# Initialize session state
if 'results' not in st.session_state:
    st.session_state['results'] = {}

# Tabs for different risk assessments
tab1, tab2, tab3, tab4, tab5 = st.tabs(["Cardiovascular Risk", "Diabetes Risk", "COPD Risk", "Asthma Risk", "Unified Care Plan"])

# Cardiovascular Risk Tab
with tab1:
    st.header("Cardiovascular Risk Assessment")
    age = st.number_input("Age", min_value=18, max_value=120, value=50, key="cardio_age")
    systolic_bp = st.number_input("Systolic Blood Pressure (mmHg)", min_value=80, max_value=200, value=120, key="systolic_bp")
    smoker = st.checkbox("Smoker", key="smoker")
    cholesterol = st.number_input("Cholesterol Level (mg/dL)", min_value=150, max_value=300, value=200, key="cholesterol")

    if st.button("Calculate Cardiovascular Risk"):
        cardio_risk = calculate_cardio_risk(age, systolic_bp, smoker, cholesterol)
        st.write(f"**Cardiovascular Risk Level**: {cardio_risk}")
        st.session_state['results']["Cardiovascular"] = cardio_risk
        st.write(ai_assistant_response("Cardiovascular", cardio_risk))

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

# Unified Care Plan Tab
with tab5:
    st.header("Unified Care Plan")
    if st.session_state['results']:
        st.write("### Suggested Patient-Friendly Care Plan")
        patient_care_plan = patient_friendly_care_plan(st.session_state['results'])
        st.write(patient_care_plan)

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
