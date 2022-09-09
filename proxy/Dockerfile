FROM python:3.5-slim

RUN pip install paho-mqtt

COPY ./main.py . 

RUN chmod +x /main.py

CMD [ "python", "-u", "main.py" ]