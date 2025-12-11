# Slabserver Diagrams

These architecture diagrams are generated using [Diagram as Code](https://diagrams.mingrammer.com), or Diagrams for short.

Diagrams provides a relatively consistent, elegant, and simple way of programmatically visualising our architecture, without having to worry about manual diagrams potentially changing in style as they require gradually updated over the years.

## Installation
Install steps are included in the main [README.md](../../../README.md) file, or found on the Diagram [site](https://diagrams.mingrammer.com/docs/getting-started/installation).

## Creating a Diagram

There are several examples within this folder, though the Diagram site has a [Quick Start](https://diagrams.mingrammer.com/docs/getting-started/installation#quick-start) guide and [Examples](https://diagrams.mingrammer.com/docs/getting-started/examples) page, which formed the basis for our existing diagrams in this documentation.

Custom icons are typically stored in `/docs/images/architecture/icons`, though the Diagrams site provides an [example](https://diagrams.mingrammer.com/docs/getting-started/examples#rabbitmq-consumers-with-custom-nodes) of how to do this via `urllib.request`. Some websites block direct downloads using `urllib` and cause a 403 Forbidden error, and so it is preferable to keep custom icons within this repository.

## Generating a Diagram
To generate a new diagram, run the following command in a working directory:

```python
python <diagram_name>.py
```

Diagrams are typically found in the `/docs/images/architecture` directory. The path/filename is set by the `with Diagram(filename="...")` value in a `<diagram_name>.py` file.