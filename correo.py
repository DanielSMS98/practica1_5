correo = input("Introduce tu correo electronico: ").strip()
usuario = correo[:correo.index('@')]
dominio = correo[correo.index('@')+1:]
print(f"Tu usuario es: {usuario}\nTu dominio: {dominio}")