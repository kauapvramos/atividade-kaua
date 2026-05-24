Instruções
    •    Crie um repositório público no GitHub com seu código.
    •    No repositório inclua um arquivo README.md com instruções de execução e o link do repositório no Google Classroom (ou cole o link direto na tarefa).
    •    Implemente a classe Queue conforme a especificação abaixo.
    •    Submeta o link do repositório no Google Classroom até a data de entrega.

Especificação da classe Queue (arquivo sugerido: queue.py)•    Classe: Queue
    •    Construtor:
    •    def _init_(): cria fila vazia; max_size opcional (None = ilimitada).
    •    Métodos obrigatórios:
    •    def enqueue(): adiciona item no final da fila; se a fila estiver cheia (quando max_size não for None), deve lançar uma exceção (por exemplo, OverflowError).
    •    

    •   
    •    def is_full(): retorna True se cheia (quando max_size definido), False caso contrário.
    •    Requisitos adicionais:
    •    Não usar collections.deque (implementar usando lista ou linked list).
    •    Documente os métodos.
    •    Trate corretamente erros e mensagens claras nas exceções.
    •    Escreva pelo menos 5 testes simples cobrindo casos normais e de erro.


clear ok 