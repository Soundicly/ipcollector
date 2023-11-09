# IPCOLLECTOR

Obtain the information about any IP Address. Built with IP2Location and fastapi.

## Usage

There are three main endpoints:

- `GET /ip` - The main endpoint. Returns the information about the IP Address
- `GET /ip/{ip}` - Returns information about the specified IP Address
- `GET /refreshdatabase` - Downloads the latest database from IP2Location (You should run this endpoint any day the first week of the month)

## Instructions

1. Clone the repository

2. Install the dependencies

    ```bash
    pip3 install -r ./requirements.txt
    ```

3. Set the environment variables (copy the `.env.example` file)

4. Run the server

    ```bash
    uvicorn main:app --reload --host 0.0.0.0 --port 8000 --env-file ./.env
    ```

## Building

To build with docker:

1. Set environment variables in the `Dockerfile` (or `docker-compose.yaml`)

2. Build the image

    ```bash
    docker build -t soundicly-ipcollector .
    ```

### IMPORTANT FOR DOCKER COMPOSE

You will need to create a volume for the database

```yaml
ipcollector:
  image: soundicly-ipcollector
  ...
  volumes:
    - ip2location-db:/app/data
volumes:
  ip2location-db:
```
