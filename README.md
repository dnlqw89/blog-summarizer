# Blog Summarizer API

Esta é uma API gratuita para resumir artigos de blogs automaticamente usando GPT-4.

## Como funciona

1. Envie uma requisição POST com a URL do blog.
2. A API faz o scraping do conteúdo.
3. O GPT-4 gera um resumo.

## Requisição

**POST /summarize**

```json
{
  "url": "https://exemplo.com/blog/artigo"
}
