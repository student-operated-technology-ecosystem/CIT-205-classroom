#!/usr/bin/env python3
"""Build reviewable fictional CIT-205 exemplary Word documents and distinct HTML detail pages."""
from pathlib import Path
from docx import Document
from docx.shared import Inches, Pt, RGBColor
from docx.enum.text import WD_ALIGN_PARAGRAPH
from docx.enum.table import WD_TABLE_ALIGNMENT
from html import escape
import json

ROOT=Path("examples/exemplary-portfolio")
DEST=ROOT/"artifacts"
DEST.mkdir(parents=True,exist_ok=True)

# Every scenario is fictional. Model how technicians document evidence; never
# represent these generated records as observations of a real student or asset.
DATA=[
("workstation-validation","Workstation Validation Report","ACE-NH-001 / WV-026","Pass after approved remediation",
["Scope | Validate authorized lab workstation ACE-NH-001 for boot, login, network, peripherals, endpoint protection, and browser access.",
"Baseline | Boot: 48 seconds (target under 90); sign-in: PASS; gateway ping: 4/4; endpoint protection: enabled; updates: no pending reboot.",
"Finding | DNS query for the approved training host timed out while the gateway remained reachable. Treat this as a DNS symptom, not a proven root cause.",
"Evidence | WV-026-E01 baseline checklist; E02 sanitized pre-change lookup; E03 change approval; E04 post-change validation. References are hypothetical.",
"Remediation | With approval CHG-DEMO-021, recorded prior adapter values, restored approved DNS configuration, and retained rollback notes.",
"Verification | Name lookup succeeded, test website loaded, and unaffected checks remained PASS. Technician: Alex Morgan; instructor review recorded as fictional."],
["TEST","EXPECTED","OBSERVED","RESULT"],[["Startup","Desktop within 90 sec","48 sec","PASS"],["Gateway","Successful response","4/4 replies","PASS"],["DNS lookup","Training host resolves","Timed out before change","FAIL → PASS"],["Browser","Training page renders","Rendered after retest","PASS"]]),
("server-validation","Server Validation Report","LAB-SRV-02 / SV-014","Conditional pass; storage risk escalated",
["Objective | Assess authorized training server health without unapproved changes to production services.",
"Scope | Read-only verification of service availability, logical volumes, scheduled patches, network interface, backup metadata, and open monitoring alerts.",
"Observed | Core application healthy; root volume 31% free; dedicated log volume 9% free against a 20% threshold.",
"Risk | Reduced log-volume capacity could interrupt logging and service continuity. A completed backup job is not equivalent to restore validation.",
"Change control | Opened DEMO-CHG-033 for storage remediation and DEMO-TKT-227 for patch planning. No log deletion or restart performed.",
"Handoff | Server remains operational with an open condition. Storage retest and restore exercise require separate approval."],
["CONTROL","BASELINE","RESULT","STATUS"],[["Service","Responsive","Responding","PASS"],["Root disk",">=20% free","31% free","PASS"],["Log disk",">=20% free","9% free","FLAG"],["Backup","Recent completed","Completed; restore untested","CONDITIONAL"]]),
("phone-support-ticket","Phone Support Ticket","HD-1042","Resolved with caller confirmation",
["Intake | 09:12 inbound call from anonymous Student A; single shared workstation sign-in failed before a lab session.",
"Impact & priority | One user temporarily blocked; no evidence of service-wide outage. Priority P3; scope recorded before attempting remediation.",
"Call script | 'I can help. What exactly appears on the screen? Please keep your password private. May we check your keyboard settings together?'",
"Investigation | At 09:14 recorded non-sensitive error; 09:16 confirmed account worked on authorized comparison device; 09:18 noticed alternate keyboard layout.",
"Resolution | Guided caller to expected layout without ever seeing password. At 09:22 student successfully signed in and confirmed access.",
"Closure | Category: access / sign-in / endpoint configuration. Root cause in this fictional scenario: mismatched layout. No escalation required."],
["TIME","ACTIVITY","EVIDENCE","OUTCOME"],[["09:12","Intake","Caller report","Open"],["09:16","Scope isolation","Account works elsewhere","Local symptom"],["09:18","Hypothesis","Layout indicator","Test"],["09:22","User test","Verbal confirmation","Resolved"]]),
("email-support-ticket","Email Support Ticket","HD-1048","Resolved; successful test print",
["User's message | 'My worksheet stays pending. I'm not sure if anyone else can print.' This anonymized text is a fictional support scenario.",
"Acknowledgment | 'Thanks for reaching out. I understand this is delaying your classwork. Please confirm the printer name and any non-sensitive error displayed. Do not send passwords or private documents.'",
"Triage | Verified the shared training printer was reachable and printed from another device. Narrowed scope to the requesting workstation.",
"Investigation | Found paused local job. Asked permission before removing the requestor's own failed job. Did not modify shared printer settings.",
"Resolution | Recreated a non-sensitive test job. Page printed normally. Requestor confirmed printing and received plain-language closure email.",
"Follow-up | 'If this recurs, please record the printer name, time, and exact message.' Status: resolved."],
["STAGE","COMMUNICATION","WHY IT MATTERS","REVIEW"],[["Acknowledgment","Clear next step","Sets expectation","PASS"],["Investigation","Consent sought","Limits impact","PASS"],["Resolution","Explains fix","Supports self-help","PASS"]]),
("knowledge-base-article","Knowledge Base Article","KB-017 / Rev 1.2","Reviewed technician procedure",
["Article metadata | Title: Diagnose DNS name-resolution failures. Category: Networking / Client Connectivity. Audience: entry-level service desk technicians. Owner: CIT-205 learning KB.",
"Symptoms | Device can communicate with an approved IP endpoint but cannot open a training website by hostname. Record exact error, time, and whether issue affects one or many users.",
"Safety & prerequisites | Authorized workstation and terminal. Do not collect passwords. Do not alter production DNS or firewall settings without change approval.",
"Procedure 1 | Record affected application and scope. Check local link status and assigned address; distinguish wired/Wi-Fi state.",
"Procedure 2 | Test gateway connectivity. Test approved IP endpoint. Perform a DNS lookup of an approved training hostname; capture sanitized outputs.",
"Procedure 3 | Compare observed resolver configuration against published approved baseline. If unauthorized or broad outage, stop and escalate.",
"Procedure 4 | Only with approval, restore authorized configuration, keep rollback record, repeat all tests, and obtain user confirmation.",
"Expected results | Working IP path plus failed hostname lookup suggests DNS investigation; simultaneous failure suggests wider connectivity issue; one-host failure suggests host-specific issue.",
"Escalation & rollback | Escalate multiple impacted devices, inconsistent authoritative DNS, unauthorized settings, or unsuccessful remediation. Restore original approved values on rollback."],
["STEP","EXPECTED SIGNAL","IF NOT OBSERVED","EVIDENCE"],[["Gateway reachability","Replies","Inspect local path","Ping log"],["IP connectivity","Response","Check route/service","Test log"],["DNS lookup","Name resolves","Compare resolver","Lookup output"],["Application test","Page loads","Escalate service issue","User confirmation"]]),
("troubleshooting-decision-tree","ACE Troubleshooting Decision Tree","ACE-DT-006","Evidence-led web access triage",
["Start condition | Report: 'I cannot open the training website.' Capture URL, exact message, affected users, time, and device state.",
"Decision A | Can other known websites open? YES: isolate the target site. NO: check link, IP configuration, gateway, and broader network.",
"Decision B | Can the approved target IP be reached? YES and name fails: investigate DNS path. NO: investigate route, service, or filtering with approved diagnostics.",
"Decision C | Does a different approved device reproduce the symptom? YES: escalate as possible shared service issue. NO: continue authorized local device investigation.",
"Stop conditions | Unknown authorization, suspected security incident, change needed outside scope, or multiple impacted users: stop and escalate.",
"Close condition | Reproduce initial failure, document hypothesis and test, perform approved fix, retest, confirm with user, and provide rollback notes.",
"Evidence trail | Record observed signals and precise branch selected. Decision branches are hypotheses until supported by testing."],
["DECISION","YES PATH","NO PATH","RECORD"],[["Other sites load?","Target-specific","Local/network","Browser test"],["Target IP works?","DNS investigation","Routing/service","IP response"],["Other device affected?","Shared issue","Local issue","Comparison"],["Fix authorized?","Proceed & retest","Escalate","Approval"]]),
("mission-proposal","Mission Proposal","ACE-MP-011","Proposed; awaits Mission Command review",
["Mission | Standardize workstation readiness validation within a fictional instructional service desk.",
"Problem | Inconsistent handoffs mean technicians cannot prove an endpoint meets the same baseline; work may be duplicated.",
"Outcome | A versioned checklist, validation record template, escalation rules, and a reviewer acceptance checklist.",
"Stakeholders | CIT-205 learners, instructor/reviewer, future support technicians. No real production authorization is asserted.",
"Method | Research existing baselines, draft checklist, pilot three training devices using two independent reviewers, record disagreements, revise, seek approval.",
"Acceptance | Two technicians independently obtain matching pass/flag decisions for three training devices; artifacts include evidence and privacy checks.",
"Dependencies | Training asset access, approved baseline, review time. Risks: oversharing credentials, unauthorized changes, inconsistent scoring.",
"Mitigation | Sanitization requirements, sign-off before changes, explicit expected vs actual, and peer-review checkpoint."],
["DELIVERABLE","MEASURE","OWNER","STATE"],[["Validation checklist","Peer-reviewed revision","Alex Morgan","Proposed"],["Three-device pilot","Matching outcomes","Two technicians","Not started"],["KB cross-reference","Working links","Documentation review","Planned"]]),
("ticket-and-knowledge-review","Ticket & Knowledge Review","REV-019","Revisions verified after peer review",
["Review scope | Evaluate fictional ticket HD-1042 and KB-017 for correctness, privacy, clarity, reproducibility, and audience suitability.",
"Finding 01 | Initial ticket described the fix but omitted user verification. Severity: moderate. Recommendation: document verbal confirmation and time.",
"Finding 02 | KB step said 'test DNS' without command objective or interpretation. Severity: moderate. Recommendation: specify expected and unexpected results.",
"Revision | Ticket closure updated with validation at 09:22. KB expanded to distinguish an IP path problem from hostname lookup failures.",
"Retest | Second reviewer followed KB with training data, reproduced the decision sequence, and found no confidential information.",
"Approval | Training review status: accepted for exemplar use. These are fictional approval entries, not genuine production signatures."],
["ID","ISSUE","CORRECTION","STATUS"],[["F-01","Missing user validation","Added test and confirmation","Closed"],["F-02","Ambiguous KB step","Added outcomes and branch logic","Closed"],["F-03","Privacy check","Anonymized identifiers","Closed"]]),
("documentation-vocabulary","Documentation Vocabulary in Context","VOC-014","Qualified: terminology correctly applied",
["Purpose | Demonstrate support terminology through contextual statements rather than a disconnected memorization list.",
"Symptom | User-observable behavior: 'The browser reports that the training hostname cannot be found.'",
"Scope | Number of impacted people/assets: 'The first report involves one workstation; other devices remain unverified.'",
"Baseline | Documented expected state: 'The approved resolver should return the published training host.'",
"Reproduction | Repeatable series: 'The same lookup fails on two runs under the recorded conditions.'",
"Evidence | Observable record: 'The sanitized lookup log includes command, time, and resulting error.'",
"Workaround | Temporary restoration: 'A permitted alternative endpoint permits work to continue, but does not resolve root cause.'",
"Root cause | A confirmed mechanism supported by evidence, not a guess. If not confirmed, explicitly label it unconfirmed.",
"Escalation | Transfer when authority or expertise is exceeded, carrying the symptom, scope, evidence, and attempted steps.",
"Validation | Confirming the change delivered the expected result. Rollback | Defined way to restore prior approved state."],
["TERM","MISUSE TO AVOID","PROFESSIONAL USE","CHECK"],[["Root cause","Guess labeled fact","Mark unconfirmed","PASS"],["Resolved","Action only","Attach successful retest","PASS"],["Escalated","No context","Supply evidence and impact","PASS"]]),
("github-evidence","GitHub Collaboration Evidence","GIT-018","Version history demonstrates improvement",
["Repository purpose | Curated public evidence; fictional examples must not be confused with production change records.",
"Commit convention | Descriptive verbs and scope, such as 'Clarify DNS test outcomes in KB-017', rather than 'update'.",
"Revision story | Draft KB-017, receive reviewer note about ambiguous branch, revise decision logic, request second review, and accept completed example.",
"Professional conduct | Every pull request includes what changed, why, how it was validated, and whether sensitive data was reviewed.",
"Traceability | A README maps portfolio artifact titles to visible files and revisions. Proof links must point to actual commits when students publish real work.",
"Privacy & boundaries | Never place credentials, students' identifiers, private tickets, internal addresses, or proprietary materials into public commits."],
["VERSION","CHANGE","REVIEW COMMENT","RESULT"],[["v1.0","Initial procedure","Branch ambiguity","Needs revision"],["v1.1","Expected results added","Privacy scan","Ready for review"],["v1.2","Escalation clarified","Acceptance check","Approved model"]]),
("resume","Professional Resume","Alex Morgan | Career evidence","Fictional resume for teaching",
["ALEX MORGAN | Entry-Level IT Support Candidate | Portfolio: this fictional example. Do not treat this as a real person's resume.",
"PROFILE | Service-oriented technical learner able to isolate symptoms, validate endpoints, write repeatable procedures, and communicate support outcomes.",
"TECHNICAL CAPABILITIES | Windows workstation readiness checks; DNS and basic connectivity triage; incident documentation; knowledge base writing; GitHub change history; privacy-aware support.",
"SELECTED PROJECT | Endpoint Readiness Validation: drafted and tested a structured checklist with before/after evidence; documented an approved training DNS correction.",
"SELECTED PROJECT | Knowledge Base KB-017: authored service-desk procedure with expected/actual outcomes, safe escalation, and rollback guidance.",
"SELECTED PROJECT | Support Communication: documented phone and email intake, user impact, consent, verification, and clear closure.",
"EDUCATION | CIT-205 Help Desk & User Support (fictional course demonstration). Replace with actual institution, program, and dates before using a real resume.",
"PROFESSIONAL PRACTICE | Claims should always match artifacts that a potential employer can inspect. Avoid fabricated metrics or certifications."],
["CAPABILITY","PORTFOLIO EVIDENCE","STATUS","NOTE"],[["Troubleshooting","ACE-DT-006","Model","Branches verified"],["Documentation","KB-017","Model","Peer reviewed"],["Client support","HD-1042 / 1048","Model","User focused"]]),
("linkedin-profile","LinkedIn Profile Plan","Alex Morgan | Digital identity","Example profile text and verification checklist",
["HEADLINE | IT Support Student | Service Desk & Documentation | Troubleshooting with Evidence.",
"ABOUT | 'I approach IT support by documenting symptoms, narrowing scope, testing carefully, and confirming results with people. My portfolio shows how I learn, practice, operate, and qualify.'",
"FEATURED | Link to public portfolio homepage. Feature the strongest reviewed validation record, KB article, and support communication artifact.",
"EXPERIENCE | Present authentic academic mission work accurately as projects, not as paid work or production ownership when it was not.",
"SKILLS | Incident triage; technical writing; Windows endpoint validation; network diagnostics; GitHub collaboration; professional communication.",
"PRIVACY | Choose appropriate visibility, avoid student ID numbers, verify images have permission, and use professional contact channels.",
"PROFILE REVIEW | Check that headline matches resume, links open on mobile, descriptions reflect evidence, and no certifications are falsely claimed."],
["SECTION","EXAMPLE","LINKED EVIDENCE","STATUS"],[["Headline","Support + evidence","Portfolio","Ready"],["Featured","Strongest artifacts","KB-017, WV-026","Ready"],["About","Plain-language goals","Reflection","Ready"]]),
("portfolio-reflection","Professional Reflection","LEARN → PRACTICE → OPERATE → QUALIFY","Evidence-focused learning narrative",
["LEARN | I learned to separate symptoms from cause, to record expected versus observed behavior, and to recognize when change authority matters.",
"PRACTICE | My first support records described the action but missed the test that confirmed success. A peer review revealed the evidence gap.",
"OPERATE | In a simulated support workflow I recorded the user's impact, gathered non-sensitive evidence, performed authorized checks, and closed only after verification.",
"QUALIFY | I can now explain a troubleshooting choice, show a reviewed KB procedure, walk through a redacted validation report, and describe how feedback improved the work.",
"BEFORE AND AFTER | Before: 'Changed DNS and fixed problem.' After: 'Gateway reachable, lookup failed, approved DNS restored, lookup and application both revalidated.'",
"NEXT TARGET | Improve accessibility for the KB reader, reduce ambiguity in decision trees, and collect stronger peer review evidence.",
"PORTFOLIO INTEGRITY | These are fictional model reflections. Real students must replace them with specific claims supported by their own work."],
["STAGE","EVIDENCE","WHAT CHANGED","NEXT STEP"],[["Learn","Vocabulary & KB","Define signals","More precise tests"],["Practice","Peer review","Better expected results","Iterate"],["Operate","Validation & tickets","User confirmation","Consistency"],["Qualify","Public portfolio","Traceable evidence","Interview demo"]]),
]

