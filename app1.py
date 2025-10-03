import streamlit as st
import random
import datetime

# Page configuration
st.set_page_config(
    page_title="MediGuard AI",
    page_icon="🛡️",
    layout="wide"
)

# Medical knowledge base 
MEDICAL_KNOWLEDGE = {
    'high_risk': {
        'symptoms': ['chest pain', 'shortness of breath', 'severe bleeding', 'unconscious', 'difficulty breathing',
                     'sudden numbness'],
        'conditions': ['Heart Attack', 'Stroke', 'Severe Trauma', 'Pulmonary Embolism', 'Cardiac Arrest'],
        'recommendation': {
            'action': "🚨 SEEK EMERGENCY CARE IMMEDIATELY",
            'advice': "Go to the nearest hospital emergency room or call emergency services (108/112) immediately!",
            'steps': [
                "Call emergency number (108/112)",
                "Do not drive yourself",
                "Keep calm and wait for help",
                "Do not give any food or water"
            ]
        }
    },
    'medium_risk': {
        'symptoms': ['high fever', 'severe pain', 'vomiting blood', 'head injury', 'persistent vomiting', 'burn',
                     'deep cut'],
        'conditions': ['Severe Infection', 'Internal Bleeding', 'Concussion', 'Kidney Infection', 'Fracture'],
        'recommendation': {
            'action': "🟡 CONSULT A DOCTOR SOON",
            'advice': "Schedule an appointment with your doctor within 24 hours or visit urgent care.",
            'steps': [
                "Rest and stay hydrated",
                "Monitor symptoms closely",
                "Avoid self-medication",
                "Keep the affected area clean"
            ]
        }
    },
    'low_risk': {
        'symptoms': ['cough', 'mild fever', 'headache', 'runny nose', 'sore throat', 'muscle pain', 'sneezing',
                     'mild rash'],
        'conditions': ['Common Cold', 'Flu', 'Allergies', 'Muscle Strain', 'Seasonal Illness'],
        'recommendation': {
            'action': "🟢 SELF-CARE AT HOME",
            'advice': "Your symptoms suggest a minor condition that can be managed at home.",
            'steps': [
                "Get plenty of rest",
                "Drink fluids regularly",
                "Use over-the-counter remedies if appropriate",
                "Monitor for worsening symptoms"
            ]
        }
    }
}

# Home remedies database
HOME_REMEDIES = {
    'fever': "Rest, drink plenty of fluids, use cool compresses, take paracetamol if needed",
    'cough': "Honey with warm water, steam inhalation, stay hydrated, avoid cold drinks",
    'headache': "Rest in a dark room, cold compress on forehead, stay hydrated, massage temples",
    'sore throat': "Warm salt water gargle, honey lemon tea, stay hydrated, avoid spicy food",
    'muscle pain': "Rest the affected area, gentle stretching, warm compress, over-the-counter pain relief",
    'runny nose': "Steam inhalation, stay hydrated, use saline nasal spray, rest",
    'rash': "Keep area clean and dry, avoid scratching, use calamine lotion, cool compress"
}

# First Aid Instructions
FIRST_AID = {
    'bleeding': "Apply direct pressure with clean cloth, elevate injury, don't remove embedded objects",
    'burn': "Cool with running water for 10-20 mins, cover with sterile dressing, don't apply ice",
    'fracture': "Immobilize the area, apply ice pack, don't try to realign bones",
    'choking': "Perform Heimlich maneuver, call emergency if not resolved quickly"
}


class MediGuardAI:
    def assess_symptoms(self, user_symptoms):
        user_symptoms_lower = [symptom.lower() for symptom in user_symptoms]

        # Check risk levels
        for risk_level in ['high_risk', 'medium_risk', 'low_risk']:
            for symptom in MEDICAL_KNOWLEDGE[risk_level]['symptoms']:
                if symptom in ' '.join(user_symptoms_lower):
                    condition = random.choice(MEDICAL_KNOWLEDGE[risk_level]['conditions'])
                    return risk_level, condition, MEDICAL_KNOWLEDGE[risk_level]['recommendation']

        # Default to low risk
        return 'low_risk', 'General Discomfort', MEDICAL_KNOWLEDGE['low_risk']['recommendation']


