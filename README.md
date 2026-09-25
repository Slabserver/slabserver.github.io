# Slabserver | The Etho Community

The home for all things Slabserver—our community's landing page, documentation, Transparency Reports, and more. This repository is built with Material for MkDocs, hosted on GitHub Pages, and lovingly crafted for you.

## Contributing
Want to contribute? If you notice something missing, unclear, or in need of improvement, simply fork the repository, make your changes, and submit a pull request for us to review.

### Getting Started
Learning how to use [Visual Studio Code](https://code.visualstudio.com/docs/getstarted/getting-started) and its [built-in Git tools](https://code.visualstudio.com/docs/sourcecontrol/intro-to-git) is **highly** encouraged for those that would like to learn more industry-standard software.

Anyone who is a member of #technology and/or is using Linux has no excuse to not be contributing to this repository.

## Creating a local environment

### Prerequisites
Before running this project locally, ensure the following are installed on your system:
- [Python 3](https://www.python.org/downloads/)
- Pip, a package installer for Python _(included with most Python 3 installations)_
- A [virtual environment](https://www.w3schools.com/python/python_virtualenv.asp) in Python _(Optional, but highly encouraged for development)_
  - For Unix systems, the following commands can be used to setup and run a venv:
    ```
    python3 -m venv path/to/venv
    source path/to/venv/bin/activate
    ```

### Installation
**Required:**
- Follow the Material for MkDocs [installation guide](https://squidfunk.github.io/mkdocs-material/getting-started/)
- Install the `mkdocs-glightbox` plugin, used for enlarging images
    -   ```pip install mkdocs-glightbox```

Architecture diagrams (see [`server-architecture.md`](docs/documentation/minecraft/server-architecture.md)) are written as [Mermaid](https://mermaid.js.org) diagrams directly in Markdown, rendered client-side via `pymdownx.superfences`—no extra tooling required.

### Running Locally
- Navigate to the project directory in your terminal
- Run `mkdocs serve` from your terminal to build and serve the site 
- In your browser, visit the local server URL provided in the terminal output

## Tips and Tricks

### Adding Announcement Banners to slabserver.org

Simply add the following `{% block announce %} ... {% endblock %}` to [`overrides/home.html`](overrides/home.html), updating the example href and text below as necessary:
```
{% extends "main.html" %}
{% block announce %}
  <div class="announcement">
      <a href="/polls/2026/" class="announcement-click">
      The Great Slabserver Poll results are out! Click here for more info
      </a>
  </div>
{% endblock %}
{% block tabs %}
  {{ super() }}
    ...
```