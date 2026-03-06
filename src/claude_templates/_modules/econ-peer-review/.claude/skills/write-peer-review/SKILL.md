---
name: write-peer-review
description: "Use this skill when writing a peer review or referee report for an economics paper. Invoke when the user mentions reviewing a paper, writing a referee report, assessing identification, or evaluating a submission — even if they just say 'review this paper' or 'what are the issues with this paper'."
---

# Write Peer Review

## When to Use

**Perfect for:**
- Writing a structured referee report for a journal submission
- Evaluating identification strategy, robustness, and contribution of an economics paper
- Organizing feedback on a working paper or thesis draft
- Responding to a referee report (tracking issues, drafting a response letter)

**Not ideal for:**
- Proofreading or copyediting only (that's a style check)
- Summarizing a paper without evaluation (use a reading note)
- Writing your own paper (use write-econ-paper skill instead)

---

> **Core Philosophy:** A good review identifies problems and suggests how to fix them. It is honest, constructive, and specific — with numbers, not vague adjectives. Criticize the paper, not the authors. The goal is to help the editor decide and help the authors improve.

## CRITICAL

1. **Every major issue must include what, why, and how to fix.** "The identification is weak" is not a review comment. "The parallel trends assumption fails because the pre-trend coefficient at t=-3 is -0.184 (s.e. = 0.149), large relative to the ATT of 0.145. The authors should show robustness to excluding this cohort or using an estimator that allows for differential pre-trends" is a review comment.
2. **Do not conflate minor and major issues.** A table formatting problem is not a reason to reject. An identification failure is not a minor comment. Misclassifying issues signals an unreliable review.
3. **The summary must be evaluation-free.** Restate the paper's question, method, and finding in your own words. If you cannot summarize the paper in one paragraph, that itself is a finding about the paper's clarity.

---

**Note on flexibility:** The structure below targets applied micro papers for top journals. Reviews for theory papers, macro papers, or field journals may need different emphasis — adapt the evaluation criteria to match the paper's contribution type.

---

## Step 1: First Read

Read the paper cover to cover without taking notes. After reading, answer:

- Can you state the research question in one sentence?
- Can you state the main finding with a number?
- Can you identify the source of identifying variation?
- Can you name the contribution relative to existing work?

If any answer is "no," that is itself a finding for the review.

## Step 2: Second Read

Read with a pen. For each section, evaluate against the relevant checklist:

### Question and Motivation

- Is the research question clearly stated?
- Is it important for economics broadly (not just the subfield)?
- Is the ex ante ambiguity clear (why is the answer not obvious)?
- Are contributions explicitly stated and genuinely novel?

### Literature Review

- Organized by mechanism/channel, not paper by paper?
- Ends with a gap statement mirroring the contributions?
- Appropriately concise (1-1.5 pages)?
- Any important missing papers?

### Data

- All sources described with coverage, unit, key variables?
- Sample restrictions justified?
- Treatment variable precisely defined?
- Summary statistics reported and discussed?
- Potential measurement error in key variables?

### Identification Strategy

- Identifying assumption stated in plain language?
- Assumption credible in this setting? What are the threats?
- Estimator appropriate for data structure?
- Standard errors clustered at the right level?
- For DiD: pre-trends shown and discussed? Staggered TWFE acknowledged?
- For IV: first stage reported? Exclusion restriction plausible?
- For RDD: bandwidth justified? Manipulation tests shown?

### Results

- Main estimates reported with standard errors?
- Economic magnitude discussed?
- Event-study plots shown?
- Robustness checks sufficient and genuine (not cosmetic)?

### Heterogeneity and Mechanisms

- Splits on predetermined variables? Labeled as descriptive?
- Mechanisms distinguished from heterogeneity?
- Theoretical framework for the channel?
- Null results discussed?

## Step 3: Write the Summary

One paragraph. Restate:
1. The research question
2. The data and setting
3. The identification strategy
4. The main finding (with the headline number)
5. The claimed contribution

No evaluation. Just description. This signals you understood the paper.

## Step 4: Write the Overall Assessment

1-2 paragraphs. Be direct:
- Is the contribution sufficient for the target journal?
- Main strength (novel data, clean identification, important question, new mechanism)
- Main weakness (identification concern, limited external validity, incomplete analysis)

Be specific: "The paper is publishable in JDE conditional on addressing the identification issues in Section 4" is better than "The paper has some interesting results but also some concerns."

## Step 5: Write Major Issues

3-5 issues maximum. For each:

1. **What** the problem is (stated precisely, with page/table references)
2. **Why** it matters for the paper's conclusions
3. **How** to fix it (if you have a suggestion)

### Evaluating Specific Designs

**DiD:** Is treatment timing exogenous? Staggered TWFE vs. modern estimators? Pre-trends flat? SUTVA plausible? Check Bacon decomposition, event-study coefficients, robustness to control group definition.

**IV:** Exclusion restriction plausible? Instrument strong (F > 10)? LATE interpretation sensible? Check first stage, reduced form, overidentification tests.

**RDD:** Running variable continuous? Manipulation evidence? Bandwidth sensitivity? Check McCrary test, covariate balance at cutoff, polynomial/bandwidth robustness.

**Poisson/count data:** Conditional mean correct? Many zeros? Avoids log(1+Y)? Uses FE Poisson (not FE NegBin)?

## Step 6: Write Minor Issues

Problems that should be fixed but don't threaten the core contribution:
- Unclear exposition in specific paragraphs
- Missing variable definitions
- Table formatting issues
- Citations to add or correct
- Inconsistencies between text and tables

## Step 7: Write the Recommendation

State clearly:

| Recommendation | When |
|----------------|------|
| **Accept** | Rare on first submission. Paper is ready. |
| **Major R&R** | Contribution is there but significant work needed (identification, missing analyses) |
| **Minor R&R** | Paper is close — fix specific issues |
| **Reject** | Fundamental problems with question, identification, or contribution that revision cannot fix |

## Step 8: Review Your Review

Before submitting:
- Is the tone constructive? Would you be comfortable receiving this review?
- Are major issues genuinely major, and minor issues genuinely minor?
- Have you suggested fixes, not just identified problems?
- Have you been specific (numbers, page references) rather than vague?
- Have you avoided asking for a different paper?

## Output

Deliver a structured referee report:

```markdown
## Summary

[One paragraph: question, method, finding, contribution — no evaluation]

## Overall Assessment

[1-2 paragraphs: main strength, main weakness, direct judgment]

## Major Issues

### 1. [Issue Title]

**Problem:** [What, with page/table reference]
**Impact:** [Why it matters for conclusions]
**Suggestion:** [How to fix]

### 2. [Issue Title]
...

### 3. [Issue Title]
...

## Minor Issues

- [p.X] [Comment]
- [Table Y] [Comment]
- [Section Z] [Comment]

## Recommendation

[Accept / Major R&R / Minor R&R / Reject — with one-sentence justification]
```

When tracking a revision response:

```markdown
## Referee Report Response Tracker

| # | Comment | Status | Response | Section |
|---|---------|--------|----------|---------|
| 1 | [Summary of referee comment] | [OPEN/IN PROGRESS/DONE] | [Your response] | [Paper section] |
```

Priority order: identification → missing analyses → structure → presentation → style → typos → citations

## Checklist

- [ ] Paper read twice (first: impression; second: detailed notes)
- [ ] Summary restates question, method, finding, contribution — no evaluation
- [ ] Overall assessment names main strength and main weakness specifically
- [ ] Major issues limited to 3-5, each with what/why/how
- [ ] Major issues are genuinely major (identification, missing analysis, interpretation)
- [ ] Minor issues are genuinely minor (exposition, formatting, citations)
- [ ] Recommendation is clear and justified
- [ ] Tone is constructive — criticizes paper, not authors
- [ ] Specific numbers cited where relevant (coefficients, SEs, F-stats)
- [ ] No demands for a different paper or infeasible analyses
- [ ] Review sat overnight before submission (tone check)
