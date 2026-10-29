---
name: idea-foundry
description: Decompose academic PDF papers into 2-3 candidate research ideas, apply research-scope and platform-independence gates, evaluate reusable ML/AI theoretical and methodological components, and maintain a deduplicated cumulative IdeaFoundry Markdown library plus a traceable excluded-paper ledger. Use when reading folders of papers, mining research ideas, filtering domain-specific systems or hardware work, building or updating idea_foundry_library.md, screening paper code repositories, or performing cross-paper component extraction and reuse analysis.
---

# IdeaFoundry

## Purpose

IdeaFoundry reads academic PDF papers from a user-specified folder, decomposes each paper into candidate ideas, and extracts reusable theory-grounded or mechanism-grounded components into one cumulative library file.

This is not a generic paper summarization skill. The goal is to build a reusable method component library for future research ideation, where the future target task may be unknown.

IdeaFoundry should focus on components with clear mathematical, probabilistic, statistical, spectral, geometric, information-theoretic, optimization-based, or distributional foundations.

When surveying a new folder, prioritize mathematically or probabilistically grounded ideas before heuristic tricks. In particular, actively look for reusable components derived from the application of probability theory, stochastic processes, Bayesian inference, variational inference, kernel or RKHS methods, optimal transport, stochastic control, game-theoretic or regret-based analysis, statistical decision theory, and other formal mathematical mechanisms.

Do not dismiss a paper as merely theoretical until you have checked whether its theorem, probabilistic construction, objective, bound, posterior, kernel, path measure, variational family, or optimization principle can be converted into a reusable modeling component. Bias toward extracting strong Type A or theory-rich Hybrid cards before spending effort on weaker heuristic tricks.

IdeaFoundry is allowed to extract theory-mother cards for classical results, even when those results are not original to the current paper, if the paper uses them as a real mechanism rather than as background decoration. This includes, for example, mathematical theorems, probabilistic inequalities, interpolation results, concentration bounds, stopping rules, approximation principles, and other formal results that may later inspire new methods in other papers.

In addition to model blocks and principle-level mechanisms, IdeaFoundry may also extract reusable strategy components when they are broadly transferable and mechanistically clear. These include, for example, loss designs, reweighting rules, calibration schemes, abstention or reject-option strategies, class-imbalance handling, debiasing rules, curriculum or self-paced schedules, denoising criteria, and optimization stabilizers.

Do not prioritize purely ad hoc tricks such as adding an unexplained auxiliary loss, concatenating features, adding a scalar weight with no rationale, or using attention without a clear mechanism. A trick-like strategy is valid only when its scope, assumptions, and mechanism can be abstracted beyond the original paper task.

## Default Output

Maintain one cumulative Markdown library file instead of creating one output file per paper.

Default output file:

```text
idea_foundry_library.md
```

If the file already exists, update it. If it does not exist, create it from the template in `templates/library_template.md`.

## Code Repository Screening

Before extracting ideas from a paper, perform a lightweight repository screen focused on whether the paper appears to have a usable Python codebase.

For each paper:

1. Check whether the paper itself includes a GitHub link or clearly points to a code repository.
2. If no GitHub repository is present, continue the normal IdeaFoundry reading and extraction workflow, but do not do any code-copy action.
3. If a GitHub repository is present, inspect it and confirm all of the following before treating it as a valid code-backed paper:
   - the repository appears to be for this paper rather than an unrelated baseline, author profile, or generic collection;
   - the repository is not an empty shell, README-only placeholder, or near-empty stub;
   - the repository is Python-based, meaning it contains substantial Python implementation files or a clearly Python-centered project structure.
4. If the repository passes all three checks, copy the paper PDF into a `havecode` folder.

Default `havecode` behavior:

- create a `havecode` subfolder inside the currently processed paper folder unless the user specifies a different location;
- copy the original PDF there without renaming it unless the user requests a different naming scheme.

Repository screening is an auxiliary research-organization step. It should not replace the main theory-grounded extraction workflow.

## Research Scope Gate

Apply a research-scope gate before allocating or updating a main-library card. The main library is an ML/AI method-component library, not a complete proceedings index.

### Default in-scope work

Retain components whose primary contribution is reusable across ML/AI research problems, including:

- learning objectives, optimization algorithms, statistical estimators, uncertainty and calibration methods;
- representation learning, generative modeling, causal inference, graph learning, foundation-model methods, and neuro-symbolic interfaces;
- general RL, imitation learning, world models, or planning mechanisms whose definition does not depend on a particular robot body or physical platform;
- distributed or federated optimization when the contribution directly changes the learning objective, estimator, convergence mechanism, or privacy model.

