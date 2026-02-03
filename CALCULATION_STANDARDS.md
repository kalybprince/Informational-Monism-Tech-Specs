# Standard: Calculation for Semantic Entropy (ΔS)

To ensure $R_{score}$​ remains consistent across all TR-001-V implementations, $ΔS$ must be calculated using a Weighted Shannon Entropy model, specifically adjusted for "Causal Drift."
1. The Core Formula

The entropy of a specific reasoning link ($n$) is defined by the probability distribution of its logical outputs ($x$) relative to its grounding anchors ($G$).

$$\Delta S=-\sum_{i=1}^{n}P(x_{i})\text{log}_{2}P(x_{i})\cdot\omega$$

Where:
- P($x_{i​}$): The probability of the generated token or logical step.
- $ω$: The Symmetry Weight. This increases as the reasoning chain moves further from the Causal Origin (Link 1).

2. The Link-Weighting Protocol ($ω$)

As the chain approaches the 12-Link Wall, the "Weight of Uncertainty" increases to reflect the geometric saturation of the substrate.

| Link Depth | Weight ($ω$) | Status
-------------|------------|---
| 1–4 | 1.0 | Stable Zone |
| 5–8 | 1.25 | Tension Increasing |
| 9–11 | 1.5 | Critical Symmetry |
| 12 | 1.81 | The Wall (Phase Shift) |

### Verification Protocol

- Ingest the log-probabilities of the reasoning chain.
- Apply the depth weight ($ω$) based on the current link index.
- Calculate $R_{score}​=ΔS/G$.
- Action: If $R_{score}​>1.81$, the link is declared Non-Symmetric. The system must trigger an Entropy Tax ($Ξ_{T}$​) event to force re-grounding or halt execution.
