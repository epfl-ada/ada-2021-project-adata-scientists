'''
Execute this script as: python query_wikidata_dump.py --input <path-to-wikidata-json-dump> --output <path-to-output-json-file>
'''

import json
import sys
from tqdm import tqdm
from argparse import ArgumentParser
import gzip
import pickle as pkl

parser = ArgumentParser()
parser.add_argument("--input", required=True)
parser.add_argument("--output", required=True)
args = parser.parse_args()

# Usage:


def main():
	#cnt = 0	
	occupations_done = 0
	with open('./categories3.pkl', 'rb') as f:   
		occupations_list = pkl.load(f)
    # Do not enforce encoding here since the input encoding is correct
	with open(args.output, "w") as output_file:
		with gzip.open(args.input, 'rb') as s_file:
			for instance in s_file:
				
				instance = instance.decode('utf-8')
				instance = instance[:-2]
				if len(instance)==0:
					continue
				try:
					s = json.loads(instance.strip("\n"))
				except Exception as exc:
					print(type(exc))
					print(exc)
					continue
				
				#if occupation of interest
				if s.get("id") in occupations_list:
				
					#testing
					#cnt += 1
					#if cnt > 100:
					#	break
					
					# Label
					if s.get("labels", {}).get("en") is not None:
						s["label"] = s["labels"]["en"]["value"]
					
					if s.get("labels") is not None:
						del s["labels"]
					else:
						continue
					
					# Subclass of
					if len(s.get("claims", {}).get("P279", [])) > 0: #subclass of
						tmp = []
						v = s["claims"]["P279"][0] # check only first parent class
						if (v["mainsnak"].get("datavalue", {}).get("value", {}).get("id") is not None):
							tmp.append(v["mainsnak"]["datavalue"]["value"]["id"])
						if len(tmp) > 0:
							s["occupation_cat"] = tmp
					
					
					# Removing leftovers and unnecessary attributes
					if s.get("aliases") is not None:
						del s["aliases"]
					if s.get("descriptions") is not None:
						del s["descriptions"]
					if s.get("sitelinks") is not None:
						del s["sitelinks"]
					if s.get("claims") is not None:
						del s["claims"]
					if s.get("lastrevid") is not None:
						del s["lastrevid"]
					if s.get("type") is not None:
						del s["type"]

					output_file.write(json.dumps(s, ensure_ascii=False) + "\n")
					
					occupations_done += 1
					
					if occupations_done == len(occupations_list): # no redirect among categories2,3
						print('Finished early!')
						break

if __name__ == "__main__":
	main()
