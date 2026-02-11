# WiFi QR Code Generator (AI Powered)

Generate secure WiFi QR codes instantly with this Streamlit application. Features include password strength checking and AI-suggested strong passwords.

## How to Run on Another PC

Follow these steps to set up and run the project on a different machine:

### 1. Prerequisites
Ensure you have **Python 3.8+** installed on your system.

### 2. Clone the Repository
Open your terminal (Command Prompt, PowerShell, or Git Bash) and run:
```bash
git clone https://github.com/codex-vivek/wifi-qr-streamlit.git
cd wifi-qr-streamlit
```

### 3. Create a Virtual Environment (Recommended)
It's best to keep dependencies isolated:
```bash
# Windows
python -m venv .venv
.\.venv\Scripts\activate

# macOS/Linux
python3 -m venv .venv
source .venv/bin/activate
```

### 4. Install Dependencies
Install the required Python packages:
```bash
pip install -r requirements.txt
```

### 5. Run the Application
Launch the Streamlit app:
```bash
streamlit run app.py
```

The application will open automatically in your default web browser.

## Features
- **WiFi QR Generation**: Create QR codes for WPA and No Password security types.
- **Password Strength Analysis**: Real-time feedback on your WiFi password security.
- **AI Password Suggestions**: Get suggestions for stronger passwords if yours is weak.
