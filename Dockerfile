FROM python:3.12-slim-bookworm
COPY --from=ghcr.io/astral-sh/uv:latest /uv /bin/uv

WORKDIR /src
COPY . /src

RUN uv venv --python 3.12 && uv pip install -r requirements.txt

ENV PATH="/src/.venv/bin:$PATH"
CMD ["python", "HoeWarmIsHetInDelft.py"]