# Instructor Run of Show — CIT-205 GitHub Knowledge Cycle

## Class 1 — Knowledge Creation

1. Students bring questions for all six scenarios.
2. Discuss what technicians must clarify before acting.
3. Assign or approve one scenario per student.
4. Model the Knowledge Article structure.
5. Students draft in Word and submit through the course channel.

**Win condition:** every student submits one complete draft that includes verification and escalation.

## Class 2 — GitHub Onboarding and Contribution

1. Direct students to the public `CIT-205-classroom` repository.
2. Complete [Start Here](../onboarding/START-HERE.md) and the welcome issue as needed.
3. Demonstrate repository → folder → file → History.
4. Show the example article and its revision.
5. Demonstrate fork → branch → file → commit → pull request.
6. Students publish revised Markdown drafts from their forks.

**Win condition:** every student can find an article and has an open pull request or a documented blocker.

### Monday migration note

Students who already created valid Markdown in a fork of the protected `SOTE-framework` repository do **not** redo the article. They copy their completed Markdown into a new branch in a fork of `CIT-205-classroom`, commit it under `knowledge/student-articles/`, and open the pull request against `CIT-205-classroom:main`.

Use the Monday permissions failure as the architecture example: the content was valid; the contribution destination was wrong.

## Class 3 — Peer Review, Version Control, and Publication

### Opening model

Teach the lifecycle before touching buttons:

**Workspace → Proposal → Review → Accepted Knowledge → Published Knowledge → Operational Canon**

Explain the layers:

- **Personal fork / branch:** contributor workspace.
- **Pull request:** proposed organizational change.
- **Peer review:** quality control and collaborative improvement.
- **Classroom `main`:** accepted classroom knowledge.
- **SOTE Command Portal:** front-end consumption of accepted classroom knowledge.
- **SOTE Framework:** protected operational canon; promotion here requires a separate governance review.

### Wednesday sequence

1. Revisit Monday's permission challenge and explain why the classroom repository is now the correct contribution boundary.
2. Give students who started Monday a short migration window using the note above.
3. Confirm each student has a pull request targeting `student-operated-technology-ecosystem/CIT-205-classroom:main`.
4. Assign each student a peer pull request.
5. Review with the [Peer Review Checklist](../assignments/PEER-REVIEW-CHECKLIST.md).
6. Students leave actionable feedback: one strength, one gap/risk/unclear point, and one concrete improvement.
7. Authors revise the **same branch** and commit. Show that the existing pull request updates automatically.
8. Open **Files changed** and compare the revision. Green is added; red is removed.
9. Instructor validates, requests changes, or merges.
10. After the first acceptable merge, open the SOTE Command Portal Knowledge Base and find the newly accepted article there as **Classroom Accepted**.
11. Compare the pull request, merged file, GitHub History, and portal article. Ask: **Which copy is current, and how can you prove it?**
12. Close by distinguishing classroom publication from promotion to SOTE operational canon.

**Win condition:** students can explain why `main` is current, how GitHub preserves the path to it, and why a published classroom article is not automatically an authorized operational procedure.

## Access Model

Because the classroom repository is public, students can read without organization membership and contribute through personal forks. They do not receive access to the private SOTE framework or infrastructure documents. GitHub account sign-in is required to comment, fork, and open a pull request.

## Instructor Validation Gate

Before merging, verify technical accuracy, safe ordering, privacy, scope, verification, and escalation. **Merged** means Classroom Accepted and makes the article eligible for display through the classroom layer of the SOTE Command Portal. It does not automatically promote the article into operational SOTE knowledge.

## Portfolio Publication Demonstration

1. Open [**View Alex Morgan’s Live Example Portfolio**](https://student-operated-technology-ecosystem.github.io/CIT-205-classroom/examples/exemplary-portfolio/) before showing the source files. Demonstrate About, Evidence, and Reflection navigation and inspect the 13 inline artifact examples.
2. Explain that Alex Morgan and the incidents are fictional quality references. Students must curate their own reviewed, sanitized evidence.
3. Follow the [ACE Portfolio Publication Mission](../assignments/ACE-portfolio-publication-mission.md) to create each student's own template-based portfolio and enable Pages.
4. Submit and verify both the live website URL and repository URL. A GitHub source view is not the published portfolio.

### Classroom example hosting

The existing `examples/exemplary-portfolio/index.html` is published by GitHub Pages from `main` and `/(root)`. Changes committed or merged into `main` automatically trigger **pages build and deployment**; verify its build and deploy jobs under **Actions** before checking the updated live site. Preserve the folder path to keep the classroom link stable.
