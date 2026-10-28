"""Builds cv/cv-nl.html and cv/cv-en.html; print them to PDF with headless Chrome (see README in commit)."""
from pathlib import Path

HERE = Path(__file__).parent

T = {
    'nl': dict(
        lang='nl', title='Cv Benjamin Herteleer',
        role='Marketing &amp; communicatie',
        profile_h='Profiel',
        profile='Marketeer die zelf maakt. Bij De Dolle Brouwers doe ik sinds 2021 de volledige marketing: campagnes, social media, events, merch en de nieuwe website, van strategie tot uitvoering. Ik zoek een rol in marketing, communicatie of events waar ik concept, content, design en organisatie kan combineren.',
        exp_h='Ervaring',
        jobs=[
            ('Marketing &amp; communicatie', 'De Dolle Brouwers, Esen', '2021 – nu', 'Jobstudent tijdens mijn studie, vast sinds 2025. In de brouwerij sinds 2017 (bar, bottellijn).', [
                '<b>Dolle Vrijdag</b> bedacht en gelanceerd als eigen merk: naam, logo, affiches, shirts en een eigen Instagram. <b>500+ tickets</b> over twee edities; na elke editie bijgestuurd op basis van welke posts tickets verkochten.',
                'Events in de brouwerij samen goed voor <b>1.000+ bezoekers</b> (Dolle Vrijdag, Zomerse Vrijdagen, Comedy Brewery).',
                'Social media (Instagram, Facebook, TikTok) in het Nederlands en Engels: foto, video, copy en eigen illustraties. Reels samen <b>36.500+ views</b>; een zelfgetekende carrousel haalde <b>440+ likes in 18 uur</b>.',
                'Merchcollectie ontworpen en gelanceerd: shirts, hoodies, sweaters en het Oeral-glas. Drukbestanden, afstemming met drukkers, fotoshoot en online lancering.',
                'Meta-advertenties opgezet en opgevolgd.',
            ]),
            ('Marketing &amp; sales intern', 'Lisbon Boat Party, Lissabon', 'sep 2024 – jan 2025', '', [
                'Social media (Instagram, TikTok) en website beheerd en geoptimaliseerd.',
                'Listings op GetYourGuide, Viator, Klook en Shotgun verbeterd (SEO en SEA), samen met hun accountteams.',
                'Meta Ads ingezet en opgevolgd: data omgezet in concrete keuzes voor content en promotie.',
            ]),
        ],
        proj_h='Websites',
        proj=[('dedollebrouwers.be', '2026', 'Nieuwe website van de brouwerij, volledig zelf ontwikkeld: structuur, tweetalige copy, design en code. Met een pagina per bier, webshop, rondleidingen boeken, verkooppuntenkaart en een maandelijkse nieuwspagina.'),
              ('krisherteleer.com', '', 'Ontwerp en bouw van een online galerij voor honderden werken van kunstenaar Kris Herteleer: 8 collecties, een interactieve kaart en een verkoopsectie.')],
        edu_h='Opleiding',
        edu=[
            ('Bachelor Communicatie &amp; Digitale Marketing', 'Arteveldehogeschool Gent', '2021 – 2025', 'Afgestudeerd met onderscheiding.'),
        ],
        contact_h='Contact',
        extra='Rijbewijs B · bereid te verhuizen',
        skills_h='Vaardigheden',
        skills=[
            ('Marketing', 'Campagnes, social media, Meta Ads, eventmarketing, SEO en SEA'),
            ('Content', 'Copywriting NL/EN, foto en video, illustratie'),
            ('Design', 'Illustrator, Photoshop, InDesign, Procreate, Canva'),
            ('Web', 'Websites van concept tot code (Astro), Shopify'),
            ('AI', 'Dagelijks aan de slag met Claude en andere AI-tools: copy, code en ideeën'),
        ],
        lang_h='Talen',
        langs='Nederlands (moedertaal)<br>Engels (zeer goed)<br>Frans (goed)',
        work_h='Bekijk mijn werk',
    ),
    'en': dict(
        lang='en', title='CV Benjamin Herteleer',
        role='Marketing &amp; communications',
        profile_h='Profile',
        profile='A marketer who makes things. Since 2021 I have run all marketing for De Dolle Brouwers, a Belgian craft brewery: campaigns, social media, events, merch and the new website, from strategy to execution. I am looking for a role in marketing, communications or events where I can combine concept, content, design and organisation.',
        exp_h='Experience',
        jobs=[
            ('Marketing &amp; communications', 'De Dolle Brouwers, Esen (BE)', '2021 – present', 'Student job during my studies, permanent since 2025. At the brewery since 2017 (bar, bottling).', [
                'Created and launched <b>Dolle Vrijdag</b> as a brand of its own: name, logo, posters, shirts and a dedicated Instagram. <b>500+ tickets</b> across two editions; adjusted after each edition based on which posts sold tickets.',
                'Brewery events drew <b>1,000+ visitors</b> in total (Dolle Vrijdag, Zomerse Vrijdagen, Comedy Brewery).',
                'Social media (Instagram, Facebook, TikTok) in Dutch and English: photo, video, copy and my own illustrations. Reels reached <b>36,500+ views</b>; a hand-drawn carousel got <b>440+ likes in 18 hours</b>.',
                'Designed and launched a merch collection: shirts, hoodies, sweaters and the Oeral glass. Print files, printer coordination, photo shoot and online launch.',
                'Set up and managed Meta ads.',
            ]),
            ('Marketing &amp; sales intern', 'Lisbon Boat Party, Lisbon (PT)', 'Sep 2024 – Jan 2025', '', [
                'Managed and optimised social media (Instagram, TikTok) and the website.',
                'Improved listings on GetYourGuide, Viator, Klook and Shotgun (SEO and SEA), working with their account teams.',
                'Ran and monitored Meta Ads, turning data into concrete content and promotion choices.',
            ]),
        ],
        proj_h='Websites',
        proj=[('dedollebrouwers.be', '2026', 'The brewery\'s new website, fully developed by me: structure, bilingual copy, design and code. With a page per beer, web shop, tour booking, a stockist map and a monthly news page.'),
              ('krisherteleer.com', '', 'Designed and built an online gallery for hundreds of works by artist Kris Herteleer: 8 collections, an interactive map and a sales section.')],
        edu_h='Education',
        edu=[
            ('Bachelor in Communication &amp; Digital Marketing', 'Arteveldehogeschool Ghent', '2021 – 2025', 'Graduated with distinction.'),
        ],
        contact_h='Contact',
        extra='Driving licence B · open to relocating',
        skills_h='Skills',
        skills=[
            ('Marketing', 'Campaigns, social media, Meta Ads, event marketing, SEO and SEA'),
            ('Content', 'Copywriting NL/EN, photo and video, illustration'),
            ('Design', 'Illustrator, Photoshop, InDesign, Procreate, Canva'),
            ('Web', 'Websites from concept to code (Astro), Shopify'),
            ('AI', 'Daily user of Claude and other AI tools: copy, code and ideas'),
        ],
        lang_h='Languages',
        langs='Dutch (native)<br>English (fluent)<br>French (good)',
        work_h='See my work',
    ),
}

