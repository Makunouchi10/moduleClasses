# main.py
# main.py

from mi_clase import MiClase

def main():
    persona = MiClase("Juan")
    saludo = persona.saludar()
    print(saludo)

if __name__ == "__main__":
    main()

from alumnoClass import Alumno

def main():
    # Crea instancia de alumno
    # Una instancia es la creacion de un objeto
    # a partir de una clase
    alumno1 = Alumno("Milan", "Hernandez", "Hernandez", "123456", 3)

    print(f"\nNombre: {alumno1.get_nombre()} {alumno1.get_apellido_paterno()} {alumno1.get_apellido_materno()}")
    print(f"No. Control: {alumno1.get_no_control()}")
    print(f"Semestre: {alumno1.get_semestre()}")
    print("Nombre Completo:", alumno1.get_nombre_completo())

    #Solo el nombre
    registro_alumnos = {}
    registro_alumnos[0] = alumno1
    print(f"\nNombre: {registro_alumnos[0].get_nombre()}")

if __name__ == "__main__":
    main()