# Base docker Image Python 3.8 Slim 
FROM python:3.8-slim 

# Copy python package requirements to current container context 
COPY requirements.txt ./

# Install Python's package manager pip and upgrade it to latest version 
RUN python -m pip install --upgrade pip

# Install API requirements 
RUN pip3 install -r requirements.txt

# Set current working directory to /app
WORKDIR /app

# Copy the source code to the current working directory
COPY ./main.py ./ 
COPY ./assets /assets
# Run the Web Server using Uvicorn web server and set host to 0.0.0.0 and port to 6000
CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "6000"]