CSS = """
@page{size:A4;margin:0}
*{box-sizing:border-box}
html,body{margin:0;background:#fff}
body{font-family:"Figtree",system-ui,sans-serif;color:#16140F;font-size:9.6pt;line-height:1.45;-webkit-print-color-adjust:exact;print-color-adjust:exact}
.page{width:210mm;height:297mm;display:grid;grid-template-columns:62mm 1fr;overflow:hidden}
aside{background:#16140F;color:#F3F1EA;padding:12mm 8mm 10mm 10mm;display:flex;flex-direction:column;gap:7mm}
aside img{width:100%;aspect-ratio:4/5;object-fit:cover;object-position:50% 40%;border-radius:4px;display:block}
aside h2{color:#F2B300}
aside p,aside li{font-size:8.8pt}
aside a{color:#F3F1EA;text-decoration:none}
aside ul{list-style:none;margin:0;padding:0;display:flex;flex-direction:column;gap:2.2mm}
aside .k{display:block;font-weight:600;color:#fff}
aside .muted{color:#BDB8AB}
main{padding:12mm 13mm 9mm 11mm;display:flex;flex-direction:column;gap:4.4mm}
h1{font-family:"Bricolage Grotesque","Arial Black",sans-serif;font-weight:800;font-size:31pt;line-height:.95;margin:0;letter-spacing:-.01em}
.role{font-size:12pt;font-weight:600;margin-top:2.5mm}
.role span{background:linear-gradient(transparent 60%,#F2B300 60%)}
h2{font-family:"IBM Plex Mono",monospace;font-size:7.6pt;font-weight:500;letter-spacing:.12em;text-transform:uppercase;margin:0 0 2.2mm;color:#5E5A50}
.profile{font-size:10.2pt;line-height:1.5}
.job{margin-bottom:3.2mm}
.job:last-child{margin-bottom:0}
.jh{display:flex;justify-content:space-between;gap:4mm;align-items:baseline}
.jh b{font-family:"Bricolage Grotesque",sans-serif;font-weight:800;font-size:11.2pt}
.when{font-family:"IBM Plex Mono",monospace;font-size:7.8pt;color:#5E5A50;white-space:nowrap}
.where{font-weight:600}
.note{color:#5E5A50;font-size:8.6pt}
ul.b{margin:1.6mm 0 0;padding:0 0 0 4mm;display:flex;flex-direction:column;gap:1.2mm}
ul.b li::marker{color:#F2B300}
ul.b b{font-weight:600}
.edu{display:grid;grid-template-columns:1fr;gap:3mm}
.edu b{display:block;font-weight:600}
"""

