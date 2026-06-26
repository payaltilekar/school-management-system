import json
import streamlit as st
from pathlib import Path

st.set_page_config(
    page_title="EduTrack — School Management",
    page_icon="🎓",
    layout="wide",
)

# ══════════════════════════════════════════════════════════════════════════════
# DESIGN SYSTEM
# Deep navy + electric violet + warm gold accent
# Input fix: white text + white placeholder on dark field
# ══════════════════════════════════════════════════════════════════════════════
st.markdown("""
<style>
@import url('https://fonts.googleapis.com/css2?family=Space+Grotesk:wght@400;500;600;700&family=Inter:wght@300;400;500&display=swap');

/* ── Reset & base ── */
*, *::before, *::after { box-sizing: border-box; }

[data-testid="stAppViewContainer"] {
    background: #080b14;
    font-family: 'Inter', sans-serif;
}

/* ── Sidebar ── */
[data-testid="stSidebar"] {
    background: #0d1120 !important;
    border-right: 1px solid #1e2740 !important;
    padding-top: 0 !important;
}
[data-testid="stSidebar"] > div:first-child { padding-top: 0 !important; }
section[data-testid="stSidebar"] * { color: #c8d0e7 !important; }

/* ── Typography ── */
h1 { font-family: 'Space Grotesk', sans-serif !important; font-size: 2rem !important;
     font-weight: 700 !important; color: #f0f4ff !important; letter-spacing: -0.5px; }
h2 { font-family: 'Space Grotesk', sans-serif !important; font-size: 1.4rem !important;
     font-weight: 600 !important; color: #e0e8ff !important; }
h3 { font-family: 'Space Grotesk', sans-serif !important; font-size: 1.1rem !important;
     font-weight: 600 !important; color: #c8d4f8 !important; }
p, div, label, span { color: #a8b4d0 !important; font-family: 'Inter', sans-serif !important; }

/* ── Metrics ── */
[data-testid="metric-container"] {
    background: linear-gradient(135deg, #111827 0%, #1a2035 100%) !important;
    border: 1px solid #2a3555 !important;
    border-radius: 16px !important;
    padding: 20px 24px !important;
    position: relative;
    overflow: hidden;
}
[data-testid="metric-container"]::before {
    content: '';
    position: absolute; top: 0; left: 0;
    width: 4px; height: 100%;
    background: linear-gradient(180deg, #7c3aed, #4f46e5);
    border-radius: 4px 0 0 4px;
}
[data-testid="stMetricValue"] {
    font-family: 'Space Grotesk', sans-serif !important;
    color: #ffffff !important; font-size: 2.2rem !important; font-weight: 700 !important;
}
[data-testid="stMetricLabel"] { color: #6b7fa8 !important; font-size: 0.8rem !important; text-transform: uppercase; letter-spacing: 0.8px; }

/* ══════════════════════════════════════════════
   INPUT FIX — visible white text while typing
   ══════════════════════════════════════════════ */
input[type="text"],
input[type="email"],
input[type="number"],
[data-testid="stTextInput"] input,
[data-testid="stNumberInput"] input,
div[data-baseweb="input"] input,
div[data-baseweb="base-input"] input {
    background-color: #151d2e !important;
    color: #ffffff !important;
    caret-color: #7c3aed !important;
    border: 1.5px solid #2a3555 !important;
    border-radius: 10px !important;
    font-family: 'Inter', sans-serif !important;
    font-size: 0.95rem !important;
    padding: 10px 14px !important;
    -webkit-text-fill-color: #ffffff !important;
}
div[data-baseweb="input"],
div[data-baseweb="base-input"] {
    background-color: #151d2e !important;
    border-radius: 10px !important;
}
input::placeholder,
[data-testid="stTextInput"] input::placeholder,
[data-testid="stNumberInput"] input::placeholder {
    color: #4a5878 !important;
    -webkit-text-fill-color: #4a5878 !important;
    opacity: 1 !important;
}
input:focus,
[data-testid="stTextInput"] input:focus,
[data-testid="stNumberInput"] input:focus {
    border-color: #7c3aed !important;
    box-shadow: 0 0 0 3px rgba(124, 58, 237, 0.15) !important;
    outline: none !important;
    color: #ffffff !important;
    -webkit-text-fill-color: #ffffff !important;
}

/* Labels above inputs */
[data-testid="stTextInput"] label,
[data-testid="stNumberInput"] label,
[data-testid="stSelectbox"] label {
    color: #8899c0 !important;
    font-size: 0.8rem !important;
    font-weight: 500 !important;
    letter-spacing: 0.5px !important;
    text-transform: uppercase !important;
}

/* ── Selectbox ── */
[data-testid="stSelectbox"] > div > div {
    background-color: #151d2e !important;
    border: 1.5px solid #2a3555 !important;
    border-radius: 10px !important;
    color: #ffffff !important;
}
[data-testid="stSelectbox"] svg { color: #7c3aed !important; fill: #7c3aed !important; }

/* ── Buttons ── */
.stButton > button {
    background: linear-gradient(135deg, #7c3aed 0%, #4f46e5 100%) !important;
    color: #ffffff !important;
    border: none !important;
    border-radius: 10px !important;
    padding: 0.6rem 1.8rem !important;
    font-family: 'Space Grotesk', sans-serif !important;
    font-weight: 600 !important;
    font-size: 0.95rem !important;
    letter-spacing: 0.3px !important;
    transition: all 0.2s ease !important;
    box-shadow: 0 4px 15px rgba(124, 58, 237, 0.3) !important;
}
.stButton > button:hover {
    transform: translateY(-1px) !important;
    box-shadow: 0 6px 20px rgba(124, 58, 237, 0.45) !important;
}
.stButton > button:active { transform: translateY(0px) !important; }

/* ── Tabs ── */
[data-testid="stTabs"] [role="tablist"] {
    background: #0d1120;
    border-radius: 12px;
    padding: 4px;
    border: 1px solid #1e2740;
    gap: 4px;
}
[data-testid="stTabs"] button[role="tab"] {
    border-radius: 8px !important;
    color: #6b7fa8 !important;
    font-family: 'Space Grotesk', sans-serif !important;
    font-weight: 500 !important;
    padding: 8px 20px !important;
    border: none !important;
    background: transparent !important;
}
[data-testid="stTabs"] button[role="tab"][aria-selected="true"] {
    background: linear-gradient(135deg, #7c3aed, #4f46e5) !important;
    color: #ffffff !important;
}

/* ── Dataframe ── */
[data-testid="stDataFrame"] {
    border: 1px solid #1e2740 !important;
    border-radius: 12px !important;
    overflow: hidden !important;
}
[data-testid="stDataFrame"] th {
    background: #111827 !important;
    color: #8899c0 !important;
    font-size: 0.75rem !important;
    text-transform: uppercase !important;
    letter-spacing: 0.8px !important;
}
[data-testid="stDataFrame"] td { color: #c8d4f8 !important; }

/* ── Alerts ── */
[data-testid="stAlertContentSuccess"] {
    background: rgba(16,185,129,0.1) !important;
    border: 1px solid rgba(16,185,129,0.3) !important;
    border-radius: 10px !important;
    color: #34d399 !important;
}
[data-testid="stAlertContentError"] {
    background: rgba(239,68,68,0.1) !important;
    border: 1px solid rgba(239,68,68,0.3) !important;
    border-radius: 10px !important;
}
[data-testid="stAlertContentWarning"] {
    background: rgba(251,191,36,0.1) !important;
    border: 1px solid rgba(251,191,36,0.3) !important;
    border-radius: 10px !important;
}
[data-testid="stAlertContentInfo"] {
    background: rgba(99,102,241,0.1) !important;
    border: 1px solid rgba(99,102,241,0.3) !important;
    border-radius: 10px !important;
    color: #a5b4fc !important;
}

/* ── Radio nav ── */
[data-testid="stRadio"] > div { gap: 4px !important; }
[data-testid="stRadio"] label {
    background: transparent !important;
    border-radius: 8px !important;
    padding: 8px 12px !important;
    cursor: pointer !important;
    transition: background 0.15s !important;
}
[data-testid="stRadio"] label:hover { background: #1e2740 !important; }

/* ── Divider ── */
hr { border-color: #1e2740 !important; }

/* ── Scrollbar ── */
::-webkit-scrollbar { width: 6px; }
::-webkit-scrollbar-track { background: #080b14; }
::-webkit-scrollbar-thumb { background: #2a3555; border-radius: 3px; }

/* ── Card-style container ── */
.card-box {
    background: linear-gradient(135deg, #111827 0%, #141c2e 100%);
    border: 1px solid #1e2740;
    border-radius: 16px;
    padding: 24px;
    margin-bottom: 16px;
}
</style>
""", unsafe_allow_html=True)


