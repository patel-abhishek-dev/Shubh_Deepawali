# Diwali Celebration

A single-page interactive Deepawali (Diwali) greeting built with HTML, CSS, and vanilla JavaScript. Light diyas, draw rangoli, launch fireworks over a moonlit ocean, open a mithai box of traditional sweets, and share festive wishes — all in a responsive, animated celebration experience.

## Features

- **Jhalar lights** — Toggle decorative string lights and side jhalars on and off.
- **Diya lighting ritual** — Eight clay diyas start unlit; tap each one to light its flame and fill the courtyard with warm light.
- **Firework courtyard** — Launch Anar fountains and Chakri spinning wheels from opposite corners of the ocean stage.
- **Full-screen ocean simulation** — A cinematic, full-screen Hanabi-style fireworks show over a dark, reflective ocean with an Exit button to return to the main page.
- **Rangoli studio** — Draw mandala-style rangoli patterns with mouse or touch, 4–16 fold radial symmetry, adjustable pen size, color swatches, mandala stamp, and clear canvas.
- **Wish lanterns** — Write a wish and release a sky lantern into the night.
- **Quote carousel** — Cycle through festive Deepawali blessings.
- **Mithai box** — Open a box of eight traditional Indian sweets; click any sweet to reveal its personalized blessing.
- **WhatsApp sharing** — Share the celebration directly to WhatsApp (includes the live page URL when hosted on HTTPS).
- **Optional sound** — Synthesized chimes that play only when explicitly enabled by the visitor.
- **Responsive design** — Adapts to desktop and mobile screens, with reduced-motion support.

## Technology Stack

- **HTML5** — Semantic markup with ARIA attributes for accessibility.
- **CSS3** — Custom properties, gradients, animations, media queries, and backdrop filters. All styling is embedded in `index.html`; no external stylesheets.
- **Vanilla JavaScript** — Canvas 2D rendering for all fireworks and particle animations; no frameworks or libraries.
- **Python 3 (standard library)** — `app.py` provides a lightweight local HTTP server using only `http.server`, `json`, `os`, `sys`, `webbrowser`, and `urllib.parse`. No `pip install` required.

## Project Structure

```
diwali-application/
├── app.py                  # Python local HTTP server entry point
├── index.html              # Main application (HTML + embedded CSS + JavaScript)
├── README.md               # Project documentation
├── requirements.txt        # Python dependencies note (standard library only)
└── .gitignore              # Git ignore rules for Python and web projects
```

## Installation Requirements

- Python 3.x (for the local server; optional — you can also open `index.html` directly in a browser)
- A modern web browser (Chrome, Edge, Firefox, Safari, etc.)

No `npm`, `pip install`, or build step is required.

## Setup Instructions

### Option 1 — Open directly in a browser

Simply open `index.html` in any modern browser. All features work immediately without a server.

### Option 2 — Run with the Python server

1. Ensure Python 3 is installed.
2. From the project directory, run:
   ```sh
   python app.py
   ```
3. The server starts and opens your default browser at:
   ```sh
   http://localhost:8000
   ```
4. A health endpoint is available at:
   ```sh
   http://localhost:8000/health
   ```
   It returns JSON: `{"status": "ok", "server": "deepawali"}`
5. Press **Ctrl+C** in the terminal to stop the server.

The server serves all static files from the project directory, handles browser refresh safely, and blocks directory-traversal requests.

## Usage Instructions

| Feature | How to use |
|---------|------------|
| Jhalar lights | Click "✨ Jhalars: On" in the topbar to toggle decorative lights. |
| Diyas | Click any unlit diya in the courtyard to light its flame. |
| Anar / Chakri | Click the firework station buttons in the ocean section. |
| Full-screen simulation | Click "Set off fireworks" or "Launch the grand chrysanthemum"; click **Exit simulation** to return. |
| Rangoli | Click "Open rangoli studio," choose 4–16 folds, then draw on the canvas. |
| Wish lantern | Type a wish and click "Release wish 🏮" or the lantern button. |
| Mithai box | Click "Open mithai box 🍬," then tap any sweet to read its blessing. |
| Quotes | Click "Another blessing" to cycle through festive messages. |
| WhatsApp | Click "Share on WhatsApp" to share the celebration. |
| Sound | Click "♫ Sound: Off" in the topbar to enable optional chimes. |

## Credits

Created for the Festival of Light. शुभ दीपावली.

All illustrations (sweets, diyas, lanterns, fireworks) are drawn with CSS and HTML5 Canvas — no external image assets or font files are required.

## Future Improvements

- Add more sweet varieties and blessings to the Mithai box.
- Add additional rangoli color palettes and symmetry presets.
- Expand the ocean fireworks simulation with more shell types.
- Add sound effects synchronized to firework bursts.
- Add a gallery to save and revisit rangoli designs.

## License

No license file is included in this repository. If you plan to publish or redistribute this project publicly, please add an appropriate `LICENSE` file (e.g., MIT, Apache-2.0) before doing so.
