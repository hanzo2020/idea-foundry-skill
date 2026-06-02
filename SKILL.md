# IdeaFoundry

## Purpose

IdeaFoundry reads academic PDF papers from a user-specified folder and extracts reusable, theory-grounded method components into one cumulative library file.

This is not a generic paper summarization skill. The goal is to build a reusable method component library for future research ideation, where the future target task may be unknown.

IdeaFoundry should focus on components with clear mathematical, probabilistic, statistical, spectral, geometric, information-theoretic, optimization-based, or distributional foundations.

In addition to model blocks and principle-level mechanisms, IdeaFoundry may also extract reusable strategy components when they are broadly transferable and mechanistically clear. These include, for example, loss designs, reweighting rules, calibration schemes, abstention or reject-option strategies, class-imbalance handling, debiasing rules, curriculum or self-paced schedules, denoising criteria, and optimization stabilizers.

Do not prioritize purely ad hoc tricks such as adding an unexplained auxiliary loss, concatenating features, adding a scalar weight with no rationale, or using attention without a clear mechanism. A trick-like strategy is valid only when its scope, assumptions, and mechanism can be abstracted beyond the original paper task.

## Default Output

Maintain one cumulative Markdown library file instead of creating one output file per paper.

Default output file:

```text
idea_foundry_library.md
```

If the file already exists, update it. If it does not exist, create it from the template in `templates/library_template.md`.

## Core Workflow

For each PDF paper in the given folder:

1. Read the paper carefully, especially the abstract, introduction, method, theory/preliminaries, experiments only when needed, and limitations if available.
2. Determine the paper type:
   - Type A: Foundational theory paper.
   - Type B: Application-oriented method paper.
   - Type C: Mostly heuristic engineering paper.
3. Extract 1鈥? reusable theory-grounded method components if available.
4. For each extracted component, specify its input, output, theoretical mechanism, suitable problem type, applicability conditions, and failure conditions.
5. Compare the extracted component with existing components in `idea_foundry_library.md`.
6. If a substantially similar component already exists, update the existing card instead of creating a duplicate.
7. If the component is theoretically distinct, create a new component ID, such as C001, C002, C003.
8. Update all relevant indexes:
   - Problem-to-Component Index
   - Theory-to-Component Index
   - Component Type Index
9. Add a short changelog entry.

## Paper Type Rules

### Type A: Foundational Theory Paper

A paper is Type A if it mainly develops, analyzes, or formalizes a theoretical mechanism, mathematical object, optimization principle, probabilistic model, statistical property, or theoretical guarantee.

For Type A papers, extract principle-level components:

- What is the core mathematical or probabilistic object?
- What assumptions does the theory require?
- What output, property, guarantee, distance, bound, transformation, or optimization principle does it provide?
- How can this principle be converted into a reusable modeling component?
- What types of machine learning problems can this principle address?

### Type B: Application-Oriented Method Paper

A paper is Type B if it mainly proposes a model or algorithm for a specific task, but contains extractable theory-grounded components.

For Type B papers, extract method-level components:

- What part of the proposed method has clear theoretical grounding?
- What input object does the component require?
- What output object does the component produce?
- What modeling problem does it solve in the original task?
- How can it be abstracted away from the original task?

### Type C: Mostly Heuristic Engineering Paper

A paper is Type C if it mainly combines empirical modules, auxiliary losses, learned weights, architectural blocks, or implementation tricks with weak theoretical grounding.

For Type C papers:

- Do not force extraction.
- Extract only the parts that can be tied to a clear theoretical mechanism.
- If no valid theory-grounded component exists, add only a short changelog note saying the paper was skipped or marked low priority.

## Valid Component Criteria

A valid component should satisfy most of the following:

1. It has a clear theoretical foundation.
2. It has a definable input object.
3. It has a definable output object.
4. It addresses a recognizable class of modeling problems.
5. It can be abstracted beyond the original paper's task.
6. It has interpretable assumptions or conditions under which it is expected to work.
7. It has potential to be recombined with other components in future model design.
8. If it is a training or inference trick, its mechanism, scope, and transfer conditions can be stated clearly enough that another researcher could reuse it outside the original task.

Do not treat the following as strong components unless they are connected to a clear theory:

- adding an auxiliary loss;
- adding a learned scalar weight;
- concatenating two representations;
- adding a generic attention module;
- stacking more layers;
- replacing an encoder without a theoretical reason;
- minor implementation tricks.

## Theoretical Grounding Levels

Classify every component as one of:

### Level A: Strong theoretical component

Directly grounded in a mature theory.

Examples:

- spectral graph filtering;
- optimal transport;
- variational inference;
- Bayesian posterior modeling;
- kernel methods;
- information bottleneck;
- energy-based modeling;
- diffusion processes;
- convex optimization;
- stochastic processes.

### Level B: Theory-inspired component with neural approximation

