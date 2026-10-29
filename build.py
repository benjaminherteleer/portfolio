"""Generates index.html (Dutch + English in one page). Edit the texts here, then run: python3 build.py"""
import json
from pathlib import Path

HERE = Path(__file__).parent

IMG = {  # width, height
    'me': (506, 1100), 'ph-dv-crowd': (1100, 733), 'ev-dv-poster': (834, 1100), 'ev-dv-logo': (964, 1100),
    'ph-dv-team': (733, 1100), 'd-dv': (860, 1100), 'web-ddb-home': (1200, 750), 'web-ddb-beer': (1200, 750),
    'web-ddb-nieuws': (1200, 750), 'web-ddb-shop': (1200, 750), 'ph-merch-hoodie': (880, 1100),
    'ph-merch-rack': (880, 1100), 'ph-merch-sweater': (880, 1100), 'ph-black-front': (880, 1100),
    'ph-black-back': (880, 1100), 'd-crew': (1054, 1010), 'd-brewing': (746, 1100), 'd-white': (1100, 513),
    'oe-glass': (690, 1038), 'brew-01': (960, 1200), 'brew-02': (960, 1200), 'brew-03': (960, 1200),
    'brew-04': (960, 1200), 'brew-05': (960, 1200), 'brew-07': (960, 1200), 'brew-09': (960, 1200),
    'brew-10': (960, 1200), 'brew-12': (960, 1200), 'stillenacht-illu': (797, 1065), 'xmas-card': (797, 799),
    'boskeun-illu': (797, 978), 'valentine': (797, 799), 'reserva': (797, 850), 'lichtervelds': (797, 999),
    'stout': (797, 1022), 'signs45': (797, 1002), 'site-home': (800, 499), 'site-collections': (800, 499),
}

# Projects: (key, cover, size class, images). Texts per language below.
PROJECTS = [
    ('ddb', 'web-ddb-home', 'wide', ['web-ddb-home', 'web-ddb-beer', 'web-ddb-nieuws', 'web-ddb-shop']),
    ('brew', 'brew-01', 'tall', ['brew-01', 'brew-02', 'brew-03', 'brew-04', 'brew-05', 'brew-07', 'brew-09', 'brew-10', 'brew-12']),
    ('merch', 'ph-merch-hoodie', 'tall', ['ph-merch-hoodie', 'ph-merch-rack', 'ph-black-front', 'ph-black-back', 'ph-merch-sweater', 'd-crew', 'd-brewing', 'oe-glass']),
    ('social', 'reserva', 'tall', ['reserva', 'lichtervelds', 'stout', 'signs45', 'ph-dv-crowd', 'ph-merch-rack']),
    ('dv', 'ev-dv-poster', 'tall', ['ph-dv-crowd', 'ev-dv-poster', 'ev-dv-logo', 'd-dv', 'ph-dv-team']),
    ('kris', 'site-home', 'wide', ['site-home', 'site-collections']),
]

