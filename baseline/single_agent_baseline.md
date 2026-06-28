# Single-Agent Baseline Comparison

## Baseline Setup

The baseline uses one generic prompt:

> Please create a 60-second promotional video plan for NUTN CSIE, including script, storyboard, subtitle, and review.

## Baseline Output Summary

A single-agent response can quickly produce a script and storyboard, but it tends to mix planning, writing, visual design, and review in one step. This makes the process harder to audit and harder to revise.

## Comparison

| Item | Single-Agent Baseline | Multi-Agent Workflow |
|---|---|---|
| Role separation | Weak. One agent does everything. | Strong. Planner, Script, Visual, Reviewer, and Finalizer each have distinct responsibilities. |
| Handoff traceability | Low. Intermediate reasoning is not structured. | High. Each step is saved as JSON in `handoff/`. |
| Error checking | Easy to miss copyright or truthfulness risks. | Reviewer Agent explicitly checks length, truthfulness, copyright, portrait rights, and privacy. |
| Zero-paid-token feasibility | Possible, but not clearly documented. | Explicitly documented through mock/stub outputs and local Python video generation. |
| Revision control | Hard to isolate which part should be fixed. | Specific agent outputs can be revised independently. |
| Report evidence | Usually only final text. | Agent prompts, handoff JSON, trace, baseline, asset sources, and video are all preserved. |

## Conclusion

The multi-agent workflow is better for this assignment because the grading emphasizes controlled workflow design, structured handoff, execution trace, baseline comparison, safety, and reproducibility. The final video is not only a media output; it is also supported by auditable process evidence.
