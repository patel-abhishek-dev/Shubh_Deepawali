#!/usr/bin/env python3
"""
Shubh Deepawali — Local Python HTTP Server

Serves the Diwali celebration application (index.html) over a local
HTTP address. Uses only the Python standard library — no external
dependencies required.

Usage:
    python app.py

Then open: http://localhost:8000

Endpoints:
    /          -> serves index.html
    /health    -> returns JSON { "status": "ok" }
    /<path>    -> serves static files (CSS, JS, images, etc.) from the
                  project root, with directory-traversal protection.
"""

import http.server
import json
import os
import sys
import webbrowser
from urllib.parse import unquote, urlparse

# ---------------------------------------------------------------------------
# Configuration
# ---------------------------------------------------------------------------
HOST = "127.0.0.1"
PORT = 8000

# Project root is the directory containing this script.
PROJECT_ROOT = os.path.dirname(os.path.abspath(__file__))

# ---------------------------------------------------------------------------
# Request handler
# ---------------------------------------------------------------------------
class DeepawaliHandler(http.server.SimpleHTTPRequestHandler):
    """Custom handler that serves the Diwali app with safety checks."""

    def __init__(self, *args, **kwargs):
        super().__init__(*args, directory=PROJECT_ROOT, **kwargs)

    # ----- Health endpoint -----
    def do_GET(self):
        parsed = urlparse(self.path)
        path = unquote(parsed.path)

        # Health check — returns JSON.
        if path == "/health":
            self.send_response(200)
            self.send_header("Content-Type", "application/json")
            self.end_headers()
            self.wfile.write(json.dumps({"status": "ok", "server": "deepawali"}).encode("utf-8"))
            return

        # Serve index.html for the root path.
        if path == "/" or path == "":
            self.path = "/index.html"
            return super().do_GET()

        # Static file request — enforce directory-traversal protection.
        # Resolve the requested path relative to PROJECT_ROOT and ensure
        # it stays inside the project directory.
        requested = os.path.normpath(os.path.join(PROJECT_ROOT, path.lstrip("/")))
        if not requested.startswith(PROJECT_ROOT + os.sep) and requested != PROJECT_ROOT:
            self.send_error(403, "Forbidden: path escapes project root")
            return

        if not os.path.exists(requested) or os.path.isdir(requested):
            # Missing file — serve index.html so client-side routing works
            # and users can refresh without 404s.
            self.path = "/index.html"
            return super().do_GET()

        # File exists — serve it normally.
        self.path = path
        return super().do_GET()

    # ----- Logging -----
    def log_message(self, format, *args):
        # Keep startup/shutdown output clean but still log requests briefly.
        sys.stderr.write("%s - - [%s] %s\n" % (self.address_string(), self.log_date_time_string(), format % args))

    # ----- Override to suppress the default noisy banner on every request -----
    def version_string(self):
        return "DeepawaliServer/1.0"


# ---------------------------------------------------------------------------
# Main entry point
# ---------------------------------------------------------------------------
def main():
    server_address = (HOST, PORT)

    try:
        httpd = http.server.HTTPServer(server_address, DeepawaliHandler)
    except OSError as exc:
        print(f"ERROR: Could not start server on {HOST}:{PORT}")
        print(f"       {exc}")
        sys.exit(1)

    url = f"http://{HOST}:{PORT}/"
    print("=" * 60)
    print("  Shubh Deepawali — Local Server")
    print("=" * 60)
    print(f"  Serving: {PROJECT_ROOT}")
    print(f"  URL:     {url}")
    print(f"  Health:  {url}health")
    print("=" * 60)
    print("  Press Ctrl+C to stop the server.")
    print("=" * 60)

    # Open the application in the default browser.
    try:
        webbrowser.open(url)
    except Exception as exc:
        print(f"  (Could not auto-open browser: {exc})")

    try:
        httpd.serve_forever()
    except KeyboardInterrupt:
        print("\n")
        print("=" * 60)
        print("  Server shutting down…")
        print("=" * 60)
        httpd.server_close()
        print("  Stopped.")
        sys.exit(0)


if __name__ == "__main__":
    main()
