import os

script_filename = os.path.splitext(os.path.basename(__file__))[0]
output_filename = script_filename + ".hex"

print(output_filename)