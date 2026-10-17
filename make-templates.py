import json
base='''DRAFT FOR COMPLETION AND PROFESSIONAL REVIEW — {{title}}
Version {{version}} | Status {{status}} | Effective date {{effectiveDate}}
Parties: Christina Loren Clement LLC (CLCLLC), in its documented capacity, and {{counterparty}}.
Family / entity / trust: {{connectedParty}}. Authorized representatives and capacities: {{representatives}}.

'''
end='''
GENERAL TERMS
Reserved matters, monetary thresholds and permitted signers: {{decisionLimits}}. No appointment under this agreement overrides the governing trust, company documents, applicable law or court orders. No authority to bind a beneficiary or another entity is implied.
Conflicts, related-party compensation and fiduciary capacity / acceptance: {{conflicts}}. Each party will disclose relevant conflicts before acting; any consent must be obtained from an authorized decision-maker. No blanket waiver of nonwaivable duties is intended.
Professional engagements and credential evidence: {{professionalEvidence}}. Regulated, legal, tax and custody work is performed only by appropriately authorized providers under documented engagements. Software access does not confer a license, fiduciary appointment or account signing power.
Term, termination, notice, record handover, outstanding fees and continuity: {{terminationTerms}}. Surviving confidentiality and record-retention duties: {{dataTerms}}.
Governing law and forum, subject to mandatory law: {{governingLaw}}. Dispute escalation and resolution: {{disputeProcess}}. Amendments require written approval by authorized parties; a portal edit is a draft until validly adopted.
Notices and incident contacts: {{incidentContact}}. Referenced schedules, protected instruments and approved exceptions: {{schedules}}.

SIGNATURES — execution method and authority must be checked by counsel
CLCLLC representative: __________________  Capacity: __________________  Date: __________
Counterparty representative: ____________  Capacity: __________________  Date: __________
Additional required fiduciary / board approvals: ________________________________________
'''
rows=[('services','Family Office Services Agreement','''1. APPOINTMENT AND DELIVERABLES
The client appoints CLCLLC to provide only {{services}}. Deliverables, review frequency and responsible professionals: {{deliverables}}. Excluded services and reserved client decisions: {{decisionLimits}}. Investment discretion, legal representation, tax return signing and custody require separate express authority and any necessary registrations.
2. FEES AND RESPONSIBILITIES
Fees, expenses, fee calculation, billing currency and third-party compensation: {{fees}}. Payment dates, dispute handling and any accepted LND conversion terms: {{paymentTerms}}. No LND parity declaration guarantees redemption or third-party acceptance. The client supplies accurate records, timely approvals and evidence of legal ownership; the office protects access, maintains records and reports exceptions.
3. ASSET AND DATA SEPARATION
Records and balances are maintained under the assigned family workspace. Accounts remain titled to the proper legal owner; the office does not pool family or charitable funds merely for administrative convenience. Bank / custodian arrangements: {{accountSchedule}}.
'''),('confidentiality','Confidentiality and Professional Access Agreement','''1. PURPOSE AND PERMITTED ACCESS
Confidential information may be used only for {{services}} and only for {{authorizedUsers}} in the assigned workspace and permission areas. Each user has an individual login. No shared credentials, delegation to unnamed firm staff, bulk reuse or access to another family is permitted without express authorization.
2. SECURITY, DISCLOSURE AND RETURN
Minimum necessary access, confidential / privileged records, approved sharing and retention: {{dataTerms}}. Incident reporting and access removal: {{incidentContact}}. Legal-compulsion and professional-retention exceptions require prompt notice where lawful. On termination, revoke access and return / retain / destroy records as documented; previously downloaded copies cannot be recalled by the portal.
3. EXCLUDED PERSONS
Identity-specific restrictions and permitted legal exceptions: {{exclusions}}. This clause does not purport to defeat mandatory rights, a court order or an instrument that has not been validly amended.
'''),('authority','Professional Appointment and Decision Authority Schedule','''1. NAMED APPOINTMENTS
CFO / controller: {{administrator}}. Tax professional: {{taxProvider}}. Attorney: {{legalProvider}}. Investment adviser: {{investmentProvider}}. Custodian: {{custodyProvider}}. Trustee / fiduciary firm and exact accepted capacity: {{fiduciaryProvider}}. Ghana foundation oversight: {{foundationLead}}.
2. AUTHORITY MATRIX
For each decision type, name the preparer, independent reviewer, final decision-maker, amount / currency limit and legal authority: {{decisionLimits}}. No person approves their own submission. Portal approval records do not instruct a bank, execute a trade or amend a trust. Reserved family / trustee / board decisions and emergency succession: {{schedules}}.
3. REVIEW AND LIABILITY
Engagement scope, fees, reporting and service standards: {{services}} / {{fees}} / {{deliverables}}. Professional liability / fiduciary insurance, exclusions and bonding evidence: {{insurance}}. Credential checks, renewals, disciplinary review and appointment revalidation: {{professionalEvidence}}.
'''),('separation','Family Asset and Foundation Fund Separation Agreement','''1. ACCOUNT OWNERSHIP
Separate workspaces and separately titled bank / custody accounts shall be identified in {{accountSchedule}}. Each family owns only the assets established by its own governing records. The foundation holds charitable funds for its authorized objects, subject to donor / grant restrictions, rather than private family entitlements.
2. BOOKKEEPING AND RECONCILIATION
Account chart, reconciliation cycle, statements, preparer and reviewer: {{deliverables}}. Each journal must balance by currency; LND, USD and GHS are recorded separately. Conversion, executable rates, fees and source evidence: {{paymentTerms}}. An internal entry does not establish external settlement.
3. TRANSFERS AND CONFLICTS
Inter-family, intercompany or foundation transfers require documented authority, purpose, restrictions, counterparty records and independent review: {{decisionLimits}}. Restricted charitable funds cannot be used to net private distributions. Any shared expense allocation, grant or related-party arrangement requires an approved basis and applicable professional review: {{conflicts}}.
'''),('investment','External Investment Adviser and Custody Services Schedule','''1. SEPARATE PROVIDERS
Investment adviser / registration / engagement: {{investmentProvider}}. Custodian and account titles: {{custodyProvider}} / {{accountSchedule}}. The client retains ownership and reserved decisions. CLCLLC’s administrative scope: {{services}}. No securities transaction or money movement is executed by this template or portal.
2. MANDATE, FEES AND CONFLICTS
Objectives, risk limits, liquidity, benchmarks and permitted discretion: {{investmentMandate}}. Advisory / custody fees, referral compensation and conflicts: {{fees}} / {{conflicts}}. State / SEC / broker or other licensing and any exemption analysis must be documented for the actual services and clients: {{professionalEvidence}}. A single-family exclusion must not be assumed to cover unrelated-family investment advice.
3. OVERSIGHT
Reports, custody statements, valuation sources and review frequency: {{deliverables}}. Instruction authentication, independent approvals and withdrawal limitations: {{decisionLimits}}. Complaints and escalation: {{incidentContact}}.
'''),('ghana','Ghana Philanthropic Program and Grant Agreement','''1. CHARITABLE PURPOSE AND PARTIES
Program, recipient legal identity, Ghana location and public-benefit audience: {{programDetails}}. Foundation board / authorized lead: {{foundationLead}}. Registration / licensing, constitutional objects and local professional review: {{professionalEvidence}}.
2. BUDGET AND RESTRICTIONS
Grant amount, currency, permitted uses, donor restrictions and milestones: {{grantRestrictions}}. Disbursement timing, FX evidence, receipts and unused-funds return terms: {{paymentTerms}}. Separate titled account and charitable ledger: {{accountSchedule}}. No private-beneficiary distribution or unrestricted related-party benefit is authorized by this agreement.
3. SAFEGUARDING AND REPORTING
Outcome measures, recipient diligence, procurement, safeguarding, monitoring, audit rights and reporting deadlines: {{deliverables}}. Suspension, misuse response and recoveries: {{terminationTerms}}. Local legal and tax responsibilities and sign-off: {{services}}.
'''),('venture','Future Endeavor and Operating Entity Agreement','''1. ENTITY AND SCOPE
Operator legal identity, jurisdiction, ownership / unit classes and issuance authority: {{operatorDetails}}. Venture purpose, services, milestones and success measures: {{services}} / {{deliverables}}. No missing ownership percentage or share total is implied.
2. CAPITAL, IP AND AUTHORITY
Capital commitments, actual funding, currency, distributions and loss allocation: {{paymentTerms}}. Art / IP title, licenses, preservation directives and disposition consent: {{ipTerms}}. Governing CLCLLC authority and operator reserved decisions: {{decisionLimits}}.
3. EXPANSION CONDITIONS
Required entity approvals, tax classification, professional engagements, contracts and regulatory determinations: {{professionalEvidence}}. No regulated service begins solely because this agreement is saved. Related-party arrangements and conflicts: {{conflicts}}.
'''),('legacy','Legacy Preservation and Authorized Access Acknowledgment','''1. PROTECTED BASELINES
Identify controlling trusts, constitution, art / IP directives, original file fingerprints, adopted versions and hierarchy: {{protectedRecords}}. Conflicts must be escalated to an authorized fiduciary and counsel; a portal alert does not itself determine legal validity.
2. ACCESS AND EXCLUSIONS
Named authorized people, professional capacities, beneficiary representation and limits: {{authorizedUsers}}. Identity-specific excluded people, indirect-benefit restrictions, successor provisions and lawful exceptions: {{exclusions}}. Minor-beneficiary access and guardianship must be reconciled with applicable law and executed instruments.
3. PRESERVATION AND SUCCESSION
Art custody, conservation, insurance, reproduction and disposition authority: {{ipTerms}}. Incapacity, successor appointment, emergency access, evidence retention and review cadence: {{deliverables}}. Changes to protected records require the actual instrument’s valid amendment process; this acknowledgment does not amend a trust.
''')]
json.dump([{'id':i,'title':t,'body':base.replace('{{title}}',t)+b+end} for i,t,b in rows],open('src/agreement-templates.json','w'),ensure_ascii=False)
