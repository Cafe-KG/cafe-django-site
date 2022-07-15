FROM python:3

ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

WORKDIR /cafe

COPY req.txt /cafe
ADD wsgi-entrypoint.sh /cafe
ENV PYTHONPATH=/cafe

RUN python -m pip install --upgrade pip
RUN pip install -r req.txt

COPY . /cafe

EXPOSE 8000

CMD [ "chmod", "+x", "wsgi-entrypoint.sh" ]
