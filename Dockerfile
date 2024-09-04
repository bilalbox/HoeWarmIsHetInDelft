FROM python:3.12-slim-bookworm
COPY --from=ghcr.io/astral-sh/uv:latest /uv /bin/uv

WORKDIR /src
COPY . /src

# ENV VIRTUAL_ENV=/opt/venv \
#     PATH="/opt/venv/bin:$PATH"

RUN uv venv --python 3.12 && uv sync
 
# FROM python:3.12-slim
# COPY --from=build /src /src
# WORKDIR /src
ENV PATH="/src/.venv/bin:$PATH"
CMD ["python", "HoeWarmIsHetInDelft.py"]