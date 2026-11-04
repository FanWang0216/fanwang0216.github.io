# Fan Wang — Personal website

Clean academic website with teaching on the homepage, a separate Research page, and email, WeChat, and LinkedIn contact details. The repository and website are public, as requested by the owner.

## Edit your content on GitHub

Open a file below, click the pencil, edit, and choose **Commit changes**. Successful GitHub Actions builds publish your changes automatically.

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

The highlighted `student_statement` in `content/home.json` is optional. Remove that field or set it to an empty string to hide the paragraph; the `student_followup` paragraph will still appear.

The `contact_intro` sentence and each course's `dates` are also optional. Remove them or set them to an empty string to hide them. When removing the last field in a JSON object, also remove the comma after the preceding field.

Edit `email` and `secondary_email` in `content/profile.json` to update your two contact addresses. Both appear as clickable email links separated by "or". The `secondary_email` field is optional; remove it or leave it empty to show only the primary address.

The optional `seo_title` and `seo_description` fields in `content/home.json` and `content/research.json` control search titles, descriptions, and link previews. Keep them accurate when your background changes. Structured profile information is generated from the current profile and introduction.

Keep `google_site_verification` in `content/profile.json`: Google uses this public verification code to maintain your Search Console ownership. It is not an email password or API key.

Bookmark this repository to edit: https://github.com/FanWang0216/fanwang0216.github.io. Repository files, commit history, and published contact details are publicly visible. Do not commit passwords, tokens, CV source documents, or other private files.

## Visibility and search preferences

- Repository: public and visible on the owner's GitHub profile.
- Website: publicly accessible at https://fanwang0216.github.io/.
- Search indexing is enabled at the owner's request. Every HTML page allows `index, follow`. The legacy Cloudflare host also sets the corresponding response header.
- `robots.txt` allows crawling, including images, and advertises the website's sitemap.
- `sitemap.xml` lists the homepage and Research page using their official website addresses.
- These settings make the website eligible for search indexing. Search engines decide whether and when to crawl, index, and display it; appearing in search results is not immediate or guaranteed.

Google reference: https://developers.google.com/search/docs/crawling-indexing/sitemaps/overview

## Hosting

The primary host is **GitHub Pages**.

- Repository: `FanWang0216/fanwang0216.github.io` (public).
- Production branch: `main`.
- Repository Settings → Pages → Build and deployment → Source: **GitHub Actions**.
- Workflow: `.github/workflows/pages.yml`.
- Build command: `python3 build.py`.
- Published output: `_site`.

Website: https://fanwang0216.github.io/

Research: https://fanwang0216.github.io/research/

Every push to `main` builds, checks the public search settings, and deploys the site. A green workflow run confirms deployment; invalid JSON prevents publication. The content files and editing process are unchanged. If you later change the domain, update `site_url` in `content/profile.json`.

The existing Cloudflare Pages project remains connected and uses the generated `_redirects` file to permanently redirect the old address (`https://fan-wang-statistics.pages.dev/`) to the matching path on GitHub Pages. GitHub Pages ignores this routing file. Keep the Cloudflare project connected so old shared links continue to work.

## Local preview

Python 3 is the only requirement; no packages need to be installed.

```sh
python3 build.py
python3 -m http.server 8000 --directory _site
```

Open `http://localhost:8000`. Re-run `build.py` after editing. `_site/` is generated output and is not committed.

## Content sources

Employment follows the supplied LinkedIn screenshot. Teaching and publications follow the supplied CVs and project summaries. Research contains 10 published articles and one preprint, with preprints separated from published papers. SimpleSum2 uses its verified 2022 publication year and corrected coauthor initials. The PRS preprint uses the public title and DOI `10.1101/2025.10.13.682102`.

The photograph is the outdoor portrait supplied by Fan Wang, resized for web use. Replacing `assets/images/profile.jpg` automatically changes the image's version in the page URL so browsers load the updated photograph. Original CVs and other personal documents are not included in this repository.

Layout reference: https://wangguan27.github.io/
