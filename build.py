#!/usr/bin/env python3
"""Build a small academic website from editable JSON. Python 3; no dependencies."""
from pathlib import Path
from html import escape
from urllib.parse import urlsplit
from string import Template
from datetime import datetime, timezone
import json, re, shutil
ROOT = Path(__file__).resolve().parent
OUT = ROOT / '_site'
def load(name): return json.loads((ROOT/'content'/f'{name}.json').read_text(encoding='utf-8'))
def e(value): return escape(str(value), quote=True)
def url(value):
    if urlsplit(value).scheme not in ('https','http'): raise ValueError(f'Use an https:// URL: {value}')
    return e(value)
def paragraphs(values): return '\n'.join(f'<p>{e(x)}</p>' for x in values)
def link(href,label): return f'<a href="{url(href)}" target="_blank" rel="noopener noreferrer">{e(label)}</a>'
def icon(body): return f'<svg aria-hidden="true" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.6" stroke-linecap="round" stroke-linejoin="round">{body}</svg>'
icons = {
 'mail_icon':icon('<rect x="3" y="5" width="18" height="14" rx="1"/><path d="m3 6 9 7 9-7"/>'),
 'wechat_icon':icon('<path d="M21 11c0 4-4 7-9 7l-6 3 1-4c-3-1-5-3-5-6 0-4 4-7 10-7s9 3 9 7Z"/><circle cx="8" cy="10" r=".7"/><circle cx="16" cy="10" r=".7"/>'),
 'linkedin_icon':icon('<rect x="3" y="3" width="18" height="18" rx="1"/><path d="M7 10v7m0-10v.1M11 17v-7m0 3c0-4 6-4 6 0v4"/>'),
 'github_icon':icon('<path d="m9 6-6 6 6 6m6-12 6 6-6 6"/>')
}
p=load('profile');home=load('home');research=load('research');courses=load('teaching');pubs=load('publications')
assert len({x['url'] for x in pubs})==len(pubs), 'Duplicate publication links.'
assert all(x['type'] in ('published','preprint') for x in pubs)
emails = [p['email']] + ([p['secondary_email']] if p.get('secondary_email') else [])
assert all(re.fullmatch(r'[^\s@]+@[^\s@]+\.[^\s@]+', address) for address in emails), 'Invalid email.'
email_links = ' or '.join(f'<a href="mailto:{e(address)}">{e(address)}</a>' for address in emails)
photo=Path(p['photo']);assert not photo.is_absolute() and '..' not in photo.parts
assert (ROOT/photo).is_file(), 'Profile image is missing.'
OUT.mkdir(exist_ok=True)
shutil.copytree(ROOT/'assets',OUT/'assets',dirs_exist_ok=True)
base=Template((ROOT/'templates/base.html').read_text())
def page(title,body,path):
    relative='../' if path=='research/index.html' else './'
    full_url=p['site_url'].rstrip('/')+('/research/' if path=='research/index.html' else '/')
    values={**{k:e(v) for k,v in p.items() if isinstance(v,str)},**icons,
     'root':relative,'title':e(title+' | '+p['name']),'description':e('Fan Wang, PhD — biostatistics, statistical genetics, teaching, and research.'),
     'canonical':url(full_url),'photo':relative+e(p['photo']),'affiliation':'<br>'.join(e(x) for x in p['affiliation']),
     'about_current':'aria-current="page"' if path=='index.html' else '',
     'research_current':'aria-current="page"' if path=='research/index.html' else '',
     'body':body,'email_links':email_links,'year':str(datetime.now(timezone.utc).year)}
    dest=OUT/path;dest.parent.mkdir(parents=True,exist_ok=True);dest.write_text(base.substitute(values),encoding='utf-8')
course_html=[]
for c in courses:
    title=link(c['url'],c['title']) if c.get('url') else e(c['title'])
    course_meta = ' · '.join(e(value) for value in (c['role'], c.get('dates')) if value)
    course_html.append(f'<li><span class="course-title">{title}</span><span class="course-institution">{e(c["institution"])}</span><span class="course-meta">{course_meta}</span></li>')
