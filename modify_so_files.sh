#!/bin/bash
 
 # Check if file exists
 if [ ! -f "proprietary-files.txt" ]; then
     echo "Error: proprietary-files.txt not found"
     exit 1
 fi
 
 # Create temp file
 tmpfile=$(mktemp)
 
 # Process each line
 while IFS= read -r line; do
     if [[ "$line" == *".so"* ]]; then
         # Prepend '-' and append ';DISABLE_DEPS'
         echo "-${line};DISABLE_DEPS" >> "$tmpfile"
     else
         echo "$line" >> "$tmpfile"
     fi
 done < "proprietary-files.txt"
 
 # Replace original file
 mv "$tmpfile" "proprietary-files.txt"
 
 echo "Modified proprietary-files.txt successfully"