import streamlit as st
from copy import deepcopy

# 1. Page Setup
st.set_page_config(
    page_title="UniBridge",
    page_icon="🎓",
    layout="wide",
    initial_sidebar_state="expanded"
)

# 2. Initial Data Structure
INITIAL_DATA = {
    "seniors": [],
    "juniors": [],
    "questions": [],
    "answers": [],
    "universities": [],
    "connections": 0,
    "current_user": "",
    "current_role": "",
    "uploaded_files": [],
    "model_settings": {
        "model": "Gemini",
        "temperature": 0.7,
        "max_tokens": 1000,
        "prompt": "You are a helpful university guidance assistant."
    },
    "settings": {
        "name": "",
        "university": "",
        "notifications": True,
        "email": True,
        "theme": "Light"
    }
}

# Initialize Session State
if "data" not in st.session_state:
    st.session_state.data = deepcopy(INITIAL_DATA)

data = st.session_state.data

# 3. Custom CSS Theme
PRIMARY = "#0F766E"
PRIMARY_DARK = "#115E59"
PRIMARY_LIGHT = "#CCFBF1"
NAVY = "#0B1F26"
NAVY_LIGHT = "#12343B"
TEXT = "#334155"
HEADING = "#12343B"
MUTED = "#64748B"
BACKGROUND = "#F4F8F7"
WHITE = "#FFFFFF"
BORDER = "#CBD5E1"

st.markdown(f"""
<style>
    .main {{ background-color: {BACKGROUND}; }}
    .stApp {{ max-width: 100%; }}
    
    .top-header {{
        background: {WHITE};
        border-bottom: 1px solid {BORDER};
        padding: 16px 24px;
        border-radius: 12px;
        margin-bottom: 20px;
        box-shadow: 0 4px 12px rgba(0,0,0,0.03);
    }}
    .brand-name {{ color: {HEADING}; font-size: 26px; font-weight: 800; }}
    .brand-name span {{ color: {PRIMARY}; }}
    .brand-tagline {{ color: {MUTED}; font-size: 13px; margin-top: 2px; }}
    
    .welcome-banner {{
        background: linear-gradient(120deg, {NAVY}, {NAVY_LIGHT} 55%, {PRIMARY});
        color: {WHITE};
        border-radius: 16px;
        padding: 28px;
        margin-bottom: 24px;
    }}
    .welcome-banner h2 {{ margin: 0 0 8px; font-size: 26px; color: {WHITE} !important; }}
    .welcome-banner p {{ margin: 0; font-size: 14px; opacity: 0.9; color: {WHITE} !important; }}
    
    .stat-card {{
        background: {WHITE};
        border: 1px solid {BORDER};
        border-radius: 12px;
        padding: 16px;
        text-align: center;
        box-shadow: 0 4px 10px rgba(15,23,42,.04);
    }}
    .stat-number {{ font-size: 24px; font-weight: 800; color: {PRIMARY}; }}
    .stat-label {{ font-size: 12px; font-weight: 700; color: {HEADING}; }}
    
    .question-card {{
        background: {WHITE};
        border: 1px solid {BORDER};
        border-radius: 12px;
        padding: 18px;
        margin-bottom: 14px;
    }}
    .question-id {{
        display: inline-block;
        padding: 4px 10px;
        background: {PRIMARY_LIGHT};
        color: {PRIMARY_DARK};
        font-weight: 800;
        border-radius: 6px;
        font-size: 12px;
        margin-bottom: 8px;
    }}
</style>
""", unsafe_allow_html=True)

# 4. Global Header Banner
st.markdown(f"""
<div class="top-header">
    <div class="brand-name">🎓 Uni<span>Bridge</span></div>
    <div class="brand-tagline">Your university, Your seniors, Your guide.</div>
</div>
""", unsafe_allow_html=True)

# 5. Dynamic Navigation Sidebar
st.sidebar.markdown("### 📌 MAIN MENU")

current_user = data.get("current_user", "")
current_role = data.get("current_role", "")

if not current_user:
    pages = ["Registration"]
