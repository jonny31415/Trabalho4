# Trabalho4

## Informações de projeto

- Tempo máximo de execução permitido no servidor: 2s
- Caso as condições das funções não sejam cumpridas é retornado o código 400 (Bad Request).
- Caso o json possua apenas um dos campos 'fact' ou 'fib', o servidor retorna apenas esse campo. Caso possua os dois campos, ambos são retornados. Caso algum campo seja diferente desses dois, é retornado o código 400 (Bad Request).

## Informações de execução

### Fatorial

- Maior profundidade de recursão: n = 980;
- Tempo de execução: Menos de 1s;

### Fibonacci Recursiva

- Tempo de execução médio (n = 40): 32s;
- Tempo limite é excedido logo, não tornando a profundidade de recursão um problema;

### Fibonacci otimizada

- Tempo de execução: Menos de 1s;
- Limite: n = 19600 (Erro na função);
- Não influencia na profundidade de recursão, quando executada com o fatorial, já que contém apenas algumas variáveis a serem alocadas na _stack_;