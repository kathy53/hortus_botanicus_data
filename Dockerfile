# Official Playwright image for Python
FROM mcr.microsoft.com/playwright/python:v1.47.0-noble

# Switch to root to install any additional dependencies
USER root

# Install system dependencies for running Playwright
RUN apt-get update && apt-get install -y \
    libnss3 \
    libatk-bridge2.0-0 \
    libgbm1 \
    libxshmfence1 \
    && apt-get clean && rm -rf /var/lib/apt/lists/*

RUN pip install --upgrade pip

RUN pip install playwright==1.47.0

RUN playwright install --with-deps

RUN mkdir -p /usr/src/app

WORKDIR /usr/src/app

# Copy your application code into the container
COPY . /usr/src/app/

RUN pip install --no-cache-dir -r requirements.txt
ENV PYTHONPATH "${PYTHONPATH}:/usr/src/app"
CMD ["tail", "-f", "/dev/null"]