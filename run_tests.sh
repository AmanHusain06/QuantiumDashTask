#!/bin/bash

source .venv/bin/activate
python -m pytest

if [ $? -eq 0 ]; then
  exit 0
else
  exit 1
fi