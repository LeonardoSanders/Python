# Encapsulamento (modificadores de acesso: public, protected, private)
# Python NÃO TEM modificadores de acesso
# Mas podemos seguir as seguintes convenções
#   (sem underline) = public
#       pode ser usado em qualquer lugar
# _ (um underline) = protected
#       Só DEVE ser usado dentro da classe
#       ou suas subclasses.
# __ (dois underlines) = private
#       "name mangling" (desfiguração de nomes) em Python
#       _NomeClasse__nome_attr_ou_method
#       só DEVE ser usado na classe em que foi
#       declarado.

class Foo:
    def __init__(self):
        self.public = "Isso é público"
        self._protected = "Isso é protegido"
        self.__private = "Isso é privado"

    def metodo_publico(self):
        print(self.__private)
        return "método público"
    
    def _metodo_protegido(self):
        return "método protegido"
    
    def __metodo_private(self):
        print("método privado")
        return "método privado"

f = Foo()
# print(f._protected)
# print(f._metodo_protegido())
# print(f.public)
# print(f.metodo_publico())