### Default out-of-scope work

Do not create main-library cards for work whose core contribution is primarily:

- chips, circuits, accelerator design, hardware mapping, or device-level implementation;
- computer architecture, memory hierarchy, cache management, interconnects, or kernel scheduling;
- computer networks, communication protocols, congestion control, routing infrastructure, or network measurement;
- systems serving, storage, database, compiler, runtime, deployment, or throughput engineering;
- robot morphology, actuator design, platform-specific control, sensor placement, or hardware benchmarking;
- a benchmark, leaderboard, dataset, or engineering pipeline with no independently reusable ML mechanism.

Record these papers in an excluded-paper ledger instead of silently dropping them. Repository screening may still be recorded independently.

### Conditional cross-domain retention

Retain a component from an otherwise out-of-scope domain only when it passes all of the following:

1. **Platform-removal test:** after removing hardware, platform, protocol, or device names, the component still has a precise ML input, transformation or decision rule, and output.
2. **Mechanism-survival test:** the contribution is not merely an implementation optimization; its objective, estimator, learning rule, uncertainty model, or guarantee remains meaningful.
3. **Transfer test:** identify at least two plausible ML/AI problem families outside the source domain that can reuse the mechanism without reproducing the original system.
4. **Evidence test:** the paper provides analysis or experiments that isolate the portable mechanism rather than only end-to-end system gains.

If any test fails, exclude the card from the main library. Do not invent broad transfer claims to rescue a domain-specific paper.

### Scope disposition

Assign one scope disposition before candidate-card dispositions:

- **IN -> Direct ML/AI:** proceed with normal extraction.
- **XFER -> Cross-domain portable:** proceed, but state why the mechanism passes all four conditional-retention tests.
- **OUT -> Domain-specific:** add a compact excluded-ledger entry with paper, domain, rejected candidates, reason, and any weak transferable hook; do not allocate a main-library component ID.

The scope gate overrides the inclusive-extraction default. A fully read OUT paper is a successful screened result even when it contributes no main-library card.

## Decomposition-First Principle

Treat every paper as a composition of research ideas rather than as one indivisible contribution. Before rating the paper or deciding whether it deserves a card, decompose it into 2-3 candidate ideas. Do this even when the paper presents one headline contribution, because the headline method usually combines a problem framing, a mechanism, an interface or composition rule, and a training or inference strategy.

For each candidate idea, write a compact decomposition map containing:

1. the local problem or design pressure it addresses;
2. the input, transformation or decision rule, and output;
3. its role in the paper and dependencies on the other candidate ideas;
4. its theoretical, empirical, or engineering rationale;
5. the section, equation, algorithm, figure, or other evidence anchor that supports the interpretation;
6. at least one plausible task-independent reuse direction.

Group tightly coupled substeps when a paper contains more than three plausible ideas. If the paper genuinely contains fewer than two separable ideas, do not invent artificial distinctions, but explicitly record why the mechanism is atomic. Do not reject the whole paper before evaluating each candidate idea independently.

Candidate ideas are analytical units, not claims about author novelty. A candidate may be the paper's main novelty, a borrowed theory operationalized by the paper, a useful composition pattern, or a reusable strategy.

## Core Workflow

For each PDF paper in the given folder:

1. Perform the repository screen described in `Code Repository Screening`.
2. Read the abstract and introduction, then assign the scope disposition defined in `Research Scope Gate`.
3. For OUT papers, inspect enough of the main method to verify that no candidate passes the conditional-retention tests, record the excluded-ledger entry, and stop main-library extraction.
4. For IN or XFER papers, read the main method section in full. Read theory, preliminaries, experiments, and limitations as needed to understand or validate the candidate mechanisms.
5. Build the 2-3-item decomposition map required by `Decomposition-First Principle` before assigning an overall paper type or making any keep/skip decision.
6. Determine the paper type:
   - Type A: Foundational theory paper.
   - Type B: Application-oriented method paper.
   - Type C: Mostly heuristic engineering paper.