# ── Data layer ────────────────────────────────────────────────────────────────
DATABASE = "school_data.json"

def load_data():
    if Path(DATABASE).exists():
        content = Path(DATABASE).read_text()
        if content.strip():
            return json.loads(content)
    return {"students": [], "teachers": []}

def save_data():
    with open(DATABASE, "w") as f:
        json.dump(st.session_state.data, f, indent=4)

def validate_email(email: str) -> bool:
    return "@" in email and "." in email

if "data" not in st.session_state:
    st.session_state.data = load_data()


# ── Sidebar ───────────────────────────────────────────────────────────────────
with st.sidebar:
    st.markdown("""
    <div style='padding:28px 20px 20px; border-bottom:1px solid #1e2740; margin-bottom:16px;'>
        <div style='font-family:Space Grotesk,sans-serif; font-size:1.4rem; font-weight:700;
                    color:#f0f4ff; letter-spacing:-0.3px;'>🎓 EduTrack</div>
        <div style='font-size:0.78rem; color:#4a5878; margin-top:4px; font-family:Inter,sans-serif;'>
            School Management System</div>
    </div>
    """, unsafe_allow_html=True)

    page = st.radio(
        "nav",
        ["📊  Dashboard", "🎒  Students", "👩‍🏫  Teachers"],
        label_visibility="collapsed",
    )

    st.markdown("<div style='height:20px'></div>", unsafe_allow_html=True)
    st.markdown("""<div style='padding:0 8px; font-size:0.72rem; text-transform:uppercase;
                               letter-spacing:1px; color:#3a4a6b; font-family:Inter,sans-serif;
                               font-weight:600;'>OVERVIEW</div>""", unsafe_allow_html=True)

    n_s = len(st.session_state.data['students'])
    n_t = len(st.session_state.data['teachers'])
    all_g = [g for s in st.session_state.data['students'] for g in s.get('grades',{}).values()]
    school_avg = sum(all_g)/len(all_g) if all_g else 0

    st.markdown(f"""
    <div style='padding:12px 8px; display:flex; flex-direction:column; gap:10px;'>
        <div style='display:flex; justify-content:space-between; align-items:center;
                    background:#111827; border:1px solid #1e2740; border-radius:10px; padding:10px 14px;'>
            <span style='font-size:0.85rem; color:#6b7fa8; font-family:Inter,sans-serif;'>Students</span>
            <span style='font-family:Space Grotesk,sans-serif; font-weight:700; font-size:1.2rem;
                         color:#a78bfa;'>{n_s}</span>
        </div>
        <div style='display:flex; justify-content:space-between; align-items:center;
                    background:#111827; border:1px solid #1e2740; border-radius:10px; padding:10px 14px;'>
            <span style='font-size:0.85rem; color:#6b7fa8; font-family:Inter,sans-serif;'>Teachers</span>
            <span style='font-family:Space Grotesk,sans-serif; font-weight:700; font-size:1.2rem;
                         color:#a78bfa;'>{n_t}</span>
        </div>
        <div style='display:flex; justify-content:space-between; align-items:center;
                    background:#111827; border:1px solid #1e2740; border-radius:10px; padding:10px 14px;'>
            <span style='font-size:0.85rem; color:#6b7fa8; font-family:Inter,sans-serif;'>Avg Grade</span>
            <span style='font-family:Space Grotesk,sans-serif; font-weight:700; font-size:1.2rem;
                         color:#34d399;'>{school_avg:.1f}</span>
        </div>
    </div>
    """, unsafe_allow_html=True)