Inspired by or structured around a theoretical mechanism, but implemented with neural approximations.

Examples:

- Dirichlet evidential prediction;
- neural mutual information estimation;
- prototype-based distribution modeling;
- graph rewiring based on curvature;
- neural coefficient generation for polynomial filters;
- reliability-aware evidence discounting.

### Level C: Mostly heuristic component

Mostly empirical, with limited theoretical foundation.

Examples:

- generic auxiliary loss;
- empirical weighting;
- feature concatenation;
- plain attention fusion without a clear assumption.

However, a loss, weighting rule, regularizer, abstention mechanism, or curriculum strategy may still qualify when it encodes a clear optimization, statistical, probabilistic, or decision-theoretic principle and is reusable beyond the original benchmark.

Prioritize Level A and Level B. Include Level C only if it is unusually reusable or important.

A reusable trick such as class-imbalance-aware loss shaping, uncertainty-aware abstention, confidence calibration, sample reweighting, or optimization stabilization should usually be treated as Level B when it is mechanism-driven and broadly transferable, and Level C when it is mostly empirical but still unusually reusable.

## Component Card Format

Each component card in the library must follow this structure:

```markdown
### CXXX. Component Name

#### Component Summary
One precise sentence describing the reusable mechanism.

#### Source Type
- Foundational theory / Application-oriented method / Hybrid / Heuristic-low-priority

#### Source Papers
- Paper title, venue, year if available.

#### Theoretical Foundation
- List the theories or mathematical foundations.

#### Input
- Describe the required input object precisely.
- Include mathematical form and structural assumptions when possible.

#### Output
- Describe the output object precisely.

#### Core Mechanism
Explain the mechanism in 2鈥? sentences. Focus on the mathematical, probabilistic, spectral, geometric, information-theoretic, or optimization principle. Do not summarize the full model pipeline.

#### Suitable Problem Types
- List the modeling problems this component can address.

#### Applicability Conditions
- State when this component is likely to work well.

#### Failure or Mismatch Conditions
- State when this component may be inappropriate or ineffective.

#### Known Variants
- List known variants if any.

#### Research Reuse Pattern
- Describe general ways this component can be reused, modified, or combined in future research.

#### Task-Independent Abstraction
Given [input object], use [theoretical mechanism] to produce [output object], so that [problem type] can be addressed.

#### Theoretical Grounding Level
Level A / Level B / Level C, with a short justification.

#### Tags
#tag1 #tag2 #tag3
```

## Duplicate and Update Rules

When processing a new paper, do not blindly create new components.

Before adding a new card, compare the extracted component with existing cards in the library.

If the new component is substantially the same as an existing component:

- update the existing component card;
- add the new paper under `Source Papers`;
- add new variants under `Known Variants`;
- refine `Applicability Conditions` or `Failure or Mismatch Conditions` if the paper provides new insight;
- update indexes if needed.

If the component is theoretically distinct:

- create a new component ID;
- add a new component card;
- update all relevant indexes.

## Library File Structure

The cumulative library file should use this structure:

```markdown
# IdeaFoundry Library

## 0. Usage Guide

## 1. Problem-to-Component Index

## 2. Theory-to-Component Index

## 3. Component Type Index

## 4. Component Cards

### C001. Component Name
...

### C002. Component Name
...

## 5. Changelog
```

## Indexing Rules

### Problem-to-Component Index

Organize components by modeling problem, such as:

- graph over-smoothing;
- heterophily;
- distribution shift;
- noisy observations;
- scarce labels;
- multi-source conflict;
- uncertainty estimation;
- representation collapse;
- high-dimensional data;
- weak supervision;
- non-Euclidean structure.

### Theory-to-Component Index

Organize components by theoretical foundation, such as:

- spectral graph theory;
- probability distribution modeling;
- Bayesian inference;
- variational inference;
- optimal transport;
- information theory;
- kernel methods;
- energy-based modeling;
- diffusion processes;
- stochastic processes;
- causal inference;
- optimization theory;
- matrix factorization;
- geometric deep learning.

### Component Type Index

Organize components by functional role, such as:

- representation components;
- graph filtering components;
- fusion components;
- calibration components;
- alignment components;
- uncertainty components;
- optimization/search components;
- explanation components;
- generative components.

## Style Rules

- Prefer precision over broad descriptions.
- Do not merely summarize the abstract.
- Do not overstate novelty.
- Separate what the paper actually proposes from task-independent abstraction.
- Focus on reusable theoretical mechanisms, not implementation details.
- If a paper contains multiple modules, decompose only the modules with theoretical meaning.
- If a component depends on a strong assumption, state it clearly.
- Keep each component card compact but complete.

## Recommended User Command

The user can invoke this skill with a command like:

```text
Use the IdeaFoundry skill. Read all PDF papers in [folder path], extract theory-grounded method components, and update idea_foundry_library.md. Do not create one file per paper. Deduplicate similar components and update the indexes.
```

