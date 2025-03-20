import sys
import csv
from sequence_align.pairwise import needleman_wunsch

file1 = sys.argv[1]
file2 = sys.argv[2]


content_1 = []
content_2 = []

with open(file1) as f1, open(file2) as f2:
	reader = csv.DictReader(f1, delimiter="\t")

	for line in reader:
		tok = line["form"]
		content_1.append((tok.strip("~"), line["upos"]))

	for line in f2:
		line = line.strip()
		if len(line) and not line.startswith("#"):
			line = line.strip().split()
			content_2.append((line[1], line[2]))



aligned_seq_a, aligned_seq_b = needleman_wunsch(
		[x for x, y in content_1],
		[x for x, y in content_2],
		match_score=1.0,
		mismatch_score=-1.0,
		indel_score=-1.0,
		gap="_",
	)


to_write = []

i, j = 0, 0
for a, b in zip(aligned_seq_a, aligned_seq_b):
	# print(a, b)
	if a == b:
		to_write.append((content_1[i][0], content_2[j][1]))
		i+=1
		j+=1
	elif a == "_":
		j+=1
	elif b == "_":
		to_write.append(content_1[i])
		i+=1
	else:
		to_write.append(content_1[i])
		i+=1
		j+=1



for x, y in to_write:
	print(f"{x}\t{y}")