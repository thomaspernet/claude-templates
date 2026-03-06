# Heterogeneity and Mechanisms

> Conventions from AER, QJE, JDE, JIE, RESTUD for applied micro papers.

## The Distinction

Heterogeneity and mechanisms are often conflated. They are distinct sections with different purposes:

- **Heterogeneity** shows *who* responds. It is **descriptive**, not causal (unless the heterogeneity dimension is itself exogenous).
- **Mechanisms** show *why* the effect exists. This is the theoretical contribution.

Example:

- Heterogeneity: "Large firms respond, small firms do not."
- Mechanism: "Large firms respond *because they have higher internal cash flow*, which enables self-financing of R&D."

The mechanisms section provides evidence for the "because" claim.

## Heterogeneity

### Purpose

Heterogeneity analysis identifies correlates of the treatment response. It answers "who is affected?" and "where is the effect strongest?"

### Rules

1. **Split on predetermined variables only.** The splitting variable must be measured before treatment. Never split on post-treatment outcomes — this introduces selection bias.
2. **State explicitly that splits are descriptive.** Use language like: "These splits are descriptive and identify correlates of the response, not causal mechanisms."
3. **Motivate each split theoretically.** Discuss the economic logic before showing results. Why would you expect the effect to differ across this dimension?
4. **Report ATTs for each subgroup with standard errors.** Don't just report whether the interaction term is significant — show the estimated effect for each group.
5. **Discuss null results.** The absence of an effect in a subgroup is informative. Don't skip it.
6. **Connect to the mechanisms section.** Heterogeneity results should motivate and set up the mechanisms analysis that follows.

### Common Mistakes

- Splitting on too many dimensions without theoretical motivation (data mining)
- Not discussing what the absence of an effect in a subgroup means
- Treating heterogeneity as mechanisms (heterogeneity shows "who," not "why")
- Splitting on post-treatment variables (endogenous)
- Running dozens of interaction terms and only reporting the significant ones

## Mechanisms

### Purpose

Mechanisms analysis provides evidence for **why** the treatment effect exists. It identifies the theoretical channel through which the treatment operates. This is often the most intellectually demanding part of the paper.

### Structure

1. **Open with a topic paragraph** explaining what the mechanisms analysis adds beyond heterogeneity
2. **State the hypothesis before the test.** "If the effect operates through financial constraints, we expect a stronger response among firms with higher cash flow."
3. **Explain operationalization.** How do you measure the proposed channel? (proxy variable, sample split, interaction, mediation)
4. **Report results** and interpret in terms of the theoretical channel
5. **Report null mechanisms.** Channels that do *not* work are informative. Showing which mechanisms fail strengthens the paper by ruling out alternatives.

### Distinguishing from Heterogeneity

| Heterogeneity | Mechanisms |
|---------------|------------|
| Large firms respond more | Large firms respond more *because* they have internal cash flow |
| Urban areas show stronger effects | The effect works through *labor market density* in urban areas |
| Descriptive — shows patterns | Analytical — provides evidence for a causal channel |
| Splits on observable characteristics | Tests a specific theoretical prediction |

### Common Mistakes

- Conflating with heterogeneity (the most common error)
- Testing too many mechanisms without a clear theoretical framework
- Not reporting null mechanisms (which mechanisms do not work)
- Not explaining how the mechanism is operationalized
- Claiming causal mediation without appropriate methods (formal mediation analysis requires strong assumptions)

## Presentation

### In the Introduction (P5: Results)

Briefly mention the key heterogeneity and mechanism findings alongside the main estimate. One sentence each is sufficient.

### As Separate Sections

For top journals, heterogeneity and mechanisms are typically:

- **Separate sections** after the main results and robustness checks
- **Ordered**: results → robustness → heterogeneity → mechanisms → conclusion
- Each section opens with a substantive claim, not "This section examines..."

### In Tables

- Use the same format as main results tables for consistency
- Panel labels to distinguish subgroups: "Panel A: High cash flow", "Panel B: Low cash flow"
- Include the number of observations for each subgroup
- Report the p-value for the difference between subgroups if economically meaningful
