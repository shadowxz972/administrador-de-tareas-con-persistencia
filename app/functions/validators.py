from datetime import datetime


def validate_str(value: str) -> bool:
    return isinstance(value, str) and len(value) > 0


def validate_date(value: str | None) -> bool:
    if value:
        # Si existe retornamos true
        try:
            datetime.strptime(value, "%d/%m/%Y")
            return True  # si la fecha es valida retornamos true
        except ValueError:
            return False  # si esta incorrecta retornamos false
    else:
        return False  # si esta vacia o es un None retornamos false


def get_valid_name(prompt="Ingrese nombre: ") -> str:
    """
    Obtienes el nombre con sus validaciones
    :return: name
    """
    while True:
        name = input(prompt)
        if validate_str(name):
            break
        print("Formato incorrecto, el nombre no puede estar vacio")
    return name


def get_valid_description(prompt="Ingrese descripcion: ") -> str:
    """
    Obtienes la descripcion con sus validaciones
    :return: description
    """
    while True:
        description = input(prompt)
        if validate_str(description):
            break
        print("Formato incorrecto, la descripcion no puede estar vacio")
    return description


def get_valid_deadline(prompt="Ingrese fecha limite (No escriba nada si no hay): ") -> str | None:
    """
    Obtienes la fecha limite con sus validaciones
    :return: deadline
    """
    while True:
        deadline = input(prompt)
        if not deadline:
            return None
        if validate_date(deadline):
            break
        print("Formato incorrecto, la fecha debe ser dd/mm/yyyy")
    return deadline
