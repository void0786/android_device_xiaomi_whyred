import sys
 import argparse
 
 def process_line(line):
   """Removes the '|' character and everything after it in a line."""
   try:
     pipe_index = line.index('|')
     return line[:pipe_index]
   except ValueError:
     # Return the original line if '|' is not found, stripping trailing newline
     return line.rstrip('\n')
 
 if __name__ == "__main__":
   parser = argparse.ArgumentParser(description="Remove text after '|' in a file.")
   parser.add_argument("filename", help="The input file to process.")
   args = parser.parse_args()
 
   try:
     with open(args.filename, 'r') as infile:
       for line in infile:
         processed = process_line(line)
         print(processed)
   except FileNotFoundError:
     print(f"Error: File not found: {args.filename}", file=sys.stderr)
     sys.exit(1)
   except Exception as e:
     print(f"An error occurred: {e}", file=sys.stderr)
     sys.exit(1)