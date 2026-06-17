# 2026 Farning School Workshop @ QAware

This repository contains code for the Farning School Workshop.
For this, a task for a two component microservice was designed, reproducing a simplified version of a car selling system, composed of a central server instance, which provides for a management of incoming and outgoing car part information as well as a client instance, which retrieves data from the server and displays it to a client or worker at the car selling company. For more information concerning the task, check out the [specifications](TASK.md).

## Installation

0.) Optionally create a virtual environment for your python packages of this project:

```
python3 -m venv venv
source venv/bin/activate
```

1.) Install all dependencies:

```
python3 -m pip install -r requirements.txt
```

2.) Start the uvicorn backend:

```
uvicorn autoteilverwaltung:app --reload
```

The reload command is used to be able to update the code and start the application automatically.

## Usage

After the installation the API can be called via curl or the browser to serve the user with data or as data storage.

## Maintainer

T. Prade, <thomas.prade@qaware.de>
T. Waegemans, <tim.waegemans@qaware.de>

Forked from original code by:

R. Kalleicher, <robin.kalleicher@qaware.de>
T. Schweitzer, <tilman.schweitzer@qaware.de>
