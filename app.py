import streamlit as st
import pandas as pd

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
                    "- **Resources**: [AHA Guidelines](https://www.heart.org/-/media/Files/Health-Topics/Hypertension/2022-Hypertension-Clinical-Practice-Guidelines-Executive-Summary.pdf)\n"
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

# Create patient-friendly care plan based on risk levels
def patient_friendly_care_plan(results):
    care_plan = []

    for condition, risk in results.items():
        care_steps = f"### Care Plan for {condition} - Risk Level: {risk}\n"
        
        if risk == "High":
            if condition == "Cardiovascular":
                care_steps += (
                    "- **Step 1**: Schedule an appointment with your healthcare provider within the next week.\n"
                    "- **Step 2**: Start a heart-healthy diet:\n"
                    "  - **Figures**: Aim for at least 5 servings of fruits and vegetables per day.\n"
                    "  - **Expected Outcome**: Reduce cholesterol by approximately 10-20% in 6 months.\n"
                    "- **Step 3**: Increase your physical activity:\n"
                    "  - **Figures**: 150 minutes of moderate exercise per week (e.g., brisk walking).\n"
                    "  - **Expected Outcome**: Improve cardiovascular fitness and lower blood pressure.\n"
                    "- **Step 4**: Monitor your weight:\n"
                    "  - **Figures**: Aim for a weight loss of 5-10% of your body weight within 6 months.\n"
                    "  - **Expected Outcome**: Lower BMI, reducing risk factors for heart disease.\n"
                    "- **Step 5**: If you smoke, quit:\n"
                    "  - **Figures**: Smoking cessation programs can improve your cardiovascular health within weeks.\n"
                    "  - **Expected Outcome**: Decreased risk of heart attack and stroke.\n"
                    "- **Step 6**: Join a support group or online community for motivation. Here’s a list of resources: [Support Groups](https://example.com/support-groups).\n"
                )
            elif condition == "Diabetes":
                care_steps += (
                    "- **Step 1**: Schedule a diabetes education appointment within the next week.\n"
                    "- **Step 2**: Dietary modifications:\n"
                    "  - **Figures**: Aim for 3 meals and 2-3 snacks daily to maintain stable blood glucose levels.\n"
                    "  - **Expected Outcome**: Reduced HbA1c by 1-2% within 3 months.\n"
                    "- **Step 3**: Regular blood glucose monitoring:\n"
                    "  - **Figures**: Check blood glucose 1-2 hours after meals.\n"
                    "  - **Expected Outcome**: Better control of blood sugar levels.\n"
                    "- **Step 4**: Increase physical activity:\n"
                    "  - **Figures**: 150 minutes of moderate exercise per week (e.g., cycling, swimming).\n"
                    "  - **Expected Outcome**: Improved insulin sensitivity and weight management.\n"
                    "- **Step 5**: If overweight, aim for a weight loss of 5-7% of total body weight in 6 months.\n"
                    "  - **Expected Outcome**: Lowered risk of diabetes complications.\n"
                    "- **Step 6**: Learn more about your condition through these [educational resources](https://example.com/education).\n"
                )
            elif condition == "COPD":
                care_steps += (
                    "- **Step 1**: Schedule a pulmonary rehabilitation program within the next week.\n"
                    "- **Step 2**: Smoking cessation:\n"
                    "  - **Figures**: Use nicotine replacement therapy or medications (e.g., varenicline).\n"
                    "  - **Expected Outcome**: Improved lung function and reduced symptoms within weeks.\n"
                    "- **Step 3**: Regular exercise:\n"
                    "  - **Figures**: Engage in 30 minutes of physical activity 3-5 times a week.\n"
                    "  - **Expected Outcome**: Increased exercise tolerance and improved quality of life.\n"
                    "- **Step 4**: Nutrition management:\n"
                    "  - **Figures**: Maintain a well-balanced diet rich in antioxidants (fruits and vegetables).\n"
                    "  - **Expected Outcome**: Better overall health and decreased exacerbations.\n"
                    "- **Step 5**: Monitor symptoms and seek medical advice for any exacerbation signs.\n"
                )
            elif condition == "Asthma":
                care_steps += (
                    "- **Step 1**: Schedule an appointment with your healthcare provider to review your asthma action plan.\n"
                    "- **Step 2**: Medication adherence:\n"
                    "  - **Figures**: Use inhaled corticosteroids daily as prescribed.\n"
                    "  - **Expected Outcome**: Reduced frequency and severity of asthma attacks.\n"
                    "- **Step 3**: Recognize triggers:\n"
                    "  - **Figures**: Identify and avoid at least 3 personal asthma triggers (e.g., allergens, smoke).\n"
                    "  - **Expected Outcome**: Improved asthma control and reduced medication need.\n"
                    "- **Step 4**: Maintain a healthy weight:\n"
                    "  - **Figures**: Aim for a healthy BMI (18.5-24.9).\n"
                    "  - **Expected Outcome**: Decreased risk of asthma complications.\n"
                    "- **Step 5**: Regular follow-up appointments every 3-6 months to assess asthma control.\n"
                )
        elif risk == "Moderate":
            if condition == "Cardiovascular":
                care_steps += (
                    "- **Step 1**: Schedule a follow-up appointment in the next month.\n"
                    "- **Step 2**: Implement dietary changes:\n"
                    "  - **Figures**: Reduce saturated fat intake to less than 7% of total calories.\n"
                    "  - **Expected Outcome**: Gradual improvement in cholesterol levels.\n"
                    "- **Step 3**: Exercise regularly:\n"
                    "  - **Figures**: 30 minutes of moderate exercise at least 5 days a week.\n"
                    "  - **Expected Outcome**: Improved cardiovascular health over time.\n"
                    "- **Step 4**: Monitor weight regularly and aim for a stable weight.\n"
                )
            elif condition == "Diabetes":
                care_steps += (
                    "- **Step 1**: Schedule an annual diabetes check-up.\n"
                    "- **Step 2**: Dietary modifications:\n"
                    "  - **Figures**: Limit processed sugars to no more than 10% of daily caloric intake.\n"
                    "  - **Expected Outcome**: Improved blood glucose levels gradually.\n"
                    "- **Step 3**: Regular physical activity:\n"
                    "  - **Figures**: 150 minutes of moderate exercise weekly.\n"
                    "  - **Expected Outcome**: Enhanced insulin sensitivity and weight maintenance.\n"
                )
            elif condition == "COPD":
                care_steps += (
                    "- **Step 1**: Schedule a check-up every 6 months.\n"
                    "- **Step 2**: Encourage smoking cessation efforts:\n"
                    "  - **Figures**: Use support groups or counseling.\n"
                    "  - **Expected Outcome**: Improved lung health over time.\n"
                )
            elif condition == "Asthma":
                care_steps += (
                    "- **Step 1**: Schedule a follow-up visit every 3-6 months.\n"
                    "- **Step 2**: Review inhaler technique regularly.\n"
                    "  - **Figures**: Practice at least once a week to ensure correct use.\n"
                    "  - **Expected Outcome**: Reduced asthma symptoms and medication use.\n"
                )

        care_plan.append(care_steps)

    return "\n\n".join(care_plan)

