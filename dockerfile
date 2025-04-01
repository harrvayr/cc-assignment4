FROM python:3.12.9-bookworm
WORKDIR /sentiment-analysis-backend
COPY requirements.txt /sentiment-analysis-backend/requirements.txt
RUN pip install -r requirements.txt
EXPOSE 8100
COPY . /sentiment-analysis-backend/
CMD ["python", "app.py"]
