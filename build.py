#!/usr/bin/env python3
"""Generate index.html for 'The Sexiest Cars in History'."""
import json, html

meta = json.load(open("meta.json"))

# key = the Wikipedia title used for the image; display fields describe the car.
CARS = [
 dict(key="Duesenberg Model J", name="Duesenberg Model J", year=1928, country="USA",
      era="Pre-War", engine="6.9L straight-8", power="265 hp", top="116 mph",
      blurb="The most extravagant American car ever built, with a straight-eight so powerful it could "
            "outrun anything of its day. Hand-built, coachbuilt and utterly gorgeous \u2014 the embodiment "
            "of Jazz Age excess."),
 dict(key="Bugatti Type 57", name="Bugatti Type 57SC Atlantic", year=1936, country="France",
      era="Pre-War", engine="3.3L supercharged straight-8", power="200 hp", top="125 mph",
      blurb="The most valuable car on Earth. Its riveted dorsal seam and teardrop bodywork make the "
            "Atlantic the Art Deco masterpiece of the automobile."),
 dict(key="Mercedes-Benz 300 SL", name="Mercedes-Benz 300 SL", year=1954, country="Germany",
      era="Golden Age", engine="3.0L straight-6", power="215 hp", top="155 mph",
      blurb="The Gullwing. A race car for the road with roof-hinged doors, direct fuel injection and a "
            "shape that still looks like the future."),
 dict(key="Citroën DS", name="Citroën DS", year=1955, country="France",
      era="Golden Age", engine="1.9L straight-4", power="75 hp", top="87 mph",
      blurb="France's spaceship. Aerodynamic to the point of alien, it floated on hydropneumatic "
            "suspension and rewrote what a car could be."),
 dict(key="Mercedes-Benz 300 SLR", name="Mercedes-Benz 300 SLR", year=1955, country="Germany",
      era="Golden Age", engine="3.0L straight-8", power="310 hp", top="180 mph",
      blurb="The car Stirling Moss drove to a legendary Mille Miglia record. A silver-arrow racer with "
            "the most beautiful curves ever drawn for competition."),
 dict(key="Aston Martin DB4 GT Zagato", name="Aston Martin DB4 GT Zagato", year=1960, country="UK",
      era="Golden Age", engine="3.7L straight-6", power="314 hp", top="154 mph",
      blurb="Just 19 were built, each a hand-beaten aluminium sculpture. The DB4 GT Zagato is the most "
            "desirable Aston Martin ever made."),
 dict(key="Jaguar E-Type", name="Jaguar E-Type", year=1961, country="UK",
      era="Golden Age", engine="3.8L straight-6", power="265 hp", top="150 mph",
      blurb="Enzo Ferrari reportedly called it \u201cthe most beautiful car ever made.\u201d Long bonnet, "
            "wire wheels and a price that made it a global sensation."),
 dict(key="Ferrari 250 GTO", name="Ferrari 250 GTO", year=1962, country="Italy",
      era="Golden Age", engine="3.0L V12", power="296 hp", top="174 mph",
      blurb="The holy grail. Only 36 were built, it won everything that mattered, and it now routinely "
            "sets records as the most expensive car sold at auction."),
 dict(key="AC Cobra", name="Shelby AC Cobra 427", year=1962, country="USA",
      era="Golden Age", engine="7.0L V8", power="425 hp", top="165 mph",
      blurb="Carroll Shelby squeezed a big American V8 into a light British roadster and created a "
            "legend. Brute force has rarely looked this good."),
 dict(key="Aston Martin DB5", name="Aston Martin DB5", year=1963, country="UK",
      era="Golden Age", engine="4.0L straight-6", power="282 hp", top="145 mph",
      blurb="Bond's car. The most famous automobile in cinema \u2014 and a superlative grand tourer in "
            "its own right."),
 dict(key="Chevrolet Corvette (C2)", name="Chevrolet Corvette Sting Ray", year=1963, country="USA",
      era="Golden Age", engine="5.4L V8", power="365 hp", top="150 mph",
      blurb="The split-window icon. Bill Mitchell's shark-nosed design gave America a genuine "
            "world-class sports car."),
 dict(key="Porsche 911", name="Porsche 911", year=1964, country="Germany",
      era="Golden Age", engine="2.0L flat-6", power="130 hp", top="130 mph",
      blurb="The shape that never needed to change. Balance, feedback and a flat-six soundtrack have "
            "kept it relevant for sixty years."),
 dict(key="Ford GT40", name="Ford GT40", year=1964, country="USA",
      era="Golden Age", engine="7.0L V8", power="485 hp", top="200 mph",
      blurb="Built to beat Ferrari at Le Mans \u2014 and it did, four years running. The GT40 is the "
            "ultimate revenge story on wheels."),
 dict(key="Lamborghini Miura", name="Lamborghini Miura", year=1966, country="Italy",
      era="Golden Age", engine="3.9L V12", power="350 hp", top="171 mph",
      blurb="The first true supercar. Mid-engined, achingly pretty, and the reason every exotic since "
            "has been measured against it."),
 dict(key="Toyota 2000GT", name="Toyota 2000GT", year=1967, country="Japan",
      era="Golden Age", engine="2.0L straight-6", power="150 hp", top="135 mph",
      blurb="Japan's first great sports car, and one of the most beautiful. A Bond car, a collector's "
            "dream, and proof that beauty has no nationality."),
 dict(key="Alfa Romeo 33 Stradale", name="Alfa Romeo 33 Stradale", year=1967, country="Italy",
      era="Golden Age", engine="2.0L V8", power="230 hp", top="160 mph",
      blurb="Arguably the most beautiful car ever built. Butterfly doors, a race-derived V8 and a price "
            "higher than a Lamborghini of the day."),
 dict(key="Nissan S30", name="Datsun 240Z", year=1969, country="Japan",
      era="Golden Age", engine="2.4L straight-6", power="151 hp", top="125 mph",
      blurb="The car that made Japanese sports cars cool. Long-nosed, affordable and beautiful enough "
            "to embarrass far more expensive machines."),
 dict(key="Lancia Stratos", name="Lancia Stratos", year=1973, country="Italy",
      era="Supercar Era", engine="2.4L V6", power="190 hp", top="144 mph",
      blurb="The first purpose-built rally car, and a wedge-shaped stunner. Ferrari V6, tiny wheelbase, "
            "enormous presence."),
 dict(key="Lamborghini Countach", name="Lamborghini Countach", year=1974, country="Italy",
      era="Supercar Era", engine="5.2L V12", power="455 hp", top="183 mph",
      blurb="The poster car of a generation. Scissor doors, razor edges and a shape that defined the "
            "word \u201csupercar\u201d for a decade."),
 dict(key="Ferrari 288 GTO", name="Ferrari 288 GTO", year=1984, country="Italy",
      era="Supercar Era", engine="2.9L twin-turbo V8", power="400 hp", top="189 mph",
      blurb="The first Ferrari \u201cspecial series\u201d hypercar, built for Group B. Twin turbos, "
            "400 hp and one of the most beautiful shapes ever to wear the badge."),
 dict(key="Porsche 959", name="Porsche 959", year=1986, country="Germany",
      era="Supercar Era", engine="2.8L twin-turbo flat-6", power="444 hp", top="197 mph",
      blurb="The most advanced car of its era \u2014 all-wheel drive, adjustable suspension and twin "
            "turbos. It rewrote what was possible."),
 dict(key="Ferrari F40", name="Ferrari F40", year=1987, country="Italy",
      era="Supercar Era", engine="2.9L twin-turbo V8", power="471 hp", top="201 mph",
      blurb="Enzo Ferrari's final masterpiece. Raw, turbocharged, Kevlar-bodied, and the last Ferrari "
            "overseen by the man himself."),
 dict(key="McLaren F1", name="McLaren F1", year=1992, country="UK",
      era="Modern Icons", engine="6.1L V12", power="627 hp", top="240 mph",
      blurb="The greatest supercar ever made. A gold-lined V12, a central driving position and a top "
            "speed that stood for a decade."),
 dict(key="Pagani Zonda", name="Pagani Zonda", year=1999, country="Italy",
      era="Modern Icons", engine="7.3L V12", power="602 hp", top="214 mph",
      blurb="A boutique hypercar of obsessive detail. Mercedes-AMG V12 power wrapped in carbon and "
            "titanium art."),
 dict(key="Ferrari Enzo", name="Ferrari Enzo", year=2002, country="Italy",
      era="Modern Icons", engine="6.0L V12", power="651 hp", top="217 mph",
      blurb="Formula 1 for the road. Named for the founder, packed with active aero and a screaming "
            "V12, and an instant modern classic."),
 dict(key="Bugatti Veyron", name="Bugatti Veyron", year=2005, country="France",
      era="Modern Icons", engine="8.0L quad-turbo W16", power="1,001 hp", top="253 mph",
      blurb="The car that redefined the possible \u2014 1,001 hp, 253 mph, and a shape that made "
            "hypercars glamorous again."),
]
CARS.sort(key=lambda c: c["year"])

