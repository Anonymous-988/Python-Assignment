dict1 = {"Second": 2, "First": 1, "Third": 3}

dictAscending = dict(sorted(dict1.items(), key=lambda item: item[1]))
dictDescending = dict(sorted(dict1.items(), key=lambda item: item[1], reverse=True))

print(f"Actual Dictionary: {dict1}")
print(f"Ascending Dictionary: {dictAscending}")
print(f"Descending Dictionary: {dictDescending}")