# Streamlit Application Layout
st.title("Healthcare Provider Risk Assessment and Care Plan")

tab1, tab2, tab3, tab4, tab5 = st.tabs(["Cardiovascular Risk Assessment", "Diabetes Risk Assessment", "COPD Risk Assessment", "Asthma Risk Assessment", "Unified Care Plan"])

# Store results in session state
if 'results' not in st.session_state:
    st.session_state['results'] = {}

# Cardiovascular Risk Tab
with tab1:
    st.header("Cardiovascular Risk Assessment")
    age_cardiovascular = st.number_input("Age", min_value=18, max_value=120, value=50, key="age_cardiovascular")
    systolic_bp = st.number_input("Systolic Blood Pressure", min_value=90, max_value=200, value=120, key="systolic_bp")
    smoker = st.checkbox("Current Smoker", key="smoker")
    cholesterol = st.number_input("Total Cholesterol", min_value=100, max_value=300, value=200, key="cholesterol")

    if st.button("Calculate Cardiovascular Risk"):
        cardio_risk = calculate_cardio_risk(age_cardiovascular, systolic_bp, smoker, cholesterol)
        st.write(f"**Cardiovascular Risk Level**: {cardio_risk}")
        st.session_state['results']["Cardiovascular"] = cardio_risk

        # Educational Resources
        st.write("### Educational Resources for Healthcare Providers")
        st.write("- [AHA Guidelines on Cardiovascular Disease Management (PDF)](https://www.heart.org/-/media/Files/Health-Topics/Hypertension/2022-Hypertension-Clinical-Practice-Guidelines-Executive-Summary.pdf)")

