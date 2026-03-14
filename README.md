# Phantom Strike — AI Automotive Configurator

**3-Day Solutions Engineer Evaluation — Game Development with Generative AI**

Phantom Strike is an interactive automotive configurator that allows users to customize a sports car in real time inside a garage environment. The application integrates a generative AI system to suggest complete car configurations based on design themes such as **Sporty, Luxury, Stealth, Racing, and Off-Road**.

The project demonstrates core skills in **interactive system design, real-time rendering, and practical AI integration** while staying within the constraints of a short development timeline.

---

# Project Overview

Phantom Strike provides a focused interactive experience where users can configure a vehicle visually while receiving AI-generated design recommendations.

Users can modify:

* Car color
* Wheel style
* Accent finish
* Showcase environment

A generative AI layer powered by **Groq (Llama 3.3 70B)** produces themed configuration suggestions which can be applied instantly to the car.

The application is implemented as a **single-page web application** with a lightweight Python server that securely handles AI requests.

---

# Core Features

## Game Mechanics

The system allows users to interactively configure the car with immediate visual feedback.

Features include:

* Select and apply **car colors**
* Switch between **multiple wheel styles**
* Choose **accent finishes**
* Change the **display environment**
* View the car from **four camera perspectives** (Side, Front, Rear, Top)
* Hover over components to view **technical specifications**
* Apply AI-generated configurations with **one click**
* Live **configuration summary and price breakdown**
* Export configuration as **JSON**

All selections update the rendered car **instantly**, providing real-time interaction.

---

## Graphics and Environment

The visual presentation focuses on clarity and atmosphere within the project scope.

Key elements include:

* A stylized **garage environment** built using CSS perspective
* Procedural **SVG car rendering** for multiple camera angles
* Dynamic lighting effects and animated ground glow
* Custom UI styling and cinematic intro screen

The approach prioritizes **clean visuals and responsiveness** rather than heavy assets.

---

## Generative AI Integration

Generative AI is used to suggest themed car configurations.

Users select a design theme such as:

* Sporty
* Luxury
* Stealth
* Racing
* Off-Road

The system then generates **three complete configurations** containing:

* car color
* wheel style
* accent finish
* build description

These suggestions are generated using the **Groq API with the Llama 3.3 70B model**.

If the AI service is unavailable, the system automatically falls back to curated preset configurations to ensure the experience always functions.

---

# Technology Stack

| Layer         | Technology                         |
| ------------- | ---------------------------------- |
| Frontend      | HTML5, CSS3, Vanilla JavaScript    |
| Car Rendering | Procedural SVG                     |
| Environment   | CSS Perspective                    |
| Backend       | Python 3 (lightweight HTTP server) |
| AI Model      | Groq API – Llama 3.3 70B           |
| Fonts         | Bebas Neue, Exo 2, JetBrains Mono  |

The system intentionally avoids heavy frameworks to keep the architecture **lightweight and transparent**.

---

# Project Structure

```
phantom-strike/
├── phantom-ultimate.html   # Frontend application
├── server.py               # Python backend (AI proxy)
└── README.md               # Project documentation
```

---

# Setup Instructions

### 1. Install Python dependency

```bash
pip install groq
```

### 2. Add your Groq API key

Edit `server.py` and set:

```python
GROQ_KEY = "YOUR_API_KEY"
```

Alternatively use an environment variable:

```bash
export GROQ_API_KEY=your_key_here
```

### 3. Start the server

```bash
python server.py
```

Open the application in your browser:

```
http://localhost:8000
```

---

# AI Request Flow

```
Browser → POST /generate → Python server → Groq API (Llama 3.3)
                                          ↓
Browser ← JSON configuration ← server response
```

The server constructs a structured prompt and returns a JSON array of configuration objects that the frontend converts into clickable build cards.

Example AI output:

```json
{
 "car_color": "red",
 "wheel_style": "racing",
 "accent_style": "carbon",
 "ai_theme": "sporty"
}
```

Selecting a generated build **instantly applies the configuration** to the live car.

---

# How to Use

1. Select a **design theme**
2. Click **Generate AI Builds**
3. Review the suggested configurations
4. Click a configuration to apply it
5. Refine options manually if desired
6. Explore different camera views
7. Submit the final build configuration

---

# Evaluation Criteria Mapping

| Evaluation Area | Implementation                                            |
| --------------- | --------------------------------------------------------- |
| Game Mechanics  | Interactive customization with real-time updates          |
| Graphics        | Clean garage environment and responsive SVG car rendering |
| AI Integration  | Generative theme-based configuration suggestions          |
| Documentation   | Structured README and in-app usage guide                  |
| Creativity      | Cinematic presentation and interactive UI features        |

---

# Summary

Phantom Strike demonstrates how **interactive visualization and generative AI** can be combined to build a lightweight automotive configurator. The project focuses on clear interaction design, practical AI usage, and efficient engineering within a limited development window.