7. Evaluate every candidate idea independently. Assign each one a disposition: create a new card, update an existing card, add a known variant or evidence boundary to an existing card, retain it as a Level C exploratory card, or reject it with a concrete reason.
8. For each retained idea, specify its input, output, mechanism, suitable problem types, applicability conditions, failure conditions, and evidence anchor.
9. Compare every retained idea with existing components in `idea_foundry_library.md`.
10. Update an existing card when the core mechanism is substantially similar.
11. Create a new component ID only when the mechanism, role, assumptions, interface, or transfer pattern is meaningfully distinct.
12. For neuro-symbolic papers, explicitly check whether the symbolic-neural interface itself deserves the primary card.
13. Explicitly check whether the paper operationalizes a classical formal object that deserves its own reusable card.
14. If every in-scope candidate was rejected, perform the second-pass salvage review defined in `Inclusive Extraction and No-Card Rule`.
15. Update all relevant indexes:
   - Problem-to-Component Index
   - Theory-to-Component Index
   - Component Type Index
16. Add a short changelog entry summarizing the scope disposition, 2-3 candidate ideas, and their dispositions, including repository-screen notes when relevant.
17. Run the card-completeness gate on every new or updated card before continuing to the next batch. If a required field is missing, merged, or only nominally filled, repair it before reporting progress.

## Card Completeness and Anti-Compression Contract

The component-card schema is a retrieval interface, not optional presentation. Every new or updated main-library card must keep all headings from `templates/component_card_template.md` as separate fields. Do not merge fields into headings such as `Source and Evidence`, `Input and Output`, `Conditions and Reuse`, or `Summary, Mechanism, and Source`.

Completeness takes priority over brevity. The instruction to keep cards compact means removing repetition; it never permits dropping the input, output, theoretical foundation, applicability conditions, failure conditions, reuse pattern, or task-independent abstraction. Batch size, elapsed time, context pressure, and a large existing library are not reasons to switch to a shorter schema.

Before accepting a card, verify all of the following:

- `Theoretical Foundation` names the formal theory, principle, estimator, geometry, optimization object, or mechanism that actually supports the card. A list of broad tags is insufficient.
- `Input` and `Output` are separate and identify object types, relevant mathematical form or structure, and important assumptions when available.
- `Core Mechanism` explains the transformation or decision rule and why it should work; it must not merely restate the summary.
- `Suitable Problem Types` includes defensible transfer targets. When the component is genuinely narrow, state that boundary instead of inventing breadth.
- `Applicability Conditions` and `Failure or Mismatch Conditions` are separate, concrete, and mechanism-specific.
- `Research Reuse Pattern` explains where the component plugs into a future pipeline, what may be replaced or combined, and what capability the reuse is intended to add.
- `Task-Independent Abstraction` explicitly instantiates the input -> mechanism -> output -> problem pattern.
- `Theoretical Grounding Level` chooses exactly one of Level A, Level B, or Level C and gives a short justification. Do not use hybrid labels such as `Level A/B`.
- `Source-Paper Role` and `Evidence Anchor` are present and trace the card back to the decomposition and paper text.
- `Source Papers` uses each paper's complete official title as printed on the paper or in authoritative metadata. Never substitute a local sequence number, renamed filename such as `61.pdf`, paper ID, component ID, abbreviated title, or title ending in `...`/`…`. Recover the title from the first page or full-text extract and cross-check it against the original-title mapping when one exists. Preserve meaningful subtitles after a colon.
- `Known Variants` remains a separate field. If none are supported, write `None identified from the current source` rather than deleting the field.

A field passes only when its content would help a future researcher decide whether and how to reuse the component. A heading with a placeholder, generic slogan, bare tag list, or content that belongs to another field counts as missing.

For batch work, validate each completed batch rather than postponing quality review until the end. Use `scripts/validate_library_cards.py` when available, passing the IDs created or updated in that batch. Structural validation is necessary but not sufficient: manually inspect representative cards for semantic specificity and source fidelity.

## Minimum Reading Requirement

Do not create or update component cards from abstract-only reading.

For every IN or XFER paper, before the final card dispositions:

- read the introduction in full;
- read the main method section in full;
- build the 2-3-item decomposition map;
- read theory, preliminaries, or analysis sections whenever a candidate depends on a theoretical claim, guarantee, or mechanism justification.

Abstract-first triage is allowed only for deciding whether a paper is likely worth deeper reading.

For an OUT disposition, read the introduction and inspect the central method sufficiently to verify that the portable-mechanism tests fail. Abstract-only domain keyword filtering is not enough. When scope is ambiguous, read more and prefer XFER only when all four retention tests can be stated concretely.

## Neuro-Symbolic Priority

