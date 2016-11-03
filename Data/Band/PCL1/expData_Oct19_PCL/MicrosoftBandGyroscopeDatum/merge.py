import json
import glob

read_files = glob.glob("*.json")
output_list = []

for f in read_files:
    with open(f, "rb") as infile:
        output_list = output_list + (json.load(infile))
	
with open("merged_file.json", "wb") as out:
    json.dump(output_list, out, indent=2)
    #out.write('\n')
	
