#!/usr/bin/env python3
"""Count surface patterns common in LLM prose.

Usage:
    python3 pattern_check.py FILE [--json]
    cat draft.txt | python3 pattern_check.py -

This is an editing aid, not a detector. Every pattern it reports also
appears in human writing. Look for clusters and repetition, then fix the
cause (see references/pattern-catalog.md). Standard library only.
"""

import json
import re
import statistics
import sys

WORDS = {
    "style verbs": [
        "delve", "delves", "delving", "delved", "underscore", "underscores",
        "underscoring", "underscored", "showcase", "showcases", "showcasing",
        "showcased", "foster", "fosters", "fostering", "fostered", "leverage",
        "leverages", "leveraging", "leveraged", "harness", "harnessing",
        "harnessed", "bolster", "bolstering", "bolstered", "unveil", "unveils",
        "unveiling", "unlock", "unlocking", "illuminate", "illuminating",
        "elucidate", "elucidating", "encompass", "encompassing", "navigate",
        "navigating", "navigates", "embark", "embarking", "elevate", "elevates",
        "elevating", "empower", "empowering", "embrace", "embracing",
        "streamline", "streamlining", "revolutionize", "revolutionizing",
        "resonate", "resonates", "resonating", "transcend", "transcends",
        "grapple", "grapples", "grappling", "garner", "garnered", "utilize",
        "utilizes", "utilizing", "utilized",
    ],
    "evaluative adjectives": [
        "crucial", "pivotal", "vital", "paramount", "comprehensive", "robust",
        "seamless", "meticulous", "meticulously", "commendable", "noteworthy",
        "invaluable", "groundbreaking", "transformative", "unparalleled",
        "profound", "multifaceted", "nuanced", "intricate", "vibrant",
        "burgeoning", "holistic", "compelling", "remarkable", "innovative",
        "dynamic", "unwavering", "indelible",
    ],
    "abstract nouns": [
        "tapestry", "testament", "realm", "landscape", "journey", "beacon",
        "interplay", "intricacies", "endeavor", "endeavors", "camaraderie",
        "solace", "synergy", "paradigm", "cornerstone", "ecosystem",
        "roadmap", "toolkit", "insights",
    ],
    "fiction beats": [
        "palpable", "unspoken", "amidst", "fleeting", "unravel", "unraveling",
        "cacophony", "unease", "pang", "wafted", "wafting", "murmured",
        "flicker", "flickered", "flickering", "glint", "glinted", "gaze",
        "shimmered", "shimmering", "hummed", "faintly", "unreadable",
    ],
}

PHRASES = [
    r"it'?s (?:important|worth|crucial) (?:to note|noting|to remember)",
    r"when it comes to", r"in today'?s [\w\- ]{0,20}world", r"in a world (?:where|of)",
    r"plays? an? (?:crucial|vital|key|pivotal|important) role",
    r"a wide (?:range|array|variety) of", r"at the end of the day",
    r"pav(?:e|es|ed|ing) the way", r"a testament to", r"stands? as an?",
    r"serves? as an?", r"the power of", r"a deeper understanding",
    r"rich tapestry", r"navigat\w+ the complexit", r"shed(?:s|ding)? light on",
    r"strike a balance", r"double-edged sword", r"game[- ]changer",
    r"at its core", r"in conclusion", r"in summary", r"to sum up",
    r"to address these limitations", r"highlights? the importance of",
    r"a sense of", r"a mix of \w+ and", r"the weight of", r"a state of \w+",
    r"voice (?:barely|just) (?:above )?a whisper", r"the air (?:was )?thick with",
    r"a smile play(?:ing|ed) (?:on|at)", r"(?:let out|released) a breath (?:she|he|they) didn'?t know",
    r"couldn'?t shake the feeling", r"something else entirely", r"hung in the air",
    r"took a deep breath", r"heart (?:pounding|hammering)",
    r"(?:the )?future (?:of [\w ]+ )?(?:is|looks) (?:bright|promising)",
    r"the journey (?:continues|ahead)", r"only time will tell", r"we hear you",
    r"we'?d love to have you", r"\b(?:in|for) (?:two|three|four|five) (?:key |main |simple )?(?:ways|reasons|things|steps)\b",
    r"\b(?:two|three|four|five) (?:key |main |big |simple )?(?:problems|reasons|lessons|takeaways|factors|pillars)\b", r"\ball (?:three|four|five)\b", r"this one(?:'s| is) for you", r"no more \w+[^.]{0,60}, (?:and )?no more",
    r"let'?s dive in", r"dive (?:deep )?into", r"in this (?:article|post|guide),? (?:we|I)'?(?:ll| will)",
]

OPENERS = [
    "additionally", "moreover", "furthermore", "notably", "consequently",
    "ultimately", "importantly", "essentially", "overall", "in conclusion",
    "in summary", "interestingly", "crucially", "indeed",
]

