"""Generates index.html (Dutch + English in one page). Edit the texts here, then run: python3 build.py"""
from pathlib import Path

HERE = Path(__file__).parent

IMG = {  # width, height
    'me': (506, 1100), 'ph-dv-crowd': (1100, 733), 'ev-dv-poster': (834, 1100), 'ev-dv-logo': (964, 1100),
    'ph-dv-team': (733, 1100), 'web-ddb-home': (1200, 750), 'web-ddb-beer': (1200, 750), 'web-ddb-nieuws': (1200, 750),
    'web-ddb-shop': (1200, 750), 'ph-merch-hoodie': (880, 1100), 'ph-merch-rack': (880, 1100), 'ph-black-front': (880, 1100),
    'oe-can-cut': (427, 671), 'brew-01': (960, 1200), 'stillenacht-illu': (797, 1065), 'reserva': (797, 850),
    'xmas-card': (797, 799), 'site-home': (800, 499), 'ev-zv-a6': (993, 1400), 'boskeun-illu': (797, 978),
    'd-crew': (1054, 1010), 'ev-comedy': (825, 1100), 'oe-glass': (690, 1038),
}

T = {
 'nl': dict(
  nav=[('#werk', 'Werk'), ('#over', 'Over mij'), ('#contact', 'Contact')], switch='EN', cv='cv-benjamin-herteleer.pdf', cv_btn='Download cv',
  avail='Op zoek naar een nieuwe job in marketing, communicatie of events',
  eyebrow='Benjamin Herteleer · marketing &amp; communicatie',
  h1='Marketeer die zelf maakt.',
  intro='Sinds 2021 doe ik de volledige marketing van <strong>De Dolle Brouwers</strong>, een Belgische ambachtelijke brouwerij: van campagne en content tot event, merch en website. Ik bedenk het idee en maak het ook. Nu zoek ik een nieuwe uitdaging.',
  cta_work='Bekijk mijn werk', photo_alt='Portret van Benjamin Herteleer',
  stats=[('500+', 'tickets verkocht', 'Dolle Vrijdag, twee edities'), ('1.000+', 'bezoekers op events', 'die ik mee organiseerde en promootte'), ('36.500+', 'views op reels', 'mijn acht best bekeken reels')],
  do_h='Wat ik doe',
  do=[('Campagnes &amp; events', 'Van idee tot uitvoering: concept, planning, promotie en ticketverkoop.'),
      ('Social media &amp; content', 'Instagram, Facebook en TikTok in het Nederlands en Engels. Foto, video, copy en Meta Ads.'),
      ('Design &amp; merch', 'Huisstijl, affiches, drukwerk en merch, tot en met de drukproef.'),
      ('Web', 'Websites van structuur en copy tot design en code.')],
  work_h='Geselecteerd werk', work_sub='Vier projecten, telkens met de opdracht, mijn aanpak en wat het opleverde.',
  lab=('Opdracht', 'Aanpak', 'Resultaat'),
  cases=[
   dict(kicker='Event · 2025–2026', title='Dolle Vrijdag', sum='Een nieuw avondevent in de brouwerij, gebouwd als eigen merk.',
        q='Een jonger publiek naar De Dolle halen, mensen die de brouwerij nog niet kenden.',
        a='Naam, logo, affiches, shirts en een eigen Instagram-account, met online ticketverkoop. Na elke editie keek ik welke posts tickets verkochten en stuurde ik bij.',
        r='<b>500+ tickets</b> over twee edities, met een publiek dat voordien niet naar de brouwerij kwam.',
        media='row', imgs=[('ph-dv-crowd', 'cover', 'Publiek op Dolle Vrijdag'), ('ev-dv-poster', 'contain', 'Affiche Terraseditie 2026'), ('ev-dv-logo', 'contain', 'Logo Dolle Vrijdag'), ('ph-dv-team', 'cover', 'Het team in de Dolle Vrijdag-shirts')],
        credit="Foto's: @howmie.be"),
   dict(kicker='Website · 2026', title='dedollebrouwers.be', sum='De nieuwe website van de brouwerij, volledig zelf ontwikkeld.',
        q='Een verouderde site vervangen door één die klinkt en eruitziet als het merk, in twee talen.',
        a='Structuur, alle copy in het Nederlands en Engels, design en ontwikkeling. Met een pagina per bier, webshop, rondleidingen boeken, een verkooppuntenkaart en een maandelijkse nieuwspagina.',
        r='<b>Live</b> op dedollebrouwers.be: één plek voor bezoekers, bierfans en verkooppunten, in het Nederlands en Engels.',
        media='web', imgs=[('web-ddb-home', 'cover', 'Homepagina'), ('web-ddb-beer', 'cover', 'Bierpagina Oerbier'), ('web-ddb-nieuws', 'cover', 'Oerbier Fake Nieuws'), ('web-ddb-shop', 'cover', 'Oershop')],
        link=('https://www.dedollebrouwers.be', 'Bezoek de site')),
   dict(kicker='Merch', title='Merchcollectie', sum='Shirts, hoodies en sweaters, plus het Oeral-glas.',
        q='Fans vroegen al vier jaar naar de sweaters. Tijd voor een collectie die past bij het merk.',
        a='Ontwerpen met de figuren van de brouwerij, drukbestanden, afstemming met drukkers en drukproeven, een fotoshoot en de online lancering.',
        r='<b>Een volledige collectie</b>, gelanceerd op social media en te koop in de Oershop op de nieuwe website.',
        media='row', imgs=[('ph-merch-hoodie', 'cover', 'Hoodie met rugprint'), ('ph-merch-rack', 'cover', 'Hoodie en sweater'), ('ph-black-front', 'cover', 'Het zwarte shirt'), ('oe-glass', 'contain', 'Het Oeral-glas')],
        credit="Productfoto's: carolleservaygephotography"),
   dict(kicker='Social media &amp; content', title='Het brouwjaar online', sum='Instagram, Facebook en TikTok, het hele jaar door.',
        q='De brouwerij het hele jaar zichtbaar houden, in het Nederlands en Engels, voor fans in binnen- en buitenland.',
        a='Content volgens het brouwjaar, van Boskeun met Pasen tot Stille Nacht in december. Foto, video, copy en eigen illustraties. Ik volg op welke posts bereik halen en welke verkopen.',
        r='<b>36.500+ views</b> op mijn acht best bekeken reels. De zelfgetekende carrousel "Brewed the Dolle way" haalde <b>440+ likes in 18 uur</b>.',
        media='row', imgs=[('brew-01', 'cover', 'Carrousel Brewed the Dolle way'), ('stillenacht-illu', 'cover', 'Stille Nacht, eigen illustratie'), ('reserva', 'cover', 'Oerbier Reserva'), ('xmas-card', 'cover', 'Kerstkaart, eigen illustratie')]),
  ],
  more_h='Meer werk',
  more=[('site-home', 'cover', 'krisherteleer.com', 'Online galerij voor honderden werken van kunstenaar Kris Herteleer, met 8 collecties en een interactieve kaart.', ('https://www.krisherteleer.com', 'Bekijk de site')),
        ('ev-zv-a6', 'contain', 'Zomerse Vrijdagen &amp; Comedy Brewery', 'Illustratie, flyers, affiches en promotie voor andere events in de brouwerij.', None),
        ('d-crew', 'contain', 'Illustratie', 'Eigen tekeningen met de figuren van de brouwerij, voor posts, kaarten en shirts.', None)],
  about_h='Over mij',
  about='Ik werk het liefst waar een idee snel zichtbaar wordt: een campagne bedenken, de affiche ontwerpen, de posts schrijven, de site bouwen en mee op het event staan. Ik studeerde Communicatie &amp; Digitale Marketing aan de Arteveldehogeschool en liep stage in Lissabon. Nu zoek ik een rol in marketing, communicatie of events, bij een merk, cultuurhuis of organisatie met een eigen verhaal.',
  about_extra='Rijbewijs B · bereid om te verhuizen',
  exp_h='Ervaring', edu_h='Opleiding',
  exp=[('2021 – nu', 'Marketing &amp; communicatie', 'De Dolle Brouwers, Esen', 'Volledige marketing: campagnes, social media en Meta Ads, events, merch en de website. In de brouwerij sinds 2017.'),
       ('2024 – 2025', 'Marketing &amp; sales intern', 'Lisbon Boat Party, Lissabon', 'Social media, Meta Ads, en SEO en SEA op GetYourGuide, Viator, Klook en Shotgun.')],
  edu=[('2021 – 2025', 'Bachelor Communicatie &amp; Digitale Marketing', 'Arteveldehogeschool Gent', 'Afgestudeerd met onderscheiding.')],
  tools_h='Tools', tools='Illustrator, Photoshop, InDesign, Procreate, Canva, Meta Business Suite en Ads Manager, Shopify, Astro',
  langs_h='Talen', langs='Nederlands (moedertaal), Engels (zeer goed), Frans (basis)',
  contact_h='Laten we praten.', contact_sub='Zoek je iemand die een campagne kan bedenken én maken? Stuur me een mail of bel me gerust.',
  copy='Kopieer', copied='Gekopieerd', footer='Zelf geschreven, ontworpen en gebouwd.', close='Sluiten',
 ),
 'en': dict(
  nav=[('#werk-en', 'Work'), ('#over-en', 'About'), ('#contact-en', 'Contact')], switch='NL', cv='cv-benjamin-herteleer-en.pdf', cv_btn='Download CV',
  avail='Looking for a new role in marketing, communications or events',
  eyebrow='Benjamin Herteleer · marketing &amp; communications',
  h1='A marketer who makes things.',
  intro='Since 2021 I have run all marketing for <strong>De Dolle Brouwers</strong>, a Belgian craft brewery: from campaign and content to event, merch and website. I come up with the idea and make it too. Now I am looking for a new challenge.',
  cta_work='See my work', photo_alt='Portrait of Benjamin Herteleer',
  stats=[('500+', 'tickets sold', 'Dolle Vrijdag, two editions'), ('1,000+', 'event visitors', 'at events I helped run and promote'), ('36,500+', 'reel views', 'my eight most viewed reels')],
  do_h='What I do',
  do=[('Campaigns &amp; events', 'From idea to execution: concept, planning, promotion and ticketing.'),
      ('Social media &amp; content', 'Instagram, Facebook and TikTok in Dutch and English. Photo, video, copy and Meta Ads.'),
      ('Design &amp; merch', 'Identity, posters, print and merch, all the way to the print proof.'),
      ('Web', 'Websites from structure and copy to design and code.')],
  work_h='Selected work', work_sub='Four projects, each with the brief, my approach and what it delivered.',
  lab=('Brief', 'Approach', 'Result'),
  cases=[
   dict(kicker='Event · 2025–2026', title='Dolle Vrijdag', sum='A new evening event at the brewery, built as a brand of its own.',
        q='Bring a younger crowd to De Dolle, people who did not know the brewery yet.',
        a='Name, logo, posters, shirts and a dedicated Instagram account, with online ticketing. After each edition I looked at which posts sold tickets and adjusted.',
        r='<b>500+ tickets</b> across two editions, from a crowd that had not come to the brewery before.',
        media='row', imgs=[('ph-dv-crowd', 'cover', 'Crowd at Dolle Vrijdag'), ('ev-dv-poster', 'contain', 'Poster, 2026 edition'), ('ev-dv-logo', 'contain', 'Dolle Vrijdag logo'), ('ph-dv-team', 'cover', 'The team in Dolle Vrijdag shirts')],
        credit='Photos: @howmie.be'),
   dict(kicker='Website · 2026', title='dedollebrouwers.be', sum="The brewery's new website, fully developed by me.",
        q='Replace an outdated site with one that sounds and looks like the brand, in two languages.',
        a='Structure, all copy in Dutch and English, design and development. With a page per beer, a web shop, tour booking, a stockist map and a monthly news page.',
        r='<b>Live</b> at dedollebrouwers.be: one place for visitors, beer fans and stockists, in Dutch and English.',
        media='web', imgs=[('web-ddb-home', 'cover', 'Homepage'), ('web-ddb-beer', 'cover', 'Oerbier beer page'), ('web-ddb-nieuws', 'cover', 'Oerbier Fake Nieuws'), ('web-ddb-shop', 'cover', 'Oershop')],
        link=('https://www.dedollebrouwers.be/en', 'Visit the site')),
   dict(kicker='Merch', title='Merch collection', sum='Shirts, hoodies and sweaters, plus the Oeral glass.',
        q='Fans had been asking for the sweaters for four years. Time for a collection that fits the brand.',
        a="Designs with the brewery's characters, print files, printer coordination and proofs, a photo shoot and the online launch.",
        r='<b>A full collection</b>, launched on social media and for sale in the Oershop on the new website.',
        media='row', imgs=[('ph-merch-hoodie', 'cover', 'Hoodie with back print'), ('ph-merch-rack', 'cover', 'Hoodie and sweater'), ('ph-black-front', 'cover', 'The black shirt'), ('oe-glass', 'contain', 'The Oeral glass')],
        credit='Product photos: carolleservaygephotography'),
   dict(kicker='Social media &amp; content', title='The brewing year online', sum='Instagram, Facebook and TikTok, all year round.',
        q='Keep the brewery visible all year, in Dutch and English, for fans at home and abroad.',
        a='Content that follows the brewing year, from Boskeun at Easter to Stille Nacht in December. Photo, video, copy and my own illustrations. I track which posts get reach and which ones sell.',
        r='<b>36,500+ views</b> on my eight most viewed reels. The hand-drawn carousel "Brewed the Dolle way" got <b>440+ likes in 18 hours</b>.',
        media='row', imgs=[('brew-01', 'cover', 'Brewed the Dolle way carousel'), ('stillenacht-illu', 'cover', 'Stille Nacht, my illustration'), ('reserva', 'cover', 'Oerbier Reserva'), ('xmas-card', 'cover', 'Christmas card, my illustration')]),
  ],
  more_h='More work',
  more=[('site-home', 'cover', 'krisherteleer.com', 'Online gallery for hundreds of works by artist Kris Herteleer, with 8 collections and an interactive map.', ('https://www.krisherteleer.com', 'View the site')),
        ('ev-zv-a6', 'contain', 'Zomerse Vrijdagen &amp; Comedy Brewery', 'Illustration, flyers, posters and promotion for other events at the brewery.', None),
        ('d-crew', 'contain', 'Illustration', "My own drawings of the brewery's characters, for posts, cards and shirts.", None)],
  about_h='About me',
  about='I work best where an idea quickly becomes visible: coming up with a campaign, designing the poster, writing the posts, building the site and being there at the event. I studied Communication &amp; Digital Marketing at Arteveldehogeschool and did an internship in Lisbon. Now I am looking for a role in marketing, communications or events, at a brand, cultural venue or organisation with a story of its own.',
  about_extra='Driving licence B · open to relocating',
  exp_h='Experience', edu_h='Education',
  exp=[('2021 – present', 'Marketing &amp; communications', 'De Dolle Brouwers, Esen (BE)', 'All marketing: campaigns, social media and Meta Ads, events, merch and the website. At the brewery since 2017.'),
       ('2024 – 2025', 'Marketing &amp; sales intern', 'Lisbon Boat Party, Lisbon (PT)', 'Social media, Meta Ads, plus SEO and SEA on GetYourGuide, Viator, Klook and Shotgun.')],
  edu=[('2021 – 2025', 'Bachelor in Communication &amp; Digital Marketing', 'Arteveldehogeschool Ghent', 'Graduated with distinction.')],
  tools_h='Tools', tools='Illustrator, Photoshop, InDesign, Procreate, Canva, Meta Business Suite and Ads Manager, Shopify, Astro',
  langs_h='Languages', langs='Dutch (native), English (fluent), French (basic)',
  contact_h="Let's talk.", contact_sub='Looking for someone who can come up with a campaign and make it too? Send me an email or give me a call.',
  copy='Copy', copied='Copied', footer='Written, designed and built by me.', close='Close',
 ),
}