Papers involving neural-symbolic methods, symbolic reasoning integrated with neural models, symbolic policy learning, symbolic abstraction inside neural pipelines, formal-neural hybrids, program-synthesis-for-neural-reasoning, or related neuro-symbolic mechanisms are mandatory-read IdeaFoundry material.

For such papers:

- do not mark them skipped without a full reading of the introduction and main method section;
- default to creating at least one card, even when the paper is partly heuristic, provided the symbolic-neural interaction itself is a reusable mechanism;
- if a paper contains both a neural backbone and a symbolic reasoning, rule, abstraction, verification, or consolidation layer, treat that interface as the primary extraction target;
- when in doubt, bias toward inclusion and extract the symbolic-neural coupling as a reusable component.

In short: neuro-symbolic papers are not low-priority triage material. They should be read carefully and should normally yield one or more component cards.

## Theory-First Preference

When there is a choice between extracting a mathematically grounded component and extracting a looser empirical trick, prefer the mathematically grounded component.

This means:

- prioritize reusable ideas built from formal mathematical or probabilistic structure;
- perform at least one explicit pass looking for probability-theory, Bayesian, kernel, variational, optimal-transport, stochastic-process, decision-theoretic, or other theorem-backed components;
- do not use "theory-only" as a reason to skip a paper unless you have already checked whether the theory can be re-expressed as a reusable modeling primitive;
- if a paper offers both a theoretical principle and a weaker implementation trick, the theoretical principle should usually be the primary card.
- if a paper's main mechanism depends on a classical theorem or formal result, you may create a standalone theory card for that result even if the theorem itself predates the paper and is not claimed as the paper's novelty.

Papers whose main value is a theorem, posterior construction, variational objective, kernel lifting, regret guarantee, bridge formulation, uncertainty decomposition, or structural identifiability result should be treated as high-priority IdeaFoundry material rather than low-priority background.

## Inclusive Extraction and No-Card Rule

Within IN and XFER papers, optimize for useful recall first and calibrated labeling second. Do not require every retained component to have a mature formal theory. Use Level A, Level B, and Level C to express grounding strength instead of using weak theory as an automatic rejection rule.

The default outcome for a fully read IN or XFER paper should be at least one library contribution. OUT papers are exempt and should normally yield only an excluded-ledger entry. This is not a numerical quota; never fabricate a component merely to satisfy it.

Before declaring a paper no-card, perform a second-pass salvage review over all candidate ideas using these lenses:

- representation or transformation mechanism;
- objective, regularization, or training strategy;
- inference, search, selection, or stopping rule;
- uncertainty, calibration, rejection, or decision strategy;
- interface, fusion, routing, or composition pattern;
- data construction, reweighting, curriculum, denoising, or optimization stabilizer.

Retain a Level C exploratory card when an in-scope idea has definable input and output, an identifiable mechanism, a plausible reuse pattern, and explicit limitations. For IN or XFER papers, a no-card decision is exceptional and must list the decomposed candidates, salvage lenses, and reasons. For OUT papers, the scope rationale and failed portability tests replace the salvage requirement.

Measure paper yield by all library contributions, not only by newly allocated component IDs. Deduplication that enriches an existing card is a successful extraction outcome rather than a skipped paper.

## Classical Theory Card Rule

Do not restrict extraction only to what the paper itself claims as novel.

If a paper substantially relies on a classical theoretical result and that result is mechanistically central, reusable, and potentially inspiring for future research, you may create or update a standalone theory card for it.

Typical eligible theory-mother cards include:

- mathematical theorems used as constructive design principles;
- probabilistic inequalities such as tail bounds or concentration results;
- interpolation, approximation, quadrature, or node-placement principles;
- optimal stopping, stopping-time, or secretary-style rules;
- geometric, variational, kernel, transport, or control principles;
- asymptotic, identifiability, calibration, regret, or decision-theoretic guarantees.

Do this especially when:

- the paper operationalizes the theory rather than merely citing it;
- the theory can clearly transplant to other tasks or modalities;
- the theory itself could inspire a separate modeling move, control layer, regularizer, discretization scheme, or search rule in future work.

Do not force a theory-mother card when the theorem is only casual background or when the paper does not actually use it as a mechanism.

## Paper Type Rules

### Type A: Foundational Theory Paper

A paper is Type A if it mainly develops, analyzes, or formalizes a theoretical mechanism, mathematical object, optimization principle, probabilistic model, statistical property, or theoretical guarantee.

For Type A papers, extract principle-level components:

