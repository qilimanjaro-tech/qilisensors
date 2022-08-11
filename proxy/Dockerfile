FROM python:3.9-alpine3.15

RUN pip install paho-mqtt

COPY ./main.py . 

ENTRYPOINT ["python","main.py"]