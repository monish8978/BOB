#!/bin/bash
if [ ! -f .env ]; then
    if [ -f .env.example ]; then
        cp .env.example .env
        echo ".env file created from .env.example"
    elif [ -f env.example ]; then
        cp env.example .env
        echo ".env file created from env.example"
    else
        echo "Error: Neither .env.example nor env.example was found!"
    fi
else
    echo ".env file already exists. Skipping copy."
fi
