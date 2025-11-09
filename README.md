# Gestor CLI

Uma pequena ferramenta de linha de comando para tarefas administrativas e de produtividade.

Versão: 0.1.0

---

## Sobre

O `gestor-cli` é uma aplicação simples em Python que fornece um menu interativo (terminal) para gerenciar funcionalidades relacionadas a pessoas, produtividade e funcionalidades básicas de IA (simuladas). Foi construída com `click` e `rich` para uma interface de terminal amigável.

## Recursos

- Menu interativo no terminal
- Módulos: Pessoas, Produtividade, IA
- Integração simples com armazenamento de configuração local (módulo `util.configuration_db`)

## Requisitos

- Python >= 3.14
- Dependências declaradas no projeto:
  - click >= 8.3.0
  - rich >= 14.2.0

## Instalação (opcional com uv)

Você pode executar o CLI diretamente com o `uv` sem instalar o pacote no sistema.

Se desejar instalar, continue usando `pip` como antes; porém o fluxo mais simples é apenas executar com `uv run` (veja abaixo).

## Uso (rodando com uv)

Executar sem instalar (recomendado quando você usa `uv`):

```bash
# Executa o módulo principal no ambiente gerenciado pelo uv
uv run python -m gestor_cli.main
```

Instalar:

```bash
uv tool install .
```

Se o pacote já estiver instalado no ambiente, você também pode executar o entry-point:

```bash
# Quando o entry-point 'gestor' estiver disponível no ambiente do uv
uv run gestor
```

Ao iniciar você verá um menu principal com opções:

- Pessoas — abre o menu de gerenciamento de pessoas
- Produtividade — abre ferramentas de produtividade
- IA — demonstração de resumo/simulação de IA
- Sair — fecha a aplicação

Exemplo rápido:

1. Rode `gestor`
2. Escolha a opção `3` para entrar no menu `IA`
3. Siga as instruções na tela

## Estrutura do projeto

- `gestor_cli/` — pacote principal
  - `main.py` — ponto de entrada e loop do menu
  - `pessoas.py` — funcionalidades relacionadas a pessoas
  - `produtividade.py` — funcionalidades de produtividade
  - `ia.py` — funcionalidades de IA (simulação)
  - `ui.py` — utilitários de interface (console, menus)
  - `util/configuration_db.py` — armazenamento/recuperação de configuração local

## Desenvolvimento

1. Clone o repositório e crie um ambiente virtual
2. Instale em modo editável: `pip install -e .`
3. Execute `gestor` para testar mudanças locais

Sugestões de próximos passos:

- Adicionar testes automatizados (pytest)
- Adicionar comandos mais específicos por módulo

## Contribuição

Contribuições são bem-vindas. Abra uma issue descrevendo a mudança proposta antes de submeter um pull request.

### Boas práticas

- Siga o estilo do código já existente
- Adicione testes quando apropriado

## Licença

Por padrão, este repositório não especifica uma licença no `PKG-INFO`. Se for abrir o projeto publicamente, adicione um arquivo `LICENSE` com a licença desejada (por exemplo, MIT) e atualize o `pyproject.toml`.

## Contato

Autor: Marcos Ramiro

---

_Gerado automaticamente por script de auxílio ao desenvolvedor._
