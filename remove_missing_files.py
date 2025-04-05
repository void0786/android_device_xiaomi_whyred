import sys
 import argparse
 import os
 
 def extract_missing_files(error_log_path):
     """Extracts file paths marked as 'file not found' from an error log."""
     missing_files = set()
     try:
         with open(error_log_path, 'r') as error_file:
             for line in error_file:
                 line = line.strip()
                 if line.endswith(': file not found'):
                     # Extract the file path before the colon
                     file_path = line.rsplit(':', 1)[0]
                     missing_files.add(file_path.strip())
     except FileNotFoundError:
         print(f"Error: Error log file not found: {error_log_path}", file=sys.stderr)
         sys.exit(1)
     except Exception as e:
         print(f"An error occurred reading the error log: {e}", file=sys.stderr)
         sys.exit(1)
     return missing_files
 
 def remove_files_from_list(file_list_path, missing_files, output_path):
     """Removes specified files from a list and writes to a new file."""
     try:
         with open(file_list_path, 'r') as infile, open(output_path, 'w') as outfile:
             for line in infile:
                 file_path = line.strip()
                 # Only write the line if the file path is not in the missing set
                 if file_path and file_path not in missing_files:
                     outfile.write(line)
         print(f"Cleaned file list saved to: {output_path}")
     except FileNotFoundError:
         print(f"Error: Input file list not found: {file_list_path}", file=sys.stderr)
         sys.exit(1)
     except Exception as e:
         print(f"An error occurred processing the file list: {e}", file=sys.stderr)
         # Attempt to remove partially created output file on error
         if os.path.exists(output_path):
             os.remove(output_path)
         sys.exit(1)
 
 if __name__ == "__main__":
     parser = argparse.ArgumentParser(description="Removes file entries from a list based on a 'file not found' error log.")
     parser.add_argument("file_list", help="Path to the file containing the list of files (e.g., proprietary-files.txt).")
     parser.add_argument("error_log", help="Path to the file containing error messages (e.g., error.log).")
     parser.add_argument("-o", "--output", help="Path for the cleaned output file. Defaults to [file_list]-cleaned.")
     args = parser.parse_args()
 
     # Determine output file path
     if args.output:
         output_file_path = args.output
     else:
         base, ext = os.path.splitext(args.file_list)
         output_file_path = f"{base}-cleaned{ext}"
 
     # Prevent overwriting the input file list accidentally
     if output_file_path == args.file_list:
         print(f"Error: Output file path cannot be the same as the input file list path.", file=sys.stderr)
         sys.exit(1)
 
     missing = extract_missing_files(args.error_log)
     if missing:
         print(f"Found {len(missing)} missing files in the error log.")
     else:
         print("No missing files found in the error log.")
         # Optionally exit if no missing files found, or proceed to copy the original file
         # For now, we'll proceed, which will effectively copy the file if no files are missing.
 
     remove_files_from_list(args.file_list, missing, output_file_path)