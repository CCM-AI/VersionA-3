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

# AI Assistant for Multidisciplinary Team Recommendations
def multidisciplinary_recommendations(condition, risk):
    recommendations = []

    if condition == "Cardiovascular":
        if risk == "High":
            recommendations.append(
                "### Cardiovascular Risk Recommendations for Healthcare Providers\n"
                "- **Pharmacotherapy**: Consider initiating antihypertensive therapy with ACE inhibitors or ARBs, statins for lipid management, and antiplatelet therapy if indicated (e.g., aspirin).\n"
                "- **Lifestyle Interventions**: Refer patients to a dietitian for personalized dietary counseling (e.g., Mediterranean diet) and recommend structured exercise programs.\n"
                "- **Monitoring**: Schedule follow-ups every 3-6 months to assess medication adherence and clinical outcomes. Use tools such as the ASCVD Risk Calculator to reassess risk periodically.\n"
                "- **Patient Education**: Provide educational materials regarding the importance of lifestyle changes and medication adherence. Consider group sessions for peer support.\n"
            )
        elif risk == "Moderate":
            recommendations.append(
                "### Cardiovascular Risk Recommendations for Healthcare Providers\n"
                "- **Monitoring**: Encourage regular monitoring of blood pressure and lipid levels. Use motivational interviewing techniques to enhance patient engagement.\n"
                "- **Lifestyle Modifications**: Educate patients on reducing sodium intake, increasing physical activity, and maintaining a healthy weight. Consider using community resources such as local fitness programs.\n"
                "- **Follow-Up**: Schedule annual check-ups to reassess risk factors and modify management as necessary.\n"
            )

    elif condition == "Diabetes":
        if risk == "High":
            recommendations.append(
                "### Diabetes Risk Recommendations for Healthcare Providers\n"
                "- **Pharmacotherapy**: Initiate Metformin as the first-line agent for glycemic control. Consider referral to an endocrinologist for complex cases.\n"
                "- **Lifestyle Interventions**: Refer patients to a diabetes education program focusing on dietary modifications (e.g., low-carb diets) and exercise regimens.\n"
                "- **Monitoring**: Schedule follow-ups every 3 months to monitor HbA1c and adjust therapy as needed. Use continuous glucose monitoring if applicable.\n"
                "- **Patient Education**: Provide resources on diabetes management and support groups to enhance self-management skills.\n"
            )
        elif risk == "Moderate":
            recommendations.append(
                "### Diabetes Risk Recommendations for Healthcare Providers\n"
                "- **Monitoring**: Regularly monitor HbA1c every 6 months and assess for complications such as retinopathy and neuropathy annually.\n"
                "- **Lifestyle Modifications**: Encourage increased physical activity and dietary adjustments. Provide materials on meal planning and portion control.\n"
                "- **Follow-Up**: Schedule follow-up visits every 6 months to assess treatment efficacy and lifestyle adherence.\n"
            )

    elif condition == "COPD":
        if risk == "High":
            recommendations.append(
                "### COPD Risk Recommendations for Healthcare Providers\n"
                "- **Pharmacotherapy**: Initiate bronchodilator therapy (SABAs and LABAs) and consider inhaled corticosteroids based on exacerbation frequency. Refer patients for pulmonary rehabilitation.\n"
                "- **Lifestyle Interventions**: Strongly encourage smoking cessation and provide access to support programs (e.g., counseling, nicotine replacement).\n"
                "- **Monitoring**: Schedule follow-ups every 1-3 months to assess treatment response and lung function (spirometry).\n"
                "- **Patient Education**: Educate patients about recognizing exacerbation signs and proper inhaler technique. Provide a COPD action plan.\n"
            )
        elif risk == "Moderate":
            recommendations.append(
                "### COPD Risk Recommendations for Healthcare Providers\n"
                "- **Monitoring**: Regularly monitor lung function and adjust therapy based on symptom control. Educate patients about medication adherence.\n"
                "- **Lifestyle Modifications**: Encourage smoking cessation and active participation in pulmonary rehabilitation.\n"
                "- **Follow-Up**: Schedule follow-up visits every 3-6 months for ongoing assessment of symptoms and treatment adherence.\n"
            )

    elif condition == "Asthma":
        if risk == "High":
            recommendations.append(
                "### Asthma Risk Recommendations for Healthcare Providers\n"
                "- **Pharmacotherapy**: Optimize inhaled corticosteroids and consider adding long-acting beta-agonists (LABAs) for better control. Referral to a specialist may be necessary for uncontrolled asthma.\n"
                "- **Lifestyle Interventions**: Educate patients on allergen avoidance and self-management strategies, including proper use of inhalers.\n"
                "- **Monitoring**: Schedule regular follow-ups every 1-3 months to assess control and adjust therapy accordingly. Consider using an asthma control questionnaire.\n"
                "- **Patient Education**: Provide an asthma action plan and information about recognizing and responding to exacerbations.\n"
            )
        elif risk == "Moderate":
            recommendations.append(
                "### Asthma Risk Recommendations for Healthcare Providers\n"
                "- **Monitoring**: Regularly assess asthma control using validated tools. Monitor inhaler technique during follow-up visits.\n"
                "- **Lifestyle Modifications**: Encourage adherence to maintenance therapy and provide resources on managing triggers and symptoms.\n"
                "- **Follow-Up**: Schedule follow-ups every 3-6 months to review asthma control and medication effectiveness.\n"
            )

    return "\n\n".join(recommendations)

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

