# PDF Text Search

[![GitHub](https://img.shields.io/badge/Visit-My%20Profile-0891B2?style=flat-square&logo=github)](https://github.com/Tgentil)

Este é um script em Python que permite buscar por um texto específico dentro de todos os arquivos PDF em uma pasta.

## Pré-requisitos

Certifique-se de ter o Python instalado em seu sistema. Além disso, instale a biblioteca PyPDF2 executando o seguinte comando:

```
pip install PyPDF2
```

## Como Usar

1. Faça o download ou clone este repositório em sua máquina.
2. Coloque os arquivos PDF nos quais você deseja realizar a busca na pasta "data" localizada no diretório do script.
3. Abra o arquivo `script.py` e localize a variável `TEXTO_PROCURADO`.
4. Substitua o valor de `TEXTO_PROCURADO` pelo texto que você deseja procurar nos arquivos PDF.
5. Salve o arquivo `script.py`.
6. Execute o script `script.py`.
7. O script irá percorrer todos os arquivos PDF na pasta "data" em busca do texto especificado.
8. Após a execução, o script exibirá os nomes dos arquivos PDF que contêm o texto procurado.
9. Se nenhum arquivo for encontrado, o script exibirá a mensagem "Nenhum arquivo encontrado."

## Notas

- Certifique-se de ter permissões de leitura na pasta "data" para acessar os arquivos PDF.
- Certifique-se de que a biblioteca PyPDF2 esteja instalada corretamente antes de executar o script.
- O texto procurado é sensível a maiúsculas e minúsculas. Certifique-se de digitar corretamente.
- O script procurará o texto em todas as páginas de cada arquivo PDF.
- Se vários arquivos forem encontrados, o script exibirá todos os nomes dos arquivos encontrados.

## Autor 

* Thiago da Silveira Gentil