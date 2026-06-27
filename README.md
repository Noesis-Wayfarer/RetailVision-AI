# 🛒 RetailVision AI

### AI Retail Video Analytics

---

## 📖 Overview

RetailVision AI is a computer vision application that analyzes retail surveillance footage to provide business insights.

The system detects customers, tracks their movement throughout the store, estimates dwell time within predefined zones, generates customer movement heatmaps, and presents the results through an interactive Streamlit dashboard.

---

## ✨ Features

- 👥 Real-time customer detection using YOLOv8
- 🎯 Multi-object tracking using DeepSORT
- 📍 Zone-wise customer analytics
- ⏱ Customer dwell time estimation
- 🔥 Customer movement heatmap generation
- 📊 Interactive Streamlit dashboard
- 📄 CSV analytics reports
- 🎥 AI-processed video output

## 🛠 Tech Stack

| Category | Technology |
|----------|------------|
| Programming Language | Python |
| Computer Vision | OpenCV |
| Object Detection | YOLOv8 |
| Multi-Object Tracking | DeepSORT |
| Data Processing | Pandas |
| Dashboard | Streamlit |
| Model Framework | Ultralytics |

## 🏗️ Project Workflow

```text
Retail Video
      │
      ▼
YOLOv8 Person Detection
      │
      ▼
DeepSORT Multi-Object Tracking
      │
      ▼
Customer Counting
      │
      ├─────────────► Zone Analytics
      │
      ├─────────────► Dwell Time Analysis
      │
      └─────────────► Heatmap Generation
                        │
                        ▼
              Streamlit Dashboard

## 📂 Project Structure

```text
RetailVision-AI/
│
├── app.py                     # Streamlit dashboard
├── Retail_Analytics.ipynb      
├── requirements.txt            # Project dependencies
├── README.md                   # Project documentation
│
├── Retail2.mp4                 # Input retail video
├── retail_analytics_output.mp4 # Processed output video
├── retail_heatmap_overlay.png  # Generated heatmap
│
├── summary.csv
├── zone_analytics.csv
└── dwell_time.csv

## 🌟 Project Highlights

- Developed an end-to-end retail analytics pipeline using computer vision.
- Implemented real-time customer detection and multi-object tracking.
- Generated business-oriented insights such as zone visits and customer dwell time.
- Designed an interactive Streamlit dashboard for visualizing analytics.
- Applied AI to transform surveillance footage into actionable retail intelligence.