def page(t):
    jobs = ''.join(
        f'<div class="job"><div class="jh"><b>{r}</b><span class="when">{w}</span></div><div class="where">{c}</div>'
        + (f'<div class="note">{n}</div>' if n else '')
        + '<ul class="b">' + ''.join(f'<li>{x}</li>' for x in bl) + '</ul></div>'
        for r, c, w, n, bl in t['jobs'])
    edu = ''.join(f'<div><b>{d}</b>{s}<div class="when">{w}</div><div class="note">{n}</div></div>' for d, s, w, n in t['edu'])
    projs = ''.join(f'<div class="job"><div class="jh"><b>{n}</b><span class="when">{w}</span></div><div>{d}</div></div>' for n, w, d in t['proj'])
    skills = ''.join(f'<li><span class="k">{k}</span>{v}</li>' for k, v in t['skills'])
    return f"""<!doctype html><html lang="{t['lang']}"><head><meta charset="utf-8"><title>{t['title']}</title>
<link rel="stylesheet" href="https://fonts.googleapis.com/css2?family=Bricolage+Grotesque:opsz,wght@12..96,800&family=Figtree:wght@400;600&family=IBM+Plex+Mono:wght@500&display=swap">
<style>{CSS}</style></head><body><div class="page">
<aside>
<img src="me-cv.jpg" alt="">
<div><h2>{t['contact_h']}</h2><ul>
<li><a href="mailto:benjaminherteleer@hotmail.com">benjaminherteleer@hotmail.com</a></li>
<li><a href="tel:+32494705597">+32 494 70 55 97</a></li>
<li><a href="https://www.linkedin.com/in/benjamin-herteleer-6a9912219">LinkedIn · Benjamin Herteleer</a></li>
<li class="muted">{t['extra']}</li></ul></div>
<div><h2>{t['work_h']}</h2><ul>
<li><a href="https://benjaminherteleer.netlify.app"><span class="k">benjaminherteleer.netlify.app</span></a></li>
<li><a href="https://www.dedollebrouwers.be">dedollebrouwers.be</a></li>
<li><a href="https://www.krisherteleer.com">krisherteleer.com</a></li></ul></div>
<div><h2>{t['skills_h']}</h2><ul>{skills}</ul></div>
<div><h2>{t['lang_h']}</h2><p style="margin:0">{t['langs']}</p></div>
</aside>
<main>
<header><h1>Benjamin<br>Herteleer</h1><div class="role"><span>{t['role']}</span></div></header>
<section><h2>{t['profile_h']}</h2><div class="profile">{t['profile']}</div></section>
<section><h2>{t['exp_h']}</h2>{jobs}</section>
<section><h2>{t['proj_h']}</h2>{projs}</section>
<section><h2>{t['edu_h']}</h2><div class="edu">{edu}</div></section>
</main></div></body></html>"""

for k, t in T.items():
    (HERE / f'cv-{k}.html').write_text(page(t), encoding='utf-8')
print('ok')
