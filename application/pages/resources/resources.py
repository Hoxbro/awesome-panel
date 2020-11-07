"""The awesome panel resources list provides a list of awesome resources for Panel"""
import pathlib

from panel.pane import Markdown

from application.config import site

RESOURCES_PATH = pathlib.Path(__file__).parent / "resources.md"
RESOURCES = RESOURCES_PATH.read_text()

@site.register(
    url="resources",
    name="Resources",
    author="Marc Skov Madsen",
    description=__doc__,
    thumbnail_url="resources.png",
    documentation_url="",
    code_url="resources/resources.py",
    gif_url="",
    mp4_url="",
    tags=[
        "Code",
        "App In Gallery",
    ],
)
def view():
    """The resources view of awesome-panel.org"""
    main = [Markdown(RESOURCES, sizing_mode="stretch_width")]
    template = site.get_template(title="Resources", main=main)
    return template


if __name__.startswith("bokeh"):
    view().servable()