CSS="""*{box-sizing:border-box}body{margin:0;background:#101827;color:#edf3fa;font:17px/1.6 system-ui,-apple-system,Segoe UI,sans-serif}a{color:#9bddff}a:focus-visible{outline:3px solid #fff;outline-offset:4px}header,main,footer{max-width:1030px;padding:24px;margin:auto}.topnav{display:flex;flex-wrap:wrap;gap:20px}h1{font-size:clamp(2.2rem,5vw,3.7rem);line-height:1.12}h2{color:#a9dcfc}.eyebrow{color:#c2d6ea;letter-spacing:.06em;text-transform:uppercase;font-size:.83rem}.grid{display:grid;grid-template-columns:repeat(auto-fit,minmax(min(100%,290px),1fr));gap:18px}.card{background:#1d2c40;border:1px solid #496178;border-radius:16px;padding:22px}.card h2{margin-top:0;font-size:1.3rem}.card a{display:inline-block;margin-top:12px}.buttons{display:flex;flex-wrap:wrap;gap:18px;padding:18px 0}.note{background:#24344a;padding:18px;border-radius:12px}footer{border-top:1px solid #42556d;color:#bbcad9}"""

def cellshade(cell):
    tcpr=cell._tc.get_or_add_tcPr()
    shade=OxmlElement("w:shd");shade.set(qn("w:fill"),"E8F2FB");tcpr.append(shade)
