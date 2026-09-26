FROM ubuntu:24.04

WORKDIR /app

# Install Python, pip and required system packages
RUN apt-get update && \
    apt-get install -y python3 python3-pip && \
    rm -rf /var/lib/apt/lists/*

# Install Python dependencies
COPY requirements.txt .
RUN pip3 install --break-system-packages -r requirements.txt

# Install Playwright + Chromium and its dependencies
RUN playwright install --with-deps firefox

# Copy test suite
COPY . .

# Run tests by default
CMD ["pytest"]