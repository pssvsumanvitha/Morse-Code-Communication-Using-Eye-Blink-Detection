# Morse-Code-Communication-Using-Eye-Blink-Detection
A real-time communication system that detects eye blinks and translates them into Morse code, enabling silent and hands-free messaging — useful in military, emergency, or assistive scenarios.
````markdown
# 🛰️ Morse Code Communication Using Eye Blink Detection
👁️ A real-time computer vision system that allows users to **communicate using Morse code through eye blinks**, using a webcam and facial landmark detection.

## 📡 What is Morse Code?
Morse code is a method of communication that encodes characters as sequences of **dots (.) and dashes (-)**. It was historically used in telegraph systems and is still used in military and emergency communication today.

- `.... . .-.. .-.. ---` → **HELLO**  
- `... --- ...` → **SOS**

This project translates eye blinks into these symbols:
- **Short Blink** → `.` (Dot)
- **Long Blink** → `-` (Dash)

## 🎯 Project Goal
Enable **hands-free**, **voice-free** communication using only **eye blinks**, with applications in:
- 🔇 Silent military or rescue missions  
- 🧑‍🦼 Assistive technology for people with limited motor abilities  
- 📴 Environments where sound or touch isn't viable

## 🧠 How It Works
- Uses **MediaPipe** to detect eye landmarks in real-time.
- Measures eye aspect ratio to detect blinks.
- Converts blink durations into Morse symbols.
- Translates Morse code into readable English text.
- Displays results on a separate GUI screen with live feedback.

## 🖼️ Demo
![Demo Screenshot](demo.gif)  
*(Insert a screen recording or image if available)*

## 🛠️ Tech Stack
- `Python`
- `OpenCV` – Video stream and display
- `MediaPipe` – Facial landmark and eye tracking
- `NumPy` – Signal processing and timing

## 🚀 Features
- Real-time blink detection from webcam  
- Dot and Dash conversion based on blink duration  
- Morse to English decoding  
- Displays live camera feed with Morse output  
- Small and adjustable face preview window  
- Lightweight, runs offline  

## ⚙️ Installation & Setup
1. **Clone the repository**
```bash
git clone https://github.com/yourusername/morse-eye-blink.git
cd morse-eye-blink
````

2. **Install dependencies**

```bash
pip install opencv-python mediapipe numpy
```

3. **Run the project**
```bash
python main.py
```

## 💻 Usage
* Look into the webcam.
* Blink **short** (≈ < 0.5 sec) for `.` and **long** (≈ ≥ 0.5 sec) for `-`.
* Morse code will display and translate in real-time.
* Press `r` to reset the message.
* Press `q` to quit.
  
## 📂 Folder Structure
<pre lang="markdown"> ```python
morse-eye-blink/
├── morse_blink.py          # Main script
├── requirements.txt        # Required packages
├── README.md               # This file
└── demo.gif                # Optional demo preview
</pre>

## 📄 License
This project is licensed under the **MIT License**.
Feel free to use, modify, and share. See the [LICENSE](LICENSE) file for details.

