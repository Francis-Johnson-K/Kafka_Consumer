FROM python:3.9
COPY ./requirements.txt /tmp/requirements.txt
RUN pip install --no-cache-dir -r /tmp/requirements.txt
RUN pip install --upgrade pip
COPY ./app/ /app
WORKDIR /app
ENV PYTHONPATH /
CMD ["python", "run.py"]