from docx.oxml import OxmlElement
from docx.oxml.ns import qn

def build_doc(item):
    slug,title,ref,state,sections,cols,rows=item
    d=Document()
    sec=d.sections[0];sec.top_margin=Inches(.74);sec.bottom_margin=Inches(.67);sec.left_margin=Inches(.82);sec.right_margin=Inches(.82)
    normal=d.styles["Normal"];normal.font.name="Aptos";normal.font.size=Pt(10);normal.font.color.rgb=RGBColor(27,44,66)
    normal.paragraph_format.space_after=Pt(7)
    for style in ("Title","Heading 1","Heading 2"):
        d.styles[style].font.name="Aptos Display"
        d.styles[style].font.color.rgb=RGBColor(15,62,102)
    head=sec.header.paragraphs[0];head.text="CIT-205  |  PROFESSIONAL ARTIFACT EXAMPLE  |  FICTIONAL DATA";head.style="Caption"
    foot=sec.footer.paragraphs[0];foot.text="Alex Morgan (fictional)  •  Student-Operated Technology Ecosystem  •  Instructor model, not operational evidence"
    foot.style="Caption"
    d.add_heading(title,0)
    d.add_paragraph(ref,style="Subtitle")
    d.add_paragraph(f"AUTHOR  Alex Morgan (fictional)     REVIEW  Instructor demonstration     STATUS  {state}")
    d.add_heading("Purpose and assessment context",level=1)
    d.add_paragraph("A structured instructor-authored model for CIT-205. It illustrates how technical work becomes verifiable evidence. All incidents, measurements, approvals and names below are fabricated for teaching.")
    for t in sections:
        label,body=t.split(" | ",1) if " | " in t else ("Record",t)
        d.add_heading(label,level=2);d.add_paragraph(body)
    d.add_heading("Evidence and verification matrix",level=1)
    table=d.add_table(rows=1, cols=len(cols));table.style="Light Shading Accent 1"
    for i,c in enumerate(cols):table.rows[0].cells[i].text=c
    for row in rows:
        cells=table.add_row().cells
        for i,v in enumerate(row):cells[i].text=v
    d.add_page_break()
    d.add_heading("Reviewer handoff and quality assurance",0)
    d.add_paragraph(f"Document: {ref} | Revision: 1.2 | Classification: public instructional example")
    d.add_heading("Acceptance checklist",level=1)
    for line in [
        "☐ Relevant user / system impact is defined without publishing confidential information.",
        "☐ Expected outcomes are distinguished from the technician's actual observations.",
        "☐ Every conclusion is supported by a specific test or appropriate evidence reference.",
        "☐ Changes are authorized, reversible when appropriate, and documented.",
        "☐ Closure includes verification, remaining risk, escalation, and reviewer disposition.",
        "☐ Accessible language is used; screenshots and supporting files are safe for public release."
    ]:d.add_paragraph(line,style="List Bullet")
    d.add_heading("Evidence register (model references)",level=1)
    for label in ["01 | Initial report or baseline","02 | Troubleshooting observations","03 | Change / review / authorization notes","04 | Final validation and user confirmation"]:
        d.add_paragraph(f"{ref} E-{label}. Synthetic exhibit reference, supplied to model documentation. Students replace with genuine, redacted records.")
    d.add_heading("Instructor review",level=1)
    d.add_paragraph("What works: the record captures context, action, evidence and outcome. Before qualifying real student work, reviewers must inspect supporting artifacts and verify that any technical claim or metric is true.")
    d.add_paragraph("Fictional review disposition: EXEMPLAR APPROVED FOR TEACHING ONLY.")
    d.add_heading("Reflection and next action",level=1)
    d.add_paragraph("The value of this artifact is not the final checkbox; it is the trace from an observed symptom through a defensible decision to validated results. A real student should explain one revision made after feedback and link the relevant commit.")
    d.save(DEST/(slug+".docx"))