def card(c):
    m = meta.get(c["key"], {})
    artist = html.escape(m.get("artist", "Unknown"))
    lic = html.escape(m.get("license", "See source"))
    page = html.escape(m.get("page", "#"))
    img = html.escape(m.get("path", f"images/{c['key']}.jpg"))
    return f"""
      <article class="card">
        <div class="thumb">
          <span class="year">{c['year']}</span>
          <span class="era">{html.escape(c['era'])}</span>
          <img src="{img}" alt="{html.escape(c['name'])}" loading="lazy" />
        </div>
        <div class="body">
          <h3>{html.escape(c['name'])}</h3>
          <div class="origin">{html.escape(c['country'])}</div>
          <ul class="specs">
            <li><span class="k">Engine</span><span class="v">{html.escape(c['engine'])}</span></li>
            <li><span class="k">Power</span><span class="v">{html.escape(c['power'])}</span></li>
            <li><span class="k">Top speed</span><span class="v">{html.escape(c['top'])}</span></li>
          </ul>
          <p class="blurb">{html.escape(c['blurb'])}</p>
          <p class="credit">Photo: {artist} \u00b7 <a href="{page}" target="_blank" rel="noopener">{lic}</a></p>
        </div>
      </article>"""

cards_html = "".join(card(c) for c in CARS)

