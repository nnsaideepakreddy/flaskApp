# Use the official Python 3.9 image
FROM python:3.9

# Set the working directory inside the container
WORKDIR /api

# Copy the local directory contents into the container at /api
COPY . .

# Install dependencies from requirements.txt
RUN pip install --no-cache-dir -r requirements.txt

# Make main.py executable
RUN chmod +x main.py

# Run streamlit app
CMD [ "streamlit run Appcode.py --server.port 2000" ] 

# Set the entry point
ENTRYPOINT ["python3", "main.py"]

# command: docker run -p 1000:8080 -p 2000:2000 <image-id>