T = {
 'nl': dict(
  nav=[('#werk', 'Werk'), ('#over', 'Over'), ('#contact', 'Contact')], switch='EN', cv='cv-benjamin-herteleer.pdf', cv_btn='Cv',
  avail='Open voor een nieuwe job',
  h1=['Marketeer', 'die zelf', 'maakt.'],
  intro='Ik ben Benjamin. Ik schrijf, ontwerp en bouw: van de copy en de campagne tot de social posts en de website. Sinds 2021 doe ik dat voor <strong>De Dolle Brouwers</strong>, nu zoek ik een nieuwe uitdaging.',
  cta_work='Bekijk mijn werk', cta_talk='Laten we praten',
  marquee=['Copy', 'Content', 'Social', 'Campagnes', 'Graphic design', 'Web', 'SEO &amp; GEO'],
  more_h='Benieuwd naar meer?', more_p='Ik vertel graag het hele verhaal achter elk project.',
  work_h='Werk', work_sub='Een greep uit wat ik maakte. Klik op een project voor meer.',
  open='Bekijk project', visit='Bezoek de site',
  projects={
   'ddb': ('dedollebrouwers.be', 'Web · Copy · SEO · Design',
           'De nieuwe website van de brouwerij, van structuur en tweetalige teksten tot design en code. Met een pagina per bier, een webshop, rondleidingen boeken, een kaart met verkooppunten en een maandelijkse krant. Ik schreef de teksten, ontwierp de pagina\'s en bouwde de site, met AI als hulpmiddel. Gebouwd om gevonden te worden, met structured data voor Google.',
           'https://www.dedollebrouwers.be'),
   'brew': ('Brewed the Dolle way', 'Social · Copy · Storytelling',
            'Een carrousel van twaalf slides die het brouwproces uitlegt, van mout tot fles: concept, tekst en beeld. De reeks kreeg daarna een tweede leven als shirt en als pagina op de nieuwe website.', None),
   'merch': ('Merch &amp; drukwerk', 'Graphic design · Productie',
             'Shirts, hoodies, sweaters en het Oeral-glas. Van ontwerp en drukbestand tot afstemming met drukkers, drukproef, fotoshoot en lancering op social en in de webshop.', None),
   'social': ('Social media', 'Content · Copy · Campagnes',
            'Instagram, Facebook en TikTok, het hele brouwjaar door: van Boskeun met Pasen tot Stille Nacht in december. Foto, video en copy in het Nederlands en Engels, Meta-advertenties, en opvolgen wat bereik haalt en wat verkoopt.', None),
   'dv': ('Dolle Vrijdag', 'Event · Branding',
          'Een avondfeest in de brouwerij, gebouwd als eigen merk om een jonger publiek binnen te halen: naam, logo met een discobal-mannetje, affiches, shirts en een eigen Instagram.', None),
   'kris': ('krisherteleer.com', 'Web · Design',
            'Een online galerij voor honderden werken van kunstenaar Kris Herteleer, met acht collecties, een interactieve kaart en een handtekening die zichzelf tekent.', 'https://www.krisherteleer.com'),
  },
  do_h='Wat ik doe',
  do=[('Copy', 'Teksten die klinken als het merk, in het Nederlands en Engels: van website en nieuwsbrief tot post en affiche.'),
      ('Social &amp; content', 'Foto, video en posts voor Instagram, Facebook en TikTok, met community en Meta Ads.'),
      ('Campagnes', 'Van idee tot uitvoering over alle kanalen, en bijsturen op basis van wat werkt.'),
      ('Graphic design', 'Huisstijlen, affiches, drukwerk en merch, tot en met de drukproef.'),
      ('Web, SEO &amp; GEO', 'Websites die gevonden worden, door Google én door AI-zoekmachines.')],
  ai_h='Gebouwd met AI.',
  ai_p='Deze site, mijn cv en dedollebrouwers.be heb ik gemaakt met Claude. Ik bedenk het idee en bewaak de smaak, AI bouwt mee. Zo maak ik in weken wat vroeger een bureau en maanden vroeg.',
  about_h='Over mij',
  about='Ik groeide op in een brouwerij, studeerde Communicatie &amp; Digitale Marketing aan de Arteveldehogeschool en liep stage in Lissabon. Ik werk het liefst in een jong team, waar een idee snel zichtbaar wordt. AI-tools gebruik ik slim om sneller te werken, de ideeën en de smaak blijven van mij. Rijbewijs B, en bereid om te verhuizen.',
  tl=[('2021 – nu', 'Marketing &amp; communicatie', 'De Dolle Brouwers · jobstudent, vast sinds 2025'),
      ('2024 – 2025', 'Marketing &amp; sales intern', 'Lisbon Boat Party, Lissabon'),
      ('2021 – 2025', 'Bachelor Communicatie &amp; Digitale Marketing', 'Arteveldehogeschool Gent · met onderscheiding')],
  tools='Illustrator · Photoshop · InDesign · Procreate · Canva · Meta Ads · Shopify · Astro · Claude',
  langs='Nederlands · Engels · Frans',
  contact_h=['Laten we', 'praten.'], contact_sub='Zoek je iemand die een idee kan bedenken én maken? Stuur me een mail.',
  copy='Kopieer', copied='Gekopieerd', footer='Zelf geschreven, ontworpen en gebouwd.', close='Sluiten',
 ),
 'en': dict(
  nav=[('#werk-en', 'Work'), ('#over-en', 'About'), ('#contact-en', 'Contact')], switch='NL', cv='cv-benjamin-herteleer-en.pdf', cv_btn='CV',
  avail='Open to a new role',
  h1=['A marketer', 'who makes', 'things.'],
  intro='I\'m Benjamin. I write, design and build: from the copy and the campaign to the social posts and the website. Since 2021 I\'ve done that for <strong>De Dolle Brouwers</strong>, now I\'m looking for a new challenge.',
  cta_work='See my work', cta_talk='Let\'s talk',
  marquee=['Copy', 'Content', 'Social', 'Campaigns', 'Graphic design', 'Web', 'SEO &amp; GEO'],
  more_h='Curious for more?', more_p='Happy to tell you the full story behind every project.',
  work_h='Work', work_sub='A selection of things I made. Click a project for more.',
  open='View project', visit='Visit the site',
  projects={
   'ddb': ('dedollebrouwers.be', 'Web · Copy · SEO · Design',
           'The brewery\'s new website, from structure and bilingual copy to design and code. With a page per beer, a web shop, tour booking, a stockist map and a monthly newspaper. I wrote the copy, designed the pages and built the site, with AI as a tool. Built to be found, with structured data for Google.',
           'https://www.dedollebrouwers.be/en'),
   'brew': ('Brewed the Dolle way', 'Social · Copy · Storytelling',
            'A twelve-slide carousel explaining the brewing process, from malt to bottle: concept, copy and visuals. The series later got a second life as a shirt and as a page on the new website.', None),
   'merch': ('Merch &amp; print', 'Graphic design · Production',
             'Shirts, hoodies, sweaters and the Oeral glass. From design and print files to printer coordination, proofs, photo shoot and launch on social and in the web shop.', None),
   'social': ('Social media', 'Content · Copy · Campaigns',
            'Instagram, Facebook and TikTok, all through the brewing year: from Boskeun at Easter to Stille Nacht in December. Photo, video and copy in Dutch and English, Meta ads, and tracking what gets reach and what sells.', None),
   'dv': ('Dolle Vrijdag', 'Event · Branding',
          'An evening party at the brewery, built as a brand of its own to bring in a younger crowd: name, a disco-ball mascot logo, posters, shirts and a dedicated Instagram.', None),
   'kris': ('krisherteleer.com', 'Web · Design',
            'An online gallery for hundreds of works by artist Kris Herteleer, with eight collections, an interactive map and a signature that draws itself.', 'https://www.krisherteleer.com'),
  },
  do_h='What I do',
  do=[('Copy', 'Copy that sounds like the brand, in Dutch and English: from website and newsletter to post and poster.'),
      ('Social &amp; content', 'Photo, video and posts for Instagram, Facebook and TikTok, with community and Meta ads.'),
      ('Campaigns', 'From idea to execution across channels, adjusting based on what works.'),
      ('Graphic design', 'Identities, posters, print and merch, all the way to the print proof.'),
      ('Web, SEO &amp; GEO', 'Websites that get found, by Google and by AI search engines.')],
  ai_h='Built with AI.',
  ai_p='This site, my CV and dedollebrouwers.be were made with Claude. I come up with the idea and guard the taste, AI helps build. That way I make in weeks what used to take an agency months.',
  about_h='About me',
  about='I grew up in a brewery, studied Communication &amp; Digital Marketing at Arteveldehogeschool and did an internship in Lisbon. I work best in a young team, where an idea quickly becomes visible. I use AI tools smartly to work faster, while the ideas and the taste stay mine. Driving licence, open to relocating.',
  tl=[('2021 – present', 'Marketing &amp; communications', 'De Dolle Brouwers · student job, permanent since 2025'),
      ('2024 – 2025', 'Marketing &amp; sales intern', 'Lisbon Boat Party, Lisbon'),
      ('2021 – 2025', 'Bachelor in Communication &amp; Digital Marketing', 'Arteveldehogeschool Ghent · with distinction')],
  tools='Illustrator · Photoshop · InDesign · Procreate · Canva · Meta Ads · Shopify · Astro · Claude',
  langs='Dutch · English · French',
  contact_h=['Let\'s', 'talk.'], contact_sub='Looking for someone who can come up with an idea and make it too? Send me an email.',
  copy='Copy', copied='Copied', footer='Written, designed and built by me.', close='Close',
 ),
}

