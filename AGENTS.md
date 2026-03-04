# Agent Guidelines

## Code Style
 * Avoid abbreviations unless they are widely standard (e.g., `cls`, `utc`).

## Multi-file refactors (safety-first)
- Validate whether a proposed change applies to each file/class/function.
  - If clearly not applicable: do not change it; leave a note.
  - If uncertain/risky: add a `TODO` explaining the risk.
  - If clearly applicable: apply the change.

## Execution environment
- Run commands/scripts in the project’s default virtual environment.

## Testing
 * do NOT run manual_* test cases since they require human interaction BUT suggest the
   applicable test cases
 * do NOT run any implementation with server access BUT suggest running them