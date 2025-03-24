import pyconll
import sys
import csv

updated_feats_file = sys.argv[1]

items_to_update = {}

with open(updated_feats_file) as fin:
	reader = csv.DictReader(fin)
	header = reader.fieldnames
	header_suff = set(header) - set(["id", "upos", "form", "context"])

	for item in reader:
		items_to_update[item["id"]] = item


original_conll = pyconll.load_from_file(sys.argv[2])

# header = ["id", "upos", "form", "context"]
# header_suff = set()

# to_print = []

with open(sys.argv[3], "w") as fout:

	for sentence in original_conll:
		# text = [token.form for token in sentence if token.upos]
	# 	items = []

		for token in sentence:
	# 		item = {}
			if token.upos:
				tok_id = f"{sentence.id}:{token.id}"

				if tok_id in items_to_update:

					token.feats = {}
					new_feats = {x:y for x, y in items_to_update[tok_id].items() if x not in ["id", "upos", "form", "context"] and len(y) > 0}
					for feat in new_feats:
						token.feats[feat] = set()
						token.feats[feat].add(new_feats[feat])

		fout.write(sentence.conll())
		fout.write("\n\n")