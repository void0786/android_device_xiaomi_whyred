#!/usr/bin/env python3
 
 import sys
 
 def modify_file(input_file, output_file=None):
     """Modify lines containing '/bin' by adding '-' prefix and ';DISABLE_DEPS' suffix"""
     if output_file is None:
         output_file = input_file
     
     with open(input_file, 'r') as f:
         lines = f.readlines()
     
     modified_lines = []
     for line in lines:
         stripped = line.strip()
         if '/bin' in stripped and not stripped.startswith('#'):
             if not stripped.startswith('-'):
                 line = '-' + line
             if not stripped.endswith(';DISABLE_DEPS'):
                 line = line.rstrip() + ';DISABLE_DEPS\n'
         modified_lines.append(line)
     
     with open(output_file, 'w') as f:
         f.writelines(modified_lines)
 
 if __name__ == '__main__':
     if len(sys.argv) < 2:
         print(f"Usage: {sys.argv[0]} <input_file> [output_file]")
         sys.exit(1)
     
     input_file = sys.argv[1]
     output_file = sys.argv[2] if len(sys.argv) > 2 else None
     modify_file(input_file, output_file)