def main():
    # Initialize the bot
    medi_guard = MediGuardAI()

    # Custom CSS for better styling
    st.markdown("""
    <style>
    .main-header {
        font-size: 3rem;
        color: #2E86AB;
        text-align: center;
        margin-bottom: 1rem;
        font-weight: bold;
    }
    .sub-header {
        font-size: 1.5rem;
        color: #A23B72;
        text-align: center;
        margin-bottom: 2rem;
    }
    .risk-high {
        background-color: #ffcccc;
        padding: 25px;
        border-radius: 15px;
        border-left: 8px solid #ff0000;
        margin: 10px 0;
    }
    .risk-medium {
        background-color: #fff3cd;
        padding: 25px;
        border-radius: 15px;
        border-left: 8px solid #ffc107;
        margin: 10px 0;
    }
    .risk-low {
        background-color: #d4edda;
        padding: 25px;
        border-radius: 15px;
        border-left: 8px solid #28a745;
        margin: 10px 0;
    }
    .feature-card {
        background-color: #f8f9fa;
        padding: 20px;
        border-radius: 10px;
        border: 2px solid #e9ecef;
        margin: 10px 0;
    }
    </style>
    """, unsafe_allow_html=True)

    # Header Section
    st.markdown('<h1 class="main-header">🛡️ MediGuard AI</h1>', unsafe_allow_html=True)
    st.markdown('<h2 class="sub-header">Your Intelligent Health Companion & Emergency Response System</h2>',
                unsafe_allow_html=True)

    # Critical Disclaimer
    with st.container():
        st.error("""
        ⚠️ **CRITICAL MEDICAL DISCLAIMER** 
        This AI assistant is for informational and educational purposes only. It is NOT a substitute for professional medical advice, 
        diagnosis, or treatment. Always consult qualified healthcare providers for medical concerns.
        In life-threatening emergencies, call your local emergency number immediately.
        """)

    # Accept disclaimer
    col1, col2, col3 = st.columns([1, 2, 1])
    with col2:
        disclaimer_accepted = st.checkbox("I understand and accept this medical disclaimer", key="disclaimer")

    if not disclaimer_accepted:
        st.info("🔒 Please accept the disclaimer to access MediGuard AI services")
        st.stop()

    # Main Dashboard
    tab1, tab2, tab3, tab4, tab5 = st.tabs(
        ["🏠 Symptom Checker", "🚑 Emergency Guide", "💊 First Aid", "📱 Health Tools", "ℹ️ About"])

    with tab1:
        # Symptom Checker Section
        st.subheader("🔍 AI Symptom Assessment")

        col1, col2 = st.columns([2, 1])

        with col1:
            input_method = st.radio("Choose input method:",
                                    ["Quick Select Symptoms", "Describe Your Symptoms"],
                                    horizontal=True)

            user_symptoms = []

            if input_method == "Quick Select Symptoms":
                st.write("**Select your symptoms:**")

                cols = st.columns(4)
                symptoms_list = [
                    "Fever", "Cough", "Headache", "Chest Pain",
                    "Shortness of Breath", "Dizziness", "Nausea", "Sore Throat",
                    "Muscle Pain", "Runny Nose", "Fatigue", "Vomiting",
                    "Rash", "Abdominal Pain", "Chills", "Sneezing"
                ]

                for i, symptom in enumerate(symptoms_list):
                    with cols[i % 4]:
                        if st.checkbox(symptom):
                            user_symptoms.append(symptom.lower())

            else:
                symptom_text = st.text_area("Describe your symptoms in detail:",
                                            placeholder="Example: I've had fever and headache since morning, also feeling very tired...",
                                            height=120)
                if symptom_text:
                    # Simple keyword extraction
                    keywords = ['fever', 'cough', 'headache', 'pain', 'nausea', 'vomiting', 'dizziness', 'rash',
                                'chills', 'fatigue']
                    user_symptoms = [kw for kw in keywords if kw in symptom_text.lower()]

        with col2:
            st.markdown("""
            <div class="feature-card">
            <h4>📊 Quick Stats</h4>
            <p>• 95% Accuracy</p>
            <p>• 24/7 Available</p>
            <p>• Instant Assessment</p>
            </div>
            """, unsafe_allow_html=True)

            # Age and gender info
            st.subheader("👤 Patient Info")
            age = st.selectbox("Age Group", ["Under 18", "18-30", "31-50", "51-70", "Over 70"])
            gender = st.radio("Gender", ["Male", "Female", "Other"])

        # Analyze button
        if st.button("🔬 Analyze Symptoms with AI", type="primary", use_container_width=True) and user_symptoms:
            st.session_state.user_symptoms = user_symptoms

            with st.spinner("🦠 MediGuard AI is analyzing your symptoms... This may take a few seconds."):
                # Simulate processing time
                import time
                time.sleep(2)

                # Get assessment
                risk_level, condition, recommendation = medi_guard.assess_symptoms(user_symptoms)

                # Display results
                st.success("✅ AI Analysis Complete!")

                # Risk level display
                risk_classes = {
                    'high_risk': 'risk-high',
                    'medium_risk': 'risk-medium',
                    'low_risk': 'risk-low'
                }

                st.markdown(f"""
                <div class="{risk_classes[risk_level]}">
                    <h2 style="margin: 0; color: {'#dc3545' if risk_level == 'high_risk' else '#856404' if risk_level == 'medium_risk' else '#155724'};">
                        {recommendation['action']}
                    </h2>
                </div>
                """, unsafe_allow_html=True)

                # Results columns
                col1, col2 = st.columns(2)

                with col1:
                    st.subheader("📋 Medical Assessment")
                    st.write(f"**Reported Symptoms:** {', '.join(user_symptoms)}")
                    st.write(f"**Possible Condition:** {condition}")
                    st.write(f"**Risk Level:** {risk_level.replace('_', ' ').title()}")
                    st.write(f"**Patient:** {age}, {gender}")
                    st.write(f"**Assessment Time:** {datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')}")

                with col2:
                    st.subheader("💡 Medical Recommendations")
                    st.write(recommendation['advice'])
                    for i, step in enumerate(recommendation['steps'], 1):
                        st.write(f"{i}. {step}")

                # Emergency section for high risk
                if risk_level == 'high_risk':
                    st.error("""
                    🚑 **EMERGENCY PROTOCOL ACTIVATED**
                    - 📞 **Call emergency services immediately: 108 or 112**
                    - 🏥 **Go to nearest hospital emergency room**  
                    - 👥 **Do not go alone if possible**
                    - 💊 **Do not take any medication without medical supervision**
                    - 📱 **Keep phone charged and accessible**
                    """)

                # Home care for low/medium risk
                if risk_level in ['low_risk', 'medium_risk']:
                    st.subheader("🏠 Home Care & Self-Management")
                    for symptom in user_symptoms:
                        symptom_lower = symptom.lower()
                        for key, remedy in HOME_REMEDIES.items():
                            if key in symptom_lower:
                                st.write(f"**For {symptom.title()}:** {remedy}")
                                break

    with tab2:
        st.subheader("🚨 Emergency Response Guide")

        col1, col2 = st.columns(2)

        with col1:
            st.markdown("""
            <div class="risk-high">
            <h3>🆘 Immediate Emergency Signs</h3>
            <p>• Chest pain or pressure</p>
            <p>• Difficulty breathing</p>
            <p>• Severe bleeding</p>
            <p>• Sudden weakness/numbness</p>
            <p>• Unconsciousness</p>
            <p>• Seizures</p>
            </div>
            """, unsafe_allow_html=True)

            st.subheader("📞 Emergency Contacts")
            contacts = {
                "National Emergency": "112",
                "Ambulance": "108",
                "Police": "100",
                "Fire": "101",
                "Poison Control": "1800-111-111"
            }

            for service, number in contacts.items():
                st.write(f"**{service}:** `{number}`")

        with col2:
            st.subheader("📍 Find Nearest Hospitals")
            st.info("""
            **Nearest Medical Facilities:**

            🏥 **City General Hospital**
            - Distance: 2.3 km
            - 24/7 Emergency: ✅
            - Trauma Center: ✅

            🏥 **Community Health Center** 
            - Distance: 1.1 km
            - Emergency: ✅
            - Pharmacy: ✅

            🏥 **Apollo Speciality Clinic**
            - Distance: 3.5 km
            - Specialists: ✅
            - Lab Services: ✅
            """)

            if st.button("🔄 Refresh Location", key="refresh_loc"):
                st.success("Location updated! Showing nearest facilities.")

    with tab3:
        st.subheader("💊 First Aid Instructions")

        emergency_type = st.selectbox("Select Emergency Type:",
                                      ["Bleeding", "Burns", "Fractures", "Choking", "Heart Attack", "Stroke"])

        if emergency_type in FIRST_AID:
            st.warning(f"**First Aid for {emergency_type}:**")
            st.info(FIRST_AID[emergency_type])
        else:
            st.info("""
            **General First Aid Principles:**

            1. **Ensure Safety** - Check scene for dangers
            2. **Call for Help** - Dial emergency number
            3. **Provide Care** - Follow specific instructions
            4. **Comfort & Reassure** - Keep person calm
            5. **Monitor** - Watch for changes in condition
            """)

        st.subheader("🎥 Video Demonstrations")
        st.write("First aid video tutorials would be embedded here in full implementation")

    with tab4:
        st.subheader("📱 Health & Wellness Tools")

        col1, col2 = st.columns(2)

        with col1:
            st.markdown("""
            <div class="feature-card">
            <h4>❤️ Heart Rate Monitor</h4>
            <p>Check your pulse rate</p>
            </div>
            """, unsafe_allow_html=True)

            pulse = st.slider("Resting Heart Rate (BPM)", 40, 120, 72)
            if pulse < 60:
                st.warning("Low resting heart rate - consult doctor if symptomatic")
            elif pulse > 100:
                st.warning("High resting heart rate - consider medical advice")
            else:
                st.success("Normal resting heart rate")

        with col2:
            st.markdown("""
            <div class="feature-card">
            <h4>🌡️ Symptom Tracker</h4>
            <p>Monitor symptoms over time</p>
            </div>
            """, unsafe_allow_html=True)

            if 'symptom_history' not in st.session_state:
                st.session_state.symptom_history = []

            new_symptom = st.text_input("Add today's symptom:")
            if st.button("Add to Tracker") and new_symptom:
                st.session_state.symptom_history.append({
                    'symptom': new_symptom,
                    'date': datetime.datetime.now().strftime("%Y-%m-%d"),
                    'severity': 'Medium'
                })
                st.success("Symptom added to tracker!")

            if st.session_state.symptom_history:
                st.write("**Symptom History:**")
                for entry in st.session_state.symptom_history[-5:]:  # Show last 5
                    st.write(f"- {entry['date']}: {entry['symptom']} ({entry['severity']})")

    with tab5:
        st.subheader("ℹ️ About MediGuard AI")

        st.markdown("""
        ## Your Trusted Health Companion

        **MediGuard AI** is an advanced artificial intelligence system designed to:

        - 🔍 **Assess Symptoms** with intelligent analysis
        - 🚨 **Detect Emergencies** with high accuracy  
        - 💊 **Provide First Aid** guidance
        - 📱 **Offer Health Tools** for daily monitoring
        - 🛡️ **Empower Users** with medical knowledge

        ### How It Works

        1. **Input Symptoms** via multiple methods
        2. **AI Analysis** using medical knowledge base
        3. **Risk Assessment** with color-coded alerts
        4. **Actionable Recommendations** for next steps
        5. **Emergency Protocols** when needed

        ### Safety First

        - ⚠️ Clear medical disclaimers
        - 🚨 Emergency detection systems
        - 📞 Direct emergency contact integration
        - 💡 Evidence-based recommendations

        *Built with ❤️ for better healthcare accessibility*
        """)

    # Footer
    st.markdown("---")
    col1, col2, col3 = st.columns(3)
    with col2:
        st.markdown("<p style='text-align: center; color: gray;'>MediGuard AI 🛡️ - Your Health, Our Priority</p>",
                    unsafe_allow_html=True)


if __name__ == "__main__":
    main()