# Session state to store results
if 'results' not in st.session_state:
    st.session_state['results'] = {}

# Tabs for each condition
tab1, tab2, tab3, tab4, tab5 = st.tabs(["Cardiovascular Risk", "Diabetes Risk", "COPD Risk", "Asthma Risk", "Personalized Care Plan"])

# Cardiovascular Risk Tab
with tab1:
    st.header("Cardiovascular Risk Assessment")
    age = st.number_input("Age", min_value=18, max_value=120, value=50, key="age_cardiovascular")
    systolic_bp = st.number_input("Systolic Blood Pressure (mmHg)", min_value=80, max_value=200, value=120, key="systolic_bp")
    smoker = st.checkbox("Smoker", key="smoker")
    cholesterol = st.number_input("Total Cholesterol (mg/dL)", min_value=100, max_value=400, value=200, key="cholesterol")

    if st.button("Calculate Cardiovascular Risk"):
        cardio_risk = calculate_cardio_risk(age, systolic_bp, smoker, cholesterol)
        st.write(f"**Cardiovascular Risk Level**: {cardio_risk}")
        st.session_state['results']["Cardiovascular"] = cardio_risk
        
        # Display multidisciplinary recommendations
        st.markdown(multidisciplinary_recommendations("Cardiovascular", cardio_risk))

# Diabetes Risk Tab
with tab2:
    st.header("Diabetes Risk Assessment")
    bmi = st.number_input("Body Mass Index (BMI)", min_value=10.0, max_value=60.0, value=25.0, key="bmi")
    age = st.number_input("Age", min_value=18, max_value=120, value=50, key="age_diabetes")
    family_history = st.checkbox("Family History of Diabetes", key="family_history")
    fasting_glucose = st.number_input("Fasting Glucose (mg/dL)", min_value=60, max_value=300, value=100, key="fasting_glucose")
    hba1c = st.number_input("HbA1c (%)", min_value=4.0, max_value=15.0, value=5.7, key="hba1c")

    if st.button("Calculate Diabetes Risk"):
        diabetes_risk = calculate_diabetes_risk(bmi, age, family_history, fasting_glucose, hba1c)
        st.write(f"**Diabetes Risk Level**: {diabetes_risk}")
        st.session_state['results']["Diabetes"] = diabetes_risk
        
        # Display multidisciplinary recommendations
        st.markdown(multidisciplinary_recommendations("Diabetes", diabetes_risk))

# COPD Risk Tab
with tab3:
    st.header("COPD Risk Assessment")
    smoking_years = st.number_input("Years of Smoking", min_value=0, max_value=60, value=20, key="smoking_years")
    age = st.number_input("Age", min_value=18, max_value=120, value=50, key="age_copd")
    fev1 = st.number_input("FEV1 (% predicted)", min_value=20, max_value=120, value=80, key="fev1")
    exacerbations_last_year = st.number_input("Number of Exacerbations Last Year", min_value=0, max_value=20, value=1, key="exacerbations")

    if st.button("Calculate COPD Risk"):
        copd_risk = calculate_copd_risk(smoking_years, age, fev1, exacerbations_last_year)
        st.write(f"**COPD Risk Level**: {copd_risk}")
        st.session_state['results']["COPD"] = copd_risk
        
        # Display multidisciplinary recommendations
        st.markdown(multidisciplinary_recommendations("COPD", copd_risk))

# Asthma Risk Tab
with tab4:
    st.header("Asthma Risk Assessment")
    frequency_of_symptoms = st.number_input("Days with Symptoms per Week", min_value=0, max_value=7, value=1, key="frequency_of_symptoms")
    nighttime_symptoms = st.number_input("Nighttime Symptoms per Month", min_value=0, max_value=30, value=1, key="nighttime_symptoms")
    inhaler_use = st.number_input("Inhaler Use per Week", min_value=0, max_value=14, value=1, key="inhaler_use")
    fev1 = st.number_input("FEV1 (% predicted)", min_value=20, max_value=120, value=80, key="fev1_asthma")
    eosinophil_count = st.number_input("Eosinophil Count (cells/uL)", min_value=0, max_value=2000, value=300, key="eosinophil_count")

    if st.button("Calculate Asthma Risk"):
        asthma_risk = calculate_asthma_risk(frequency_of_symptoms, nighttime_symptoms, inhaler_use, fev1, eosinophil_count)
        st.write(f"**Asthma Risk Level**: {asthma_risk}")
        st.session_state['results']["Asthma"] = asthma_risk
        
        # Display multidisciplinary recommendations
        st.markdown(multidisciplinary_recommendations("Asthma", asthma_risk))

# Unified Care Plan Tab
with tab5:
    st.header("Personalized Care Plan")
    if st.session_state['results']:
        care_plan = patient_friendly_care_plan(st.session_state['results'])
        st.markdown(care_plan)
    else:
        st.write("Please complete the assessments to see your personalized care plan.")
