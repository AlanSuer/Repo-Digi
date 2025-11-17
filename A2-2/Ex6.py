preus1 = {'pa': 1.2, 'llet': 0.9}
preus2 = {'formatge': 2.5, 'pa': 1.1}

preus_fusio = preus1.copy()
preus_fusio.update(preus2)

print(preus_fusio)