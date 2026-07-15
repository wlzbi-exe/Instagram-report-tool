# Instagram-report-tool
IG-TOOL is a Python‑based command‑line utility that demonstrates how Instagram’s reporting endpoints can be programmatically triggered. It retrieves your session ID and CSRF token, converts a username to a user ID, and sends either a detailed report (via the official get_frx_prompt endpoint) or a lightweight flag request.

# 🔥 IG-TOOL – Instagram Reporting Utility

> **⚠️ DISCLAIMER:** This tool is provided for **educational and research purposes only**.  
> Misuse of this tool to harass, spam, or violate Instagram's Terms of Service is strictly prohibited.  
> The author assumes no responsibility for any illegal or unethical use.

---

## 📌 Overview

**IG-TOOL** is a Python‑based script designed to automate the process of submitting reports against Instagram accounts. It supports two reporting methods:

- **Full Report** – Sends a detailed report with a comprehensive payload, mimicking the official Instagram reporting flow.  
- **Lite Report** – Uses a simpler endpoint (`i.instagram.com/users/{id}/flag/`).

The tool is intended for testing and understanding Instagram’s reporting mechanisms. It requires a valid **session ID** from your Instagram account.

---

## ✨ Features

- ✅ **Two report modes** – Full and Lite.
- ✅ **Automatic CSRF token retrieval** – fetches the `csrftoken` from Instagram’s homepage.
- ✅ **User ID resolution** – converts a username to a numeric user ID via `instaloader`.
- ✅ **Colorful console output** – uses `cfonts` and `rich` for an enhanced terminal experience.
- ✅ **Continuous reporting loop** – runs indefinitely until manually stopped (Ctrl+C).

---

## 🧰 Requirements

- Python **3.6** or higher
- Required packages:
  - `instaloader`
  - `requests`
  - `rich`
  - `cfonts` (for banner text)

All other modules (`os`, `sys`, `time`, `random`, `datetime`, `webbrowser`, `typing`) are part of the Python standard library.

---

## 📦 Installation

1. **Clone the repository** (or download the script).
   ```bash
   git clone https://github.com/yourusername/ig-tool.git
   cd ig-tool
