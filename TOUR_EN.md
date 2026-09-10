# 🌐 Understand Rudis — Guided Tour

**Language / Idioma:** **English** · [Español](./TOUR_ES.md)

> **You do not need to read the Corpus to know whether Rudis deserves your attention.**

This tour has one job: in a few minutes, help you explain **what problem Rudis addresses, what is being built, what makes it different and what actually exists today**.

After that, you can decide whether you simply want to keep exploring, evaluate the product, review the architecture or enter an investor path.

---

# 1. Start with the problem, not the names

Software is gaining the ability to act: agents call tools, systems move money, identities persist across sessions, automations modify infrastructure and digital worlds develop institutions of their own.

The problem is that **technical capability and legitimate authority are not the same thing**.

An agent may know how to issue a payment and still have no right to do so. A person may prove their identity correctly and still lack competence for a particular action. A system may restore a valid snapshot and accidentally resurrect permissions that were already revoked.

Rudis starts from this class of failure.

Its central principle is:

> **A representation of state does not acquire authority over reality merely by claiming to represent it.**

In plain language: **a system having a record, a signature, a session or a capability is not enough to justify a consequence**.

The compact invariants used throughout Rudis summarize that boundary:

```text
CAPABILITY != AUTHORITY
IDENTITY != COMPETENCE
REPRESENTATION != AUTHORITY
```

You do not need to memorize them. They are shorthand for failure modes the system is trying to prevent.

---

# 2. What Rudis is building

Rudis is not a single application. Today it is organized around three main surfaces.

## StateOS

StateOS is the institutional-state architecture. It is designed to preserve an understandable causal path between **who acts, which claim they present, which competence they need, which authority is current, which rule applies, which mandate permits execution, what effect occurs and what evidence remains afterward**.

The point is not that every user sees this full chain all the time. The point is that the chain exists and can be opened when an action needs to be explained, audited or disputed.

## RAL — Rudis Authority Layer

RAL focuses on the moment when intent is about to become effect.

A conventional system may ask: “does this agent have access to this tool?” RAL tries to ask a stronger question: **“can this actor be shown to be authorized to cause this effect, now, under this competence and this rule?”**

## Rudis Habitat

Habitat is the habitable product direction. The same institutional state may be represented through web, mobile, immersive environments, agents or APIs without allowing any one interface to invent the reality it displays.

For example, the same Assembly decision may be visible in a mobile app and a 3D environment. Both may represent it; neither should be able to create it merely because it can render it.

```text
ONE INSTITUTIONAL STATE
-> MANY LEGITIMATE REPRESENTATIONS
```

---

# 3. What changes for a person

The difference should not feel like “more bureaucracy.” It should feel like **greater clarity about what happened and why**.

If you attempt a sensitive action, Rudis should not merely return “success” or “403.” It should be able to explain, progressively, what authority was used, what rule applied and what mandate produced the effect.

If you return after several days, Rudis should be able to show what changed while you were away: a decision that now affects you, a contribution that reached review, a research result that was falsified or a new learning route.

If you want to learn, contribute, participate or ask for help, the interface should begin with **your intent**, not by forcing you to know the institutional org chart first.

For practical examples of this layer, continue afterward with **[Living Rudis](./LIVING_RUDIS_EN.md)**.

---

# 4. What makes the architecture different

Rudis deliberately separates concepts that software often collapses together.

**Authentication is not authorization.** Proving who you are answers “who are you?”; it does not automatically answer “what are you allowed to do?”

**A valid signature does not prove current authority.** It may correctly authenticate a mandate that has already expired or been revoked.

**Recovering data does not mean recovering power.** A snapshot may be historically accurate and politically stale.

**A summary is not the source.** It may orient an Assembly or visitor, but it should not erase votes, dissent or primary evidence.

**Code is not a legislator.** If a required rule is missing, the Forge should not invent one for engineering convenience.

Only after understanding those ideas do these abbreviations become useful:

```text
AUTHENTICATION != AUTHORIZATION
VALID SIGNATURE != CURRENT AUTHORITY
STATE RECOVERY != AUTHORITY RECOVERY
SUMMARY != SOURCE
CODE != LEGISLATOR
```

---

# 5. Rudis learns by trying to break itself

Rudis separates three acts: **discovering**, **deciding** and **building**.

A researcher may demonstrate a failure. That produces evidence, not law. An Assembly or competent authority may decide a rule. That creates a norm, but does not prove the implementation is correct. The Forge implements what is authorized, and the implementation should then remain open to reproduction, attack and falsification.

A well-documented failure can therefore be valuable: it reveals a false claim before it becomes false confidence.

```text
DISCOVER != DECIDE != BUILD
```

This approach runs through security, recovery, currentness, institutional memory, RU continuity, AssemblyOS and other research lines.

---

# 6. What exists today — and what does not

Rudis has a public Corpus, architecture, a separate private Forge, PRE-D3 implementation, tests, adversarial research, product routes and public diligence material.

That is enough for there to be something real to inspect and challenge.

It is not enough to call Rudis a finished production product.

```text
PRE-D3 = ACTIVE
D3 OPEN = NO
D4 / PRODUCTION = NO
REAL CUSTOMERS = NO
REAL MONEY = NO
```

A component PASS is not a system PASS. A green build is not accreditation. A strategic proposal is not evidence of a real customer or partner.

Honesty about that boundary is part of the product, not a footnote.

---

# 7. Choose your next step

## 👁️ If you are visiting

Continue with **[Living Rudis](./LIVING_RUDIS_EN.md)**. It shows how someone could learn, contribute, participate, request help, understand a decision and return to a world that continued while they were away.

If you then want product detail: [Rudis Habitat](./products/Rudis_Habitat.md).

## 💼 If you are an investor or strategic partner

Now that you understand the thesis, continue with **[Investor / Strategic Partner — Read First](./external/Investor_Read_First.md)**.

That document does not explain Rudis from zero again. It answers the next questions: **what could become a business, what can be financed, what evidence should be requested, what is the maturity level and what rights can or cannot be bought through a transaction**.

## 🧪 If you are evaluating technically

Start with the [External Reading Hub](./external/README.md#technical-diligence--diligencia-t%C3%A9cnica).

## 🏛️ If you want to inspect current Canon

Use the [Canon Register](./Quebranto-00_Registro_de_Canon_Vigente.md). Do not infer currentness from file age or filename.

---

# The idea worth remembering

> **Rudis is trying to make consequential digital actions prove where their authority comes from, and to keep the system honest when that authority cannot be demonstrated.**

That is the core. The rest of the project deepens, tests, protects or makes that idea habitable.
