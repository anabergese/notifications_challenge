FROM python:alpine

RUN apk add --no-cache gcc musl-dev linux-headers

COPY ./tests/requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt
COPY ./tests .
COPY ./src /src

WORKDIR /tests

CMD ["ptw", "--runner", "pytest --maxfail=5 --disable-warnings"]