def img(name, fit, alt, cls='shot', sizes=''):
    w, h = IMG[name]
    return (f'<button class="{cls} {fit}" type="button" data-full="img/{name}.webp" data-cap="{alt}">'
            f'<img src="img/{name}.webp" alt="{alt}" width="{w}" height="{h}" loading="lazy"></button>')

def view(k, t):
    s = '' if k == 'nl' else '-en'
    nav = ''.join(f'<a href="{h}">{l}</a>' for h, l in t['nav'])
    stats = ''.join(f'<div class="stat"><b>{n}</b><span>{w}</span><small>{c}</small></div>' for n, w, c in t['stats'])
    do = ''.join(f'<div class="do"><span class="num">0{i+1}</span><h3>{h}</h3><p>{p}</p></div>' for i, (h, p) in enumerate(t['do']))
    cases = ''
    for i, c in enumerate(t['cases']):
        media = ''.join(img(n, f, a) for n, f, a in c['imgs'])
        link = f'<a class="btn" href="{c["link"][0]}" target="_blank" rel="noopener">{c["link"][1]} ↗</a>' if c.get('link') else ''
        credit = f'<p class="credit">{c["credit"]}</p>' if c.get('credit') else ''
        cases += (f'<article class="case"><div class="case-head"><div><p class="kicker"><span>0{i+1}</span>{c["kicker"]}</p><h3>{c["title"]}</h3><p class="sum">{c["sum"]}</p>{link}</div>'
                  f'<dl class="qar"><div><dt>{t["lab"][0]}</dt><dd>{c["q"]}</dd></div><div><dt>{t["lab"][1]}</dt><dd>{c["a"]}</dd></div><div class="res"><dt>{t["lab"][2]}</dt><dd>{c["r"]}</dd></div></dl></div>'
                  f'<div class="media {c["media"]}">{media}</div>{credit}</article>')
    more = ''
    for n, f, h, p, l in t['more']:
        link = f'<a href="{l[0]}" target="_blank" rel="noopener">{l[1]} ↗</a>' if l else ''
        more += f'<div class="more-card">{img(n, f, h)}<h3>{h}</h3><p>{p}</p>{link}</div>'
    tl = lambda rows: ''.join(f'<li><span class="when">{w}</span><div><b>{r}</b><span class="org">{o}</span><p>{d}</p></div></li>' for w, r, o, d in rows)
    return f'''<div class="lang" id="lang-{k}" lang="{k}"{'' if k == 'nl' else ' hidden'}>
<header class="top"><div class="wrap bar"><a class="mark" href="#top{s}">Benjamin Herteleer</a><nav aria-label="Menu">{nav}</nav><div class="right"><a class="btn small" href="{t['cv']}" target="_blank" rel="noopener">{t['cv_btn']}</a><button class="langbtn" type="button" data-set="{'en' if k == 'nl' else 'nl'}">{t['switch']}</button></div></div></header>
<main class="wrap">
<section class="hero" id="top{s}"><div class="hero-copy"><p class="avail"><i></i>{t['avail']}</p><p class="eyebrow">{t['eyebrow']}</p><h1>{t['h1']}</h1><p class="intro">{t['intro']}</p>
<div class="cta"><a class="btn" href="#werk{s}">{t['cta_work']}</a><a class="btn ghost" href="{t['cv']}" target="_blank" rel="noopener">{t['cv_btn']} ↗</a><a class="btn ghost" href="https://www.linkedin.com/in/benjaminherteleer" target="_blank" rel="noopener">LinkedIn ↗</a></div></div>
<figure class="hero-img"><img src="img/me.webp" alt="{t['photo_alt']}" width="506" height="1100"></figure></section>
<div class="stats">{stats}</div>
<section class="block"><h2 class="sec">{t['do_h']}</h2><div class="dos">{do}</div></section>
<section class="block" id="werk{s}"><div class="sec-row"><h2 class="sec">{t['work_h']}</h2><p>{t['work_sub']}</p></div>{cases}</section>
<section class="block"><h2 class="sec">{t['more_h']}</h2><div class="more">{more}</div></section>
<section class="block about" id="over{s}"><div><h2 class="sec">{t['about_h']}</h2><p class="about-text">{t['about']}</p><p class="extra">{t['about_extra']}</p></div>
<div class="cv-col"><h3>{t['exp_h']}</h3><ul class="tl">{tl(t['exp'])}</ul><h3>{t['edu_h']}</h3><ul class="tl">{tl(t['edu'])}</ul>
<div class="facts"><div><h3>{t['tools_h']}</h3><p>{t['tools']}</p></div><div><h3>{t['langs_h']}</h3><p>{t['langs']}</p></div></div></div></section>
</main>
<section class="contact" id="contact{s}"><div class="wrap"><h2>{t['contact_h']}</h2><p class="contact-sub">{t['contact_sub']}</p>
<div class="contact-row"><div class="copyrow"><code class="mail">benjaminherteleer@hotmail.com</code><button type="button" class="copybtn" data-copy="{t['copy']}" data-copied="{t['copied']}">{t['copy']}</button></div>
<a href="tel:+32494705597">+32 494 70 55 97</a><a href="https://www.linkedin.com/in/benjaminherteleer" target="_blank" rel="noopener">LinkedIn ↗</a><a href="{t['cv']}" target="_blank" rel="noopener">{t['cv_btn']} ↗</a></div>
<footer><span>© 2026 Benjamin Herteleer</span><span>{t['footer']}</span></footer></div></section>
</div>'''

