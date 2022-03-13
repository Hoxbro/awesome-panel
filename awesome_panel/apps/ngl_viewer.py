# pylint: disable=line-too-long, wrong-import-position
"""
This is an example of a Protein viewer app, using the [NGL Viewer](https://github.com/nglviewer/ngl).

You can import it from the `awesome-panel-extensions` package via
`from awesome_panel_extensions.widgets.ngl_viewer import NGLViewer`.

The NGL Viewer was developed with help from the community.

Checkout [Discourse 583](https://discourse.holoviz.org/t/how-to-use-ngl-webgl-protein-viewer-in-panel/583).
"""
# pylint: enable=line-too-long
import panel as pn
import param
from awesome_panel_extensions.widgets.ngl_viewer import NGLViewer

from awesome_panel import config

DEFAULT_RCSB_ID = "1NKT"


class ProteinViewer(param.Parameterized):
    """This is an example of a Protein viewer app, using the [NGL Viewer]\
(https://github.com/nglviewer/ngl)."""

    input_option = param.Selector(default="RCSB PDB", objects=["RCSB PDB", "Upload File"])
    rcsb_id = param.String(default=DEFAULT_RCSB_ID)
    load_structure = param.Action(label="LOAD STRUCTURE")

    def __init__(self, **params):
        super().__init__(**params)
        self.load_structure = self._load_structure
        self.file_widget = pn.widgets.FileInput(accept=".pdb")
        self.ngl_html = NGLViewer(sizing_mode="stretch_both")
        self.ngl_html_container = pn.Column(self.ngl_html, height=600, sizing_mode="stretch_width")

        pn.state.onload(self._load_structure)

    def _load_structure(self, *_):
        if self.input_option == "Upload File":
            if self.file_widget.value:
                string = self.file_widget.value.decode()
                self.ngl_html.pdb_string = string
            else:
                pass
        elif self.input_option == "RCSB PDB":
            self.ngl_html.rcsb_id = self.rcsb_id

    def view(self):
        """Returns a view of the app in the FastListTemplate"""
        settings = pn.Column(
            pn.pane.Markdown("## Settings", margin=0),
            *pn.Param(
                self.param, widgets={"load_structure": {"button_type": "primary"}}, show_name=False
            ),
            self.file_widget,
            self.ngl_html.param.representation,
            self.ngl_html.param.color_scheme,
            self.ngl_html.param.spin,
            max_width=300,
        )
        alert = pn.pane.Alert(
            """You can find **Rcsb ids** at <a href="https://www.rcsb.org/"
target="_blank">rcsb.org</a>. A few examples are: `2GQ5`, `3UOG` and `5TXH`.""",
            margin=0,
        )
        main_ = pn.Column(alert, self.ngl_html_container)

        return pn.Row(settings, main_)


def serve():
    """Serves the app"""
    config.extension(url="ngl_viewer")
    viewer = ProteinViewer()

    settings, main = viewer.view()

    settings.servable(area="sidebar")
    main.servable()


if __name__.startswith("bokeh"):
    serve()
