# Manutenção Preventiva — Projeto Revisado

## Backend
```bash
cd manutencao_preventiva
python -m venv venv
# Windows: venv\Scripts\activate
# Linux/Mac: source venv/bin/activate
pip install -r requirements.txt
python -m flask --app src/main.py run
```

API estará em http://localhost:5000/api

## Frontend
```bash
cd manutencao-frontend
npm install
npm run dev
```

App em http://localhost:5173 — o proxy envia `/api/*` para o backend.
