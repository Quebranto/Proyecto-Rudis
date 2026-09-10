# 🌐 Project Rudis — Guided Tour

**Language / Idioma:** **English** · [Español](./TOUR_ES.md)

> **Welcome to Rudis. You do not need to read the whole Corpus to understand what is being built.**

This tour is designed for a first visit. Its purpose is not to teach the full architecture, but to give you enough context to decide whether you want to go deeper.

You can follow two routes:

- 👁️ **Visitor — 8–10 minutes:** understand the problem, the architecture, what could feel different when using Rudis and what the current limits are.
- 💼 **Investor / Strategic Partner — 12–15 minutes:** understand the thesis, what can be financed, what evidence matters and where investment ends and project sovereignty begins.

If you want to imagine what it would mean to enter, participate and return to Rudis as a user, continue after the tour with [Living Rudis](./LIVING_RUDIS_EN.md).

---

# 👁️ Visitor Tour

## Stop 1 — What problem is Rudis trying to solve?

Rudis is an experimental project in **constitutional architecture, distributed systems and institutional infrastructure**.

Its starting point is a very ordinary intuition: a system saying “this is true” does not mean the system has authority to make it true.

Imagine an AI agent that can send money, modify an account or act on infrastructure. It may have the technical ability to do so and still lack legitimate permission. Or imagine an application that displays someone as still holding an office because it has an old record, even though the office was revoked. The software represents a state, but that representation may be stale, incomplete or unauthorized.

Rudis is designed around preventing those confusions from becoming normal.

Its central principle is:

> **A representation of state does not acquire authority over reality merely by claiming to represent it.**

The compact formulas you will see throughout Rudis summarize that idea; they are not substitutes for explanation:

```text
CAPABILITY != AUTHORITY
IDENTITY != COMPETENCE
REPRESENTATION != AUTHORITY
```

In plain language: **being able to do something, proving who you are or appearing correctly in an interface does not by itself prove that you are entitled to cause a consequence.**

## Stop 2 — What is being built?

Rudis currently has three main product/architecture surfaces.

**StateOS** is the institutional-state architecture. It is designed to preserve a causal chain between who is acting, which claim they present, which competence must be demonstrated, what rule applies, which mandate authorizes execution, what effect occurs and what evidence remains afterward.

**RAL — Rudis Authority Layer** focuses on the most dangerous moment: when an intention is about to become a consequential action. Its question is not merely “can the agent call this tool?” but “can the system demonstrate that this actor is authorized to cause this effect now?”

**Rudis Habitat** is the habitable expression of that institutional state. It may appear through web, mobile, immersive environments, agents or APIs, but none of those windows should become sovereign simply because they are the interface you happen to be using.

A compact way to express that is:

```text
ONE CAUSAL INSTITUTIONAL STATE
-> MANY LEGITIMATE REPRESENTATIONS
```

For example, the same institutional decision could be visible through a mobile app, a web interface or a 3D environment. All three may represent the decision, but none should be able to invent it.

## Stop 3 — What makes the architecture different?

Rudis spends a lot of effort separating concepts that conventional systems often collapse together.

**Authentication and authorization are different.** You may successfully prove your identity and still lack permission for a particular action.

**A valid signature does not prove current authority.** The signature can be authentic while the mandate behind it has expired or been revoked.

**Recovering state does not mean recovering authority.** Restarting a system from an old snapshot should not resurrect dead permissions.

**A summary is not the source.** An Assembly may use a synthesis to orient itself, but the synthesis must not erase votes, dissent or primary evidence.

**Code is not a legislator.** If a political or constitutional decision is missing, the implementation should not invent it merely so the software can proceed.

That is why Rudis uses invariants such as:

```text
AUTHENTICATION != AUTHORIZATION
VALID SIGNATURE != CURRENT AUTHORITY
RECOVERED STATE != RECOVERED AUTHORITY
SUMMARY != SOURCE
CODE != LEGISLATOR
```

The point is not to memorize those lines. The point is to understand which failure classes they are trying to prevent.

## Stop 4 — What would using Rudis actually feel like?

Rudis should not feel like a collection of constitutional documents.

A participant should be able to enter and see what is alive, what changed since the last visit, which matters need attention, what can be learned, where contribution is possible and which institutions are acting.

If the participant attempts a sensitive action, the system should not merely return “success” or “403.” Rudis should be able to explain progressively **who requested the action, what authority was demonstrated, what rule applied and what mandate produced the effect**.

If an authority is no longer current, the system should be able to say so in ordinary language: “this authorization existed, but we cannot demonstrate that it is still current.”

That is the difference between architecture that lives only in diagrams and architecture turned into a usable experience.

For a deeper explanation of this layer, continue with [Living Rudis](./LIVING_RUDIS_EN.md).

## Stop 5 — What is real today?

Rudis is currently **PRE-D3**. This means architecture, a public Corpus, private implementation, tests, research and adversarial work all exist, but Rudis is not claiming to be a finished production platform.

Some properties have moved from pure theory into executable tests and independent reproduction. Even so, one component passing a test does not prove the whole system is secure, and a green build is not the same as independent accreditation.

Current public status:

```text
PRE-D3 = ACTIVE
D3 OPEN = NO
D4 / PRODUCTION = NO
REAL CUSTOMERS = NO
REAL MONEY = NO
```

In other words: **there is something serious enough to audit and attack, but not something that should yet be presented as finished.**

## Stop 6 — How does Rudis learn?

Rudis tries to keep discovering a problem, deciding what should be done and building the solution as separate acts.

