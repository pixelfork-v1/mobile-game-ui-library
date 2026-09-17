"""
Generate an image with the Gemini API.

The key is never printed and never passes through the chat. It is looked up, in this order:
  1. --key-cmd "…"     any command that prints the key, e.g.
                         --key-cmd "op read op://Personal/Gemini/credential"        (1Password CLI)
                         --key-cmd "security find-generic-password -w -s gemini"    (macOS Keychain)
  2. --key-file PATH   a file holding the key, or a KEY=value line containing it
  3. tools/.env        GEMINI_API_KEY=...   (git-ignored)
  4. the environment   GEMINI_API_KEY / GOOGLE_API_KEY

Usage:
  python3 tools/gen_image.py "a chunky red potion bottle, transparent background" out.png
  python3 tools/gen_image.py --model imagen-4.0-generate-001 "…" out.png
  python3 tools/gen_image.py --prompt-file prompt.txt out.png
"""
import argparse, base64, json, os, pathlib, sys, urllib.error, urllib.request

ENV = pathlib.Path(__file__).with_name('.env')
if ENV.exists():                                   # optional local file, gitignored
    for line in ENV.read_text().splitlines():
        line = line.strip()
        if line and not line.startswith('#') and '=' in line:
            k, v = line.split('=', 1)
            os.environ.setdefault(k.strip(), v.strip().strip('"\''))

ap = argparse.ArgumentParser()
ap.add_argument('--key-cmd', help='command that prints the key (1Password, Keychain, …)')
ap.add_argument('--key-file', help='file holding the key')
ap.add_argument('prompt', nargs='?', default=None)
ap.add_argument('out')
ap.add_argument('--model', default='gemini-2.5-flash-image')
ap.add_argument('--prompt-file')
a = ap.parse_args()

def find_key(args):
    if args.key_cmd:
        import subprocess
        out = subprocess.run(args.key_cmd, shell=True, capture_output=True, text=True)
        if out.returncode:
            sys.exit(f'key command failed: {out.stderr.strip()[:200]}')
        return out.stdout.strip()
    if args.key_file:
        for line in pathlib.Path(args.key_file).expanduser().read_text().splitlines():
            line = line.strip()
            if not line or line.startswith('#'):
                continue
            return (line.split('=', 1)[1] if '=' in line else line).strip().strip('"\'')
    return os.environ.get('GEMINI_API_KEY') or os.environ.get('GOOGLE_API_KEY')

KEY = find_key(a)
if not KEY:
    sys.exit('No key found. Pass --key-cmd or --key-file, or set GEMINI_API_KEY in tools/.env')

prompt = pathlib.Path(a.prompt_file).read_text() if a.prompt_file else a.prompt
if not prompt:
    sys.exit('Give a prompt, or --prompt-file')

url = f'https://generativelanguage.googleapis.com/v1beta/models/{a.model}:generateContent'
body = json.dumps({'contents': [{'parts': [{'text': prompt}]}]}).encode()
req = urllib.request.Request(url, data=body, headers={'Content-Type': 'application/json', 'x-goog-api-key': KEY})
try:
    res = json.loads(urllib.request.urlopen(req, timeout=180).read())
except urllib.error.HTTPError as e:
    detail = e.read().decode()[:400].replace(KEY, '***')          # never echo the key
    sys.exit(f'{a.model}: HTTP {e.code}\n{detail}')

parts = res.get('candidates', [{}])[0].get('content', {}).get('parts', [])
data = next((p['inlineData']['data'] for p in parts if 'inlineData' in p), None)
if not data:
    text = ' '.join(p.get('text', '') for p in parts)[:400]
    sys.exit(f'No image came back. Model said: {text or json.dumps(res)[:400]}')

out = pathlib.Path(a.out); out.parent.mkdir(parents=True, exist_ok=True)
out.write_bytes(base64.b64decode(data))
print(f'wrote {out} ({out.stat().st_size // 1024} KB)')
