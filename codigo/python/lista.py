class Lista:
    """Classe Lista para armazenar inteiros"""
    
    def __init__(self, elementos=None):
        """
        Inicializa a lista com elementos opcionais
        
        Args:
            elementos: lista de inteiros (opcional)
        """
        if elementos is None:
            self.elementos = []
        else:
            self.elementos = list(elementos)
    
    def __len__(self):
        """Retorna o tamanho da lista"""
        return len(self.elementos)
    
    def __getitem__(self, index):
        """Permite acessar elementos por índice"""
        return self.elementos[index]
    
    def __setitem__(self, index, valor):
        """Permite modificar elementos por índice"""
        self.elementos[index] = valor
    
    def __repr__(self):
        """Representação da lista"""
        return f"Lista({self.elementos})"
    
    def adicionar(self, valor):
        """Adiciona um inteiro à lista"""
        self.elementos.append(valor)
    
    def obter_elementos(self):
        """Retorna a lista de elementos"""
        return self.elementos
    
    def limpar(self):
        """Limpa a lista"""
        self.elementos = []


class Array:
    """Classe Array (mantida para compatibilidade)"""
    
    def __init__(self, elements):
        self.elements = elements

    def __len__(self):
        return len(self.elements)

    def __getitem__(self, index):
        return self.elements[index]

    def __setitem__(self, index, value):
        self.elements[index] = value

    def __repr__(self):
        return f"Array({self.elements})"
