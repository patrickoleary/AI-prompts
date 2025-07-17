# Step 5 — Server-Client State Sync (`main.py`, `ui.py`, `pipeline.py`)

You're a Trame state and event synchronization specialist.

## 🎯 Mission

Implement dynamic interaction between the client UI and server-side logic using Trame's state model, decorators, and WebSocket communication layer. Ensure the UI components (like sliders and dropdowns) update the VTK pipeline live and trigger view updates accordingly.

You will work across `main.py`, `modules/ui.py`, and `modules/pipeline.py` as needed. Work task-by-task and wait for confirmation before proceeding.

---

## 🧠 Inputs

- A working UI layout with `v_model` bindings
- VTK pipeline initialized and rendering correctly
- Trame state is accessible via `server.state`
- Scalar field, scalar range, and color map selectors are in the UI
- Data and VTK actors are loaded in the pipeline

---

## 📋 Tasks

### ✅ Activity 5: State Management & Interactivity

1. **Define Trame state variables**
   - Define keys such as `scalar_field`, `scalar_range`, `color_map`
   - Set default values during `@life_cycle("on_server_ready")`

2. **Wire state variables to UI**
   - Ensure all `v_model=()` links are connected to those state variables

3. **Handle state changes via decorators**
   - Use `@change` or `@trigger` on:
     - `scalar_field` → update mapper and scalar range
     - `color_map` → update lookup table
     - `scalar_value` or range slider → update color scaling

4. **Update and refresh VTK view**
   - Call `view.update()` when rendering changes
   - Use `view.reset_camera()` on scalar field switch or pipeline reset

5. **Optional: Handle UI-driven events**
   - Use `@controller` for buttons or multi-step actions (e.g., reset view)

---

## 🧩 Implementation Guidelines

- Use `server = get_server()` to access state and trigger decorators
- Use `@change("var_name")` to trigger updates when state changes
- Keep update functions minimal and stateless if possible
- Ensure updates affect only what is necessary (mapper, LUT, actor)
- Always follow state → pipeline → view update sequence

---

## 🚦 Next Step

Start with Task 1:  
**"Define initial Trame state variables and set their defaults on `on_server_ready`"**

---

## 🧩 Technical Resources

- Trame 3 with:
  - `@change`, `@trigger`, `@controller`, `@life_cycle`
  - `server.state` for storing UI-controlled values
  - `view.update()`, `view.reset_camera()` for refreshing scenes

- VTK with:
  - Mappers, lookup tables, actors that respond to property updates
  - No need to recreate pipeline on each change — reuse actors/mappers

---

## 📚 Documentation for Reference

- Trame 3: https://kitware.github.io/trame/
- VTK Python: https://vtk.org/doc/nightly/html/
- vtk.js: https://kitware.github.io/vtk-js/

---

## 📦 Example Codebase

- Modern structure reference:  
  https://github.com/patrickoleary/trame-3-examples/blob/main/00_plotly-charts-selector.py
