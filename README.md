
# Webhook Test

A trivial Flask application for testing webhooks.

## Summary

To test another application that calls a webhook, run this app and 
make its URL the webhook url to see when webhook calls come in.

## Usage

### Installation

`python3 -m pip install .`

### Running

`python3 -m webhook_test`

This will start the application running on `localhost:8080`.
This can be configured by environment variables or by a `.env` file in the 
current working directory.

### Configuration

This application respects two environment variables, which can be provided
as OS environment variables or can be provided in a `.env` file in the same
directory in which you run the file.

* `APP_HOST`: Defaults to "localhost"
* `APP_PORT`: Defaults to 8080

### Docker

Build the image:

```
docker build -t webhook-test .
```

Run the image:

```
docker run -it \
    -p 8888:8080 \
    -e APP_HOST="0.0.0.0" \
    --name webhook-test \
    webhook-test
```

// HERE

## Contributing (as a contributor)

## Custom Section(s)

## Files

## Acknowledgements

### By

### Built With