- Default to inclusion unless the theory is genuinely too paper-specific to transplant.
- Be aggressive about converting theorems, posteriors, kernels, objectives, path measures, variational programs, or guarantees into reusable components.
- What is the core mathematical or probabilistic object?
- What assumptions does the theory require?
- What output, property, guarantee, distance, bound, transformation, or optimization principle does it provide?
- How can this principle be converted into a reusable modeling component?
- What types of machine learning problems can this principle address?
- Which concrete downstream problem types, especially outside the paper's immediate framing, might plausibly benefit from this principle?

### Type B: Application-Oriented Method Paper

A paper is Type B if it mainly proposes a model or algorithm for a specific task, but contains extractable theory-grounded components.

For Type B papers, extract method-level components:

- First look for mathematically grounded submodules before considering weaker heuristic tricks.
- What part of the proposed method has clear theoretical grounding?
- What input object does the component require?
- What output object does the component produce?
- What modeling problem does it solve in the original task?
- How can it be abstracted away from the original task?
- Beyond the original task, what other domains or problem types with similar structure could reuse it in a still-novel way?

### Type C: Mostly Heuristic Engineering Paper

A paper is Type C if it mainly combines empirical modules, auxiliary losses, learned weights, architectural blocks, or implementation tricks with weak theoretical grounding.

For Type C papers:

- Evaluate all decomposed candidates instead of rejecting the paper at the type level.
- Retain reusable engineering strategies, interfaces, composition patterns, or control rules as Level C exploratory cards when their mechanism and reuse boundary can be stated clearly.
- Prefer a calibrated Level C card over a no-card decision when the idea is transferable but weakly theorized.
- Apply the full no-card and salvage procedure if nothing qualifies.

## Suitable Problem Type Guidance

The `Suitable Problem Types` field should be written with deliberate transfer-oriented thinking.

- Do not merely restate the source paper's original task unless it is needed as a reference point.
- For Type B method papers, prioritize non-original-task applications where reusing the component could still count as a meaningful innovation.
- Prefer structurally analogous problems in other domains, modalities, data regimes, or decision settings over near-duplicate benchmark variants.
- For Type A foundational theory papers, it is acceptable to extrapolate outward and list concrete downstream problems where the principle may plausibly help, even if the paper itself does not test them.
- When plausible, include both the native task family and several cross-task reuse directions, but make the cross-task directions more prominent.
- Avoid fake breadth: every listed problem type should be defensible from the component's mechanism, assumptions, input object, and output object.

A good `Suitable Problem Types` section should help a future researcher ask not only "where was this used?" but also "where else could this be transplanted and still feel new?"

## Valid Component Criteria

A valid component should satisfy the first four criteria and most of the remaining criteria, with grounding strength recorded separately:

1. It has a definable input object.
2. It has a definable output object.
3. It has an identifiable mechanism or decision rule.
4. It addresses a recognizable class of modeling problems.
5. It has a theoretical, empirical, or engineering rationale whose strength can be labeled honestly.
6. It can be abstracted beyond the original paper's task.
7. It has interpretable assumptions or conditions under which it is expected to work.
8. It has potential to be recombined with other components in future model design.
9. Its scope and transfer conditions can be stated clearly enough for another researcher to reuse it.
10. It may be a classical theorem or formal result, provided the paper uses it as a real mechanism and the result can function as a reusable source of method design.

Do not treat the following operations alone as strong components unless their role, interaction, or rationale creates an identifiable reusable mechanism:

- adding an auxiliary loss;
- adding a learned scalar weight;
- concatenating two representations;
- adding a generic attention module;
- stacking more layers;
- replacing an encoder without a theoretical reason;
- minor implementation tricks.

Do not automatically reject a composition of generic operations. Retain it at the appropriate grounding level when the interaction pattern, placement, schedule, or control logic is itself reusable. Conversely, treat a classical theorem, inequality, approximation principle, or stopping rule as a potentially strong component when it genuinely drives the paper's method and can be abstracted into a reusable research primitive.

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

### Level C: Exploratory mechanism-grounded component

Mostly empirical or engineering-driven, with limited theoretical foundation but a definable reusable mechanism and explicit limitations.

Examples:

- generic auxiliary loss;
- empirical weighting;
- feature concatenation;
- plain attention fusion without a clear assumption.

However, a loss, weighting rule, regularizer, abstention mechanism, or curriculum strategy may still qualify when it encodes a clear optimization, statistical, probabilistic, or decision-theoretic principle and is reusable beyond the original benchmark.

