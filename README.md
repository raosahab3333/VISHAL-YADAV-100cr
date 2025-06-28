# V20 Stock Scanner – Batched yfinance Edition

This version uses **one bulk `yfinance.download()` call** to avoid Yahoo rate limits on Render.

## Deploy

1. Push this folder to GitHub (public or private).
2. On Render > New Service > Web, connect the repo.
3. Render reads `render.yaml` for build & start commands.
4. Wait ~1‑2 min, open the live URL.

---

Last generated: 2025-06-28 18:08 UTC