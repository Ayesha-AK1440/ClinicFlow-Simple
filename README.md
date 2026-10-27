# ClinicFlow Simple — AI-Powered Clinic Workflow Automation

**AI Growth & Automation Associate — Task 1**

ClinicFlow Simple is a lightweight healthcare-administration prototype designed to simplify appointment request management and routine communication. It combines a simple web dashboard with optional AI-assisted response drafting to demonstrate how automation can reduce repetitive administrative work.

> **Project status:** Demonstration prototype. It uses fictional data and is not intended for production healthcare operations.

## 1. Problem Statement

Small clinics may handle appointment requests and routine inquiries manually. This can create repetitive administrative work and make requests harder to organize and track.

ClinicFlow Simple demonstrates a simple workflow for recording appointment requests, updating their statuses, and preparing administrative acknowledgment drafts.

## 2. Features

- **Appointment request form:** Add requests using a name, contact detail, preferred date, and reason for the visit.
- **Request dashboard:** View appointment requests and their current statuses.
- **Search and filtering:** Find requests by name, reason, or request ID and filter by status.
- **Status management:** Update requests to New, Under Review, Confirmed, or Cancelled.
- **AI-assisted response drafting:** Optionally generate polite administrative acknowledgments using the Groq API.
- **Fallback response:** Use a predefined template when an AI API key is unavailable or the AI request fails.
- **Downloadable drafts:** Download generated or fallback response text for staff review.

The application does not diagnose conditions, recommend treatments, check real clinic availability, book real appointments, or send messages automatically.

## 3. Technology Stack

- **Language:** Python
- **Frontend and application framework:** Streamlit
- **HTTP requests:** Requests
- **Optional AI integration:** Groq API with an OpenAI-compatible chat completions endpoint
- **Version control:** Git and GitHub
- **Optional deployment:** Streamlit Community Cloud

## 4. Application Workflow

1. Open ClinicFlow Simple.
2. Enter a fictional appointment request.
3. View, search, and filter requests in the dashboard.
4. Update the request status as needed.
5. Select a request and generate an administrative reply draft.
6. Review and download the draft.

The reply is a draft for human review. The application does not send it to the patient.

## 5. Requirements

- Python 3.10 or newer.
- Internet access for installing dependencies.
- Internet access and a valid Groq API key if you want to enable live AI-generated responses.

## 6. Run Locally

### Step 1: Download the project

Clone the GitHub repository or download the project ZIP and extract it.

Open a terminal in the project root directory containing `app.py` and `requirements.txt`.

### Step 2: Create a virtual environment

**Windows PowerShell:**

```powershell
python -m venv .venv
```

Activate it:

```powershell
.\.venv\Scripts\Activate.ps1
```

If your terminal uses a different Python installation, configure a supported Python version before creating the environment.

**macOS/Linux:**

```bash
python3 -m venv .venv
source .venv/bin/activate
```

### Step 3: Install dependencies

```bash
python -m pip install -r requirements.txt
```

### Step 4: Start the application

```bash
streamlit run app.py
```

Open the local URL displayed in the terminal. It is usually:

http://localhost:8501

## 7. Optional: Enable Groq AI

ClinicFlow Simple can run without an API key using its predefined response template.

To enable live AI-generated drafts:

1. Obtain your own API key from the official Groq Console: https://console.groq.com/
2. Configure the key as an environment variable.
3. Restart the application in the same terminal session.

**Windows PowerShell:**

```powershell
$env:GROQ_API_KEY="your_key_here"
streamlit run app.py
```

**macOS/Linux:**

```bash
export GROQ_API_KEY="your_key_here"
streamlit run app.py
```

Replace `your_key_here` with your own key. Never commit the key to GitHub or share it publicly.

When the key is configured, the application attempts to generate a response using the configured Groq model. If the API call fails, the application falls back to a predefined template.

**Privacy note:** When live AI generation is enabled, the selected request's name, preferred date, reason, and status are included in the request sent to the Groq API. Use fictional demonstration data only.

## 8. Deploy to Streamlit Community Cloud

To make the application accessible through a public web link:

1. Push the project files to a GitHub repository.
2. Visit https://share.streamlit.io/
3. Sign in using GitHub and authorize access to the repository.
4. Create a new app and select your repository.
5. Choose the `main` branch and set the main file path to `app.py`.
6. Deploy the application.
7. Open the generated URL and test the application.

If you enable live AI generation in the hosted application, configure `GROQ_API_KEY` through the hosting platform's secrets settings. Do not store API keys in the repository.

## 9. Testing Checklist

Before presenting the project, verify the following:

- The application starts without errors.
- Missing required fields trigger validation.
- A new appointment request can be created.
- Search and status filters return the expected requests.
- Request statuses can be updated.
- Reply drafting works using the template fallback.
- Live AI generation works if a valid API key is configured.
- The draft can be downloaded.
- No email or SMS is sent automatically.
- The deployed application opens through its public URL, if hosted.

Record the actual results of your tests in `docs/Manual_Test_Checklist.md`.

## 10. AI Tools and Prompt Engineering

AI tools were used during project development to help plan the workflow, implement application features, refine the AI response instructions, and prepare test scenarios.

The prompt documentation is maintained in:

`docs/Prompt_Documentation.md`

It records the development prompts, significant refinements, and iteration notes. Update it to reflect the AI tools and prompts actually used during development.

## 11. Project Documentation

The `docs/` directory contains:

- `Manual_Test_Checklist.md` — Manual verification steps and expected results.
- `Prompt_Documentation.md` — Development prompts and iteration log.
- `Video_Presentation_Script.md` — Suggested structure for the project demonstration video.
- `Submission_Email_Draft.txt` — Draft email for the assessment submission.

## 12. Limitations

- Requests are stored in Streamlit session state and are not persisted in a database.
- Data may reset when the session or application restarts.
- User authentication and role-based access control are not implemented.
- Real clinic availability and calendar integrations are not implemented.
- Email and SMS delivery are not implemented.
- AI-generated drafts may contain errors and require human review.
- The application is not designed for real patient data or production healthcare use.

## 13. Future Improvements

Potential improvements include:

- Persistent storage using SQLite or MySQL.
- Secure user authentication and access control.
- Calendar integration and real appointment availability checks.
- Optional email notifications with appropriate authorization.
- Improved logging, error handling, and automated testing.

## 14. Project Goal

ClinicFlow Simple demonstrates how a small administrative workflow can be organized through a working web application, optional AI-assisted drafting, and structured prompt engineering.

The goal is to demonstrate practical problem-solving and responsible AI integration rather than merely describe a proposed solution.
