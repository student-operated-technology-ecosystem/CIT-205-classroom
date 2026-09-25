# Knowledge Article Peer Review

A peer review has two views: first read the article as a technician would use it, then inspect the exact changed lines in the pull request.

## Part 1 — Read the rendered article

1. Open the assigned pull request.
2. Open the changed Knowledge Article.
3. Use the rendered **Preview** view when available so headings, lists, and sections appear as the technician will read them.
4. Read the entire article before commenting.

Ask:

### Usability

- Is the problem stated clearly?
- Are observations separated from assumptions?
- Could another technician follow the steps in order?
- Does each important branch or result tell the technician what to do next?

### Safety and Scope

- Does the article identify permissions and consent?
- Are destructive or risky steps avoided?
- Are stop and escalation conditions specific?
- Is private or identifying information absent?

### Technical Quality

- Are claims supported by the scenario, testing, course material, or cited sources?
- Does the resolution avoid pretending an untested guess is confirmed?
- Does verification prove the user-facing problem is resolved?

## Part 2 — Compare the proposed change

1. Return to the pull request.
2. Open **Files changed**.
3. For a Markdown article, use GitHub's **rich/rendered diff** control in the file header to read the change as rendered prose. This is the clearest view for understanding what was added or removed in context.
4. When you need to comment on an exact sentence or line, switch back to the normal **source diff**.
5. Find the exact line or small group of lines connected to your feedback.
6. Use GitHub's line-comment control beside that line to leave a review comment.
7. When replacement wording would help, write the proposed wording directly in the comment. If GitHub offers a **suggested change** option, you may use it for a small exact replacement.
8. Continue until your required feedback is attached to the relevant lines.
9. Submit the review when finished.

**Rendered diff = understand the article change. Source diff = comment on the exact line.**

Do not edit your classmate's branch directly. Peer review proposes changes; the article author decides how to revise the branch.

## Required Review Response

Your review must include:

1. **Strength:** name a specific section or step that works well.
2. **Concern:** identify the exact unclear, missing, unsafe, or unsupported passage.
3. **Proposed change:** supply replacement wording or an additional step.
4. **Reason:** explain how the change helps the next technician.

A useful review changes the work. “Looks good” alone does not meet the requirement.

## What happens next

The author revises the same article branch. The pull request updates automatically. Reviewers can return to **Files changed** to compare the revision, and the instructor can see the discussion and revision history before deciding whether to merge the article.
