# From Flask Api To A Robust Container From Scratch

# Summary

[Introduction](#introduction)<br>
[Requirements](#requirements)<br>
[I - Initialisation](#i---initialisation)<br>
-- [1 - Clone the repository](#1---clone-the-repository)<br>
-- [2 - Initialise the project](#2---initialise-the-project)<br>
[II - First steps in the projects](#ii---first-steps-in-the-projects)<br>
-- [1 - Start the API server](#1---start-the-api-server)<br>
-- [2 - Test the API endpoints](#2---test-the-api-endpoints)

# Introduction

The following commands are compatible with Linux/MacOS terminals, if you use 
Windows please try WSL to follow this write up.

# Requirements

-- A Linux/MacOS workstation with a terminal working<br>
-- Git, python and curl install<br>
-- Docker ready and started (daemon running)

# I - Initialisation

## 1 - Clone the repository

Using https :
```
git clone https://github.com/victor-sys-admin/BASE_from_flask_api_to_a_robust_container_from_scratch.git
```

Using ssh :
```
git clone git@github.com:victor-sys-admin/BASE_from_flask_api_to_a_robust_container_from_scratch.git
```

## 2 - Initialise the project

Create a venv :
```sh
python3 -m venv .venv
```

Activate the venv :
```sh
. .venv/bin/activate
```

Install flask module :
```sh
pip install flask
```

# II - First steps in the projects

## 1 - Start the API server

```sh
python3 main.py
```

## 2 - Test the API endpoints

Get the root :
```sh
curl 127.0.0.1:5000
```

We expect a response like this :
```json
{"Welcome":"This is a demo API"}
```

Get the health :
```sh
curl 127.0.0.1:5000/health
```

We expect a response like this :
```json
{"success":"The API is UP"}
```
