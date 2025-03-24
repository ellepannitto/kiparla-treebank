import pyconll
import sys
import csv

file_content = pyconll.load_from_file(sys.argv[1])

header = ["id", "upos", "form", "context"]
header_suff = set()

to_print = []

for sentence in file_content:

	text = [token.form for token in sentence if token.upos]
	items = []

	for token in sentence:
		item = {}
		if token.upos:
			item["id"] = f"{sentence.id}:{token.id}"
			item["form"] = token.form
			item["upos"] = token.upos
			for feat in token.feats:
				item[feat] = " ".join(token.feats[feat])
				header_suff.add(feat)
			# print(item)
			# input()
			items.append(item)

	for i, item in enumerate(items):
		item["context"] = " ".join(text[max(i-3, 0):min(i+4, len(text))])
		to_print.append(item)


header = header + list(sorted(header_suff))

with open(sys.argv[2], "w") as fout:
	writer = csv.DictWriter(fout, fieldnames=header)

	writer.writeheader()

	for element in to_print:
		writer.writerow(element)
