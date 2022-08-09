# This is a [Quarto](https://quarto.org/) blog

## Organization

I've decided to organize things into three main sections:

* `blog`
* `talks`
* `projects`

<br>

Each has it's own landing page and `_metadata.yml` file. Additionally the `ejs` directory contains a small custom listing template for the main landing page.

Some older blog posts are not rendered; rather, they're sort of put together with images and text. I don't really want to try and find versions of packages from 2013 to make them _run_ the way they _would have_.

Talks and projects use an `<iframe>` to source the `html` file in with an option to make it full screen, which I thought was a neat idea.

<br>

## Environment management

In order to manage the coding environments for the site I'm using virtual environments via environment managers for both `R` and `Python`. I don't necessarily have strong opinions about the ones I'm using. In connection to `R` there aren't a ton of choices and with respect to `python` there are *many* choices.

<br>

### `R`

I am using [`renv`](https://rstudio.github.io/renv/articles/renv.html), which is activated in the `.Rprofile` via `source("renv/activate.R")`. Outside of `packrat` there aren't a lot of choices and the `R` tooling is built *around* `renv` and it works!

<br>

### `Python`

I am using [`mamba`](https://mamba.readthedocs.io/en/latest/user_guide/mamba.html), which is a "reimplementation of the conda package manager in C++" (from the [`README`](https://github.com/mamba-org/mamba)). If you want to learn more about the motivation check out the [announcement blog post](https://medium.com/@QuantStack/open-software-packaging-for-science-61cecee7fc23).

<br>

## Theming

I've sort of based the theme on a tshirt I love from one of my favorite streetwear brands [Extra-Vitamins](https://extra-vitamins.com/products/higher-than-the-sun-tee). The branding font is using [Victor-Mono](https://rubjo.github.io/victor-mono/), which I will try to add as the mono typeface for the site eventually.