A researcher may demonstrate that a vulnerability exists. That does not automatically make the researcher a legislator. An Assembly may decide a rule. That does not by itself prove the technical implementation is correct. And a Forge team may implement a solution only when there is legitimate authority to do so.

The compact form is:

```text
DISCOVER != DECIDE != BUILD
```

Current research rounds attack questions such as continuity, currentness, recovery, authority, privacy, institutional memory, coordinator capture and catastrophic reconstitution. The aim is for Rudis to improve because its claims can be challenged, reproduced and falsified.

## Stop 7 — Where should I go next?

If you want to understand how being inside the system should feel, go to **[Living Rudis](./LIVING_RUDIS_EN.md)**.

If you care about product surfaces, continue with [Product Surface](./products/README.md) and [Rudis Habitat](./products/Rudis_Habitat.md).

If you want to inspect current law and constitutional currentness, use the [Canon Register](./Quebranto-00_Registro_de_Canon_Vigente.md).

If you are evaluating architecture, maturity or security, enter through the [External Reading Hub](./external/README.md).

You are not expected to read everything. The Corpus is the source layer; this tour is the front door.

---

# 💼 Investor / Strategic Partner Tour

## Stop 1 — The investment thesis

As AI agents, autonomous software and digital institutions gain the ability to act, the cost of confusing **technical capability** with **legitimate authority** increases.

An agent may know how to issue a payment and still lack authority to do so. An employee may retain a technically valid token after losing a competence. An interface may show an old decision as though it were still current. A recovered system may restore correct historical data while still lacking authority to restore old power.

Rudis investigates an architecture where those questions become explicit and auditable.

The investment thesis is not “Rudis is finished.” It is that **authority, currentness, continuity and auditable execution become more strategically important as software becomes more capable of acting**, and that Rudis has developed a differentiated architecture worth falsifying, testing and integrating.

## Stop 2 — What can be financed?

Strategic capital can accelerate technical and product work without purchasing the project's constitution.

It can fund StateOS integration, RAL, Rudis Habitat, recovery, stale-state testing, security hardening, reproducibility, clients, agent surfaces, applied research, legal/IP readiness and controlled demonstrations.

The important point is that capital should move against evidence, not merely against a growing feature list.

For example, one phase may promise to show that a third party can reproduce a PRE-D3 candidate and that revoked authority fails correctly. If the evidence exists, the next phase can open. If it does not, the partner should be able to stop.

The compact form is:

```text
AGREED GATE
-> EVIDENCE PACKAGE
-> REVIEW
-> NEXT COMMITMENT
```

## Stop 3 — What are the maturity limits?

Rudis should currently be evaluated as a serious experimental, pre-production architecture under adversarial development.

D3 is not open. D4, production, real customers and real money are not active. That transparency is not a weakness in the proposal; it lets an investor know exactly what is being financed and what would have to be demonstrated before the next stage.

```text
PRE-D3 = ACTIVE
D3 OPEN = NO
D4 / PRODUCTION = NO
REAL CUSTOMERS = NO
REAL MONEY = NO
```

## Stop 4 — What does investment not buy?

A partner may negotiate economic rights, licenses, diligence access, preferred integration, reporting or ordinary corporate rights in a future commercial vehicle.

What investment does not create by default is constitutional authority over Rudis, control of the Canon, citizenship, votes, Red Button control, monetary authority or unrestricted Forge access.

The reason is straightforward: if Rudis claims capability and authority must remain separate, its own financing structure should not violate that principle.

```text
INVESTMENT != CANON CONTROL
CAPITAL != CAPTURE
```

## Stop 5 — What evidence should an investor ask for?

A serious investor should not ask only “does the component exist?” A better question is “what claim does this component make, how could the claim fail, and who other than the builder reproduced the result?”

Useful diligence moves from public thesis and architecture toward maturity limits, sanitized evidence and, when there is real fit, purpose-bound restricted review.

The central question becomes: **can an independent party demonstrate both the expected PASS and the expected failure?**

That is why Rudis treats falsification as a diligence asset rather than a reputational threat.

## Stop 6 — How does this become a product?

The architecture can materialize through several product lines: agent authority, institutional StateOS, Rudis Habitat, continuity/recovery, learning and evolution through the Evolutionary Palace, AssemblyOS, audit tooling and enterprise integration surfaces.

Current strategic proposals for partners such as Microsoft or Meta are integration hypotheses, not evidence of an existing commercial relationship. Their purpose is to show how an abstract architecture might connect to concrete problems in agents, learning, collaboration, identity and persistent environments.

## Stop 7 — Recommended reading order

1. [Investor Read First — English](./external/Investor_Read_First.md)
2. [Investor & Strategic Partner Dossier — English + Español](./external/Rudis_Investor_Introduction_ES_EN.md)
3. [Living Rudis](./LIVING_RUDIS_EN.md)
4. [Public One-Pager](./external/Rudis_Public_OnePager.md)
5. [Maturity & Limits Statement](./external/Maturity_and_Limits_Statement.md)
6. [Sanitized Security Posture](./external/Sanitized_Security_Posture.md)
7. [External Reading Hub](./external/README.md)

---

# The one sentence to remember

> **Rudis is trying to make consequential digital action prove where its authority comes from — and to remain honest when that authority cannot be demonstrated.**

And if you want to understand what that means for a person entering the system:

> **[Living Rudis](./LIVING_RUDIS_EN.md): enter, orient yourself, act, understand a consequence and return to something that continued without you.**

**Language / Idioma:** **English** · [Español](./TOUR_ES.md)
