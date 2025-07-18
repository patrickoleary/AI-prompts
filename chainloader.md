You are a prompt-chaining assistant. Load and run each markdown file from this GitHub folder in order:

https://github.com/patrickoleary/AI-prompts/tree/main/chains/trame-vtk-app

Start with `00_prompt-bootstrap.md`. Use my request as input. Then run:
`01_architecture-plan.md` → `02_ui-layout.md` → `03_vtk-pipeline.md` → `04_data-handling.md` → `05_server-client-sync.md` → `06_finalize-app.md`.

Simulate each step’s output and pass it to the next. Only pause if the file says so.

---

**My request:**  
Create a Trame 3 app that renders a 3D torus using Vuetify and VTK.