else:
    if current_role == "Junior":
        pages = ["Dashboard", "Ask a Question", "History", "Data Upload", "Model Settings", "Run Prediction", "Results", "Settings"]
    else:
        pages = ["Dashboard", "Senior Questions", "History", "Data Upload", "Model Settings", "Run Prediction", "Results", "Settings"]

selected_page = st.sidebar.radio("Go to", pages)

st.sidebar.markdown("---")
if current_user:
    st.sidebar.markdown(f"👤 **{current_user}** ({current_role})")
else:
    st.sidebar.markdown("👤 **Guest User**")
st.sidebar.caption("🎓 *Small steps today, big dreams tomorrow.*")

# Helper functions
def clean_text(val):
    return (val or "").strip()

def normalize(val):
    return clean_text(val).casefold()

# ============================================================
# PAGE 1: REGISTRATION
# ============================================================
if selected_page == "Registration":
    st.markdown("""
    <div class="welcome-banner">
        <h2>Welcome to UniBridge! 👋</h2>
        <p>First, create your profile. Your role decides which guidance menu opens next.</p>
    </div>
    """, unsafe_allow_html=True)
    
    with st.form("registration_form"):
        st.subheader("👤 Create Profile")
        name = st.text_input("Name", placeholder="Enter your full name")
        role = st.radio("Register As", ["Senior", "Junior"])
        university = st.text_input("University", placeholder="e.g. University of Engineering")
        department = st.text_input("Department", placeholder="e.g. Computer Science / AI")
        
        submit_reg = st.form_submit_button("Create Profile")
        if submit_reg:
            if not clean_text(name) or not clean_text(university):
                st.error("⚠️ Please fill in all required fields (Name and University).")
            else:
                existing = data["seniors"] if role == "Senior" else data["juniors"]
                duplicate = any(
                    normalize(p["name"]) == normalize(name) and 
                    normalize(p["university"]) == normalize(university)
                    for p in existing
                )
                if duplicate:
                    st.error("⚠️ Profile already exists.")
                else:
                    person = {"name": name, "university": university, "department": department or "General"}
                    existing.append(person)
                    if normalize(university) not in [normalize(u) for u in data["universities"]]:
                        data["universities"].append(university)
                    
                    data["current_user"] = name
                    data["current_role"] = role
                    data["settings"]["name"] = name
                    data["settings"]["university"] = university
                    st.success(f"🎉 Registration successful! Logged in as **{name}** ({role}).")
                    st.rerun()

# ============================================================
# PAGE 2: DASHBOARD
# ============================================================
elif selected_page == "Dashboard":
    st.markdown("""
    <div class="welcome-banner">
        <h2>UniBridge Dashboard 🏠</h2>
        <p>Track your university community and access your role-based guidance tools.</p>
    </div>
    """, unsafe_allow_html=True)
    
    c1, c2, c3, c4, c5 = st.columns(5)
    c1.markdown(f"<div class='stat-card'><div class='stat-number'>{len(data['seniors'])}</div><div class='stat-label'>Seniors</div></div>", unsafe_allow_html=True)
    c2.markdown(f"<div class='stat-card'><div class='stat-number'>{len(data['juniors'])}</div><div class='stat-label'>Juniors</div></div>", unsafe_allow_html=True)
    c3.markdown(f"<div class='stat-card'><div class='stat-number'>{len(data['questions'])}</div><div class='stat-label'>Questions</div></div>", unsafe_allow_html=True)
    c4.markdown(f"<div class='stat-card'><div class='stat-number'>{len(data['answers'])}</div><div class='stat-label'>Answers</div></div>", unsafe_allow_html=True)
    c5.markdown(f"<div class='stat-card'><div class='stat-number'>{len(data['universities'])}</div><div class='stat-label'>Universities</div></div>", unsafe_allow_html=True)

    st.markdown("### 👨‍🎓 Search Seniors")
    col_a, col_b = st.columns(2)
    s_univ = col_a.text_input("Filter by University")
    s_dept = col_b.text_input("Filter by Department")
    
    if st.button("Find Seniors"):
        su, sd = normalize(s_univ), normalize(s_dept)
        results = [s for s in data["seniors"] if (not su or su in normalize(s["university"])) and (not sd or sd in normalize(s["department"]))]
        if results:
            for s in results:
                st.info(f"👤 **{s['name']}** | 🏫 **University:** {s['university']} | 📚 **Dept:** {s['department']}")
        else:
            st.warning("No matching seniors found.")

    st.markdown("### 🎓 Search Juniors")
    col_c, col_d = st.columns(2)
    j_univ = col_c.text_input("Filter Juniors by University")
    j_dept = col_d.text_input("Filter Juniors by Department")
    
    if st.button("Find Juniors"):
        ju, jd = normalize(j_univ), normalize(j_dept)
        results = [j for j in data["juniors"] if (not ju or ju in normalize(j["university"])) and (not jd or jd in normalize(j["department"]))]
        if results:
            for j in results:
                st.info(f"👤 **{j['name']}** | 🏫 **University:** {j['university']} | 📚 **Dept:** {j['department']}")
        else:
            st.warning("No matching juniors found.")