ASSISTANT = [
    r"^\s*(?:certainly|absolutely|sure)[!,.]", r"^\s*(?:here is|here's|below is)\b",
    r"great question", r"i hope this helps", r"let me know if",
    r"feel free to", r"happy to help",
]

NEG_PARALLEL = [
    # "not just/only/merely X, but Y"
    r"\bnot (?:just|only|merely|simply)\b[^.;:!?]{1,80}?,?\s*(?:but|it'?s|they'?re)\b",
    # "It's not X. It's Y." / "This isn't about X. It's about Y."
    r"\b(?:it|this|that|they)(?:'s| is| are|'re)? ?(?:not|n't)\b[^.!?]{1,80}[.!?;]\s+(?:it|this|that|they)(?:'s| is| are|'re)\b",
    r"\b(?:isn'?t|aren'?t|wasn'?t)\b[^.!?]{1,60}[.!?;]\s+(?:it|this|that|they)(?:'s| is| are|'re| was)\b",
    # "not X — Y" / "not X, but Y"
    r"\bnot\b[^.!?\n]{1,60}\s*[—–]\s*\w",
    r"\bnot\b[^.!?\n]{1,60}[,;:]\s*but\b",
    r"\bno longer\b[^.!?]{1,60}[.!?]\s+(?:it|they|this)\b",
]

HEDGED = r"\b(?:seemed|seems|appeared|appears|began|begins|started|starts) to\b"
PARTICIPLE_TAIL = r",\s+(?:\w+ly\s+)?(?:highlighting|underscoring|showcasing|reflecting|emphasizing|demonstrating|signaling|signalling|marking|making|creating|ensuring|allowing|enabling|leaving|offering|providing|revealing|adding|fostering|paving|setting|turning|giving|bringing|cementing|solidifying|illustrating|capturing|serving)\b"
GENERIC_ING_TAIL = r",\s+[a-z]+ing\b[^,.;]*[.;]"
TRIAD = r"\b\w+(?: \w+)?, \w+(?: \w+)?,? (?:and|or) \w+"
NOT_ONLY = r"\bnot only\b[^.]{0,120}\bbut also\b"


def split_sentences(text):
    flat = re.sub(r"\s+", " ", text)
    parts = re.split(r"(?<=[.!?])\s+(?=[\"'“(A-Z0-9])", flat)
    return [p.strip() for p in parts if len(p.strip().split()) >= 2]


def paragraphs(text):
    return [p.strip() for p in re.split(r"\n\s*\n", text) if p.strip()]


def find(pattern, text, flags=re.I):
    return [m.group(0) for m in re.finditer(pattern, text, flags)]


def analyze(text):
    lower = text.lower()
    tokens = re.findall(r"[a-z']+", lower)
    n_words = max(len(tokens), 1)
    per_k = lambda c: round(1000 * c / n_words, 1)
    report = {"words": len(tokens)}

    vocab = {}
    for cat, words in WORDS.items():
        hits = {}
        for w in words:
            c = len(re.findall(r"\b" + re.escape(w) + r"\b", lower))
            if c:
                hits[w] = c
        if hits:
            vocab[cat] = {"total": sum(hits.values()), "per_1k": per_k(sum(hits.values())), "hits": hits}
    report["vocabulary"] = vocab

    phrase_hits = {}
    for p in PHRASES:
        found = find(p, text)
        if found:
            phrase_hits[found[0].lower()] = len(found)
    report["stock_phrases"] = phrase_hits

    neg = []
    for p in NEG_PARALLEL:
        neg += find(p, text)
    report["negative_parallelism"] = sorted(set(n.strip() for n in neg))
    report["not_only_but_also"] = find(NOT_ONLY, text)
    report["hedged_verbs"] = find(HEDGED, text)
    report["participle_tails_listed"] = find(PARTICIPLE_TAIL, text)
    report["participle_tails_any"] = len(find(GENERIC_ING_TAIL, text, 0))
    report["triads"] = len(find(TRIAD, text, 0))

    sents = split_sentences(text)
    starts = {}
    for s in sents:
        first = s.lower().lstrip("\"'“(").split(",")[0]
        for o in OPENERS:
            if first.startswith(o):
                starts[o] = starts.get(o, 0) + 1
    report["transition_openers"] = starts

    assist = []
    for p in ASSISTANT:
        assist += find(p, text, re.I | re.M)
    report["assistant_framing"] = assist

    lengths = [len(s.split()) for s in sents]
    if len(lengths) >= 3:
        mean = statistics.mean(lengths)
        sd = statistics.pstdev(lengths)
        report["sentences"] = {
            "count": len(lengths), "mean_words": round(mean, 1),
            "stdev": round(sd, 1), "cv": round(sd / mean, 2) if mean else 0,
            "shortest": min(lengths), "longest": max(lengths),
        }
    run = runs = 0
    for n in lengths:
        run = run + 1 if n <= 7 else 0
        if run == 4:
            runs += 1
    report["short_sentence_runs"] = runs
    first_words = [s.split()[0].lower().strip("\"'“(") for s in sents if s.split()]
    rep = {}
    for a, b in zip(first_words, first_words[1:]):
        if a == b and a not in ("i", "the", "a"):
            rep[a] = rep.get(a, 0) + 1
    report["repeated_sentence_starts"] = rep

    paras = paragraphs(text)
    plens = [len(p.split()) for p in paras]
    if len(plens) >= 3:
        m = statistics.mean(plens)
        report["paragraphs"] = {
            "count": len(plens), "mean_words": round(m, 1),
            "cv": round(statistics.pstdev(plens) / m, 2) if m else 0,
        }
    report["em_dashes"] = {"count": text.count("—") + len(re.findall(r"\s--\s", text)),
                           "per_1k": per_k(text.count("—") + len(re.findall(r"\s--\s", text)))}
    report["markdown"] = {
        "headers": len(re.findall(r"^\s{0,3}#{1,6}\s", text, re.M)),
        "bold_label_bullets": len(re.findall(r"^\s*(?:[-*•]|\d+\.)\s+\*\*[^*\n]+\*\*\s*[:—-]", text, re.M)),
        "bold_spans": len(re.findall(r"\*\*[^*\n]+\*\*", text)),
        "bullets": len(re.findall(r"^\s*(?:[-*•]|\d+\.)\s+", text, re.M)),
    }
    if paras:
        last = paras[-1].lower()
        closers = [c for c in ["ultimately", "in the end", "in conclusion", "remember", "journey",
                               "future", "remind", "testament", "together", "the key is",
                               "at the end of the day", "only time will tell", "hope this helps"]
                   if c in last]
        report["ending_markers"] = closers
    return report


