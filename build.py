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
    ('illu', 'stillenacht-illu', 'tall', ['stillenacht-illu', 'xmas-card', 'boskeun-illu', 'valentine', 'reserva', 'lichtervelds', 'stout', 'signs45']),
    ('dv', 'ev-dv-poster', 'tall', ['ph-dv-crowd', 'ev-dv-poster', 'ev-dv-logo', 'd-dv', 'ph-dv-team']),
    ('kris', 'site-home', 'wide', ['site-home', 'site-collections']),
]

T = {
 'nl': dict(
  nav=[('#werk', 'Werk'), ('#over', 'Over'), ('#contact', 'Contact')], switch='EN', cv='cv-benjamin-herteleer.pdf', cv_btn='Cv',
  badge='OPEN VOOR EEN NIEUWE JOB · AI-ENTHOUSIAST · ',
  h1=['Marketeer', 'die zelf', 'maakt.'],
  intro='Ik ben Benjamin. Ik bedenk merken, campagnes en content, en ik maak ze ook: van de affiche tot de website. Sinds 2021 doe ik dat voor <strong>De Dolle Brouwers</strong>, nu zoek ik een nieuw team.',
  cta_work='Bekijk mijn werk', cta_talk='Laten we praten',
  marquee=['Branding', 'Content', 'Web', 'Illustratie', 'AI', 'Social', 'Merch'],
  more_h='Benieuwd naar meer?', more_p='Ik vertel graag het hele verhaal achter elk project.',
  work_h='Werk', work_sub='Een greep uit wat ik maakte. Klik op een project voor meer.',
  open='Bekijk project', visit='Bezoek de site',
  projects={
   'ddb': ('dedollebrouwers.be', 'Web · Copy · Design · AI',
           'De nieuwe website van de brouwerij, van structuur en tweetalige teksten tot design en code. Met een pagina per bier, een webshop, rondleidingen boeken, een kaart met verkooppunten en een maandelijkse krant. Gebouwd met Claude: ik bedacht, schreef en stuurde bij, AI bouwde mee.',
           'https://www.dedollebrouwers.be'),
   'brew': ('Brewed the Dolle way', 'Illustratie · Social',
            'Twaalf zelfgetekende slides die het brouwproces uitleggen, met de Oerbier-mannetjes in de hoofdrol. De tekeningen kregen daarna een tweede leven als shirt en als pagina op de nieuwe website.', None),
   'merch': ('Merch', 'Design · Productie',
             'Shirts, hoodies, sweaters en het Oeral-glas. Van ontwerp en drukbestand tot drukproef, fotoshoot en lancering. Fans vroegen al jaren naar de sweaters, nu zijn ze er.', None),
   'illu': ('Social &amp; illustratie', 'Content · Illustratie',
            'Het brouwjaar online, van Boskeun met Pasen tot Stille Nacht in december. Eigen foto\'s, video en illustraties waarin de figuren van de brouwerij nieuwe scènes beleven, in het Nederlands en Engels.', None),
   'dv': ('Dolle Vrijdag', 'Event · Branding',
          'Een avondfeest in de brouwerij, gebouwd als eigen merk om een jonger publiek binnen te halen: naam, logo met een discobal-mannetje, affiches, shirts en een eigen Instagram.', None),
   'kris': ('krisherteleer.com', 'Web · Design',
            'Een online galerij voor honderden werken van kunstenaar Kris Herteleer, met acht collecties, een interactieve kaart en een handtekening die zichzelf tekent.', 'https://www.krisherteleer.com'),
  },
  do_h='Wat ik doe',
  do=[('Merk &amp; design', 'Huisstijlen, logo\'s, affiches en merch die je herkent van ver.'),
      ('Content &amp; social', 'Foto, video, copy en illustraties, in het Nederlands en Engels.'),
      ('Web', 'Sites van structuur en teksten tot design en code.'),
      ('AI', 'Ik werk elke dag met Claude: sneller maken, zonder dat het naar AI ruikt.')],
  ai_h='Gebouwd met AI.',
  ai_p='Deze site, mijn cv en dedollebrouwers.be heb ik gemaakt met Claude. Ik bedenk het idee en bewaak de smaak, AI bouwt mee. Zo maak ik in weken wat vroeger een bureau en maanden vroeg.',
  about_h='Over mij',
  about='Ik groeide op in een brouwerij, studeerde Communicatie &amp; Digitale Marketing aan de Arteveldehogeschool en liep stage in Lissabon. Ik werk het liefst in een jong team, waar een idee snel zichtbaar wordt. Rijbewijs B, en bereid om te verhuizen.',
  tl=[('2021 – nu', 'Marketing &amp; communicatie', 'De Dolle Brouwers · jobstudent, vast sinds 2025'),
      ('2024 – 2025', 'Marketing &amp; sales intern', 'Lisbon Boat Party, Lissabon'),
      ('2021 – 2025', 'Bachelor Communicatie &amp; Digitale Marketing', 'Arteveldehogeschool Gent · met onderscheiding')],
  tools='Illustrator · Photoshop · InDesign · Procreate · Canva · Meta Ads · Shopify · Astro · Claude',
  langs='Nederlands · Engels · Frans',
  contact_h=['Laten we', 'praten.'], contact_sub='Zoek je iemand die een idee kan bedenken én maken? Stuur me een mail.',
  sticker='Let\'s talk!', copy='Kopieer', copied='Gekopieerd', footer='Zelf ontworpen en gebouwd, met Claude.', close='Sluiten',
 ),
 'en': dict(
  nav=[('#werk-en', 'Work'), ('#over-en', 'About'), ('#contact-en', 'Contact')], switch='NL', cv='cv-benjamin-herteleer-en.pdf', cv_btn='CV',
  badge='OPEN TO A NEW ROLE · AI ENTHUSIAST · ',
  h1=['A marketer', 'who makes', 'things.'],
  intro='I\'m Benjamin. I come up with brands, campaigns and content, and I make them too: from the poster to the website. Since 2021 I\'ve done that for <strong>De Dolle Brouwers</strong>, now I\'m looking for a new team.',
  cta_work='See my work', cta_talk='Let\'s talk',
  marquee=['Branding', 'Content', 'Web', 'Illustration', 'AI', 'Social', 'Merch'],
  more_h='Curious for more?', more_p='Happy to tell you the full story behind every project.',
  work_h='Work', work_sub='A selection of things I made. Click a project for more.',
  open='View project', visit='Visit the site',
  projects={
   'ddb': ('dedollebrouwers.be', 'Web · Copy · Design · AI',
           'The brewery\'s new website, from structure and bilingual copy to design and code. With a page per beer, a web shop, tour booking, a stockist map and a monthly newspaper. Built with Claude: I came up with it, wrote it and steered it, AI helped build it.',
           'https://www.dedollebrouwers.be/en'),
   'brew': ('Brewed the Dolle way', 'Illustration · Social',
            'Twelve hand-drawn slides explaining the brewing process, starring the little Oerbier men. The drawings later got a second life as a shirt and as a page on the new website.', None),
   'merch': ('Merch', 'Design · Production',
             'Shirts, hoodies, sweaters and the Oeral glass. From design and print files to proofs, photo shoot and launch. Fans had been asking for the sweaters for years, now they\'re here.', None),
   'illu': ('Social &amp; illustration', 'Content · Illustration',
            'The brewing year online, from Boskeun at Easter to Stille Nacht in December. My own photos, video and illustrations that put the brewery\'s characters in new scenes, in Dutch and English.', None),
   'dv': ('Dolle Vrijdag', 'Event · Branding',
          'An evening party at the brewery, built as a brand of its own to bring in a younger crowd: name, a disco-ball mascot logo, posters, shirts and a dedicated Instagram.', None),
   'kris': ('krisherteleer.com', 'Web · Design',
            'An online gallery for hundreds of works by artist Kris Herteleer, with eight collections, an interactive map and a signature that draws itself.', 'https://www.krisherteleer.com'),
  },
  do_h='What I do',
  do=[('Brand &amp; design', 'Identities, logos, posters and merch you recognise from afar.'),
      ('Content &amp; social', 'Photo, video, copy and illustration, in Dutch and English.'),
      ('Web', 'Sites from structure and copy to design and code.'),
      ('AI', 'I work with Claude every day: making things faster, without it smelling like AI.')],
  ai_h='Built with AI.',
  ai_p='This site, my CV and dedollebrouwers.be were made with Claude. I come up with the idea and guard the taste, AI helps build. That way I make in weeks what used to take an agency months.',
  about_h='About me',
  about='I grew up in a brewery, studied Communication &amp; Digital Marketing at Arteveldehogeschool and did an internship in Lisbon. I work best in a young team, where an idea quickly becomes visible. Driving licence, open to relocating.',
  tl=[('2021 – present', 'Marketing &amp; communications', 'De Dolle Brouwers · student job, permanent since 2025'),
      ('2024 – 2025', 'Marketing &amp; sales intern', 'Lisbon Boat Party, Lisbon'),
      ('2021 – 2025', 'Bachelor in Communication &amp; Digital Marketing', 'Arteveldehogeschool Ghent · with distinction')],
  tools='Illustrator · Photoshop · InDesign · Procreate · Canva · Meta Ads · Shopify · Astro · Claude',
  langs='Dutch · English · French',
  contact_h=['Let\'s', 'talk.'], contact_sub='Looking for someone who can come up with an idea and make it too? Send me an email.',
  sticker='Let\'s talk!', copy='Copy', copied='Copied', footer='Designed and built by me, with Claude.', close='Close',
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
 <h1>{words}</h1>
 <div class="hero-side">
  <div class="portrait">{pic('me', 'Benjamin Herteleer', lazy=False)}{badge_svg(t['badge'])}<img class="sticker s1" src="img/d-crew.webp" alt="" width="1054" height="1010"><img class="sticker s2" src="img/ev-dv-logo.webp" alt="" width="964" height="1100"></div>
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

<section class="ai">
 <div class="ai-in reveal"><span class="spark" aria-hidden="true">✦</span><h2>{t['ai_h']}</h2><p>{t['ai_p']}</p></div>
</section>

<section class="about" id="over{s}">
 <div class="reveal"><h2>{t['about_h']}</h2><p class="lead">{t['about']}</p>
 <div class="facts"><p>{t['tools']}</p><p>{t['langs']}</p></div>
 <div class="cta"><a class="pill dark" href="{t['cv']}" target="_blank" rel="noopener">{t['cv_btn']} ↗</a><a class="pill" href="https://www.linkedin.com/in/benjamin-herteleer-6a9912219" target="_blank" rel="noopener">LinkedIn ↗</a></div></div>
 <ul class="tl reveal">{tl}</ul>
</section>

<section class="contact" id="contact{s}">
 <span class="talk" aria-hidden="true">{t['sticker']}</span>
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
<title>Benjamin Herteleer · marketeer die zelf maakt</title>
<meta name="description" content="Portfolio van Benjamin Herteleer: merk, content, web en AI. Marketeer die zelf maakt, van affiche tot website.">
<meta property="og:title" content="Benjamin Herteleer · marketeer die zelf maakt">
<meta property="og:description" content="Merk, content, web en AI: van de affiche tot de website.">
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