def layout(body,title,root=""):
    return f'''<!doctype html><html lang="en"><head><meta charset="utf-8"><meta name="viewport" content="width=device-width,initial-scale=1"><title>{escape(title)} | Alex Morgan</title><link rel="stylesheet" href="{root}portfolio.css"></head><body><header><nav class="topnav"><a href="{root}index.html">← Portfolio home</a><a href="{root}index.html#artifacts">All artifacts</a><a href="https://github.com/student-operated-technology-ecosystem/CIT-205-classroom">CIT-205 GitHub</a></nav></header><main>{body}</main><footer>Alex Morgan is fictional. All example findings and approval records are synthetic teaching materials.</footer></body></html>'''

( ROOT/"portfolio.css").write_text(CSS)
cards=[]
for item in DATA:
    slug,title,ref,state,sections,cols,rows=item
    build_doc(item)
    desc=sections[0].split(" | ",1)[-1]
    cards.append(f'<article class="card"><p class="eyebrow">{escape(ref)}</p><h2>{escape(title)}</h2><p>{escape(desc)}</p><a href="artifacts/{slug}.html">Explore artifact →</a></article>')
    sec_html="".join(f'<section class="card"><h2>{escape(s.split(" | ",1)[0])}</h2><p>{escape(s.split(" | ",1)[1] if " | " in s else s)}</p></section>' for s in sections)
    heads="".join(f'<th scope="col">{escape(x)}</th>' for x in cols)
    trs="".join("<tr>"+"".join(f"<td>{escape(v)}</td>" for v in r)+"</tr>" for r in rows)
    content=f'<p class="eyebrow">{escape(ref)}</p><h1>{escape(title)}</h1><p>{escape(state)}</p><div class="note"><strong>Actual formatted Word document</strong><p>Open or download the multi-page formatted PDF. The webpage below is a readable preview of its contents.</p><div class="buttons"><a href="{slug}.pdf">Open full PDF ↗</a><a href="{slug}.pdf" download>Download PDF ↓</a></div></div><h2>Document contents</h2>{sec_html}<h2>Evidence and verification</h2><div style="overflow-x:auto"><table border="1" cellpadding="9"><thead><tr>{heads}</tr></thead><tbody>{trs}</tbody></table></div><p class="note">Review and quality-assurance checklist are included on page two of the downloadable PDF document. All sample records are fictional.</p>'
    (DEST/(slug+".html")).write_text(layout(content,title,"../"))
home=f'''<p class="eyebrow">CIT-205 | FICTIONAL INSTRUCTOR PORTFOLIO</p><h1>Alex Morgan</h1><p>Entry-level IT support professional | Service Desk • Troubleshooting • Documentation • Validation</p><p class="note"><strong>Teaching model, not a real student.</strong> Explore thirteen complete, editable Word documents. Every artifact has its own page and a download link. Students must publish their own authentic, safely redacted evidence.</p><h2>Professional introduction</h2><p>I make support problems observable, repeatable, and solvable. My work emphasizes careful validation, clear communication, traceable evidence, and responsible changes.</p><h2 id="artifacts">Artifact library</h2><div class="grid">{''.join(cards)}</div><h2>Professional growth</h2><p>LEARN → PRACTICE → OPERATE → QUALIFY. The work is demonstrated by a collection of technical and communication artifacts, not a disconnected final exam.</p>'''
(ROOT/"index.html").write_text(layout(home,"Example IT Support Portfolio"))
print(f"Generated {len(DATA)} individual PDF artifacts and {len(DATA)} artifact webpages.")
