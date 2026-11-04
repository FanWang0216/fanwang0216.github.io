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

The highlighted `student_statement` in `content/home.json` is optional. Remove that field or set it to an empty string to hide the paragraph; the `student_followup` paragraph will still appear.

The `contact_intro` sentence and each course's `dates` are also optional. Remove them or set them to an empty string to hide them. When removing the last field in a JSON object, also remove the comma after the preceding field.

Edit `email` and `secondary_email` in `content/profile.json` to update your two contact addresses. Both appear as clickable email links separated by "or". The `secondary_email` field is optional; remove it or leave it empty to show only the primary address.

The public website has no repository or editing link. Bookmark this private repository to edit. Research software links still point to the relevant public scientific tools.

## Visibility and search preferences

- Repository: private; its files are not visible to people browsing your public GitHub profile.
- Website: publicly accessible at https://fan-wang-statistics.pages.dev/.
- Search indexing is enabled at the owner's request. Every HTML page and the `X-Robots-Tag` response header allow `index, follow`.
- `robots.txt` allows crawling, including images, and advertises the website's sitemap.
- `sitemap.xml` lists the homepage and Research page using their official website addresses.
- These settings make the website eligible for search indexing. Search engines decide whether and when to crawl, index, and display it; appearing in search results is not immediate or guaranteed.

Google reference: https://developers.google.com/search/docs/crawling-indexing/sitemaps/overview

## Hosting

The selected host is **Cloudflare Pages (Free)**. GitHub stores the private source; Cloudflare builds and publishes it. Do not make the repository public to enable GitHub Pages.

Cloudflare settings:

- Repository: `FanWang0216/fanwang0216.github.io`
- Production branch: `main`
- Framework preset: None
- Build command: `python3 build.py`
- Output directory: `_site`

Website: https://fan-wang-statistics.pages.dev/

Research: https://fan-wang-statistics.pages.dev/research/

Cloudflare republishes commits automatically. If you later change the domain, update `site_url` in `content/profile.json`. The GitHub Actions workflow also checks that the site builds and that the public search settings and sitemap are valid; it does not deploy to GitHub Pages.

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
