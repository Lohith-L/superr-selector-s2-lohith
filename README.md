# Who Delivers When It Matters?

**Pressure-adjusted ratings of IPL and T20I batters and bowlers**
Submission for the Rajasthan Royals **SupeRR Selector Season 2** hackathon (Round 1), by **Lohith L**.

**Live site:** https://superr-selector-s2-lohith.vercel.app

---

## The question

Which batters and bowlers deliver most reliably in high-pressure match situations, compared with their usual level?

## What I built

An analysis pipeline and an interactive site that:

1. **Defines pressure from the data, with no hand-picked cut-offs.** A cross-fitted win-probability model scores every delivery by *leverage*: how far that one ball can swing the match. The top 25% of deliveries by leverage count as high pressure.
2. **Rates players against what an average player does in the same situation**, using an expected-outcome model that accounts for match state, competition, pace or spin, and opposition quality.
3. **Shrinks small samples** toward each player's own usual level, so a hot streak cannot outrank a long record.
4. **Tests the result honestly**: out-of-sample prediction, bootstrap rank ranges, sensitivity checks, and robustness across data lenses.

## Key findings

- **The data has traps.** The `extras1_runs` column is a type code, not a run count. Wide, bye and leg-bye runs are not stored. The winning delivery is missing from 113 of 390 successful chases.
- **Pressure samples are small, so most "clutch" statistics are mostly noise.** Hierarchical shrinkage toward a player's own level made the ratings far more reliable.
- **Out-of-sample results (30 random half-splits, Spearman rho):**
  - On future win-probability impact under pressure, the rating beats death-over strike rate and economy (batters 0.13 vs 0.04, bowlers 0.18 vs 0.01).
  - On raw pressure runs, plain overall strike rate or economy predicts better, because raw numbers mostly reflect a player's role. Most "pressure skill" looks like general quality, and the method adds a modest pressure tilt.
- **The list depends on the data lens.** Restricting to IPL only, T20Is only, or one era keeps only 5 to 7 of the top 10. The site reports a robustness count for every player.

## The rating

For each player, using only his high-pressure deliveries:

| Component | Meaning |
|---|---|
| **H** | Pressure runs above expected per 100 balls, shrunk toward his own usual level: `(pressure RAE + 150 × usual) / (pressure balls + 150) × 100` |
| **A** | Win probability added above expected per 100 pressure balls, shrunk to the league mean |
| **C** | Share of pressure innings with positive impact, shrunk with a prior of 6 innings |

`Score = 0.65 × z(H) + 0.25 × z(A) + 0.10 × z(C)`, standardised across eligible players.
Eligible: at least 100 pressure balls over at least 12 pressure innings.

## Site features

- **Rankings:** recalculated live in the browser. Change the pressure level, minimum sample, weights, competition and seasons.
- **Player profiles:** click any row to open a player's page with KPIs, a match-by-match impact chart, robustness and squad fit.
- **Compare:** side-by-side view of two or three players.
- **Evidence:** cleaning, pressure definition, validation and limits.

## Repository layout

```
index.html           The full site: one self-contained file, data embedded
source/
  template.html      Page source
  build.py           Embeds the JSON data into index.html
  data/              Derived per-player, per-match aggregates and evidence tables
```

Optionally, add an `analysis/` folder with the pipeline scripts:

| Script | Purpose |
|---|---|
| `01_clean.py` | Cleaning rules and match-state features |
| `02_pressure_model.py` | Win-probability, leverage and expected-outcome models |
| `03_rank.py` | Ratings, bootstrap, validation, sensitivity |
| `export_lovable_data.py` | Exports the compact JSON used by the site |

## Run or deploy

The site needs no server and no build step. Open `index.html`, or deploy it as a static page on Vercel, Netlify or GitHub Pages.

To rebuild after editing the page:

```bash
cd source
python build.py
```

## Data

The ball-by-ball and match data were supplied by Rajasthan Royals for the hackathon and are **not included** in this repository. The `source/data/` files contain only derived, aggregated numbers. To reproduce the pipeline you need the original files from the hackathon and must adjust the file paths at the top of each script.

## Limitations

- Pressure samples are small, so the order inside each list is uncertain.
- Batting ratings do not predict well across years (chronological split rho about 0.00 for batters, 0.29 for bowlers).
- The winning delivery is missing in about 29% of successful chases, and wide and bye runs are imputed (reconstructed margins are off by about 2.5 runs on average).
- No pitch, venue-par or fielding data, and T20I opposition varies widely.
- Squad-fit notes use Rajasthan Royals' 2026 squad as the baseline and may change once IPL 2027 retentions are announced.

## Tech

Python (pandas, scikit-learn, SciPy, matplotlib) for the analysis. Plain HTML, CSS and JavaScript for the site, with no framework.

## Author

**Lohith L**
