from __future__ import annotations

FAQ = {"hours": "Open 9 to 5.", "shipping": "Ships in 3 days."}

def calc(expr: str) -> str:
    allowed = set("0123456789+-*/(). ")
    if not expr or any(c not in allowed for c in expr):
        return "invalid"
    return str(eval(expr, {"__builtins__": {}}, {}))

def run(message: str) -> dict:
    t = message.lower()
    if any(k in t for k in FAQ):
        key = next(k for k in FAQ if k in t)
        return {"tool": "faq", "answer": FAQ[key]}
    if t.startswith("calc "):
        return {"tool": "calc", "answer": calc(message[5:])}
    return {"tool": None, "answer": "I can answer hours, shipping, or calc <expr>."}
