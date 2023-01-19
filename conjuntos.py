usuarios_data_science = [15, 23, 43, 56]
usuarios_machine_learning = [13, 23, 56, 42]
usuarios_data_science = set(usuarios_data_science)
usuarios_machine_learning = set(usuarios_machine_learning)

print(usuarios_data_science | usuarios_machine_learning)
print(usuarios_data_science & usuarios_machine_learning)
print(usuarios_data_science - usuarios_machine_learning)
print(usuarios_data_science ^ usuarios_machine_learning)

usuarios = {1, 2, 19, 10, 50, 34}
usuarios.add(49)
print(usuarios, len(usuarios))

usuarios = frozenset(usuarios)
print(usuarios)

texto = "Olá mundo!"
texto.split()
print(set(texto.split()))
