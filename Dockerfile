FROM python:alpine3.17
RUN addgroup mosihere && adduser mosihere -S -G mosihere mosihere
USER mosihere
WORKDIR /app
COPY requirements.txt .
RUN python -m pip install -r requirements.txt
COPY . .
ENV PYTHONUNBUFFERED=1
EXPOSE 8020
CMD ["python", "manage.py", "runserver", "0.0.0.0:8020"]