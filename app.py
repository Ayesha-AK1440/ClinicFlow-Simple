import os
from datetime import date, datetime
import streamlit as st
import requests

st.set_page_config(page_title="ClinicFlow Simple", page_icon="🏥", layout="wide")

st.title("🏥 ClinicFlow Simple")
st.caption("AI-assisted clinic administration • Demo prototype using fictional data only")

if "requests" not in st.session_state:
    st.session_state.requests = [
        {
            "id": 1001, "name": "Aarav Demo", "contact": "demo@example.com",
            "visit_date": str(date.today()), "reason": "Routine check-up",
            "status": "New", "created": datetime.now().strftime("%Y-%m-%d %H:%M")
        },
        {
            "id": 1002, "name": "Maya Sample", "contact": "sample@example.com",
            "visit_date": str(date.today()), "reason": "Follow-up appointment",
            "status": "Confirmed", "created": datetime.now().strftime("%Y-%m-%d %H:%M")
        },
    ]

def draft_reply(patient_name, visit_date, reason, status):
    """Use Groq if configured; otherwise produce a clearly labelled demo draft."""
    api_key = os.getenv("GROQ_API_KEY", "").strip()
    if api_key:
        prompt = f"""
You are a clinic administrative assistant. Draft a concise, polite appointment
acknowledgment using only these details:
Name: {patient_name}
Requested date: {visit_date}
Reason supplied by patient: {reason}
Current request status: {status}

Do not diagnose, provide medical advice, promise availability, or claim that an
appointment is confirmed unless the status is Confirmed. If the status is New,
say the clinic team will review availability. End by asking the patient to contact
the clinic directly if they need urgent help. This is a draft for staff review,
not a message sent to the patient.
"""
        try:
            response = requests.post(
                "https://api.groq.com/openai/v1/chat/completions",
                headers={"Authorization": f"Bearer {api_key}", "Content-Type": "application/json"},
                json={
                    "model": "llama-3.3-70b-versatile",
                    "messages": [
                        {"role": "system", "content": "You write safe, clear clinic administration drafts."},
                        {"role": "user", "content": prompt}
                    ],
                    "temperature": 0.3,
                    "max_tokens": 220
                },
                timeout=20
            )
            response.raise_for_status()
            return response.json()["choices"][0]["message"]["content"].strip(), "Generated with Groq AI"
        except Exception:
            return (
                f"Hello {patient_name}, thank you for contacting our clinic. "
                f"We have received your request for {visit_date} regarding {reason}. "
                f"Current status: {status}. Our clinic team will review the request and "
                "follow up about availability. Please contact the clinic directly if you need urgent assistance.",
                "Template fallback (AI unavailable)"
            )
    return (
        f"Hello {patient_name}, thank you for contacting our clinic. "
        f"We have received your request for {visit_date} regarding {reason}. "
        f"Current status: {status}. Our clinic team will review the request and "
        "follow up about availability. Please contact the clinic directly if you need urgent assistance.",
        "Template fallback (add GROQ_API_KEY to enable AI generation)"
    )

all_requests = st.session_state.requests
c1, c2, c3 = st.columns(3)
c1.metric("Total requests", len(all_requests))
c2.metric("New", sum(r["status"] == "New" for r in all_requests))
c3.metric("Confirmed", sum(r["status"] == "Confirmed" for r in all_requests))

st.divider()
tab1, tab2, tab3 = st.tabs(["➕ New request", "📋 Request dashboard", "✉️ AI reply draft"])

with tab1:
    st.subheader("Create an appointment request")
    st.info("Use fictional details for this demonstration. Do not enter real patient or medical information.")
    with st.form("appointment_form", clear_on_submit=True):
        name = st.text_input("Patient name (demo)")
        contact = st.text_input("Contact email or phone (demo)")
        visit_date = st.date_input("Preferred appointment date", min_value=date.today())
        reason = st.selectbox("Reason for visit", [
            "Routine check-up", "Follow-up appointment", "Vaccination inquiry",
            "General consultation inquiry", "Other administrative request"
        ])
        submitted = st.form_submit_button("Add request", type="primary")
        if submitted:
            if not name.strip() or not contact.strip():
                st.error("Please enter a demo name and contact detail.")
            else:
                next_id = max([r["id"] for r in st.session_state.requests], default=1000) + 1
                st.session_state.requests.append({
                    "id": next_id, "name": name.strip(), "contact": contact.strip(),
                    "visit_date": str(visit_date), "reason": reason, "status": "New",
                    "created": datetime.now().strftime("%Y-%m-%d %H:%M")
                })
                st.success(f"Request #{next_id} added. Status set to New.")
                st.rerun()

with tab2:
    st.subheader("Appointment request dashboard")
    search = st.text_input("Search by name, reason, or request ID")
    status_filter = st.selectbox("Filter by status", ["All", "New", "Under Review", "Confirmed", "Cancelled"])
    filtered = []
    for r in st.session_state.requests:
        searchable = f'{r["id"]} {r["name"]} {r["reason"]}'.lower()
        if search.lower() in searchable and (status_filter == "All" or r["status"] == status_filter):
            filtered.append(r)
    if not filtered:
        st.warning("No requests match those filters.")
    for r in reversed(filtered):
        with st.container(border=True):
            left, middle, right = st.columns([3, 2, 2])
            left.markdown(f'**#{r["id"]} — {r["name"]}**')
            left.write(f'{r["reason"]} • Preferred date: {r["visit_date"]}')
            left.caption(f'Contact: {r["contact"]} • Created: {r["created"]}')
            middle.write(f'**Status:** {r["status"]}')
            with right:
                options = ["New", "Under Review", "Confirmed", "Cancelled"]
                current = r["status"] if r["status"] in options else "New"
                new_status = st.selectbox("Update status", options, index=options.index(current), key=f'status_{r["id"]}')
                if new_status != r["status"]:
                    r["status"] = new_status
                    st.rerun()

with tab3:
    st.subheader("AI-assisted administrative reply")
    if not st.session_state.requests:
        st.write("Add a request first.")
    else:
        choices = {f'#{r["id"]} — {r["name"]} ({r["status"]})': r for r in st.session_state.requests}
        selected_label = st.selectbox("Choose a request", list(choices.keys()))
        selected = choices[selected_label]
        st.write("The generated text is a draft only. A staff member must review it before sending.")
        if st.button("Generate reply draft", type="primary"):
            draft, source = draft_reply(
                selected["name"], selected["visit_date"], selected["reason"], selected["status"]
            )
            st.session_state.last_draft = draft
            st.session_state.draft_source = source
        if "last_draft" in st.session_state:
            st.caption(st.session_state.get("draft_source", "Draft"))
            st.text_area("Reply draft", value=st.session_state.last_draft, height=180)
            st.download_button("Download draft as TXT", st.session_state.last_draft, file_name="clinicflow_reply_draft.txt")

st.divider()
st.caption("Prototype limitations: data is held in the current Streamlit session and is not a production database. No messages are sent. Do not use real patient data.")
