#!/bin/bash

INPUT_FILE=$1   # Tham số đầu vào (file JSON)
ID=$2           # Tham số ID

echo "Converting $INPUT_FILE to hsd format"
python3 convert.py "$INPUT_FILE" "$ID"

echo "Running haplogrep"
python3 haplogrep.py "./output_hsd/$ID.hsd" "./output_haplogrep/$ID"
