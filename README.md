# Who delivers when it matters? (SupeRR Selector S2) - website
Single self-contained file: `index.html` (about 3 MB, data embedded). No server, no build step, no login.
Deploy: drag the folder or index.html onto Netlify Drop, or push to GitHub Pages / Vercel / Cloudflare Pages.
After deploying: test in an incognito window and on a phone; click a player row to open the profile; try the sliders.
Editing: `source/template.html` is the page; `cd source && python build.py` re-embeds `source/data/*.json` into `../index.html`.
