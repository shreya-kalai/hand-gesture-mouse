# 🖐️ Hand Gesture-Based Mouse & Screen Text Reader with Voice Feedback

A Python-based system that uses real-time **hand gesture recognition** to control mouse actions and optionally **extracts screen text**, which is read aloud using **pyttsx3**. Built for enhanced accessibility and contactless control.

---

## 🚀 Features

- 🎯 **Hand Gesture Mouse Control**
  - Move cursor left/right
  - Single click, double click, right click
  - Scroll up/down

- 📋 **Screen Text Extraction**
  - Capture screen content using OCR (Tesseract)
  - Read aloud using pyttsx3 for accessibility

- 🗣️ **Voice Feedback** for every action

---

## 🛠️ Tech Stack

- `Python`
- `OpenCV` – webcam feed + frame capture
- `MediaPipe` – hand tracking (via custom `hand_tracking.py`)
- `PyAutoGUI` – perform mouse actions + screenshot
- `pyttsx3` – offline text-to-speech
- `pytesseract` – OCR text extraction from screenshots
- `PyMuPDF (fitz)` – reserved for future PDF support

---

## 📦 Installation

1. **Clone the repository:**
```bash
git clone https://github.com/shreya-kalai/hand-gesture-mouse.git
cd hand-gesture-mouse
