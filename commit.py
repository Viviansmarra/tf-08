class Commit:
    # Guarda as informações do commit e seu antecessor.
    def __init__(self, id, mensagem, autor, pai=None):
        self.id = id
        self.mensagem = mensagem
        self.autor = autor
        self.pai = pai

    # Mostra o commit atual e os anteriores.
    def historico(self):
        print(f"#{self.id} {self.mensagem} ({self.autor})")
        if self.pai is not None:
            self.pai.historico()


class Repositorio:
    # Cria o repositório sem commits.
    def __init__(self, nome, autor):
        self.nome = nome
        self.autor = autor
        self.head = None
        self.contador = 0

    # Cria um commit e o define como o mais recente.
    def commitar(self, mensagem):
        self.contador += 1
        novo_commit = Commit(
            self.contador,
            mensagem,
            self.autor,
            self.head
        )
        self.head = novo_commit

    # Mostra o histórico do repositório.
    def log(self):
        if self.head is None:
            print("Nenhum commit ainda")
            return
        self.head.historico()

    # Conta todos os commits do repositório.
    def total_de_commits(self):
        total = 0
        commit_atual = self.head
        while commit_atual is not None:
            total += 1
            commit_atual = commit_atual.pai
        return total


# Testa o repositório e mostra seu histórico.
repositorio = Repositorio("tf-08", "Vivian Smarra - 6326269")
repositorio.log()
repositorio.commitar("Inicia o projeto tf-08")
repositorio.commitar("Adiciona a classe Commit")
repositorio.commitar("Finaliza os métodos do repositório")
repositorio.log()
print(repositorio.total_de_commits())
