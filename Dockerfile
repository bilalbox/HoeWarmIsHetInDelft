FROM python:3.12 AS build

WORKDIR /src
COPY . /src

ENV VIRTUAL_ENV=/opt/venv \
    PATH="/opt/venv/bin:$PATH"

RUN python -m venv /opt/venv && pip install --no-cache -r requirements.txt
 
FROM python:3.12-slim
COPY --from=build /src /src
COPY --from=build /opt/venv /opt/venv
WORKDIR /src
ENV PATH="/opt/venv/bin:$PATH"
CMD ["python", "HoeWarmIsHetInDelft.py"]