import math, json

def calc_returns(initial: float, final: float, years: float) -> dict:
    if initial is None or final is None or years is None:
        raise ValueError("All inputs are required")
    initial = float(initial)
    final = float(final)
    years = float(years)
    if initial <= 0.0:
        raise ValueError("Initial amount must be > 0")
    if final < 0.0:
        raise ValueError("Final amount cannot be negative")
    if years < 0.0:
        raise ValueError("Years cannot be negative")

    roi = (final - initial) / initial
    cagr = None
    if years > 0.0 and initial > 0.0:
        try:
            cagr = (final / initial) ** (1.0 / years) - 1.0
        except Exception:
            cagr = None
    return {"roi_pct": roi * 100.0,
            "cagr_pct": (cagr * 100.0) if cagr is not None else None}