# ============================================================
# PAGE 3: ASK A QUESTION (JUNIORS ONLY)
# ============================================================
elif selected_page == "Ask a Question":
    st.subheader("💬 Ask a Senior")
    q_text = st.text_area("Your Question", placeholder="Ask anything about academics, guidance, or university life...")
    q_dept = st.text_input("Department", value=data["settings"].get("department", ""))
    
    if st.button("Post Question"):
        if not clean_text(q_text):
            st.error("⚠️ Please enter a question.")
        else:
            used_ids = [int(q.get("id", 0)) for q in data.get("questions", [])]
            q_id = max(used_ids, default=0) + 1
            data["questions"].append({
                "id": q_id,
                "question": q_text,
                "department": q_dept or "General",
                "asked_by": data["current_user"],
                "answer": "",
                "answered_by": ""
            })
            st.success(f"✅ Question posted with **Question ID Q{q_id:03d}**!")

# ============================================================
# PAGE 4: SENIOR QUESTIONS (SENIORS ONLY)
# ============================================================
elif selected_page == "Senior Questions":
    st.subheader("❓ Unanswered Questions from Juniors")
    unanswered = [q for q in data["questions"] if not clean_text(q.get("answer", ""))]
    
    if not unanswered:
        st.info("There are currently no unanswered questions.")
    else:
        for q in unanswered:
            st.markdown(f"""
            <div class="question-card">
                <span class="question-id">Q{int(q['id']):03d}</span>
                <h4>{q['question']}</h4>
                <p>📚 <b>Department:</b> {q['department']} | 👤 <b>Asked by:</b> {q['asked_by']}</p>
            </div>
            """, unsafe_allow_html=True)
        
        q_options = {f"Q{int(q['id']):03d} - {q['question'][:40]}...": q["id"] for q in unanswered}
        selected_q = st.selectbox("Select Question to Answer", list(q_options.keys()))
        answer_text = st.text_area("Your Senior Answer")
        
        if st.button("Post Answer"):
            if not clean_text(answer_text):
                st.error("⚠️ Please write an answer.")
            else:
                target_id = q_options[selected_q]
                for q in data["questions"]:
                    if q["id"] == target_id:
                        q["answer"] = answer_text
                        q["answered_by"] = data["current_user"]
                        data["answers"].append({
                            "question_id": target_id,
                            "answer": answer_text,
                            "answered_by": data["current_user"]
                        })
                        st.success(f"✅ Answer posted for Q{target_id:03d}!")
                        st.rerun()

# ============================================================
# PAGE 5: HISTORY
# ============================================================
elif selected_page == "History":
    st.subheader("📜 Question & Answer History")
    answered = [q for q in data["questions"] if clean_text(q.get("answer", ""))]
    
    if not answered:
        st.info("No questions have been answered yet.")
    else:
        for q in answered:
            st.markdown(f"""
            <div class="question-card">
                <span class="question-id">Q{int(q['id']):03d}</span>
                <h4>❓ {q['question']}</h4>
                <p>📚 <b>Department:</b> {q['department']} | 👤 <b>Asked by:</b> {q['asked_by']}</p>
                <hr style="margin: 10px 0;">
                <p style="color: {PRIMARY_DARK}; font-weight: bold;">✅ Senior Answer:</p>
                <p>{q['answer']}</p>
                <p style="font-size: 12px; color: {MUTED};">👨‍🎓 <b>Answered by:</b> {q['answered_by']}</p>
            </div>
            """, unsafe_allow_html=True)

