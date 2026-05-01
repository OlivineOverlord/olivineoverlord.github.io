# olivineoverlord.github.io

Personal academic website built with [Quarto](https://quarto.org).
Hosted at <https://olivineoverlord.github.io>.

---

## First-time setup

### 1. Create the GitHub repository

1. On GitHub, create a new public repository named **exactly** `olivineoverlord.github.io`.
2. Don't initialise it with a README/license — this folder already has them.
3. From this folder, in a terminal:

   ```bash
   git init -b main
   git add .
   git commit -m "Initial commit: Quarto site scaffold"
   git remote add origin git@github.com:olivineoverlord/olivineoverlord.github.io.git
   git push -u origin main
   ```

### 2. Turn on GitHub Pages

1. Go to **Settings → Pages** in the repository.
2. Under **Build and deployment → Source**, choose **GitHub Actions**.
3. The first push will trigger the workflow in `.github/workflows/publish.yml`. After
   ~2 minutes, the site will be live at <https://olivineoverlord.github.io>.

### 3. Install Quarto locally (so you can preview before pushing)

- macOS: `brew install --cask quarto`
- Linux: download from <https://quarto.org/docs/get-started/>
- Windows: download installer from <https://quarto.org/docs/get-started/>

Verify with `quarto --version` (should be ≥ 1.5).

---

## Daily workflow

```bash
# Live preview while editing — auto-refreshes the browser on save
quarto preview

# One-off render of the full site to ./_site
quarto render

# Push changes — GitHub Actions renders + deploys
git add .
git commit -m "Update CV"
git push
```

That's it. The Actions workflow is configured to render and deploy on every push to `main`.

---

## Editing guide

| What | Where |
|---|---|
| Home page | `index.qmd` |
| Research overview | `research.qmd` |
| Publications | `publications.qmd` (markdown) and `references.bib` (BibTeX) |
| CV | `cv.qmd` |
| Notes / blog landing | `posts.qmd` |
| Individual blog posts | `posts/<date-slug>/index.qmd` |
| Students / collaborators | `students.qmd` |
| Site config (nav, links, theme) | `_quarto.yml` |
| Theme variables (colours, fonts) | `theme.scss` |
| Small CSS overrides | `styles.css` |

### Adding a new blog post

1. Create a new folder under `posts/`, e.g. `posts/2026-03-iceland-vents/`.
2. Add an `index.qmd` inside it. Copy the YAML header from
   `posts/2026-01-revised-mantle-carbon/index.qmd` as a template.
3. Drop any figures into the same folder; reference them with relative paths
   (e.g. `![](figure1.png)`).
4. `quarto preview` to check, then push.

Posts auto-appear in the listing on `posts.qmd`, sorted by date.

### Updating publications

Two options, depending on how much you want to maintain:

- **Quick:** edit the markdown list in `publications.qmd` directly.
- **Proper:** add a BibTeX entry to `references.bib`, then on the page write
  `[@your-cite-key]` to render the formatted citation. The CSL is set to
  Geochimica et Cosmochimica Acta — change in `_quarto.yml` if you prefer another style.

### Replacing the placeholders

Search the codebase for these and replace:

```
0000-0000-0000-0000     ← your real ORCID
YOUR_ID                 ← your Google Scholar user ID
```

Both appear in `_quarto.yml`, `index.qmd`, `cv.qmd`, and `publications.qmd`.

### Adding a profile photo

1. Drop a square image into `images/` (e.g. `images/joshua-shea.jpg`, ~400×400 px).
2. In `index.qmd`, replace the hero block with one of these patterns:

   ```markdown
   :::: {.columns}
   ::: {.column width="30%"}
   ![](images/joshua-shea.jpg){.rounded fig-alt="Portrait of Joshua Shea"}
   :::
   ::: {.column width="70%"}
   ::: {.home-hero}
   ::: {.name}
   Joshua Shea
   :::
   ... etc
   :::
   :::
   ::::
   ```

---

## Theming

The site uses **EB Garamond** (body) and **JetBrains Mono** (code) from Google Fonts,
with a muted moss-olive accent (`#5d6b3d`) — a quiet nod to your handle.

To change the accent colour, edit `theme.scss`:

```scss
$primary:   #5d6b3d;   // change this
```

Other variables to know about: `$body-bg`, `$body-color`, `$border-color`. SCSS
recompiles on every render, so just save and refresh.

---

## Custom domain (optional, later)

If you ever want `joshuashea.com` (or similar):

1. Buy the domain from a registrar (Cloudflare, Namecheap, Porkbun).
2. Add a `CNAME` file at the repo root containing only the domain name.
3. Set DNS records as per the [GitHub Pages custom-domain docs](https://docs.github.com/en/pages/configuring-a-custom-domain-for-your-github-pages-site).
4. Update `site-url` in `_quarto.yml`.

---

## Troubleshooting

**The Actions build is failing on "quarto render".**
Look at the failed step's log — almost always a YAML typo in a `.qmd` header.
The error message usually points to the file and line.

**Fonts look different than in preview.**
Google Fonts can be blocked on some networks. The CSS falls back to Georgia, which
is close but not identical. Nothing to do about it on your end.

**The CV page won't print to PDF cleanly.**
Use the browser's "Print → Save as PDF" with margins set to default. The print
stylesheet in `styles.css` hides the navbar and sidebar.

**I want to embed a Python plot in a blog post.**
Uncomment the Python setup blocks in `.github/workflows/publish.yml` and add a
`requirements.txt` to the repo root. Then in your post:

````qmd
```{python}
#| label: fig-isotopes
#| fig-cap: "Carbon isotope distribution"
import matplotlib.pyplot as plt
# ...
```
````

---

## Licence

Content (text, figures): © Joshua Shea. All rights reserved unless stated otherwise on individual posts.

Code (the scaffold itself, theme files): MIT — feel free to lift it for your own site.
