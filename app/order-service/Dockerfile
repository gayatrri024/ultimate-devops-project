FROM alpine:3.24 AS builder

RUN apk add --no-cache python3 py3-pip

WORKDIR /build

COPY requirements.txt .

RUN pip install --no-cache-dir --prefix=/install -r requirements.txt

FROM alpine:3.24

RUN apk add --no-cache python3

WORKDIR /app

COPY --from=builder /install /usr/local
COPY . .

ENV PYTHONPATH=/usr/local/lib/python3.14/site-packages
ENV PYTHONUNBUFFERED=1

EXPOSE 8001

CMD ["python3", "app.py"]
