# ClinicFlow Simple — Manual Test Checklist

Run `streamlit run app.py` and test each item. Mark pass/fail only after trying it.

| # | Test | Steps | Expected result | Actual result |
|---|---|---|---|---|
| 1 | App starts | Run Streamlit command | App opens without errors | [Fill in] |
| 2 | Required fields | Submit form with name or contact missing | Validation message appears; request is not added | [Fill in] |
| 3 | Add request | Enter fictional name/contact and submit | Request appears with a new ID and New status | [Fill in] |
| 4 | Search | Search for the new request name | Matching request is shown | [Fill in] |
| 5 | Status filter | Filter by New, then Confirmed | Only requests with selected status are shown | [Fill in] |
| 6 | Update status | Change a request to Under Review | Updated status appears | [Fill in] |
| 7 | Draft without API key | Ensure GROQ_API_KEY is unset and generate draft | Template fallback appears and is labelled | [Fill in] |
| 8 | Draft with API key | Configure key securely and generate draft | AI draft appears, or a clear fallback if API call fails | [Fill in] |
| 9 | No automatic sending | Generate a draft | No email/SMS is sent; user can review/download text | [Fill in] |
| 10 | Privacy note | Review screen and README | Fictional-data and prototype warnings are visible | [Fill in] |
