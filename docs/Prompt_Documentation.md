# ClinicFlow Simple — Prompt Documentation
AI Growth & Automation Associate — Task 1

> Important: This is a prompt log template for documenting your actual process. Use the prompts below with your chosen AI tool, make the project, and adjust this document to accurately reflect the prompts you really used. Do not claim you used a tool or prompt unless you did.

## Prompt 1 — Define the problem and scope
"I am building a beginner-friendly healthcare automation prototype called ClinicFlow Simple for an AI Growth & Automation Associate assessment. Propose a practical, small-clinic administrative workflow that is safe for a demo. It should handle appointment requests and administrative response drafts, not diagnosis or treatment. Give me a minimum viable feature list, user flow, risks, and success criteria. Use fictional data only."

## Prompt 2 — Choose the implementation
"Recommend the simplest way to build ClinicFlow Simple as a working prototype that I can run locally and demonstrate in a short video. Prefer Python and a simple web UI. Explain the file structure, dependencies, setup commands, and how to test the workflow. Avoid paid services as a requirement."

## Prompt 3 — Build the initial application
"Create a Streamlit app for ClinicFlow Simple with a form to add fictional appointment requests, a dashboard with search and status filters, status updates, and a reply-draft screen. Keep the code beginner-friendly and include input validation. The app must clearly say it is a prototype, use fictional data only, and must not send messages automatically."

## Prompt 4 — Add AI-assisted reply generation
"Add an optional AI-generated administrative acknowledgment to the app. Use a provider API only when an API key is supplied as an environment variable; never hard-code secrets. If the API is unavailable or no key is configured, provide a clearly labelled template fallback. The prompt must not provide medical advice, diagnose, promise appointment availability, or claim a booking is confirmed unless the request status is Confirmed. The draft must require staff review."

## Prompt 5 — Improve safety and user experience
"Review the ClinicFlow Simple code for beginner-level usability and safety. Check missing-field validation, status updates, clear feedback, readable layout, safe handling of API keys, fictional-data warnings, and a clear note that this is not production-ready. Suggest fixes and explain why each matters."

## Prompt 6 — Test the app
"Create a manual test checklist for ClinicFlow Simple covering: missing name/contact, adding a request, search, status filtering, status update, reply draft with no API key, reply draft with a configured API key, and confirmation that no message is sent automatically. Present expected results for each test."

## Prompt 7 — Prepare the final submission
"Using the assessment requirements, help me prepare a two-minute-plus demo video structure, a concise project README, and a final submission checklist. The video must explain AI tools and why I chose them, how I designed and refined prompts, my approach, challenges and solutions, and demonstrate the actual working app. Do not invent results or claim features that have not been tested."

## Iteration log — fill this in after your real testing
| Iteration | What I noticed | Prompt/change I made | Result after testing |
|---|---|---|---|
| 1 | Initial feature scope needed to be manageable | Used Prompt 1 and Prompt 2 | Fill in the actual result |
| 2 | Need a working form and dashboard | Used Prompt 3 | Fill in the actual result |
| 3 | Need safe AI draft generation | Used Prompt 4 | Fill in the actual result |
| 4 | Need to verify edge cases | Used Prompt 5 and Prompt 6 | Fill in the actual result |

## Tool disclosure
Fill in truthfully:
- AI assistant(s) used: [name the tools you actually used]
- Code editor: [e.g., VS Code, if used]
- Optional model API: [Groq only if you configured and tested it; otherwise say template fallback]
- Hosting: [local demo / Streamlit Community Cloud / other actual host]