CSS = (HERE / 'site.css').read_text(encoding='utf-8')
JS = (HERE / 'site.js').read_text(encoding='utf-8')

html = f'''<!doctype html>
<html lang="nl">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1, viewport-fit=cover">
<title>Benjamin Herteleer · marketing &amp; communicatie</title>
<meta name="description" content="Portfolio van Benjamin Herteleer, marketeer die zelf maakt: campagnes, events, social media, merch en websites, onder meer dedollebrouwers.be.">
<meta property="og:title" content="Benjamin Herteleer · marketing &amp; communicatie">
<meta property="og:description" content="Marketeer die zelf maakt: campagnes, events, social media, merch en websites.">
<link rel="preconnect" href="https://fonts.googleapis.com"><link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
<link rel="stylesheet" href="https://fonts.googleapis.com/css2?family=Bricolage+Grotesque:opsz,wght@12..96,500;12..96,800&family=Figtree:wght@400;500;600&family=IBM+Plex+Mono:wght@500&display=swap">
<style>
{CSS}</style>
</head>
<body>
{view('nl', T['nl'])}
{view('en', T['en'])}
<dialog id="lb" aria-label="Afbeelding"><form method="dialog"><button aria-label="Sluiten">×</button></form><img id="lbimg" alt=""><p id="lbcap"></p></dialog>
<script>
{JS}</script>
</body>
</html>
'''
(HERE / 'index.html').write_text(html, encoding='utf-8')
print('ok')
