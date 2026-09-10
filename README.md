# 🛡️ DarkComet RAT Behavioral Analyzer Using AI

An AI-powered cybersecurity project designed to analyze system behavior and identify suspicious activity associated with Remote Access Trojan (RAT)-like behavior.

The project monitors **process activity, file activity, network activity, and system resource usage**, then uses machine learning and threat-scoring techniques to identify potentially malicious behavior.

> ⚠️ **Educational & Defensive Security Project:**  
> This project is designed for cybersecurity learning, behavioral analysis, and threat detection. It does not contain or execute the DarkComet RAT malware itself.

---

## 🚀 Features

- 🔍 **Process Monitoring**
  - Monitors running processes
  - Collects CPU and memory usage
  - Records suspicious process behavior

- 📁 **File Activity Monitoring**
  - Tracks file-system activity
  - Helps identify unusual file behavior

- 🌐 **Network Monitoring**
  - Monitors network-related activity
  - Helps identify potentially suspicious connections

- 🤖 **AI/ML-Based Detection**
  - Uses machine learning to classify system behavior
  - Detects normal and anomalous activity

- 🚨 **Threat Scoring**
  - Calculates behavioral threat scores
  - Helps categorize suspicious activities

- 📊 **Interactive Dashboard**
  - Built with Streamlit
  - Displays monitoring and detection results
  - Provides a simple cybersecurity analysis interface

- 🧪 **Safe Activity Simulator**
  - Simulates suspicious system behavior for testing
  - Allows the detection system to be demonstrated safely

---

## 🏗️ Project Architecture

text
DarkComet_RAT_Behavioral_Analyzer_Using_AI/
│
├── app.py
│
├── data/
│   ├── malicious_behavior.csv
│   ├── normal_behavior.csv
│   └── training_data.csv
│
├── detector/
│   ├── ml_detector.py
│   └── threat_score.py
│
├── monitor/
│   ├── process_monitor.py
│   ├── file_monitor.py
│   └── network_monitor.py
│
├── simulator/
│   └── attack_simulator.py
│
├── logs/
│   ├── activity_log.csv
│   └── ai_results.csv
│
├── requirements.txt
└── README.md


⚙️ Installation
1. Clone the repository
git clone https://github.com/MGiridhara/DarkComet_Analyzer.git
2. Navigate to the project
cd DarkComet_Analyzer
3. Create a virtual environment
python -m venv venv
4. Activate the virtual environment
Windows PowerShell
venv\Scripts\activate

If PowerShell blocks script execution, you can run the project directly using:

.\venv\Scripts\python.exe
5. Install dependencies
pip install streamlit pandas scikit-learn psutil streamlit-autorefresh matplotlib
▶️ Running the Project
Start the Process Monitor
python monitor/process_monitor.py

The monitor collects system activity and stores information in the logs/ directory.

Run the AI Detector

Open another terminal:

python detector/ml_detector.py

The machine-learning detector analyzes the collected behavioral information and produces detection results.

Start the Streamlit Dashboard
streamlit run app.py

Open the URL displayed in the terminal, usually:

http://localhost:8501
🧪 Safe Activity Simulation

For testing and demonstration purposes, the project includes an activity simulator.

Run:

python simulator/attack_simulator.py

The simulator generates controlled system activity so that the monitoring and detection components can be tested without executing real malware.

🧠 How It Works
        System Activity
              │
              ▼
      ┌─────────────────┐
      │ Activity Monitor│
      └────────┬────────┘
               │
       ┌───────┼────────┐
       ▼       ▼        ▼
   Process    File    Network
   Monitor   Monitor   Monitor
       │       │        │
       └───────┼────────┘
               ▼
        Behavioral Data
               │
               ▼
      ┌─────────────────┐
      │  ML Detection   │
      └────────┬────────┘
               │
               ▼
       Threat Scoring
               │
               ▼
      ┌─────────────────┐
      │ Streamlit       │
      │ Dashboard       │
      └─────────────────┘
📊 Detection Approach

The system uses behavioral indicators rather than relying only on malware signatures.

Examples of monitored indicators include:

CPU utilization
Memory utilization
Process activity
File activity
Network activity
Behavioral patterns
Anomalous system activity

The collected information is analyzed using machine-learning techniques and a threat-scoring mechanism to identify potentially suspicious behavior.

📁 Dataset

The project includes sample behavioral datasets:

data/
├── malicious_behavior.csv
├── normal_behavior.csv
└── training_data.csv

These datasets are used for testing and machine-learning-based behavioral classification.

🔐 Cybersecurity Concepts Demonstrated

This project demonstrates practical concepts in:

Malware behavioral analysis
RAT detection
Endpoint monitoring
Anomaly detection
Machine learning for cybersecurity
Threat scoring
Process monitoring
Network monitoring
File monitoring
Security dashboards
Defensive cybersecurity


👨‍💻 Author

M Giridhara

Computer Science & Engineering Student
Java Developer | Python Developer | Cybersecurity Enthusiast

GitHub

https://github.com/MGiridhara