# ============================================================
# PAGE 6: DATA UPLOAD
# ============================================================
elif selected_page == "Data Upload":
    st.subheader("📤 Upload Documents")
    uploaded_files = st.file_uploader("Upload course materials, notes, or resources", accept_multiple_files=True)
    
    if st.button("Process Uploads"):
        if uploaded_files:
            for file in uploaded_files:
                if file.name not in data["uploaded_files"]:
                    data["uploaded_files"].append(file.name)
            st.success("✅ Files successfully attached to session state.")
        else:
            st.warning("⚠️ Please select files to upload.")
            
    if data["uploaded_files"]:
        st.markdown("#### Stored Session Files:")
        for fname in data["uploaded_files"]:
            st.markdown(f"- 📄 **{fname}**")

# ============================================================
# PAGE 7: MODEL SETTINGS
# ============================================================
elif selected_page == "Model Settings":
    st.subheader("⚙️ AI Guidance Model Settings")
    model = st.selectbox("Select Model", ["Gemini", "GPT-4", "Claude"], index=0)
    temp = st.slider("Temperature", 0.0, 1.0, data["model_settings"]["temperature"])
    tokens = st.number_input("Max Tokens", 100, 4000, data["model_settings"]["max_tokens"])
    prompt = st.text_area("System Prompt", value=data["model_settings"]["prompt"])
    
    if st.button("Save Model Settings"):
        data["model_settings"] = {
            "model": model,
            "temperature": temp,
            "max_tokens": tokens,
            "prompt": prompt
        }
        st.success("✅ Model Settings Saved!")

# ============================================================
# PAGE 8: RUN PREDICTION
# ============================================================
elif selected_page == "Run Prediction":
    st.subheader("🚀 Run AI Senior Prediction")
    query = st.text_input("Enter your guidance query:")
    
    if st.button("Generate Guidance"):
        if not clean_text(query):
            st.warning("⚠️ Please enter a prompt query.")
        else:
            st.markdown(f"""
            ### 💡 Suggested Guidance
            > {query}
            
            1. 📚 Check official course syllabi and guidelines.
            2. 👨‍🎓 Consult senior students within your department.
            3. 📝 Maintain consistent study schedules and track project deadlines.
            
            *Config:* Model **{data['model_settings']['model']}** | Temp **{data['model_settings']['temperature']}**
            """)

# ============================================================
# PAGE 9: RESULTS
# ============================================================
elif selected_page == "Results":
    st.subheader("📊 Platform Results & Analytics")
    st.json({
        "Seniors": len(data["seniors"]),
        "Juniors": len(data["juniors"]),
        "Questions": len(data["questions"]),
        "Answers": len(data["answers"]),
        "Universities": len(data["universities"]),
        "Uploaded Files": len(data["uploaded_files"])
    })

# ============================================================
# PAGE 10: SETTINGS
# ============================================================
elif selected_page == "Settings":
    st.subheader("🔧 System & Profile Settings")
    set_name = st.text_input("User Name", value=data["settings"].get("name", ""))
    set_univ = st.text_input("University", value=data["settings"].get("university", ""))
    set_notif = st.checkbox("Notifications Enabled", value=data["settings"].get("notifications", True))
    set_email = st.checkbox("Email Alerts Enabled", value=data["settings"].get("email", True))
    set_theme = st.selectbox("UI Theme", ["Light", "Dark"], index=0)
    
    if st.button("Save Settings"):
        data["settings"] = {
            "name": set_name,
            "university": set_univ,
            "notifications": set_notif,
            "email": set_email,
            "theme": set_theme
        }
        if set_name:
            data["current_user"] = set_name
        st.success("✅ System Settings Saved!")
        st.rerun()
