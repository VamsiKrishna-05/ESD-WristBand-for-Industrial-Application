<div align="center">
⚡ Smart ESD Wristband Monitoring System
Real-time Electrostatic Discharge Compliance for Electronics Workstations
<img src="https://img.shields.io/badge/Platform-Raspberry%20Pi-red"> <img src="https://img.shields.io/badge/Language-Python-blue"> <img src="https://img.shields.io/badge/Domain-Embedded%20Systems-green"> <img src="https://img.shields.io/badge/Use%20Case-Industrial%20ESD%20Safety-orange"> </div>
🚀 Why This Project Exists

Electrostatic Discharge (ESD) is one of the silent killers in electronics manufacturing.
Even a small grounding failure can destroy high-value components without visible damage.

Smart ESD Wristband Monitoring System
Real-Time Electrostatic Discharge Compliance for Electronics Workstations
Overview

Electrostatic Discharge (ESD) is a critical reliability risk in electronics manufacturing.
Even minor grounding failures can cause irreversible damage to sensitive components.

This project presents an automated, real-time ESD wristband monitoring system designed to ensure continuous operator grounding compliance at industrial workstations.

Problem

Traditional ESD safety methods rely heavily on manual checks and standalone testers.
These approaches do not guarantee continuous monitoring and are prone to human error.

Undetected grounding failures result in:

Component damage

Quality degradation

Increased rework and cost

Solution

A Raspberry Pi–based monitoring system that continuously verifies:

Operator presence at the workstation

Wristband grounding integrity

System power state

Audible alerts are triggered immediately when ESD protection is compromised.

System Concept

Operator presence is detected using an IR sensor.
Wristband grounding is measured as an analog voltage through an ADC.
Decision logic evaluates safety conditions in real time.
A buzzer alerts the operator when unsafe conditions occur.

Core Capabilities

Continuous monitoring
Real-time alerting
Configurable voltage thresholds
Lightweight embedded design
Scalable to multiple workstations

Hardware

Raspberry Pi
MCP3008 Analog-to-Digital Converter
ESD Wristband
IR Proximity Sensor
Buzzer

Software

Python
SPI communication
GPIO control

Logic Summary

If no operator is detected, the system remains silent.
If an operator is present without proper grounding, the buzzer is activated.
If grounding and presence are both valid, the system operates normally.

Voltage Thresholds

Wristband connected below 2.0 volts
Power-off condition between 1.3 and 1.8 volts

Thresholds are adjustable to match different workstation requirements.

Project Structure

Source code is separated from configuration files.
Development environment is containerized using GitHub Codespaces.
The repository is organized for clarity, review, and scalability.

Execution

The application runs continuously and evaluates safety conditions in a loop.
Hardware execution is intended for Raspberry Pi platforms.

Applications

Electronics manufacturing
SMT assembly lines
Quality assurance labs
ESD-controlled environments

Future Scope

Centralized monitoring dashboards
Factory system integration
Operator-level compliance analytics
Wearable embedded implementations

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
