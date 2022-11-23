FROM python:3
ENV PYTHONUNBUFFERED 1
RUN mkdir /code-agentcultural
COPY requirements.txt /code-agentcultural/
WORKDIR /code-agentcultural
RUN pip install -r requirements.txt
COPY . /code-agentcultural
