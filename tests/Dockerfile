FROM python:3.9

WORKDIR /tests

COPY ./tests/requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

COPY ./src /src
COPY ./tests .

CMD ["ptw", "--runner", "pytest --maxfail=5 --disable-warnings"]