# ══════════════════════════════════════════════════════════════════════════════
# DASHBOARD
# ══════════════════════════════════════════════════════════════════════════════
if page == "📊  Dashboard":
    st.markdown("# 📊 Dashboard")
    st.markdown("<div style='color:#4a5878; margin-top:-12px; margin-bottom:24px; font-size:0.95rem;'>Your school at a glance</div>", unsafe_allow_html=True)

    students = st.session_state.data["students"]
    teachers = st.session_state.data["teachers"]

    col1, col2, col3 = st.columns(3)
    col1.metric("Total Students", len(students))
    col2.metric("Total Teachers", len(teachers))
    all_g = [g for s in students for g in s.get("grades", {}).values()]
    col3.metric("School Avg Grade", f"{sum(all_g)/len(all_g):.1f}" if all_g else "—")

    st.markdown("<div style='height:8px'></div>", unsafe_allow_html=True)

    left, right = st.columns([3, 2])

    with left:
        st.markdown("### 🏆 Student Leaderboard")
        if students:
            ranked = []
            for i, s in enumerate(students):
                grades = s.get("grades", {})
                avg_s = sum(grades.values()) / len(grades) if grades else 0
                ranked.append({"#": i+1, "Name": s["name"], "Roll No": s["roll_no"],
                                "Avg": round(avg_s, 1), "Subjects": len(grades)})
            ranked.sort(key=lambda x: x["Avg"], reverse=True)
            for i, r in enumerate(ranked):
                r["#"] = i + 1
            st.dataframe(ranked, use_container_width=True, hide_index=True)
        else:
            st.info("No students registered yet. Head to the Students page to add one.")

    with right:
        st.markdown("### 👩‍🏫 Teachers")
        if teachers:
            for t in teachers:
                st.markdown(f"""
                <div style='background:#111827; border:1px solid #1e2740; border-radius:12px;
                             padding:14px 16px; margin-bottom:10px; display:flex; align-items:center; gap:14px;'>
                    <div style='width:40px; height:40px; border-radius:50%;
                                background:linear-gradient(135deg,#7c3aed,#4f46e5);
                                display:flex; align-items:center; justify-content:center;
                                font-family:Space Grotesk,sans-serif; font-weight:700;
                                color:#fff; font-size:1rem; flex-shrink:0;'>
                        {t['name'][0].upper()}
                    </div>
                    <div>
                        <div style='font-family:Space Grotesk,sans-serif; font-weight:600;
                                    color:#e0e8ff; font-size:0.95rem;'>{t['name']}</div>
                        <div style='font-size:0.8rem; color:#6b7fa8;'>{t['subject']} · {t['emp_id']}</div>
                    </div>
                </div>
                """, unsafe_allow_html=True)
        else:
            st.info("No teachers registered yet.")


