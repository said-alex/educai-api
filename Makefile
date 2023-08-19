default: app-start

install-dependencies:
	pip install -r requirements.txt

app-start:
	uvicorn app.main:app --host 0.0.0.0 --port 8000 --reload