HTML = f"""<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="UTF-8" />
<meta name="viewport" content="width=device-width, initial-scale=1.0" />
<title>The Sexiest Cars in History</title>
<meta name="description" content="A hall of fame of the most beautiful cars ever built — from the Duesenberg to the McLaren F1, with photos, specs and stories." />
<meta property="og:title" content="The Sexiest Cars in History" />
<meta property="og:description" content="A hall of fame of the most beautiful cars ever built — with photos, specs and stories." />
<meta property="og:type" content="website" />
<link rel="icon" href="data:image/svg+xml,%3Csvg xmlns='http://www.w3.org/2000/svg' viewBox='0 0 100 100'%3E%3Ctext y='.9em' font-size='90'%3E%F0%9F%8F%86%3C/text%3E%3C/svg%3E" />
<link rel="preconnect" href="https://fonts.googleapis.com" />
<link rel="preconnect" href="https://fonts.gstatic.com" crossorigin />
<link href="https://fonts.googleapis.com/css2?family=Inter:wght@400;500;600;700&family=Playfair+Display:ital,wght@0,600;0,700;0,800;1,600&display=swap" rel="stylesheet" />
<style>
  :root {{
    --bg: #0d0c0a;
    --panel: #16140f;
    --panel-2: #1c1913;
    --line: #2c2820;
    --text: #f4f1ea;
    --muted: #a49e90;
    --gold: #c9a34a;
    --gold-2: #e8c874;
  }}
  * {{ box-sizing: border-box; }}
  body {{
    margin: 0;
    background: var(--bg);
    color: var(--text);
    font-family: "Inter", -apple-system, BlinkMacSystemFont, "Segoe UI", Roboto, sans-serif;
    line-height: 1.55;
    -webkit-font-smoothing: antialiased;
  }}
  a {{ color: inherit; }}

  header.bar {{
    position: sticky; top: 0; z-index: 20;
    display: flex; align-items: center; justify-content: space-between;
    padding: 0.9rem clamp(1rem, 4vw, 3rem);
    background: rgba(13,12,10,0.75);
    backdrop-filter: blur(12px);
    border-bottom: 1px solid var(--line);
  }}
  header.bar .brand {{
    font-family: "Playfair Display", serif; font-weight: 700; font-size: 1.05rem;
    letter-spacing: 0.04em;
  }}
  header.bar .brand b {{ color: var(--gold); }}
  header.bar nav a {{
    color: var(--muted); text-decoration: none; font-size: 0.85rem; font-weight: 500; margin-left: 1.25rem;
  }}
  header.bar nav a:hover {{ color: var(--text); }}

  .hero {{
    position: relative; overflow: hidden;
    padding: clamp(3.25rem, 9vw, 6.5rem) clamp(1rem, 4vw, 3rem) clamp(2.25rem, 5vw, 3.5rem);
    border-bottom: 1px solid var(--line);
    background:
      radial-gradient(900px 400px at 20% 0%, rgba(201,163,74,0.14), transparent 62%),
      radial-gradient(700px 360px at 92% 25%, rgba(201,163,74,0.07), transparent 60%);
  }}
  .hero-inner {{ max-width: 1120px; margin: 0 auto; }}
  .kicker {{
    display: inline-block; font-size: 0.76rem; font-weight: 600; letter-spacing: 0.24em;
    text-transform: uppercase; color: var(--gold-2);
    border: 1px solid var(--line); border-radius: 999px; padding: 0.35rem 0.9rem; margin-bottom: 1.2rem;
    background: rgba(255,255,255,0.02);
  }}
  .hero h1 {{
    font-family: "Playfair Display", serif;
    font-size: clamp(2.5rem, 7.5vw, 5.4rem); line-height: 1.03; letter-spacing: -0.01em;
    margin: 0 0 1rem; font-weight: 800;
  }}
  .hero h1 em {{ font-style: italic; color: var(--gold-2); }}
  .hero p.lead {{ max-width: 690px; margin: 0 0 1.75rem; color: var(--muted); font-size: clamp(1rem, 2vw, 1.18rem); }}
  .hero .stats {{ display: flex; gap: 2.5rem; flex-wrap: wrap; }}
  .hero .stats .n {{ font-family: "Playfair Display", serif; font-size: 1.7rem; font-weight: 700; color: var(--gold-2); }}
  .hero .stats .l {{ font-size: 0.72rem; letter-spacing: 0.14em; text-transform: uppercase; color: var(--muted); }}
  .hero .stats > div {{ display: flex; flex-direction: column; }}

  main {{ max-width: 1340px; margin: 0 auto; padding: clamp(2.25rem, 4vw, 3.5rem) clamp(1rem, 4vw, 3rem); }}
  .grid {{ display: grid; grid-template-columns: repeat(auto-fill, minmax(330px, 1fr)); gap: 1.5rem; }}

  .card {{
    background: linear-gradient(180deg, var(--panel), var(--panel-2));
    border: 1px solid var(--line); border-radius: 0.9rem; overflow: hidden;
    display: flex; flex-direction: column;
    transition: transform 0.25s ease, border-color 0.25s ease, box-shadow 0.25s ease;
  }}
  .card:hover {{
    transform: translateY(-4px);
    border-color: rgba(201,163,74,0.55);
    box-shadow: 0 18px 50px rgba(0,0,0,0.6), 0 0 0 1px rgba(201,163,74,0.12);
  }}
  .thumb {{ position: relative; aspect-ratio: 16 / 10; overflow: hidden; background: #0a0908; }}
  .thumb img {{ width: 100%; height: 100%; object-fit: cover; display: block; transition: transform 0.6s ease; filter: saturate(1.02) contrast(1.02); }}
  .card:hover .thumb img {{ transform: scale(1.06); }}
  .thumb::after {{ content: ""; position: absolute; inset: 0; background: linear-gradient(to top, rgba(13,12,10,0.6), transparent 48%); pointer-events: none; }}
  .year {{
    position: absolute; top: 0.8rem; left: 0.8rem; z-index: 2;
    font-family: "Playfair Display", serif; font-weight: 700; font-size: 1.05rem;
    color: var(--gold-2); background: rgba(10,9,8,0.62); border: 1px solid rgba(201,163,74,0.4);
    border-radius: 0.45rem; padding: 0.15rem 0.55rem; backdrop-filter: blur(6px);
  }}
  .era {{
    position: absolute; top: 0.95rem; right: 0.8rem; z-index: 2;
    font-size: 0.66rem; font-weight: 600; letter-spacing: 0.1em; text-transform: uppercase;
    color: #efe7d5; background: rgba(10,9,8,0.55); border: 1px solid rgba(255,255,255,0.14);
    border-radius: 999px; padding: 0.22rem 0.6rem; backdrop-filter: blur(6px);
  }}
  .body {{ padding: 1.15rem 1.3rem 1.35rem; display: flex; flex-direction: column; flex: 1; }}
  .body h3 {{ font-family: "Playfair Display", serif; font-size: 1.32rem; margin: 0 0 0.15rem; letter-spacing: 0.005em; }}
  .origin {{ font-size: 0.72rem; letter-spacing: 0.14em; text-transform: uppercase; color: var(--gold); margin-bottom: 0.85rem; }}
  .specs {{
    list-style: none; display: grid; grid-template-columns: 1.3fr 0.9fr 0.9fr; gap: 0.5rem;
    margin: 0 0 0.95rem; padding: 0.7rem 0; border-top: 1px solid var(--line); border-bottom: 1px solid var(--line);
  }}
  .specs li {{ display: flex; flex-direction: column; gap: 0.1rem; }}
  .specs .k {{ font-size: 0.62rem; letter-spacing: 0.12em; text-transform: uppercase; color: var(--muted); }}
  .specs .v {{ font-size: 0.9rem; font-weight: 600; }}
  .specs li:nth-child(2) .v {{ color: var(--gold-2); }}
  .blurb {{ margin: 0 0 1.1rem; color: #cfc9bc; font-size: 0.92rem; }}
  .credit {{ margin-top: auto; font-size: 0.68rem; color: #6f6a5e; }}
  .credit a {{ color: #8f8877; text-decoration: none; border-bottom: 1px dotted #464034; }}
  .credit a:hover {{ color: var(--text); }}

  footer {{ border-top: 1px solid var(--line); padding: 2.5rem clamp(1rem, 4vw, 3rem); color: var(--muted); font-size: 0.82rem; }}
  footer .fin {{ max-width: 1340px; margin: 0 auto; display: flex; flex-wrap: wrap; gap: 1rem; justify-content: space-between; }}
</style>
</head>
<body>
  <header class="bar">
    <div class="brand">The <b>Hall of Fame</b></div>
    <nav><a href="#hall">The Cars</a><a href="#about">About</a></nav>
  </header>

  <section class="hero">
    <div class="hero-inner">
      <span class="kicker">A Century of Beauty</span>
      <h1>The Sexiest Cars<br /><em>in History</em></h1>
      <p class="lead">
        Twenty-six machines that defined desire across nearly a hundred years \u2014 from Art Deco
        teardrops and chrome-age grand tourers to the hypercars that rewrote the rules.
      </p>
      <div class="stats">
        <div><span class="n">26</span><span class="l">Legends</span></div>
        <div><span class="n">1928</span><span class="l">Oldest</span></div>
        <div><span class="n">2005</span><span class="l">Newest</span></div>
        <div><span class="n">8</span><span class="l">Countries</span></div>
      </div>
    </div>
  </section>

  <main id="hall">
    <div class="grid">{cards_html}
    </div>
  </main>

  <footer id="about">
    <div class="fin">
      <span>Photographs via Wikimedia Commons, used under their respective Creative Commons licences (credited on each card).</span>
      <span>A hall of fame for enthusiasts</span>
    </div>
  </footer>
</body>
</html>
"""
open("index.html", "w").write(HTML)
print("wrote index.html", len(HTML), "bytes,", len(CARS), "cars")
