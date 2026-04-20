# Architecture

Sentinel Lite follows a modular EDR design:

## Components

### Agent

Responsible for collecting process data from `/proc`.

### Detection Engine

Loops through all processes and applies detection modules.

### Detection Modules

Each module implements a `detect()` function.

### Utils

Shared functionality such as logging and allowlists.

---

## Data Flow

1. Collect processes
2. Filter safe processes
3. Apply detection modules
4. Log alerts

---

## Design Goals

* Simplicity
* Modularity
* Extensibility
