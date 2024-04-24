class PokemonMapper:
    def __init__(self, base_url, limite_registros):
        # Constructor de la clase PokemonMapper
        # Inicializa los atributos de instancia base_url y limite_registros
        self._base_url = base_url
        self._limite_registros = limite_registros

    # Propiedad para acceder al atributo base_url
    @property
    def base_url(self):
        return self._base_url

    # Setter para modificar el atributo base_url
    @base_url.setter
    def base_url(self, value):
        self._base_url = value

    # Propiedad para acceder al atributo limite_registros
    @property
    def limite_registros(self):
        return self._limite_registros

    # Setter para modificar el atributo limite_registros
    @limite_registros.setter
    def limite_registros(self, value):
        self._limite_registros = value

    def obtener_listado_pokemon(self):
        # Método para obtener el listado de Pokémon
        # Imprime un mensaje indicando que se está obteniendo el listado de Pokémon
        print("Obteniendo listado de Pokémon...")
        # Código para obtener el listado de Pokémon desde la API
        pass

# Ejemplo de uso
# Se crea una instancia de la clase PokemonMapper
# Se solicita al usuario que ingrese la URL base y el límite de registros para el listado de Pokémon
base_url = input("Ingrese la URL base para el listado de Pokémon: ")
limite_registros = int(input("Ingrese el límite de registros para el listado de Pokémon: "))
mapper_pokemon = PokemonMapper(base_url, limite_registros)
# Se llama al método obtener_listado_pokemon para obtener el listado de Pokémon
mapper_pokemon.obtener_listado_pokemon()
