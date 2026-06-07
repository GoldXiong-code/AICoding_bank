ARG PIP_INDEX_URL=https://pypi.org/simple

FROM python:3.11-slim

ARG PIP_INDEX_URL
ENV PIP_INDEX_URL=${PIP_INDEX_URL}

WORKDIR /app

COPY requirements.txt .
RUN pip install --no-cache-dir --timeout 120 -i "${PIP_INDEX_URL}" -r requirements.txt

COPY src/ ./src/
COPY data/ ./data/
COPY .streamlit/ ./.streamlit/

RUN mkdir -p artifacts

EXPOSE 8004

HEALTHCHECK --interval=30s --timeout=5s --start-period=10s --retries=3 \
  CMD curl -fsS http://localhost:8004/_stcore/health || exit 1

CMD ["streamlit", "run", "src/app.py", "--server.port=8004", "--server.address=0.0.0.0"]
