# Step 4 — Data Handling and Exposure (`modules/pipeline.py`)

You're a scientific data engineer integrating VTK with Trame.

## 🎯 Mission

Implement data handling logic to read, process, and expose relevant data properties (e.g., scalar ranges, array names, available fields) for downstream use in the VTK pipeline and Trame state.

Work task-by-task, pausing after each for user confirmation before continuing.

---

## 🧠 Inputs

- `.vtp` and `.vtu` files in the `/data` folder
- VTK readers already in use (`vtkXMLPolyDataReader`, `vtkXMLUnstructuredGridReader`)
- Trame server and state accessible via `get_server()`
- The app plan from Step 1 and pipeline logic from Step 3

---

## 📋 Tasks

### ✅ Activity 3 Extension: Data Handling

1. **Expose scalar array names to the UI**
   - From the `.vtu` file, extract list of point or cell data arrays
   - Store in Trame state as a list for populating a `VSelect`

2. **Extract scalar range for default array**
   - Compute min/max of the default scalar array
   - Store in Trame state as `scalar_min`, `scalar_max`, and/or `scalar_range`

3. **Support dynamic array selection**
   - Use a `@change` or `@trigger` decorator to update VTK mapper and scalar range when a new array is selected from the UI

4. **Normalize and preprocess data if needed**
   - Optionally normalize values, clean mesh, or apply filters (e.g., `vtkThreshold`, `vtkContourFilter`)

5. **Expose color maps (LUT presets)**
   - Define a list of available colormap names
   - Populate a dropdown in the UI (`VSelect`) and connect to the rendering logic

---

## 🧩 Implementation Guidelines

- Use `vtkDataSet.GetPointData()` or `GetCellData()` to access arrays
- Use `.GetArrayName(i)` in a loop over `GetNumberOfArrays()`
- Use `GetRange()` to compute scalar ranges
- Store outputs in Trame state (e.g., `state.scalar_field_names`, `state.scalar_range`)
- For dynamic updates, make sure to call `view.update()` or `view.reset_camera()` as needed

---

## 🚦 Next Step

Start with Task 1:  
**"Extract list of scalar array names from `.vtu` file and store in Trame state"**

---

## 🧩 Technical Resources

- Trame 3 with:
  - `@change`, `@trigger`, `@controller`, `@life_cycle`
  - `trame.app.get_server()` modular design
  - `state.scalar_field_names`, `state.scalar_range`, etc.

- VTK with:
  - `vtkmodules.vtkIOXML.vtkXMLUnstructuredGridReader`
  - `vtkmodules.vtkDataSetAttributes`, `vtkDataArray`
  - `vtkDataSet.GetPointData()`, `GetArray(i)`, `GetRange()`

---

## 📚 Documentation for Reference

- Trame 3: https://kitware.github.io/trame/
- VTK Python: https://vtk.org/doc/nightly/html/
- vtk.js: https://kitware.github.io/vtk-js/

---

## 📦 Example Codebase

- Modern structure reference:  
  https://github.com/patrickoleary/trame-3-examples/blob/main/00_plotly-charts-selector.py
