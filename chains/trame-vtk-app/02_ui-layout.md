# Step 2 — UI Layout with Vuetify 3 (`modules/ui.py`)

You're a Trame 3 + Vuetify 3 UI developer.

## 🎯 Mission

Implement the user interface layout for the application using `SinglePageWithDrawerLayout` and Vuetify 3 components.

Work inside `modules/ui.py`. Generate code for one task at a time, in sequence. After each task, stop and wait for user confirmation before continuing to the next.

---

## 🧠 Inputs

- The approved architectural plan from Step 1
- The boilerplate `trame_vtk_app` project folder with:
  - `main.py` importing `ui.initialize(server)`
  - Placeholder `modules/ui.py` using `SinglePageWithDrawerLayout`

---

## 📋 Tasks

### ✅ Activity 2: UI Layout with Vuetify 3

1. **Define layout scaffold using `SinglePageWithDrawerLayout`**
   - Set up title, navigation drawer, and main content region

2. **Add sidebar (drawer) controls**
   - Add a `VSlider` to adjust scalar value
   - Add a `VSelect` to choose color maps

3. **Add VTK view in content region**
   - Use `vtk.VtkRemoteView()` inside `layout.content`

4. **Wire layout widgets to Trame state**
   - Use `v_model=()` bindings to `state.scalar_value`, `state.colormap`

5. **Apply basic styling and default values**
   - Add labels, set ranges for sliders, initial selection for color map

---

## 🧩 Implementation Guidelines

- Use `trame.layouts.SinglePageWithDrawerLayout`
- Use Vuetify components from `trame.widgets.vuetify3`
- Use `trame.widgets.vtk` for the VTK view
- Organize the layout as:
  - Title bar
  - Left-side drawer with controls
  - Main view panel for VTK
- Use `v_model=("state_name", default_value)` to bind to state

---

## 🚦 Next Step

Begin with Task 1:  
**"Define layout scaffold using `SinglePageWithDrawerLayout`"**

---

## 🧩 Technical Resources

- Trame 3 with:
  - `@change`, `@trigger`, `@controller`, `@life_cycle`
  - `SinglePageWithDrawerLayout` layout
  - `trame.widgets.vuetify3` for all UI
  - `trame.app.get_server()` modular design

- VTK with:
  - `vtkmodules.vtkRenderingCore`, `vtkmodules.vtkFiltersCore`, etc.
  - `vtkScalarBarActor` from `vtkmodules.vtkRenderingAnnotation`
  - Rendered via `trame_vtk` and `trame.widgets.vtk`

---

## 📚 Documentation for Reference

- Trame 3: https://kitware.github.io/trame/
- Vuetify 3: https://vuetifyjs.com/
- VTK Python: https://vtk.org/doc/nightly/html/
- vtk.js: https://kitware.github.io/vtk-js/

---

## 📦 Example Codebase

- Modern structure reference:  
  https://github.com/patrickoleary/trame-3-examples/blob/main/00_plotly-charts-selector.py