def flags(r):
    out = []
    w = max(r["words"], 1)
    vocab_total = sum(v["total"] for v in r["vocabulary"].values())
    if vocab_total >= 3 and 1000 * vocab_total / w >= 6:
        out.append(f"High density of overused vocabulary ({vocab_total} hits).")
    if len(r["stock_phrases"]) >= 2:
        out.append("Several stock phrases.")
    if r["negative_parallelism"] or r["not_only_but_also"]:
        out.append("Negative parallelism / 'not only…but also' present: state the positive claim.")
    if len(r["participle_tails_listed"]) >= 2 or (r["participle_tails_any"] >= 3 and r["participle_tails_any"] * 1000 / w >= 8):
        out.append("Many trailing -ing clauses: split or cut.")
    if len(r["hedged_verbs"]) >= 2:
        out.append("Hedged/inceptive verbs (seemed to, began to).")
    if r["triads"] >= 3 and r["triads"] * 1000 / w >= 6:
        out.append("Frequent lists of three.")
    if sum(r["transition_openers"].values()) >= 2:
        out.append("Sentence-initial transitions (Additionally, Moreover, Ultimately…).")
    if r["assistant_framing"]:
        out.append("Assistant framing present.")
    s = r.get("sentences")
    if s and s["count"] >= 8 and s["cv"] < 0.35:
        out.append(f"Sentence lengths are uniform (cv {s['cv']}).")
    if r.get("short_sentence_runs"):
        out.append(f"Runs of 4+ very short sentences ({r['short_sentence_runs']}): check for staccato.")
    p = r.get("paragraphs")
    if p and p["count"] >= 4 and p["cv"] < 0.25:
        out.append(f"Paragraph lengths are uniform (cv {p['cv']}).")
    if r["em_dashes"]["per_1k"] > 4:
        out.append(f"Em dashes: {r['em_dashes']['count']} ({r['em_dashes']['per_1k']}/1k words).")
    md = r["markdown"]
    if md["bold_label_bullets"]:
        out.append("Bold-label bullets.")
    if md["headers"] and w < 600:
        out.append("Headers in a short piece.")
    if r.get("ending_markers"):
        out.append("Ending may recap or moralize: " + ", ".join(r["ending_markers"]))
    if r["repeated_sentence_starts"]:
        out.append("Consecutive sentences start with the same word.")
    return out


def main():
    args = [a for a in sys.argv[1:] if not a.startswith("--")]
    if not args:
        print(__doc__)
        sys.exit(1)
    text = sys.stdin.read() if args[0] == "-" else open(args[0], encoding="utf-8").read()
    r = analyze(text)
    r["flags"] = flags(r)
    if "--json" in sys.argv:
        print(json.dumps(r, indent=2, ensure_ascii=False))
        return
    print(f"Words: {r['words']}")
    print("\nFlags (check in context; none is proof of anything):")
    for f in r["flags"] or ["None."]:
        print(f"  - {f}")
    print("\nDetails:")
    for k, v in r.items():
        if k in ("flags", "words") or not v:
            continue
        print(f"  {k}: {json.dumps(v, ensure_ascii=False)}")


if __name__ == "__main__":
    main()
