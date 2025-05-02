# Use a Python 3.9 image
FROM python:3.9-slim

# Set the working directory
WORKDIR /app

# Copy the current directory content into the container at /app
COPY . /app

# Install the required Python dependencies
RUN pip install --no-cache-dir -r requirements.txt

# Expose port 5000 (not required but helpful for future expansion)
EXPOSE 5000

# Run the bot.py script
CMD ["python", "bot.py"]
