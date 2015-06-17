FROM python:latest
ADD requirements.txt .
RUN pip install -r requirements.txt
WORKDIR /src
ENTRYPOINT ["python", "manage.py"]
CMD ["runserver", "0.0.0.0:8000"]