# Diabetes Risk Tab
with tab2:
    st.header("Diabetes Risk Assessment")
    age_diabetes = st.number_input("Age", min_value=18, max_value=120, value=50, key="age_diabetes")
    bmi = st.number_input("BMI", min_value=10.0, max_value=50.0, value=25.0, key="bmi")
    family_history = st.checkbox("Family History of Diabetes", key="family_history")
    fasting_glucose = st.number_input("Fasting Glucose (mg/dL)", min_value=70, max_value=300, value=100, key="fasting_glucose")
    hba1c = st.number_input("HbA1c (%)", min_value=4.0, max_value=14.0, value=5.7, key="hba1c")

    if st.button("Calculate Diabetes Risk"):
        diabetes_risk = calculate_diabetes_risk(bmi, age_diabetes, family_history, fasting_glucose, hba1c)
        st.write(f"**Diabetes Risk Level**: {diabetes_risk}")
        st.session_state['results']["Diabetes"] = diabetes_risk

        # Educational Resources
        st.write("### Educational Resources for Healthcare Providers")
        st.write("- [ADA Standards of Medical Care](https://www.diabetes.org/clinical-resources/standards-of-care)")

# COPD Risk Tab
with tab3:
    st.header("COPD Risk Assessment")
    age_copd = st.number_input("Age", min_value=18, max_value=120, value=50, key="age_copd")
    smoking_years = st.number_input("Years of Smoking", min_value=0, max_value=50, value=10, key="smoking_years")
    fev1 = st.number_input("FEV1 (% predicted)", min_value=0.0, max_value=100.0, value=80.0, key="fev1")
    exacerbations_last_year = st.number_input("Number of Exacerbations Last Year", min_value=0, max_value=10, value=1, key="exacerbations_last_year")

    if st.button("Calculate COPD Risk"):
        copd_risk = calculate_copd_risk(smoking_years, age_copd, fev1, exacerbations_last_year)
        st.write(f"**COPD Risk Level**: {copd_risk}")
        st.session_state['results']["COPD"] = copd_risk

        # Educational Resources
        st.write("### Educational Resources for Healthcare Providers")
        st.write("- [GOLD Guidelines](https://goldcopd.org/gold-reports/)")

# Asthma Risk Tab
with tab4:
    st.header("Asthma Risk Assessment")
    age_asthma = st.number_input("Age", min_value=18, max_value=120, value=50, key="age_asthma")
    frequency_of_symptoms = st.number_input("Frequency of Symptoms per Week", min_value=0, max_value=14, value=3, key="frequency_of_symptoms")
    nighttime_symptoms = st.number_input("Nighttime Symptoms per Month", min_value=0, max_value=30, value=1, key="nighttime_symptoms")
    inhaler_use = st.number_input("Days of Rescue Inhaler Use per Week", min_value=0, max_value=7, value=2, key="inhaler_use")
    eosinophil_count = st.number_input("Eosinophil Count (cells/µL)", min_value=0, max_value=1000, value=300, key="eosinophil_count")

    if st.button("Calculate Asthma Risk"):
        asthma_risk = calculate_asthma_risk(frequency_of_symptoms, nighttime_symptoms, inhaler_use, fev1, eosinophil_count)
        st.write(f"**Asthma Risk Level**: {asthma_risk}")
        st.session_state['results']["Asthma"] = asthma_risk

        # Educational Resources
        st.write("### Educational Resources for Healthcare Providers")
        st.write("- [AAFA Guidelines](https://www.aafa.org)")

# Unified Care Plan Tab
with tab5:
    st.header("Unified Care Plan")

    if st.session_state['results']:
        st.write("### Multidisciplinary Recommendations")
        recommendations = ai_assistant_response("Generate multidisciplinary recommendations", st.session_state['results'])
        st.write(recommendations)

        st.write("### Patient-Friendly Care Steps")
        care_plan = patient_friendly_care_plan(st.session_state['results'])
        st.write(care_plan)

    else:
        st.write("Please complete the assessments in the previous tabs to view the Unified Care Plan.")

# End of Streamlit Application
