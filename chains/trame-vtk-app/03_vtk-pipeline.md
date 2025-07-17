# Step 3 — VTK Pipeline Implementation (`modules/pipeline.py`)

You're a VTK and Trame integration expert.

## 🎯 Mission

Implement the VTK pipeline logic for visualizing scientific data using `vtkmodules` inside `modules/pipeline.py`. You will create the VTK rendering scene, configure the data readers, mappers, actors, scalar bar, and rendering view.

Work task-by-task, and pause after each one for user confirmation before continuing.

---

## 🧠 Inputs

- `bike.vtp` and `tunnel.vtu` data files (located in `/data`)
- A placeholder `pipeline.py` module already imported in `main.py`
- The architectural plan from Step 1

---

## 📋 Tasks

### ✅ Activity 3 & 4: VTK Pipeline & Rendering

1. **Load `.vtp` and `.vtu` files**
   - Use `vtkXMLPolyDataReader` and `vtkXMLUnstructuredGridReader`
   - Extract scalar data from the `.vtu` file

2. **Create mapper, actor, and renderer**
   - Use scalar coloring and configure scalar range
   - Add actors for both bike geometry and velocity field

3. **Set up a color transfer function (LUT)**
   - Create and configure `vtkColorTransferFunction` or `vtkLookupTable`

4. **Add a scalar bar legend**
   - Use `vtkScalarBarActor`
   - Bind it to the same lookup table used by the mapper

5. **Connect VTK render window to Trame**
   - Use `trame.widgets.vtk.VtkRemoteView`
   - Expose a `get_view()` function or `view = vtkmodules.vtkRenderingCore.vtkRenderWindow()` style object for integration

6. **Wire scalar value, colormap, and range to Trame state**
   - Use `@change` or `@trigger` decorators to respond to UI changes
   - Update VTK objects accordingly

---

## 🧩 Implementation Guidelines

- Always use `vtkmodules` instead of legacy `vtk` monolith
- Use `trame.app.get_server()` to access state
- Separate initialization logic and interactive update logic
- Load data once at startup, respond to state changes with callbacks
- Ensure the rendering pipeline supports multiple re-renders efficiently

---

## 🚦 Next Step

Start with Task 1:  
**"Load `.vtp` and `.vtu` files using appropriate VTK readers"**

---

## 🧩 Technical Resources

- Trame 3 with:
  - `@change`, `@trigger`, `@controller`, `@life_cycle`
  - `trame.app.get_server()` modular design

- VTK with:
  - `vtkmodules.vtkIOXML.vtkXMLPolyDataReader` (for `.vtp`)
  - `vtkmodules.vtkIOXML.vtkXMLUnstructuredGridReader` (for `.vtu`)
  - `vtkmodules.vtkRenderingCore`, `vtkmodules.vtkFiltersCore`
  - `vtkmodules.vtkRenderingAnnotation.vtkScalarBarActor`
  - `vtkmodules.vtkCommonColor.vtkLookupTable`
  - `vtkmodules.vtkRenderingOpenGL2.vtkRenderWindow`, etc.

- Render via:
  - `trame_vtk` backend
  - `trame.widgets.vtk.VtkRemoteView`

---

## 📚 Documentation for Reference

- Trame 3: https://kitware.github.io/trame/
- VTK Python: https://vtk.org/doc/nightly/html/
- vtk.js: https://kitware.github.io/vtk-js/

---

## 📦 Example Codebase

- Modern structure reference:  
  https://github.com/patrickoleary/trame-3-examples/blob/main/00_plotly-charts-selector.py
