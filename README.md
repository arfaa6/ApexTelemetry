# 🏎️ ApexTelemetry

> A production-grade, real-time motorsport race strategy and telemetry simulation platform built for the pit wall.

![ApexTelemetry Dashboard](https://img.shields.io/badge/Status-Production%20Ready-06d6a0?style=flat-square)
![FastAPI](https://img.shields.io/badge/FastAPI-0.100%2B-005571?style=flat-square&logo=fastapi)
![Tailwind CSS](https://img.shields.io/badge/Tailwind_CSS-3.0%2B-38bdf8?style=flat-square&logo=tailwindcss)
![Chart.js](https://img.shields.io/badge/Chart.js-4.0%2B-ff6384?style=flat-square&logo=chartdotjs)

---

## 🎯 Overview

**ApexTelemetry** is a decoupled full-stack web application designed to simulate race dynamics and calculate optimal pit-wall strategies in real time. It combines a high-performance Python math and simulation backend with a modern, dark-mode engineering dashboard styled after professional F1 pit walls.

---

## 🚀 Key Features

* **Advanced Simulation Engine**: Computes non-linear tire degradation curves, fuel burn rates, estimated lap times, and dynamic pit-stop probabilities based on compound characteristics (Soft, Medium, Hard).
* **Interactive Telemetry Visualizations**: Features live-updating `Chart.js` graphs that plot lap-time degradation across an entire race stint.
* **Modern Pit-Wall UI**: Built with **Tailwind CSS** featuring custom typography (`JetBrains Mono`), responsive card layouts, and dynamic status indicators.
* **Robust REST API**: Powered by **FastAPI** and validated via **Pydantic**, ensuring type safety, rapid execution, and automatic OpenAPI documentation.

---

## 🛠️ Tech Stack

* **Backend**: Python, FastAPI, Pydantic, Uvicorn, NumPy / Pandas
* **Frontend**: HTML5, JavaScript (ES6+), Tailwind CSS, Chart.js
* **Testing**: Pytest

---

## 📂 Project Architecture

```text
race-strategy-sim/
├── src/
│   ├── __init__.py
│   ├── api.py           # FastAPI application routes & static file mounting
│   ├── engine.py        # Core race simulation & mathematical models
│   └── static/
│       └── index.html   # Tailwind CSS & Chart.js dashboard UI
├── tests/
│   └── test_engine.py   # Automated pytest suite for backend logic
├── requirements.txt     # Project dependencies
└── README.md