from trame.layouts import SinglePageWithDrawerLayout
from trame.widgets import vuetify3, vtk

def initialize(server):
    state = server.state

    with SinglePageWithDrawerLayout(server) as layout:
        layout.title.set_text("Trame VTK App")

        with layout.drawer:
            vuetify3.VSlider(v_model=("scalar_value", 0), min=0, max=100, label="Scalar Value")

        with layout.content:
            vtk.VtkRemoteView()
