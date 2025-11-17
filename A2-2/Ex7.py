notes = {
    'Anna': [8, 9, 7],
    'Pau': [5, 6, 6],
    'Maria': [10, 9, 9],
    'Jordi': [4, 7, 6]
}

for alumne, llista_notes in notes.items():
    mitjana = sum(llista_notes) / len(llista_notes)
    print(f"{alumne} → {mitjana:.2f}")