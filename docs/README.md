To build the docs,

First activate `venv2` where `sphinx` and `sphinx-rtd-theme` is installed, then run

```
make clean && rm -rf _build _autosummary ../__pycache__ ../xplaypen/__pycache__ && make html
```

from the `doc` directory.


Then the static web files will be built in `_build/html`
