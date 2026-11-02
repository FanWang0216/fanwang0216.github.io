# Fan Wang — Personal website

Clean academic website with teaching on the homepage, a separate Research page, and email, WeChat, and LinkedIn contact details. The repository is private. Keep it private.

## Edit your content on GitHub

Open a file below, click the pencil, edit, and choose **Commit changes**. After hosting is connected, successful builds publish your changes automatically.

| What to change | File |
| --- | --- |
| Name, sidebar, email, WeChat, LinkedIn | `content/profile.json` |
| Introduction, student message, contact text | `content/home.json` |
| Courses, institutions, roles, dates | `content/teaching.json` |
| Publications and preprints | `content/publications.json` |
| Research introduction and software | `content/research.json` |
| Profile photograph | `assets/images/profile.jpg` |
| Fonts, spacing, colors, mobile layout | `assets/style.css` |
| Shared structure and navigation | `templates/base.html` |

Preserve JSON double quotes and commas. Copy an existing entry to add a course or publication. Entries appear in file order. Publications have `"type": "published"` or `"type": "preprint"`. Invalid JSON stops the build.

The public website has no repository or editing link. Bookmark this private repository to edit. Research software links still point to the relevant public scientific tools.

## Visibility and search preferences

- Repository: private; its files are not visible to people browsing your public GitHub profile.
- Website: accessible to anyone who has its link once published.
- Every HTML page includes `noindex, nofollow, noimageindex`.
- Crawling HTML is allowed so search engines can read `noindex`. Images are blocked in `robots.txt`.
- No sitemap is generated. `_headers` provides an additional `X-Robots-Tag` for hosts that support it, including Cloudflare Pages.
- These settings request exclusion from search engines; they are not a password or a guarantee that a public link cannot be shared or discovered.

Google reference: https://developers.google.com/search/docs/crawling-indexing/block-indexing

## Hosting

Your current GitHub plan does not support Pages from this private repository. Do not make it public to enable Pages. Hosting requires either a supported GitHub plan or an external host that can deploy from private repositories.

For Cloudflare Pages, connect this repository with production branch `main`, build command `python3 build.py`, and output directory `_site`. Use the free plan for this static site. After deployment, set `site_url` in `content/profile.json` to the actual public URL. GitHub remains the content editor; Cloudflare publishes each change.

For GitHub Pages after an eligible plan upgrade: choose **Settings → Pages → GitHub Actions**, then add repository Actions variable `GITHUB_PAGES_ENABLED` with value `true`. Run **Build personal website** from Actions. Its deployment job is disabled until that variable is set; the build and search-exclusion checks run on each push regardless.

Intended GitHub Pages URL if that route is selected: `https://fanwang0216.github.io/`.

## Local preview

Python 3 is the only requirement; no packages need to be installed.

```sh
python3 build.py
python3 -m http.server 8000 --directory _site
```

Open `http://localhost:8000`. Re-run `build.py` after editing. `_site/` is generated output and is not committed.

## Content sources

Employment follows the supplied LinkedIn screenshot. Teaching and publications follow the supplied CVs and project summaries. Research contains 10 published articles and one preprint, with preprints separated from published papers. SimpleSum2 uses its verified 2022 publication year and corrected coauthor initials. The PRS preprint uses the public title and DOI `10.1101/2025.10.13.682102`.

The photograph is Fan Wang's existing GitHub avatar. Original CVs and personal documents are not included in this repository.

Layout reference: https://wangguan27.github.io/
