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
                "- **Step 2**: Maintain a balanced diet with plenty of fruits and vegetables.\n"
                "- **Step 3**: Engage in regular physical activity, aiming for at least 150 minutes a week.\n"
                "- **Step 4**: Monitor any symptoms and keep a journal of your health.\n"
                "- **Step 5**: Stay informed about your health condition by reading credible sources.\n"
            )

        care_plan.append(care_steps)

    return "\n\n".join(care_plan)

# Main Streamlit app
st.title("Health Risk Assessment and Management")

# User Input Section
st.header("Patient Information")
age = st.number_input("Enter age:", min_value=0, max_value=120, value=30)
systolic_bp = st.number_input("Enter systolic blood pressure:", min_value=80, max_value=200, value=120)
smoker = st.radio("Do you smoke?", ("Yes", "No")) == "Yes"
cholesterol = st.number_input("Enter cholesterol level:", min_value=100, max_value=300, value=200)

bmi = st.number_input("Enter BMI:", min_value=10.0, max_value=60.0, value=25.0)
family_history = st.radio("Family history of diabetes?", ("Yes", "No")) == "Yes"
fasting_glucose = st.number_input("Enter fasting glucose level:", min_value=70, max_value=300, value=100)
hba1c = st.number_input("Enter HbA1c level:", min_value=4.0, max_value=14.0, value=5.5)

smoking_years = st.number_input("Enter years of smoking:", min_value=0, max_value=100, value=0)
fev1 = st.number_input("Enter FEV1 percentage:", min_value=20, max_value=120, value=80)
exacerbations_last_year = st.number_input("Enter exacerbations in the last year:", min_value=0, max_value=20, value=0)

frequency_of_symptoms = st.number_input("Enter frequency of asthma symptoms per week:", min_value=0, max_value=10, value=0)
nighttime_symptoms = st.number_input("Enter nighttime asthma symptoms per month:", min_value=0, max_value=10, value=0)
inhaler_use = st.number_input("Enter number of rescue inhaler uses per week:", min_value=0, max_value=20, value=0)
eosinophil_count = st.number_input("Enter eosinophil count:", min_value=0, max_value=1000, value=300)

if st.button("Assess Risk"):
    # Risk Assessment
    cardio_risk = calculate_cardio_risk(age, systolic_bp, smoker, cholesterol)
    diabetes_risk = calculate_diabetes_risk(bmi, age, family_history, fasting_glucose, hba1c)
    copd_risk = calculate_copd_risk(smoking_years, age, fev1, exacerbations_last_year)
    asthma_risk = calculate_asthma_risk(frequency_of_symptoms, nighttime_symptoms, inhaler_use, fev1, eosinophil_count)

    risk_results = {
        "Cardiovascular": cardio_risk,
        "Diabetes": diabetes_risk,
        "COPD": copd_risk,
        "Asthma": asthma_risk,
    }

    # Display Results
    st.header("Risk Assessment Results")
    for condition, risk in risk_results.items():
        st.write(f"{condition} Risk: {risk}")

    # AI Assistant Response
    st.header("AI Assistant Response")
    ai_response = ai_assistant_response("Provide care plan based on risks", risk_results)
    st.markdown(ai_response)

    # Patient-Friendly Care Plan
    st.header("Patient-Friendly Care Plan")
    care_plan = patient_friendly_care_plan(risk_results)
    st.markdown(care_plan)
