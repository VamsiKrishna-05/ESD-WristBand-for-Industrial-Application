*Smart ESD Wrist Band Monitoring System*
Overview

Electrostatic Discharge (ESD) poses a serious risk to sensitive electronic components in manufacturing and testing environments. Manual verification of ESD wrist band usage is error-prone and not scalable.
This project implements an automated ESD wrist band monitoring system using a Raspberry Pi to ensure operator grounding compliance in real time.

Problem Statement

In electronics production lines:

Operators may work without wearing an ESD wrist band

Grounding connections can become loose or disconnected

Manual supervision cannot guarantee continuous compliance

These issues can lead to component damage, quality failures, and financial loss.

Proposed Solution

A Raspberry Pi–based system that:

Detects operator presence using an IR sensor

Monitors ESD wrist band grounding via MCP3008 ADC

Triggers an audible alert when ESD protection is not ensured

Provides real-time monitoring at the workstation level

System Architecture

Signal Flow:

IR sensor detects operator presence at the workstation

MCP3008 reads analog voltage from the ESD wrist band

Raspberry Pi evaluates grounding status using voltage thresholds

Buzzer alerts when unsafe conditions are detected

Hardware Components

Raspberry Pi

MCP3008 (10-bit ADC)

ESD Wrist Band

IR Proximity Sensor

Buzzer

Power Supply & Wiring

Software Stack

Python 3

RPi.GPIO for GPIO control

spidev for SPI communication with MCP3008

Working Logic
Condition	System Action
No operator detected	Buzzer OFF
Operator detected + box power OFF	Buzzer ON
Operator detected + wrist band disconnected	Buzzer ON
Operator detected + wrist band properly grounded	Buzzer OFF
Voltage Thresholds Used

Wrist band connected: Voltage < 2.0 V

Box power OFF range: 1.3 V – 1.8 V

These thresholds can be calibrated based on workstation requirements.
Project Structure
ESD-Wristband-Monitoring/
│
├── src/
│   └── esd_monitor.py
│
├── .devcontainer/
│   ├── devcontainer.json
│   └── Dockerfile
│
├── requirements.txt
├── README.md
└── .gitignore

Running the Project
python src/esd_monitor.py
Applications

Electronics manufacturing units

ESD-protected workstations

Quality assurance and compliance monitoring

Industrial safety automation

Future Enhancements

Web dashboard for multi-workstation monitoring

MQTT / HTTP integration for factory systems

Employee-level compliance logging

BLE-based anti-theft detection

ESP32-based wearable version
