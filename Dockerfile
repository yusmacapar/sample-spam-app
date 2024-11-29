from python:3.9-slim

workdir /app

copy requirements.txt ./requirements.txt

run pip install --no-cache-dir -r requirements.txt

copy app.py ./app.py
copy model ./model

expose 8501

cmd ["streamlit","run","./app.py"]