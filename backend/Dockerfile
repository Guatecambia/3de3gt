FROM python:3
# Set environment variables
ENV PYTHONUNBUFFERED 1
COPY requirements.txt /
# Install dependencies.
RUN pip install -r /requirements.txt
# Set work directory.
RUN mkdir /code
WORKDIR /code
COPY . .
EXPOSE 80
