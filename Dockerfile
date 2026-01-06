# 1. Use an official lightweight Python runtime as a parent image
FROM python:3.9-slim

# 2. Set the working directory inside the container
WORKDIR /app

# 3. Copy the requirements file into the container at /app
# We copy this first to leverage Docker cache for dependencies
COPY requirements.txt .

# 4. Install any needed packages specified in requirements.txt
# --no-cache-dir prevents storing the cache to keep the image small
RUN pip install --no-cache-dir -r requirements.txt

# 5. Copy the rest of the application code into the container
COPY . .

# 6. Make port 8000 available to the world outside this container
EXPOSE 8000

# 7. Define the command to run the application using Uvicorn
# --host 0.0.0.0 is crucial for Docker containers to be accessible externally
CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "8000"]