def pic(name, alt, cls='', lazy=True):
    w, h = IMG[name]
    lz = ' loading="lazy"' if lazy else ''
    return f'<img class="{cls}" src="img/{name}.webp" alt="{alt}" width="{w}" height="{h}"{lz}>'

def badge_svg(text):
    return ('<svg class="badge" viewBox="0 0 200 200" aria-hidden="true"><defs><path id="c" d="M100,100 m-78,0 a78,78 0 1,1 156,0 a78,78 0 1,1 -156,0"/></defs>'
            f'<text><textPath href="#c">{text}{text}</textPath></text><circle cx="100" cy="100" r="30"/></svg>')

def view(k, t):
    s = '' if k == 'nl' else '-en'
    nav = ''.join(f'<a class="pill" href="{h}">{l}</a>' for h, l in t['nav'])
    words = ''.join(f'<span class="w" style="--i:{i}"><span>{w}</span></span>' for i, w in enumerate(t['h1']))
    mq = ''.join(f'<span>{w}</span><i>✱</i>' for w in t['marquee']) * 2
    cards = ''
    for key, cover, size, imgs in PROJECTS:
        title, tags, text, link = t['projects'][key]
        data = json.dumps({'t': title, 'g': tags, 'p': text, 'l': link, 'v': t['visit'], 'i': [[f'img/{n}.webp', IMG[n][0], IMG[n][1]] for n in imgs]}, ensure_ascii=False).replace("'", '&#39;')
        cards += (f'<button class="card {size} reveal" type="button" data-project=\'{data}\' aria-label="{t["open"]}: {title}">'
                  f'<span class="frame">{pic(cover, title)}</span><span class="meta"><b>{title}</b><em>{tags}</em><span class="go" aria-hidden="true">↗</span></span></button>')
    dos = ''.join(f'<li class="reveal"><span class="n">0{i+1}</span><h3>{h}</h3><p>{p}</p><span class="arr" aria-hidden="true">→</span></li>' for i, (h, p) in enumerate(t['do']))
    tl = ''.join(f'<li><span>{w}</span><b>{r}</b><em>{o}</em></li>' for w, r, o in t['tl'])
    return f'''<div class="lang" id="lang-{k}" lang="{k}"{'' if k == 'nl' else ' hidden'}>
<header class="top"><a class="logo" href="#top{s}" aria-label="Benjamin Herteleer">BH</a><nav aria-label="Menu">{nav}</nav>
<div class="right"><a class="pill dark" href="{t['cv']}" target="_blank" rel="noopener">{t['cv_btn']} ↗</a><button class="langbtn" type="button" data-set="{'en' if k == 'nl' else 'nl'}">{t['switch']}</button></div></header>

<section class="hero" id="top{s}">
 <p class="avail"><i></i>{t['avail']}</p>
 <h1>{words}</h1>
 <div class="hero-side">
  <div class="portrait">{pic('me', 'Benjamin Herteleer', lazy=False)}</div>
 </div>
 <p class="intro">{t['intro']}</p>
 <div class="cta"><a class="pill big dark" href="#werk{s}">{t['cta_work']} →</a><a class="pill big" href="#contact{s}">{t['cta_talk']}</a></div>
</section>

<div class="marquee" aria-hidden="true"><div class="track">{mq}</div></div>

<section class="work" id="werk{s}">
 <div class="sec-head reveal"><h2>{t['work_h']}</h2><p>{t['work_sub']}</p></div>
 <div class="grid">{cards}<a class="card tall more reveal" href="#contact{s}"><span class="frame"><span class="more-in"><b>{t['more_h']}</b><span>{t['more_p']}</span><span class="go" aria-hidden="true">→</span></span></span></a></div>
</section>

<section class="dos">
 <h2 class="reveal">{t['do_h']}</h2>
 <ul>{dos}</ul>
</section>


<section class="about" id="over{s}">
 <div class="reveal"><h2>{t['about_h']}</h2><p class="lead">{t['about']}</p>
 <div class="facts"><p>{t['tools']}</p><p>{t['langs']}</p></div>
 <div class="cta"><a class="pill dark" href="{t['cv']}" target="_blank" rel="noopener">{t['cv_btn']} ↗</a><a class="pill" href="https://www.linkedin.com/in/benjamin-herteleer-6a9912219" target="_blank" rel="noopener">LinkedIn ↗</a></div></div>
 <ul class="tl reveal">{tl}</ul>
</section>

<section class="contact" id="contact{s}">
 <h2><span>{t['contact_h'][0]}</span><span>{t['contact_h'][1]}</span></h2>
 <p>{t['contact_sub']}</p>
 <div class="row"><div class="copyrow"><a class="mail" href="mailto:hallo@benjaminherteleer.work">hallo@benjaminherteleer.work</a><button type="button" class="copybtn" data-copy="{t['copy']}" data-copied="{t['copied']}">{t['copy']}</button></div>
 <a class="pill light" href="tel:+32494705597">+32 494 70 55 97</a><a class="pill light" href="https://www.linkedin.com/in/benjamin-herteleer-6a9912219" target="_blank" rel="noopener">LinkedIn ↗</a></div>
 <footer><span>© 2026 Benjamin Herteleer</span><span>{t['footer']}</span></footer>
</section>
</div>'''

