# 📈 Tarkov Market Sentry: Live Time-Series ETL Pipeline

An automated, end-to-end Data Engineering pipeline that intercepts live marketplace data via GraphQL, applies rigorous normalization rules, and compiles a time-series database for economic trend analysis. 

## 🏗️ Architecture Overview

This project demonstrates the complete lifecycle of modern data ingestion and quality control:
1. **Extract:** Interfaces with the live `tarkov.dev` GraphQL API to pull heavily nested JSON arrays.
2. **Transform:** Utilizes `Pandas` and custom Regular Expressions (Regex) to execute surgical data cleaning—stripping currency anomalies, handling null values, and standardizing data types into a strict, math-ready schema.
3. **Load:** Appends pristine records to a continuous, time-stamped local CSV ledger, engineered to handle continuous polling intervals safely.
4. **Visualize:** Generates automated Business Intelligence (BI) trend overlays using `matplotlib` to flag economic inflation and baseline deviations.

## 🛠️ Tech Stack
* **Language:** Python 3.x
* **Data Processing:** Pandas, Regex (`re`)
* **Network/API:** Requests, GraphQL
* **Data Visualization:** Matplotlib

## ⚙️ Core Features
* **Defensive Querying:** Built-in error handling to catch and report GraphQL payload rejections (e.g., `404` or bad schema architecture) without crashing the pipeline.
* **Currency Normalization:** Automated detection and conversion of mixed string formats (USD vs. RUB) into a single base integer using dynamic exchange constants.
* **Autonomous Polling:** Configured with a `while True` sentry loop and `time.sleep()` pacing to execute continuous data collection while respecting server rate limits.

## 🧠 About the Developer
**Rocky Audenried**
Drawing on an extensive background in clinical diagnostics and laboratory science, I treat data pipelines with the same rigorous standard of quality control required in healthcare. My focus is on building robust systems that take unstructured, chaotic inputs and transform them into precise, verifiable, and globally standardized intelligence.