#!/bin/bash

echo "Applying solution..."

cp app/main_clean.py app/main.py

echo "Running tests..."

pytest tests/

echo "Done."