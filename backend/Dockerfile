# Step 1: Base image
FROM python:3.11-slim

# Step 2: Install netcat-openbsd for wait-for-it.sh
RUN apt-get update && apt-get install -y netcat-openbsd curl && apt-get clean

# Step 3: Set working directory
WORKDIR /app

# Step 4: Copy necessary files
COPY ./app /app

# Add project path to PYTHONPATH
ENV PYTHONPATH=/app/app

# Step 5: Download wait-for-it.sh script
RUN curl -sSL https://raw.githubusercontent.com/vishnubob/wait-for-it/master/wait-for-it.sh -o /wait-for-it.sh

# Step 6: Make wait-for-it.sh executable
RUN chmod +x /wait-for-it.sh

# Step 7: Copy requirements.txt and install dependencies
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Step 8: Run the application with wait-for-it.sh
CMD ["/wait-for-it.sh", "mysql:3306", "--", "python3", "-m", "uvicorn", "main:app", "--host", "0.0.0.0", "--port", "8000", "--reload"]
