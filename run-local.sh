#!/usr/bin/env bash
# Lokalny runner PoC M1/M2: FastAPI na 127.0.0.1:8003
set -Eeuo pipefail

ROOT="$(cd -- "$(dirname -- "${BASH_SOURCE[0]}")" && pwd)"
cd "$ROOT"
VENV="$ROOT/.venv"
PY="$VENV/bin/python"
HOST="127.0.0.1"
PORT=8003

usage() {
  cat <<'HELP'
Użycie: ./run-local.sh [setup|test|start|check|all|help]
  setup  - utwórz .venv i zainstaluj zależności
  test   - uruchom testy pytest (instaluje zależności w razie potrzeby)
  start  - uruchom FastAPI na http://127.0.0.1:8003 (Ctrl+C zatrzymuje)
  check  - sprawdź endpoint /health działającej aplikacji
  all    - instalacja, testy i uruchomienie FastAPI (domyślnie)
  help   - pokaż pomoc
HELP
}

setup() {
  if ! command -v python3 >/dev/null 2>&1; then
    echo 'BŁĄD: Brak python3 w PATH.' >&2; exit 1
  fi
  if [[ ! -x "$PY" ]]; then
    echo '==> Tworzenie środowiska .venv'
    python3 -m venv "$VENV"
  fi
  echo '==> Instalacja zależności (requirements-dev.txt)'
  "$PY" -m pip install -r requirements-dev.txt
}

ensure_venv() {
  if [[ ! -x "$PY" ]]; then
    setup
  fi
}

run_tests() {
  ensure_venv
  echo '==> Testy pytest'
  "$PY" -m pytest -v
}

start_app() {
  ensure_venv
  if ! "$PY" - <<'PY'
import socket
s = socket.socket()
try:
    s.bind(('127.0.0.1', 8003))
except OSError:
    raise SystemExit(1)
finally:
    s.close()
PY
  then
    echo 'BŁĄD: Port 8003 jest już zajęty. Zatrzymaj poprzednią instancję.' >&2
    exit 1
  fi
  echo '==> Aplikacja: http://127.0.0.1:8003'
  echo '==> Swagger UI: http://127.0.0.1:8003/docs'
  echo '==> Health: http://127.0.0.1:8003/health'
  exec "$PY" -m uvicorn app.main:app --reload --host "$HOST" --port "$PORT"
}

check_app() {
  ensure_venv
  "$PY" - <<'PY'
import json
from urllib.request import urlopen
from urllib.error import URLError
url = 'http://127.0.0.1:8003/health'
try:
    with urlopen(url, timeout=5) as r:
        body = json.load(r)
        print(f'HTTP {r.status}: {body}')
        if r.status != 200 or body.get('status') != 'ok':
            raise SystemExit(1)
except (URLError, TimeoutError) as exc:
    print(f'BŁĄD: aplikacja nie odpowiada: {exc}')
    raise SystemExit(1)
PY
}

case "${1:-all}" in
  setup) setup ;;
  test) run_tests ;;
  start) start_app ;;
  check) check_app ;;
  all) setup; run_tests; start_app ;;
  help|-h|--help) usage ;;
  *) usage >&2; exit 2 ;;
esac
