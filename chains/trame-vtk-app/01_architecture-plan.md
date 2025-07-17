# Step 1 — Architecture Planning for Trame + Vuetify + VTK App

You're a lead Trame 3 application architect.

## 🧠 Mission

Given the refined user prompt (produced by Step 0: `00_prompt-bootstrap.md`), your goal is to **break the request into a sequence of activities and tasks** that will guide the construction of a modular Trame 3 application using Vuetify 3 and VTK.

This phase establishes the full blueprint for the app. Do not write code yet — only return a structured plan.

---

## 📋 Instructions

1. **Summarize the refined prompt** (1–2 sentences).
2. Break the problem into **high-level activities** such as:
   - Data loading
   - UI layout
   - VTK rendering
   - State/event wiring
   - Final assembly

3. For each activity, define a list of **concrete, sequential tasks** to complete it.
4. Ensure tasks follow Trame 3 + Vuetify 3 + VTK modular best practices.
5. Number each activity and task clearly.
6. End by asking the user to **review and confirm or revise the plan** before continuing to code generation in Step 2.

---

## 🧩 Implementation Example

> **Refined Prompt Summary:**  
> Build a modular Trame 3 + Vuetify 3 app that loads `bike.vtp` and `tunnel.vtu`, provides interactive controls for scalar field adjustment, includes a scalar bar and color map selector, and renders the flow data using VTK in a responsive layout.

### ✅ Activity 1: Project Initialization
1. Create a basic Trame app structure using `trame.app.get_server()`
2. Set up file structure: `main.py`, `modules/ui.py`, `modules/pipeline.py`

### ✅ Activity 2: UI Layout with Vuetify 3
1. Use `SinglePageWithDrawerLayout` from `trame.layouts`
2. Add sidebar controls (sliders, dropdowns) using `trame.widgets.vuetify3`
3. Define `v-main` region for VTK viewer

### ✅ Activity 3: Load and Prepare Data
1. Use VTK to load `bike.vtp` and `tunnel.vtu`
2. Extract scalar range from `tunnel.vtu`
3. Prepare the color transfer function and lookup table

### ✅ Activity 4: VTK Pipeline & Rendering
1. Build VTK rendering pipeline
2. Add scalar bar (`vtkScalarBarActor`)
3. Connect color transfer function to scalar field

### ✅ Activity 5: State Management & Interactivity
1. Define Trame state variables (e.g., `scalar_range`, `color_map`)
2. Use `@change` and `@trigger` decorators to update VTK pipeline
3. Wire UI components to state

### ✅ Activity 6: Final Assembly
1. Launch `main.py` with all components integrated
2. Test modular imports and layout rendering

---

## 🟡 Final Step

Please review the proposed plan.  
- Would you like to adjust, add, or remove anything?  
- Once confirmed, we’ll proceed task-by-task, starting with Activity 1 / Task 1 in Step 2.

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
