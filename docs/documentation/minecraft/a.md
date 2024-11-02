### Navigation tabs

<!-- md:version 1.1.0 -->
<!-- md:feature -->

When tabs are enabled, top-level sections are rendered in a menu layer below
the header for viewports above `1220px`, but remain as-is on mobile.[^1] Add
the following lines to `mkdocs.yml`:

  [^1]:
    Prior to <!-- md:version 6.2.0 -->, navigation tabs had a slightly different
    behavior. All top-level pages (i.e. all top-level entries directly
    referring to a `*.md` file) defined inside the `nav` entry of `mkdocs.yml`
    were grouped under the first tab which received the title of the first page.
    This made it impossible to include a top-level page (or external link) as a
    tab item, as was reported in #1884 and #2072. From <!-- md:version 6.2.0 -->
    on, navigation tabs include all top-level pages and sections.

``` yaml
theme:
  features:
    - navigation.tabs
```

=== "With tabs"

    [![Navigation tabs enabled]][Navigation tabs enabled]

=== "Without"

    [![Navigation tabs disabled]][Navigation tabs disabled]

  [Navigation tabs enabled]: ../assets/screenshots/navigation-tabs.png
  [Navigation tabs disabled]: ../assets/screenshots/navigation.png

#### Sticky navigation tabs