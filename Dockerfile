# Use the official fastapi uvicorn image
FROM tiangolo/uvicorn-gunicorn-fastapi:python3.8

# Set the working directory
WORKDIR /app

# Install any needed packages specified in requirements.txt
COPY python-lib.txt /app/
RUN pip install --no-cache-dir -r python-lib.txt

# Copy the current directory contents into the container at /app
COPY . /app

# Make port 80 available to the world outside this container
EXPOSE 8000

# Run the application
CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "8000"]