Prioritize Level A and Level B when choosing the primary card, but use Level C to preserve transferable ideas that would otherwise be lost. Do not use Level C as a reason to skip a candidate.

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
- Complete official paper title, venue, and year if available. Use the title printed on the paper or authoritative metadata; never use a local number/filename, paper ID, component ID, shortened title, or ellipsis placeholder.
- If the card is a classical theory card, include both the current paper that operationalizes it and, when useful, note that the underlying result is classical rather than original to that paper.

#### Source-Paper Role
- Identify which decomposed candidate idea produced this card, its role in the source pipeline, and its dependencies on the other candidate ideas.

#### Evidence Anchor
- Cite the supporting section, equation, algorithm, figure, or page when available.

#### Theoretical Foundation
- List the theories or mathematical foundations.

#### Input
- Describe the required input object precisely.
- Include mathematical form and structural assumptions when possible.

#### Output
- Describe the output object precisely.

#### Core Mechanism
Explain the mechanism in 2-4 sentences. Focus on the mathematical, probabilistic, spectral, geometric, information-theoretic, or optimization principle. Do not summarize the full model pipeline.

#### Suitable Problem Types
- List the modeling problems this component can address.
- Prefer transfer-oriented problem types rather than only the source paper's original task.
- For task-specific method papers, include plausible cross-domain or cross-task applications where reusing the idea would still be innovative.
- For foundational theory papers, freely enumerate concrete downstream problems that the principle could plausibly improve.

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

If the component is meaningfully distinct in mechanism, role, assumptions, interface, or transfer pattern:

- create a new component ID;
- add a new component card;
- update all relevant indexes.

When a repository screen yields useful information, also update the changelog with a compact note such as:

- paper had no GitHub link;
- paper had a GitHub link but the repo was empty or non-Python;
- paper had a valid Python code repository and the PDF was copied to `havecode`.

For every processed paper, also record the candidate idea count and disposition summary, for example: `3 candidates: C014 created; C006 updated with a variant; one rejected as task-specific.`

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
- Focus on reusable mechanisms and decision rules; use grounding levels to distinguish formal theory from empirical engineering.
- Decompose every paper into 2-3 candidate ideas before evaluating it. Do not evaluate the paper as one indivisible unit.
- If a component depends on a strong assumption, state it clearly.
- Keep each component card compact but complete. Here, compact means non-redundant; it does not authorize merged headings, omitted fields, telegraphic fragments, or a batch-specific abbreviated schema.
- Treat repository-screen claims conservatively. Do not call a repo valid unless you have checked that it is paper-matched, non-empty, and Python-based.
- Do not confuse paper novelty with card worthiness: a card may be valuable because it captures a reusable classical theorem or formal principle that the paper operationalizes.

## Encoding and Bilingual Integrity

- Read and write every Markdown, TSV, CSV, and JSON artifact explicitly as UTF-8; never rely on the active Windows code page.
- For user-facing Markdown and tabular ledgers on Windows, prefer UTF-8 with BOM (`utf-8-sig`) so PowerShell, Excel, and common editors detect the encoding reliably.
- Preserve English and Chinese files as separate artifacts with identical card-ID sets and scope dispositions.
- When both language versions are being maintained, every new or updated card must have the same field set, evidence anchors, grounding level, conditions, failure boundaries, and reuse content in both languages. Translation may be idiomatic, but the Chinese version must not be a shortened digest of the English version, and neither version may merge required fields.
- Before reporting completion, decode every generated text artifact as UTF-8, assert that it contains no Unicode replacement character (`U+FFFD`), and scan for common mojibake fragments.
- Prefer ASCII hyphens and arrows (`2-3`, `->`) in workflow instructions and machine-maintained fields when typographic punctuation offers no semantic benefit.

## Recommended User Command

The user can invoke this skill with a command like:

```text
Use the IdeaFoundry skill. Read all PDF papers in [folder path], decompose each paper into 2-3 candidate ideas before evaluation, retain reusable components at calibrated grounding levels, and update idea_foundry_library.md. Do not create one file per paper. Deduplicate similar components and update the indexes.
```

If the user also wants code-backed paper collection, a recommended command is:

```text
Use the IdeaFoundry skill. Read all PDF papers in [folder path], screen each paper for a GitHub repository before extraction, confirm whether the repo is non-empty and Python-based, copy qualifying PDFs into havecode, then extract theory-grounded method components and update idea_foundry_library.md.
```