# ══════════════════════════════════════════════════════════════════════════════
# STUDENTS
# ══════════════════════════════════════════════════════════════════════════════
elif page == "🎒  Students":
    st.markdown("# 🎒 Students")
    st.markdown("<div style='color:#4a5878; margin-top:-12px; margin-bottom:24px; font-size:0.95rem;'>Register, grade, and review students</div>", unsafe_allow_html=True)

    tab1, tab2, tab3 = st.tabs(["➕  Register", "📝  Add Grade", "🔍  View Details"])

    with tab1:
        st.markdown("### Register a New Student")
        st.markdown("<div style='height:4px'></div>", unsafe_allow_html=True)

        c1, c2 = st.columns(2)
        name    = c1.text_input("Full Name", placeholder="e.g. Rahul Sharma", key="reg_name")
        age     = c2.number_input("Age", min_value=5, max_value=100, value=16, key="reg_age")
        email   = c1.text_input("Email Address", placeholder="rahul@example.com", key="reg_email")
        roll_no = c2.text_input("Roll Number", placeholder="e.g. STU001", key="reg_roll")

        st.markdown("<div style='height:4px'></div>", unsafe_allow_html=True)

        if st.button("Register Student →", use_container_width=True, key="btn_reg_student"):
            if not name or not email or not roll_no:
                st.error("Please fill in all fields before registering.")
            elif not validate_email(email):
                st.error("That email address doesn't look right. Include @ and a domain.")
            elif any(s["roll_no"] == roll_no for s in st.session_state.data["students"]):
                st.warning(f"Roll number **{roll_no}** is already taken.")
            else:
                st.session_state.data["students"].append({
                    "name": name, "age": int(age),
                    "email": email, "roll_no": roll_no, "grades": {}
                })
                save_data()
                st.success(f"✅ **{name}** has been registered successfully!")
                st.rerun()

    with tab2:
        st.markdown("### Add or Update a Grade")
        students = st.session_state.data["students"]
        if not students:
            st.info("Register a student first before adding grades.")
        else:
            options = {f"{s['name']}  ({s['roll_no']})": s["roll_no"] for s in students}
            choice  = st.selectbox("Select Student", list(options.keys()), key="grade_sel")
            roll_no = options[choice]

            c1, c2 = st.columns(2)
            subject = c1.text_input("Subject", placeholder="e.g. Mathematics", key="grade_sub")
            marks   = c2.number_input("Marks (out of 100)", min_value=0.0, max_value=100.0, value=0.0, step=0.5, key="grade_marks")

            if st.button("Save Grade →", use_container_width=True, key="btn_grade"):
                if not subject:
                    st.error("Please enter a subject name.")
                else:
                    for s in st.session_state.data["students"]:
                        if s["roll_no"] == roll_no:
                            s["grades"][subject] = marks
                            save_data()
                            st.success(f"✅ **{subject}: {marks:.1f}** saved for {s['name']}")
                            break
                    st.rerun()

    with tab3:
        st.markdown("### Student Details")
        students = st.session_state.data["students"]
        if not students:
            st.info("No students registered yet.")
        else:
            options = {f"{s['name']}  ({s['roll_no']})": s["roll_no"] for s in students}
            choice  = st.selectbox("Select Student", list(options.keys()), key="view_sel")
            roll_no = options[choice]

            for s in students:
                if s["roll_no"] != roll_no:
                    continue
                grades = s.get("grades", {})
                avg    = sum(grades.values()) / len(grades) if grades else 0

                # Profile card
                st.markdown(f"""
                <div style='background:linear-gradient(135deg,#111827,#141c2e); border:1px solid #1e2740;
                             border-radius:16px; padding:24px; margin:16px 0; display:flex;
                             align-items:center; gap:20px;'>
                    <div style='width:64px; height:64px; border-radius:50%;
                                background:linear-gradient(135deg,#7c3aed,#4f46e5);
                                display:flex; align-items:center; justify-content:center;
                                font-family:Space Grotesk,sans-serif; font-weight:700;
                                color:#fff; font-size:1.6rem; flex-shrink:0;'>
                        {s['name'][0].upper()}
                    </div>
                    <div>
                        <div style='font-family:Space Grotesk,sans-serif; font-weight:700;
                                    font-size:1.3rem; color:#f0f4ff;'>{s['name']}</div>
                        <div style='font-size:0.85rem; color:#6b7fa8; margin-top:2px;'>
                            Roll No: {s['roll_no']} &nbsp;·&nbsp; Age: {s['age']} &nbsp;·&nbsp; {s['email']}
                        </div>
                        <div style='margin-top:8px; display:inline-block; background:rgba(124,58,237,0.2);
                                    border:1px solid rgba(124,58,237,0.4); color:#c4b5fd;
                                    font-size:0.8rem; border-radius:20px; padding:2px 12px;
                                    font-family:Space Grotesk,sans-serif; font-weight:600;'>
                            Avg: {avg:.1f} / 100
                        </div>
                    </div>
                </div>
                """, unsafe_allow_html=True)

                if grades:
                    st.markdown("#### 📚 Subject Grades")
                    gdata = [{"Subject": sub, "Marks": f"{m:.1f}", "Status": "✅ Pass" if m >= 40 else "❌ Fail"}
                             for sub, m in grades.items()]
                    st.dataframe(gdata, use_container_width=True, hide_index=True)
                else:
                    st.info("No grades recorded yet.")
                break

            st.markdown("---")
            st.markdown("### 📋 All Students")
            rows = []
            for s in students:
                g = s.get("grades", {})
                a = sum(g.values())/len(g) if g else 0
                rows.append({"Name": s["name"], "Roll No": s["roll_no"],
                              "Age": s["age"], "Email": s["email"],
                              "Subjects": len(g), "Avg Grade": f"{a:.1f}"})
            st.dataframe(rows, use_container_width=True, hide_index=True)


