from collections import Counter
import string
import matplotlib.pyplot as plt
file_path = "text.txt"
with open(file_path, 'r', encoding='utf-8') as file:
    text = file.read().lower()
letters = [char for char in text if char in string.ascii_lowercase]
letter_counts = Counter(letters)
plt.figure(figsize=(10, 6))
plt.bar(letter_counts.keys(), letter_counts.values(), color='green', alpha=0.7)
plt.title("Гістограма частот англійських літер")
plt.xlabel("Літери")
plt.ylabel("Частота")
plt.grid(axis='y', linestyle='--', alpha=0.7)
plt.show()
