# language: pt

Funcionalidade: Todo List

  Cenário: Criar um cartão de todo
    Dado que eu esteja na página
    Quando criar um todo
    | nome    | descrição  |
    | Dormir  | é bom      |
    Então o todo deve estar na pilha "A fazer"