# ══════════════════════════════════════════════════════════════════════════════
# TEACHERS
# ══════════════════════════════════════════════════════════════════════════════
elif page == "👩‍🏫  Teachers":
    st.markdown("# 👩‍🏫 Teachers")
    st.markdown("<div style='color:#4a5878; margin-top:-12px; margin-bottom:24px; font-size:0.95rem;'>Register and manage teaching staff</div>", unsafe_allow_html=True)

    tab1, tab2 = st.tabs(["➕  Register", "🔍  View Details"])

    with tab1:
        st.markdown("### Register a New Teacher")
        c1, c2 = st.columns(2)
        name    = c1.text_input("Full Name", placeholder="e.g. Priya Desai", key="t_name")
        age     = c2.number_input("Age", min_value=18, max_value=100, value=30, key="t_age")
        email   = c1.text_input("Email Address", placeholder="priya@school.edu", key="t_email")
        subject = c2.text_input("Subject Taught", placeholder="e.g. Physics", key="t_sub")
        emp_id  = st.text_input("Employee ID", placeholder="e.g. EMP001", key="t_emp")

        st.markdown("<div style='height:4px'></div>", unsafe_allow_html=True)

        if st.button("Register Teacher →", use_container_width=True, key="btn_reg_teacher"):
            if not name or not email or not subject or not emp_id:
                st.error("Please fill in all fields before registering.")
            elif not validate_email(email):
                st.error("That email address doesn't look right.")
            elif any(t["emp_id"] == emp_id for t in st.session_state.data["teachers"]):
                st.warning(f"Employee ID **{emp_id}** is already registered.")
            else:
                st.session_state.data["teachers"].append({
                    "name": name, "age": int(age),
                    "email": email, "subject": subject, "emp_id": emp_id
                })
                save_data()
                st.success(f"✅ **{name}** has been registered successfully!")
                st.rerun()

    with tab2:
        st.markdown("### Teacher Details")
        teachers = st.session_state.data["teachers"]
        if not teachers:
            st.info("No teachers registered yet.")
        else:
            options = {f"{t['name']}  ({t['emp_id']})": t["emp_id"] for t in teachers}
            choice  = st.selectbox("Select Teacher", list(options.keys()), key="t_view")
            emp_id  = options[choice]

            for t in teachers:
                if t["emp_id"] != emp_id:
                    continue
                st.markdown(f"""
                <div style='background:linear-gradient(135deg,#111827,#141c2e); border:1px solid #1e2740;
                             border-radius:16px; padding:24px; margin:16px 0; display:flex;
                             align-items:center; gap:20px;'>
                    <div style='width:64px; height:64px; border-radius:50%;
                                background:linear-gradient(135deg,#059669,#0d9488);
                                display:flex; align-items:center; justify-content:center;
                                font-family:Space Grotesk,sans-serif; font-weight:700;
                                color:#fff; font-size:1.6rem; flex-shrink:0;'>
                        {t['name'][0].upper()}
                    </div>
                    <div>
                        <div style='font-family:Space Grotesk,sans-serif; font-weight:700;
                                    font-size:1.3rem; color:#f0f4ff;'>{t['name']}</div>
                        <div style='font-size:0.85rem; color:#6b7fa8; margin-top:2px;'>
                            Emp ID: {t['emp_id']} &nbsp;·&nbsp; Age: {t['age']} &nbsp;·&nbsp; {t['email']}
                        </div>
                        <div style='margin-top:8px; display:inline-block; background:rgba(5,150,105,0.2);
                                    border:1px solid rgba(5,150,105,0.4); color:#6ee7b7;
                                    font-size:0.8rem; border-radius:20px; padding:2px 12px;
                                    font-family:Space Grotesk,sans-serif; font-weight:600;'>
                            {t['subject']}
                        </div>
                    </div>
                </div>
                """, unsafe_allow_html=True)
                break

            st.markdown("---")
            st.markdown("### 📋 All Teachers")
            rows = [{"Name": t["name"], "Emp ID": t["emp_id"],
                     "Subject": t["subject"], "Age": t["age"], "Email": t["email"]}
                    for t in teachers]
            st.dataframe(rows, use_container_width=True, hide_index=True)