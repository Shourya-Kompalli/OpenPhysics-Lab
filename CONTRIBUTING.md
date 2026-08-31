# Contributing to OpenPhysics-Lab

Thank you for contributing to OpenPhysics-Lab.

OpenPhysics-Lab is an open-source collection of physics simulations, numerical experiments, and visualizations. The project aims to make computational physics understandable, reproducible, and accessible to contributors.

## Ways to contribute

You can contribute by:

* Adding a new physics simulation
* Improving an existing simulation
* Fixing bugs
* Adding tests
* Improving numerical accuracy
* Improving visualizations
* Improving documentation
* Suggesting new experiments
* Reviewing pull requests

## Before contributing

Please check the existing issues before starting significant work.

For larger changes, open an issue first so the proposed change can be discussed before implementation.

## Development workflow

The general workflow is:

```text
Issue
↓
Create a branch
↓
Make the change
↓
Run the simulation
↓
Run tests
↓
Validate the result
↓
Commit
↓
Push
↓
Pull Request
```

Keep pull requests focused on a specific change.

## Physics and scientific validation

Physics simulations should clearly document:

* The physical model
* Equations used
* Assumptions
* Parameters
* Initial conditions
* Units
* Numerical method
* Known limitations

Whenever possible, numerical results should be compared with an analytical solution, known result, conservation law, convergence test, or another appropriate validation method.

A simulation producing a visually convincing result is not by itself evidence that the implementation is correct.

## Code style

Prefer code that is:

* Readable
* Simple
* Well documented
* Reproducible
* Easy for another contributor to understand

Avoid unnecessary dependencies and overly complicated abstractions.

## Commit messages

Use clear commit messages that describe the change.

Good examples:

```text
Add simple pendulum simulation
Fix projectile range calculation
Add numerical convergence test
Improve orbital mechanics documentation
```

Avoid vague messages such as:

```text
update
changes
stuff
final
```

## Pull requests

Pull requests should explain:

* What was changed
* Why it was changed
* How it was tested
* How the result was validated
* Whether documentation was updated

Please make sure the project still runs and the existing tests pass before submitting a pull request.

## Questions and discussions

If you are unsure about an implementation, open an issue or discussion before making a large change.

Constructive scientific and technical discussion is encouraged.

Thank you for helping improve OpenPhysics-Lab.
