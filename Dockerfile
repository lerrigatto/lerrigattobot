FROM python:3.7-slim AS builder

RUN pip install poetry

WORKDIR /build
COPY . /build
RUN poetry build

FROM python:3.7-slim
WORKDIR /app
COPY --from=builder /build/dist/ /app/dist
RUN pip install /app/dist/*.whl
CMD ["lerrigattobot"]
