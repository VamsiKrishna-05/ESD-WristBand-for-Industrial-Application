<div align="center">
⚡ Smart ESD Wristband Monitoring System
Real-time Electrostatic Discharge Compliance for Electronics Workstations
<img src="https://img.shields.io/badge/Platform-Raspberry%20Pi-red"> <img src="https://img.shields.io/badge/Language-Python-blue"> <img src="https://img.shields.io/badge/Domain-Embedded%20Systems-green"> <img src="https://img.shields.io/badge/Use%20Case-Industrial%20ESD%20Safety-orange"> </div>
🚀 Why This Project Exists

Electrostatic Discharge (ESD) is one of the silent killers in electronics manufacturing.
Even a small grounding failure can destroy high-value components without visible damage.

Most factories still rely on manual checks or standalone ESD testers, which:

Do not provide continuous monitoring

Cannot verify operator presence

Fail to scale across multiple workstations

👉 This project solves that gap.

🧠 What This System Does

A smart, automated ESD wristband monitoring system that ensures an operator is:

Present at the workstation

Wearing the ESD wristband

Properly grounded

If any safety condition fails, the system instantly alerts via a buzzer.

🏗️ System Architecture
┌────────────┐     ┌────────────┐     ┌────────────┐
│ IR Sensor  │ ──▶ │ Raspberry  │ ──▶ │   Buzzer   │
│ (Presence) │     │    Pi      │     │  (Alert)   │
└────────────┘     │            │     └────────────┘
                   │            │
┌────────────┐     │            │
│ ESD Band   │ ──▶ │ MCP3008    │
│ (Analog)   │     │  ADC       │
└────────────┘     └────────────┘

⚙️ Core Features

✔ Real-time operator detection
✔ Wristband grounding verification using ADC
✔ Intelligent buzzer logic
✔ Configurable voltage thresholds
✔ Lightweight & scalable design
✔ GitHub Codespaces ready

🔌 Hardware Stack
Component	Purpose
Raspberry Pi	Main controller
MCP3008	Analog-to-Digital Converter
ESD Wristband	Grounding detection
IR Sensor	Operator presence
Buzzer	Audible alert
💻 Software Stack

Python 3

RPi.GPIO – GPIO control

spidev – SPI communication

GitHub Codespaces – Cloud development

🧪 Decision Logic
Condition	Buzzer
No operator detected	OFF
Operator detected + box OFF	ON
Operator detected + wristband disconnected	ON
Operator detected + proper grounding	OFF
🔋 Voltage Thresholds
Wristband Connected : < 2.0V
Box Power OFF Range : 1.3V – 1.8V


Thresholds are configurable for different ESD setups.

📁 Project Structure
ESD-Wristband-Monitoring/
│
├── src/
│   └── esd_monitor.py
├── .devcontainer/
│   ├── devcontainer.json
│   └── Dockerfile
├── requirements.txt
├── README.md
└── .gitignore

▶️ How to Run
python src/esd_monitor.py


⚠️ Hardware execution requires a Raspberry Pi.
Codespaces is provided for development & review.

🏭 Industrial Use Cases

Electronics manufacturing lines

SMT workstations

Quality assurance labs

ESD-controlled environments

🔮 Future Roadmap

🌐 Web dashboard for multiple stations

📡 MQTT / HTTP factory integration

📊 Operator-level compliance logs

🔵 BLE-based anti-theft detection

⚡ ESP32 wearable version
