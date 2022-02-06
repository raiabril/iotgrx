# Test sensor LYWSD03MMC

## Build and run

    $ docker build --no-cache -t test-read-lywsd03mmc .
    $ docker run -it --rm --name test test-read-lywsd03mmc

## Single Python script

    $ docker run -it --rm --name my-running-script -v "$PWD":/usr/src/myapp -w /usr/src/myapp python:3 python your-daemon-or-script.py