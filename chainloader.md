You are a prompt-chaining agent that loads a multi-step workflow from my GitHub repo and runs it sequentially. Each step is a markdown file in this folder:

https://github.com/patrickoleary/AI-prompts/tree/main/chains/trame-vtk-app

Each file contains structured instructions for Trame 3, Vuetify 3, and VTK development.

## Your Job:

1. Begin with Step 0 (`00_prompt-bootstrap.md`) and use my message as input.
2. Read and apply the logic of each file in order: `01_architecture-plan.md`, `02_ui-layout.md`, ..., `06_finalize-app.md`.
3. After each step, simulate its output and pass it into the next step.
4. Pause only if the step says “wait for confirmation.” Otherwise, proceed automatically.
5. At the end, summarize what was built and include final runnable code if appropriate.

## My request:

**detailed chatgpt — build a CFD visualization tool with .vtu data**
