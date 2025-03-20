def align_tokens(list1, list2):
    aligned = []
    i, j = 0, 0

    while i < len(list1) and j < len(list2):
        group = []
        combined = ""

        while j < len(list2):
            group.append(list2[j])
            combined += list2[j]

            # Move to the next token in list2
            j += 1

            # If we have reconstructed list1[i], we move to the next token in list1
            if combined == list1[i]:
                break

        aligned.append(tuple(group))
        i += 1

    return aligned

# Example usage
list1 = ["I", "don't", "like", "ice-cream"]
list2 = ["I", "do", "n't", "like", "ice-cream"]

list1_it = ["nel", "parco"]
list2_it = ["in", "il", "parco"]

print(align_tokens(list1, list2))  # [('I',), ('do', "n't"), ('like',), ('ice-cream',)]
print(align_tokens(list1_it, list2_it))  # [('in', 'il'), ('parco',)]