CSS = (HERE / 'site.css').read_text(encoding='utf-8')
JS = (HERE / 'site.js').read_text(encoding='utf-8')

html = f'''<!doctype html>
<html lang="nl">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1, viewport-fit=cover">
<title>Benjamin Herteleer · copy, content &amp; campagnes</title>
<meta name="description" content="Portfolio van Benjamin Herteleer: copy, social media, campagnes, graphic design, web en SEO. Marketeer die zelf maakt.">
<meta property="og:title" content="Benjamin Herteleer · marketeer die zelf maakt">
<meta property="og:description" content="Copy, social media, campagnes, graphic design en web: van de affiche tot de website.">
<meta property="og:image" content="https://benjaminherteleer.work/img/web-ddb-home.webp">
<link rel="preconnect" href="https://fonts.googleapis.com"><link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
<link rel="stylesheet" href="https://fonts.googleapis.com/css2?family=Archivo:wdth,wght@112,500;112,800;125,900&family=Figtree:wght@400;500;600&display=swap">
<style>
{CSS}</style>
</head>
<body>
{view('nl', T['nl'])}
{view('en', T['en'])}
<dialog id="pm" aria-labelledby="pm-t"><form method="dialog"><button class="x" aria-label="Sluiten">×</button></form>
<div class="pm-head"><em id="pm-g"></em><h3 id="pm-t"></h3><p id="pm-p"></p><a id="pm-l" class="pill dark" target="_blank" rel="noopener"></a></div>
<div class="pm-imgs" id="pm-i"></div></dialog>
<script>
{JS}</script>
</body>
</html>
'''
(HERE / 'index.html').write_text(html, encoding='utf-8')
print('ok')
