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

# AI Assistant Function
def ai_assistant_response(query, results):
    responses = []

    for condition, risk in results.items():
        if condition == "Cardiovascular":
            if risk == "High":
                responses.append(
                    "### Cardiovascular Risk Management\n"
                    "- **Management**: Initiate lifestyle changes including a heart-healthy diet, regular physical activity, and weight management. Consider pharmacotherapy for blood pressure and cholesterol management as per AHA/ACC guidelines.\n"
                    "- **Medications**: Start on a statin for cholesterol if appropriate, and consider an ACE inhibitor for hypertension management.\n"
                    "- **Follow-Up**: Schedule regular follow-up visits every 3-6 months to monitor blood pressure, cholesterol levels, and overall cardiovascular health.\n"
                    "- **Patient Education**: Discuss the importance of medication adherence and routine check-ups.\n"
                    "- **Resources**: [AHA Guidelines](https://www.heart.org/en/professional/quality-improvement/aha-quality-improvement-guidelines)\n"
                )
            elif risk == "Moderate":
                responses.append(
                    "### Cardiovascular Risk Management\n"
                    "- **Management**: Encourage patients to adopt heart-healthy lifestyle changes such as reducing sodium intake, increasing physical activity, and maintaining a healthy weight. Monitor blood pressure and cholesterol regularly.\n"
                    "- **Medications**: Consider starting low-dose aspirin if risk factors warrant.\n"
                    "- **Follow-Up**: Consider annual check-ups to assess risk factors and medication adherence.\n"
                    "- **Patient Education**: Provide resources on dietary recommendations and the benefits of exercise.\n"
                )

        elif condition == "Diabetes":
            if risk == "High":
                responses.append(
                    "### Diabetes Risk Management\n"
                    "- **Management**: Recommend a structured diabetes management plan including dietary modifications (e.g., DASH diet), regular blood glucose monitoring, and potential initiation of pharmacotherapy (e.g., Metformin) based on ADA guidelines.\n"
                    "- **Medications**: Start Metformin and consider additional agents (e.g., SGLT2 inhibitors) if HbA1c remains above target.\n"
                    "- **Follow-Up**: Schedule follow-ups every 3 months to adjust treatment based on glucose levels and HbA1c, and review diabetes self-management education (DSME).\n"
                    "- **Patient Education**: Educate about the importance of blood sugar monitoring, recognizing signs of hypo/hyperglycemia, and dietary management.\n"
                    "- **Resources**: [ADA Standards of Medical Care](https://www.diabetes.org/clinical-resources/standards-of-care)\n"
                )
            elif risk == "Moderate":
                responses.append(
                    "### Diabetes Risk Management\n"
                    "- **Management**: Advise patients on lifestyle changes including increased physical activity and dietary adjustments to reduce sugar and carbohydrate intake.\n"
                    "- **Medications**: Monitor glucose levels regularly; initiate Metformin if there is a significant risk of progression to diabetes.\n"
                    "- **Follow-Up**: Regular monitoring of blood glucose levels and annual HbA1c testing. Encourage participation in diabetes education programs.\n"
                    "- **Patient Education**: Discuss the benefits of physical activity and provide resources for meal planning.\n"
                )

        elif condition == "COPD":
            if risk == "High":
                responses.append(
                    "### COPD Risk Management\n"
                    "- **Management**: Immediate initiation of smoking cessation programs and pulmonary rehabilitation. Consider medications such as bronchodilators and corticosteroids as per GOLD guidelines.\n"
                    "- **Medications**: Initiate long-acting bronchodilators and assess need for inhaled corticosteroids based on symptoms.\n"
                    "- **Follow-Up**: Schedule regular follow-ups every 1-3 months to monitor lung function and exacerbation history, and adjust medications as needed.\n"
                    "- **Patient Education**: Provide education on inhaler technique, smoking cessation resources, and recognizing exacerbation signs.\n"
                    "- **Resources**: [GOLD Guidelines](https://goldcopd.org/gold-reports/)\n"
                )
            elif risk == "Moderate":
                responses.append(
                    "### COPD Risk Management\n"
                    "- **Management**: Encourage smoking cessation and prescribe bronchodilators as needed. Educate patients on recognizing early signs of exacerbation.\n"
                    "- **Medications**: Prescribe short-acting bronchodilators for symptom relief and consider long-acting options if symptoms persist.\n"
                    "- **Follow-Up**: Biannual follow-ups to assess lung function and medication effectiveness.\n"
                    "- **Patient Education**: Emphasize the importance of adherence to medication and regular monitoring of symptoms.\n"
                )

        elif condition == "Asthma":
            if risk == "High":
                responses.append(
                    "### Asthma Risk Management\n"
                    "- **Management**: Optimize medication adherence by prescribing inhaled corticosteroids and educating patients about proper inhaler technique. Develop a comprehensive asthma action plan.\n"
                    "- **Medications**: Initiate daily inhaled corticosteroids and assess need for rescue inhalers.\n"
                    "- **Follow-Up**: Schedule visits every 1-3 months to reassess control and medication needs, with a focus on asthma triggers.\n"
                    "- **Patient Education**: Educate on asthma triggers, proper inhaler use, and the importance of a written action plan.\n"
                    "- **Resources**: [AAFA Guidelines](https://www.aafa.org)\n"
                )
            elif risk == "Moderate":
                responses.append(
                    "### Asthma Risk Management\n"
                    "- **Management**: Reinforce the importance of adherence to maintenance therapy and review the asthma action plan regularly.\n"
                    "- **Medications**: Prescribe a low-dose inhaled corticosteroid for maintenance and a rescue inhaler for acute symptoms.\n"
                    "- **Follow-Up**: Schedule follow-ups every 3-6 months to monitor asthma control and adjust medications as needed.\n"
                    "- **Patient Education**: Discuss the importance of recognizing worsening symptoms and when to seek medical help.\n"
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
                "- **Step 2**: Maintain a balanced diet and engage in regular physical activity.\n"
                "- **Step 3**: Monitor your health metrics as advised by your provider.\n"
                "- **Step 4**: Stay informed by reading about your condition. Here’s a good [resource](https://example.com/information).\n"
                "- **Step 5**: Reach out for help if you feel overwhelmed.\n"
            )

        care_plan.append(care_steps)

    return "\n\n".join(care_plan)

