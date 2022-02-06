FROM python:3

WORKDIR /app

# Install and upgrade pip
RUN pip install --upgrade pip

# Collect and install requirements
COPY requirements.txt ./
RUN pip3 install -r requirements.txt

# Get the code
COPY . .

# Switching to a non-root user
RUN useradd appuser && chown -R appuser /app
USER appuser

# Run the program
CMD [ "python3", "test-read-sensor-lywsd03mmc.py", "A4:C1:38:59:41:79", "salon" ]