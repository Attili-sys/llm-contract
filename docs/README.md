# llm-contracts Documentation

This directory contains the documentation for the llm-contracts project, published using GitHub Pages.

## Local Development

To preview the documentation locally:

1. Install Jekyll and dependencies:
   ```bash
   gem install jekyll bundler
   bundle install
   ```

2. Run the Jekyll server:
   ```bash
   bundle exec jekyll serve
   ```

3. Open your browser to `http://localhost:4000`

## Documentation Structure

- `index.md`: Home page
- `installation.md`: Installation guide
- `getting-started.md`: Getting started guide
- `features.md`: Core features documentation
- `frontend.md`: Web frontend documentation
- `examples.md`: Usage examples
- `api-reference.md`: API reference

## Adding Content

To add new pages:

1. Create a new Markdown file with the following front matter:
   ```yaml
   ---
   layout: default
   title: Your Page Title
   nav_order: [order number]
   description: "Page description"
   ---
   ```

2. Add your content in Markdown format

## Publishing

The documentation is automatically published to GitHub Pages when changes are pushed to the main branch. 