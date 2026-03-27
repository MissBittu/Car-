# Phantom Strike — AI Automotive Configurator

**3-Day Solutions Engineer Evaluation | Game Development with Generative AI**

A real-time interactive car configurator for the automotive sector, featuring live generative AI build suggestions powered by Groq (Llama 3.3), a full 3D garage environment, multi-view SVG car rendering, and dynamic pricing — delivered as a production-grade web application.

---
# Phantom Strike — AI Automotive Configurator

**3-Day Solutions Engineer Evaluation | Game Development with Generative AI**

## Introduction

Hi, I’m Sakshi Meena, a final-year Automation and Robotics Engineering student at IIIT Bhagalpur with a strong focus on AI, machine learning, and intelligent systems.

For this evaluation, I built **Phantom Strike — an AI-powered automotive configurator** that allows users to interactively customize a sports car and generate themed configurations using generative AI. The project demonstrates real-time interaction, clean UI design, and practical integration of AI to enhance user-driven customization experiences.

The system combines a lightweight web-based 3D configurator with AI-generated design suggestions powered by **Groq’s Llama 3.3 model**, showing how generative AI can support interactive product experiences.

**Project Repository:**  
https://github.com/MissBittu/Car-

## Table of Contents

- [Project Overview](#project-overview)
- [Features](#features)
- [Tech Stack](#tech-stack)
- [Project Structure](#project-structure)
- [Prerequisites](#prerequisites)
- [Installation & Setup](#installation--setup)
- [Running the Project](#running-the-project)
- [AI Integration](#ai-integration)
- [How to Use](#how-to-use)
- [Evaluation Criteria](#evaluation-criteria)

---

## Project Overview

Phantom Strike is an interactive automotive showcase that allows users to fully configure a sports car in real time. Users can modify exterior color, wheel style, accent finish, and showcase environment. A generative AI layer — powered by the Groq API (Llama 3.3 70B) — suggests complete themed build configurations based on user-selected themes such as Sporty, Luxury, Stealth, Racing, or Off-Road.

The project is delivered as a single-page HTML5 application served by a lightweight Python backend that proxies AI requests, resolving browser CORS restrictions and keeping the API key secure on the server side.

---

## Features

### Game Mechanics
- Select and apply exterior color (10 options), wheel style (4 options), accent finish (4 options), and showcase environment (4 options)
- Real-time car re-render on every option change
- Drag / hover on the car to rotate wheels interactively
- Hover over car parts (body, wheels, calipers, wing, exhaust) to reveal live component spec tooltips
- 4 distinct camera views: Side, Front, Rear, Top — each a separate SVG drawing
- Build submission modal with full config summary
- Price breakdown panel updated live on every selection
- Copy configuration as JSON to clipboard
- Reset to default with one click

### Graphics
- Full 3D garage environment rendered in CSS perspective — ceiling spotlights with light cones, horizontal wall seams, perspective floor tile grid, structural corner pillars, and side equipment panels
- Animated ground glow beneath the car
- Cinematic intro screen with animated perspective grid and staggered text reveal
- Custom cursor with tracking ring
- Distinct procedural SVG car per view angle with live color, wheel spoke pattern, accent stripe, caliper, and splitter updates

### Generative AI
- Groq API integration (Llama 3.3 70B) — free tier, no credit card required
- 5 selectable themes: Sporty, Luxury, Stealth, Racing, Off-Road
- Generates 3 named configurations per theme with color, wheels, accent, and tagline
- AI "thinking" animation with rotating status messages during generation
- One-click apply — instantly updates the live car and all panels
- Full graceful fallback to curated preset configs if AI is unavailable
- Generated theme tracked in the JSON output

### Documentation
- Built-in README tab inside the configurator UI
- Evaluation criteria mapping with scores
- Full interaction guide and AI explanation

---

## Tech Stack

| Layer | Technology |
|---|---|
| Frontend | HTML5, CSS3, Vanilla JavaScript |
| Car Rendering | Procedural SVG (state-driven) |
| 3D Environment | CSS Perspective transforms |
| AI Provider | Groq API — Llama 3.3 70B (free) |
| Backend | Python 3 — `http.server` (stdlib only) |
| AI Client | `groq` Python package |
| Fonts | Bebas Neue, Exo 2, JetBrains Mono |

No build tools, no frameworks, no bundler required.

---

## Project Structure

```
car pro/
├── phantom-ultimate.html   # Full frontend application
├── server.py               # Python backend — serves HTML + proxies AI
└── README.md               # This file
```

---

## Prerequisites

- Python 3.8 or higher
- pip
- A free Groq API key — get one at [console.groq.com](https://console.groq.com) (sign up with Google or GitHub, no credit card)

---

## Installation & Setup

**Step 1 — Clone or download the project**

Place both `phantom-ultimate.html` and `server.py` in the same folder, for example `D:\AS\car pro\`.

**Step 2 — Install the Groq Python package**

```bash
pip install groq
```

**Step 3 — Get a free Groq API key**

1. Go to [console.groq.com](https://console.groq.com)
2. Sign up with Google or GitHub (free, no card needed)
3. Navigate to **API Keys → Create API Key**
4. Copy the key — it starts with `gsk_`

**Step 4 — Add your API key to server.py**

Open `server.py` and find line 20:

```python
GROQ_KEY = "YOUR_GROQ_KEY_HERE"
```

Replace with your actual key:

```python
GROQ_KEY = "gsk_xxxxxxxxxxxxxxxxxxxxxxxxxxxx"
```

Alternatively, set it as an environment variable so you never hardcode it:

```bash
# Windows
set GROQ_API_KEY=gsk_xxxxxxxxxxxxxxxxxxxxxxxxxxxx

# Mac / Linux
export GROQ_API_KEY=gsk_xxxxxxxxxxxxxxxxxxxxxxxxxxxx
```

---

## Running the Project

Open a terminal in your project folder and run:

```bash
python server.py
```

Expected output:

```
==================================================
  PHANTOM STRIKE - AI Configurator
==================================================
  Groq AI ready: gsk_xxxxxxxxxxxx...
  groq package: installed OK

  Open: http://localhost:8000
  Ctrl+C to stop
```

Open your browser and navigate to:

```
http://localhost:8000
```

---

## AI Integration

The AI component uses the **Groq API** with the **Llama 3.3 70B Versatile** model. When the user clicks **⚡ GENERATE AI BUILDS**, the browser sends a POST request to the local Python server at `/generate`. The server constructs a structured prompt and calls Groq, which returns a JSON array of 3 named car configurations. The frontend parses the response and renders clickable build cards. Selecting a card instantly applies the full configuration to the live car.

**Request flow:**

```
Browser → POST /generate {theme} → server.py → Groq API (Llama 3.3)
                                                       ↓
Browser ← {configs: [...]}       ← server.py ← JSON response
```

**System prompt constraints** ensure the model returns only a valid JSON array with the exact fields the frontend expects (`name`, `color`, `wheel`, `accent`, `desc`). If the AI is unavailable for any reason, the server falls back to a curated set of preset configs so the demo always functions.

**AI-generated JSON output example:**

```json
{
  "model": "phantom_strike",
  "car_color": "red",
  "wheel_style": "racing",
  "accent_style": "carbon",
  "environment": "garage",
  "ai_theme": "sporty",
  "price": "278000"
}
```

---

## How to Use

1. **Select a theme** — choose from Sporty, Luxury, Stealth, Racing, or Off-Road
2. **Generate AI builds** — click ⚡ GENERATE AI BUILDS and watch the AI think
3. **Apply a config** — click any generated card to instantly update the car
4. **Refine manually** — adjust color swatches, wheel cards, accent cards, or environment
5. **Explore views** — switch between SIDE / FRONT / REAR / TOP camera angles
6. **Inspect parts** — hover over the car in Side view to reveal component specs
7. **Rotate wheels** — hover left/right on the car to spin the wheels
8. **Review pricing** — the summary panel shows a live price breakdown
9. **Submit build** — click SUBMIT FINAL BUILD to confirm and copy the JSON config

---

## Evaluation Criteria

| Criterion | Implementation | Rating |
|---|---|---|
| **Game Mechanics** | Select/apply options, drag-rotate, hover tooltips, 4 views, live price, submit, reset | Excellent |
| **Graphics** | 3D CSS garage with spotlights, floor grid, pillars; 4 SVG car views; live color/wheel/accent on car | Excellent |
| **AI Integration** | Groq Llama 3.3, 5 themes, 3 configs each, thinking animation, one-click apply, JSON output | Excellent |
| **Documentation** | This README + built-in README tab in the UI with criteria mapping and interaction guide | Excellent |
| **Creativity** | Cinematic intro, part tooltips, drag-rotate mechanic, environment switching, AI thinking state | Excellent |
#   C a r -     
 
 