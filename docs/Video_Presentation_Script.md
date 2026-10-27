# ClinicFlow Simple — Video Presentation Script (target: 2:30–3:00)

**Before recording:** Run the app and test each step. Replace bracketed items with your actual experience. Do not claim Groq AI is active unless you configured and tested it.

## 0:00–0:20 — Introduction
"Hello, this is my Task 1 project, ClinicFlow Simple. It is an AI-assisted clinic administration prototype designed to organize appointment requests and help staff draft routine acknowledgments. I focused on a real workflow problem: handling repetitive requests manually."

## 0:20–0:45 — AI tools and approach
"I used [name the AI tool you actually used] to help plan the scope, generate and refine code, and prepare test cases. I chose [tool] because [your real reason]. I used Python and Streamlit to make a working interface quickly, so the result could be demonstrated rather than remaining only an idea."

## 0:45–1:15 — Prompt engineering
"I started with a prompt defining the problem and safe boundaries. Then I refined it to request specific features: a request form, dashboard, search and status updates. I used a follow-up prompt to add AI-assisted reply drafts with an environment variable for the API key and a fallback if AI is unavailable. I also prompted for testing and safety checks. My prompt documentation records the prompts and the actual changes I made."

## 1:15–2:15 — Live demonstration
[Show the running app.]
"Here are the dashboard counts. I will add a fictional appointment request. The app validates the required fields and assigns the New status. Next, I can search for a request and update its status. In the AI reply tab, I select a request and generate a draft. The draft is for staff review; the application does not send messages automatically. [Explain whether you tested Groq generation or the template fallback.]"

## 2:15–2:40 — Challenge and solution
"One challenge was making AI optional so the demo could still run without an API key. I handled this with an environment-variable configuration and a fallback draft. I also kept the scope administrative and used fictional information to avoid exposing patient data. [Add one real bug or issue you encountered and how you fixed it.]"

## 2:40–3:00 — Outcome and close
"The outcome is a working prototype for adding and tracking appointment requests and preparing administrative reply drafts. It is not a production medical system and does not diagnose, check real availability, or send messages. Thank you for reviewing my project."

## Recording checklist
- Show the actual application, not only slides.
- Ensure the video is at least 2 minutes.
- Show add request, search/status update, and draft generation.
- Explain the AI tools and prompt refinements truthfully.
- Mention one genuine challenge and its solution.
- Do not show API keys, real patient data, or private information.