# Streamlit App
st.title("Personalized Care Plan Generator")

st.header("Patient Information")
age = st.number_input("Age", min_value=0, max_value=120)
systolic_bp = st.number_input("Systolic Blood Pressure", min_value=80, max_value=250)
smoker = st.checkbox("Smoker")
cholesterol = st.number_input("Cholesterol Level", min_value=100, max_value=300)
bmi = st.number_input("BMI", min_value=10.0, max_value=60.0, step=0.1)
family_history = st.checkbox("Family History of Diabetes")
fasting_glucose = st.number_input("Fasting Glucose", min_value=70, max_value=300)
hba1c = st.number_input("HbA1c", min_value=4.0, max_value=15.0, step=0.1)
smoking_years = st.number_input("Years of Smoking", min_value=0, max_value=50)
fev1 = st.number_input("FEV1", min_value=0, max_value=10.0, step=0.1)
exacerbations_last_year = st.number_input("Exacerbations Last Year", min_value=0, max_value=10)
frequency_of_symptoms = st.number_input("Frequency of Symptoms (Days/Week)", min_value=0, max_value=7)
nighttime_symptoms = st.number_input("Nighttime Symptoms (Days/Month)", min_value=0, max_value=30)
inhaler_use = st.number_input("Inhaler Use (Days/Month)", min_value=0, max_value=30)
eosinophil_count = st.number_input("Eosinophil Count", min_value=0, max_value=1000)

if st.button("Generate Care Plan"):
    results = {
        "Cardiovascular": calculate_cardio_risk(age, systolic_bp, smoker, cholesterol),
        "Diabetes": calculate_diabetes_risk(bmi, age, family_history, fasting_glucose, hba1c),
        "COPD": calculate_copd_risk(smoking_years, age, fev1, exacerbations_last_year),
        "Asthma": calculate_asthma_risk(frequency_of_symptoms, nighttime_symptoms, inhaler_use, fev1, eosinophil_count)
    }

    # Display results
    st.subheader("Risk Assessment Results")
    for condition, risk in results.items():
        st.write(f"**{condition} Risk Level**: {risk}")

    # AI Assistant response
    st.subheader("AI Assistant Response")
    ai_response = ai_assistant_response("Provide a detailed care plan based on risk levels", results)
    st.markdown(ai_response)

    # Patient-friendly care plan
    st.subheader("Patient-Friendly Care Plan")
    care_plan = patient_friendly_care_plan(results)
    st.markdown(care_plan)
