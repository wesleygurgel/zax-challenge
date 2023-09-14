
# Projeto Desenvolvimento Teste Zax
### Desenvolvedor: Wesley Gurgel M de Oliveira

---
## Descrição

O Projeto desenvolvido é um sistema de distribuição que lida com lojas, pedidos e entregadores. Ele permite o gerenciamento eficiente de entregas utilizando diferentes estratégias de distribuição e oferece recursos para filtrar e visualizar informações sobre os entregadores.

## Instalação

1. Clone o repositório.
2. Navegue até a raiz do projeto.
3. Crie um ambiente virtual para trabalhar. | Sugestão: `python -m venv venv`
3. Instale as dependências executando:

```bash
pip install -r requirements.txt
```

## Como Executar

Você pode executar o projeto de duas maneiras:

- Usando o VSCode: configure o arquivo `launch.json` e utilize a opção "Python: Arquivo Atual" para executar o script. No modelo a seguir estamos usando o filtro por argumento, caso não deseje utilizar, basta deixar o array `args` vazio.
```json
{
    "version": "0.2.0",
    "configurations": [
        {
            "name": "Python: Arquivo Atual",
            "type": "python",
            "request": "launch",
            "program": "${file}",
            "console": "integratedTerminal",
            "justMyCode": true,
            "cwd": "${fileDirname}",
            "env": {
                "PYTHONPATH": "${workspaceFolder}"
            },
            "args": [
                "--motoboy_id",
                "1"
            ]
        }
    ]
}
```
- Usando o terminal: execute o seguinte comando na raiz do projeto.

```bash
python src/main.py
```

### Argumentos

O script aceita um argumento opcional `--motoboy_id`, que pode ser usado para filtrar informações sobre um entregador específico. Exemplo:

```bash
python src/main.py --motoboy_id 1
```

Qualquer outro argumento será ignorado, e uma mensagem será impressa para informar qual argumento foi recebido e sugerir o uso correto.

## Estrutura do Código

- `src/`: contém o código principal.
  - `models/`: classes para lojas, entregadores e pedidos.
  - `strategies/`: lógica de distribuição.
  - `utils/`: utilitários, como inicializadores, argumentos e decorators.
  - `main.py`: script principal.
- `tests/`: testes para as classes e estratégias.

## Uso do Design Pattern Strategies

Foi implementado como solução o Design Pattern Strategies para lidar com a distribuição de pedidos. Isso permite uma flexibilidade significativa na maneira como os pedidos são distribuídos, possibilitando a implementação de diferentes estratégias de distribuição sem alterar o código que usa essas estratégias.

### Estrutura

- **Context**: Classe que mantém uma referência à estratégia atual e pode trocar a estratégia em tempo de execução.
- **DistributionStrategy**: Uma interface abstrata que define um método `distribute` que deve ser implementado por todas as estratégias concretas.
- **ExclusiveFirstStrategy**: Uma estratégia concreta que implementa a interface `DistributionStrategy`. Distribui os pedidos de acordo com regras exclusivas primeiro e, em seguida, distribui os pedidos restantes igualmente.

### Código

#### distribution_strategy.py

A classe `Context` é usada para definir e executar a estratégia de distribuição. A classe abstrata `DistributionStrategy` define o contrato para todas as estratégias concretas.

```python
class Context():
    # ...
    def exec_distribution(self, motoboys, stores) -> None:
        self._strategy.distribute(motoboys, stores)
```

#### exclusive_first_strategy.py

A classe `ExclusiveFirstStrategy` implementa a estratégia concreta. A distribuição é feita em duas etapas: distribuição exclusiva e distribuição igual dos pedidos restantes.

```python
class ExclusiveFirstStrategy(DistributionStrategy):
    def distribute(self, motoboys, stores):
        # ...
        # Distribute exclusive orders
        self.distribute_exclusive_orders(motoboys, stores, orders_queue)
        # Distribute remaining orders equally
        self.distribute_remaining_orders_equally(motoboys, orders_queue)
```

### Benefícios

A utilização do padrão Strategies facilita a expansão do sistema com novas estratégias de distribuição, promovendo um código mais limpo e modular. Ele encapsula cada estratégia em uma classe separada, tornando mais fácil testar e reutilizar a lógica de distribuição.

## Decorators

O projeto inclui um decorator `execution_time` que mede o tempo de execução do script. O resultado é impresso em um formato de milissegundo.