contact=f'''<ul class="contact-list"><li><strong>Email:</strong> {email_links}</li><li><strong>WeChat:</strong> <span class="wechat-id">{e(p['wechat'])}</span><button class="copy-wechat" data-wechat="{e(p['wechat'])}" aria-label="Copy WeChat ID">Copy ID</button><span id="copy-status" class="copy-status" role="status" aria-live="polite"></span></li><li><strong>LinkedIn:</strong> {link(p['linkedin'],'Fan Wang')}</li></ul>'''
student_statement_html = f'<p class="student-statement">{e(home["student_statement"])}</p>' if home.get('student_statement') else ''
contact_intro_html = f'<p>{e(home["contact_intro"])}</p>' if home.get('contact_intro') else ''
home_html=f'''<h1>{e(home['title'])}</h1>{paragraphs(home['paragraphs'])}
{student_statement_html}<p class="student-followup">{e(home['student_followup'])}</p>
<p class="research-link"><a href="research/">Research and publications →</a></p>
<section id="teaching"><h2>{e(home['teaching_heading'])}</h2><p>{e(home['teaching_intro'])}</p><ul class="teaching-list">{''.join(course_html)}</ul><h3>{e(home['teaching_other_heading'])}</h3><ul class="additional-teaching">{''.join('<li>'+e(x)+'</li>' for x in home['teaching_other'])}</ul></section>
<section id="contact"><h2>{e(home['contact_heading'])}</h2>{contact_intro_html}{contact}</section>'''
page(home['title'],home_html,'index.html')
def publication_list(kind):
    rows=[]
    for paper in [x for x in pubs if x['type']==kind]:
        authors=re.sub(r'\bWang F(\*)?(?=[,.; ])',r'<strong>Wang F\1</strong>',e(paper['authors']))
        rows.append(f'''<li><div class="publication-title">{link(paper['url'],paper['title'])}</div><div class="publication-authors">{authors}</div><div class="publication-venue"><em>{e(paper['journal'])}</em>, {e(paper['year'])}{', <span class="publication-details">'+e(paper['details'])+'</span>' if paper.get('details') else ''}.</div><div class="publication-links">{link(paper['url'],'[Paper]')}</div></li>''')
    return '<ol class="publication-list">'+''.join(rows)+'</ol>'
software='<ul class="software-list">'+''.join('<li>'+link(x['url'],x['name'])+' — '+e(x['description'])+'</li>' for x in research['software'])+'</ul>'
research_html=f'''<h1>{e(research['title'])}</h1>{paragraphs(research['paragraphs'])}<h2>{e(research['published_heading'])}</h2><p class="publication-note">{e(research['publication_note'])}</p>{publication_list('published')}<h2>{e(research['preprints_heading'])}</h2>{publication_list('preprint')}<h2>{e(research['software_heading'])}</h2>{software}'''
page(research['title'],research_html,'research/index.html')
(OUT/'.nojekyll').write_text('')
# The public website permits crawling and indexing; the source repository stays private.
site_url = p['site_url'].rstrip('/')
(OUT/'robots.txt').write_text(f'User-agent: *\nAllow: /\n\nSitemap: {site_url}/sitemap.xml\n', encoding='utf-8')
sitemap_urls = [site_url+'/', site_url+'/research/']
(OUT/'sitemap.xml').write_text('<?xml version="1.0" encoding="UTF-8"?>\n<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">\n'+''.join(f'  <url><loc>{url(href)}</loc></url>\n' for href in sitemap_urls)+'</urlset>\n', encoding='utf-8')
(OUT/'_headers').write_text('/*\n  X-Robots-Tag: index, follow\n')
print(f'Built homepage and research page: {len(courses)} courses, {len(pubs)} papers.')
