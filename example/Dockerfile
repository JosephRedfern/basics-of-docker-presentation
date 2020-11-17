# Specify the image on which this image will be based.
FROM python:3.8.3 

# Sets the working directory for subsequent commands.
WORKDIR /usr/src/app

# Copy requirements from current directory on build machine
# to the working directory on the image.
COPY requirements.txt ./

# Copy the src/ directory on build machine to src on image.
COPY src ./src

# Install python dependencies from requirements.txt.
# --no-cache-dir stops pip from caching the packages, which
# saves some space.
RUN pip install --no-cache-dir -r requirements.txt

# CMD specifies the command (and it's arguments) to be run
# when the container starts
CMD [ "python", "./src/coolscript.py"]
