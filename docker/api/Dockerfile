FROM python:3.5
ENV PYTHONUNBUFFERED 1

RUN mkdir -p /srv/project/src/

WORKDIR /srv/project/src/

COPY api-requirements.txt /tmp/requirements.txt
RUN pip install -r /tmp/requirements.txt

COPY ./api.py /srv/project/src/

ENTRYPOINT ["gunicorn", "api:app", "-b", "0.0.0.0:8888"]
