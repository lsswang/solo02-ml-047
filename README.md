# Ordered sketch regression and plotting

`traces.py` fits one regularized cubic to every ordered trace. `plotter.py`
accepts cubic geometry directly and uses nearest-entry, forward-only drawing.
`demo.py` passes actual fitted curves to the plotting reader and emits the full
pen command stream. Run `python demo.py` after installing `requirements.txt`.

The supplied code is an ordinary starting implementation. The task statement
defines the requested model-selection and exact planning behavior. The fixture
is example input, not an exhaustive test set. No graphical device is needed.
