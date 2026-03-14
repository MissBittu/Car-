import json
from http.server import HTTPServer, SimpleHTTPRequestHandler
from groq import Groq

import os
GROQ_KEY = os.environ.get("GROQ_API_KEY", "")
client = Groq(api_key=GROQ_KEY)

class Handler(SimpleHTTPRequestHandler):
    def do_POST(self):
        if self.path == '/api/generate':
            length = int(self.headers['Content-Length'])
            body = json.loads(self.rfile.read(length))
            theme = body.get('theme', 'sporty')
            try:
                resp = client.chat.completions.create(
                    model="llama3-70b-8192",
                    messages=[
                        {"role": "system", "content": "You are a luxury car configurator AI. Given a theme, return exactly 3 car build configurations as a valid JSON array ONLY. No markdown, no explanation, just the array. Each object must have: name (2 words max, uppercase), color (one of: black/red/blue/white/silver/gold/green/purple/orange/carbon), wheel (one of: racing/sport/luxury/classic), accent (one of: carbon/chrome/matte/neon), desc (tagline under 50 chars)."},
                        {"role": "user", "content": f'Generate 3 Phantom Strike configurations for theme: "{theme}"'}
                    ],
                    max_tokens=1200,
                )
                text = resp.choices[0].message.content.replace("```json","").replace("```","").strip()
                cfgs = json.loads(text)
                self.send_response(200)
                self.send_header('Content-Type','application/json')
                self.send_header('Access-Control-Allow-Origin','*')
                self.end_headers()
                self.wfile.write(json.dumps(cfgs).encode())
            except Exception as e:
                self.send_response(500)
                self.send_header('Content-Type','application/json')
                self.send_header('Access-Control-Allow-Origin','*')
                self.end_headers()
                self.wfile.write(json.dumps({"error": str(e)}).encode())
        else:
            self.send_response(404)
            self.end_headers()

    def do_OPTIONS(self):
        self.send_response(200)
        self.send_header('Access-Control-Allow-Origin','*')
        self.send_header('Access-Control-Allow-Methods','POST, OPTIONS')
        self.send_header('Access-Control-Allow-Headers','Content-Type')
        self.end_headers()

    def log_message(self, format, *args):
        print(f"[{self.address_string()}] {format % args}")

if __name__ == '__main__':
    server = HTTPServer(('localhost', 8000), Handler)
    print("Server running at http://localhost:8000")
    server.serve_forever()
