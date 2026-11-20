"""FluentBooking graphics kit (DRAFT v0.1): HTML building blocks for website-illustration-style boards.

Import from a generator script:
    import sys; sys.path.insert(0, '<skill dir>/scripts')
    from kit import *

Every function returns an HTML string with inline styles. Compose a scene with absolutely
positioned pieces inside board(), then write_board() for the .dc.html canvas file and
write_preview() for the local render check (see render.py).

Colours were sampled from the FluentBooking logo and the 19 website illustrations; Jost was
matched by eye against the illustrations. Both are draft and marked so in tokens.json.
"""
import os, re, json

HERE = os.path.dirname(os.path.abspath(__file__))
ASSETS = os.path.join(HERE, '..', 'assets')

JOST = "font-family: 'Jost', 'Inter', system-ui, sans-serif"   # illustrations, headlines, copy
INT = "font-family: 'Inter', system-ui, sans-serif"            # literal product UI only

# ---------------------------------------------------------------- colours (draft)
BLUE, BLUE_DEEP, BLUE_BRIGHT = '#2653C7', '#1B48BC', '#006BFF'   # logo blue, slot text, selected day
BLUE_LINE, BLUE_TINT, BLUE_WASH = '#4587EC', '#DBE9FC', '#EEF2FC'  # card outlines, toggles, soft fills
INDIGO = '#4428BF'                                               # accent shape, one per scene
SKY, PEACH, MINT, BUTTER, AQUA_BG = '#E1F1FF', '#FFE8E1', '#E9FFE1', '#FFFCE1', '#E1FFF8'  # grounds
AQUA, SUN, ORANGE = '#B1FDEB', '#F4CF45', '#FF9900'              # decorative accents
INK, SLATE, MUTED, LINE, CELL = '#1D2432', '#5B6478', '#8E96A8', '#E5E7EB', '#F4F5F7'
GROUNDS = (SKY, PEACH, MINT, BUTTER, AQUA_BG)
CARD_SHADOW = 'box-shadow: 0 14px 32px rgba(27,72,188,0.14)'
FLOAT_SHADOW = 'box-shadow: 0 18px 40px rgba(27,72,188,0.20)'

# booking statuses (FluentBooking 2.4.0 labels) and payment statuses: text / background
STATUS = {'Scheduled': ('#0B4A8B', '#E1F1FF'), 'Rescheduled': ('#5B3A00', '#FFF4D6'), 'Completed': ('#0B4627', '#E0FAEC'),
          'Pending': ('#624C18', '#FFFAEB'), 'Cancelled': ('#681219', '#FFEBEC'), 'Rejected': ('#3A3F4B', '#EEF0F3'),
          'Paid': ('#0B4627', '#E0FAEC'), 'Refunded': ('#3A3F4B', '#EEF0F3'), 'Subscribed': ('#0B4627', '#E0FAEC')}

# ---------------------------------------------------------------- glyphs (24x24, solid, placeholder set)
# FluentBooking ships no public icon set we have files for yet. These simple solid glyphs stand in
# until official icons are supplied; never mix them with a second icon set in one graphic.
G = {
    'calendar': '<path fill-rule="evenodd" d="M7 2a1 1 0 0 1 1 1v1h8V3a1 1 0 1 1 2 0v1h1a3 3 0 0 1 3 3v12a3 3 0 0 1-3 3H5a3 3 0 0 1-3-3V7a3 3 0 0 1 3-3h1V3a1 1 0 0 1 1-1ZM4 10v9a1 1 0 0 0 1 1h14a1 1 0 0 0 1-1v-9H4Z"/>',
    'clock': '<path fill-rule="evenodd" d="M12 2a10 10 0 1 1 0 20 10 10 0 0 1 0-20Zm1 5a1 1 0 1 0-2 0v5.4l3.3 3.3a1 1 0 0 0 1.4-1.4L13 11.6V7Z"/>',
    'pin': '<path fill-rule="evenodd" d="M12 2a8 8 0 0 1 8 8c0 5.3-6.2 11.2-7.3 12a1 1 0 0 1-1.4 0C10.2 21.2 4 15.3 4 10a8 8 0 0 1 8-8Zm0 5a3 3 0 1 0 0 6 3 3 0 0 0 0-6Z"/>',
    'video': '<path d="M4 6h10a2 2 0 0 1 2 2v1.5l4.4-2.9A1 1 0 0 1 22 7.4v9.2a1 1 0 0 1-1.6.8L16 14.5V16a2 2 0 0 1-2 2H4a2 2 0 0 1-2-2V8a2 2 0 0 1 2-2Z"/>',
    'user': '<path d="M12 3a4.5 4.5 0 1 1 0 9 4.5 4.5 0 0 1 0-9Zm0 11c4.4 0 8 2.2 8 5v1a1 1 0 0 1-1 1H5a1 1 0 0 1-1-1v-1c0-2.8 3.6-5 8-5Z"/>',
    'users': '<path d="M9 4a4 4 0 1 1 0 8 4 4 0 0 1 0-8Zm7.5 1.5a3 3 0 1 1 0 6 3 3 0 0 1 0-6ZM9 13.5c3.9 0 7 1.9 7 4.5v1.5a1 1 0 0 1-1 1H3a1 1 0 0 1-1-1V18c0-2.6 3.1-4.5 7-4.5Zm8 .1c2.9.3 5 1.9 5 4v1.9a1 1 0 0 1-1 1h-3.3c.2-.3.3-.6.3-1V18c0-1.7-.4-3.1-1-4.4Z"/>',
    'rotate': '<path d="M12 4a8 8 0 0 1 7.4 5H21a1 1 0 0 1 .8 1.6l-3 4a1 1 0 0 1-1.6 0l-3-4A1 1 0 0 1 15 9h2.1A6 6 0 1 0 18 14a1 1 0 1 1 1.9.6A8 8 0 1 1 12 4Z"/>',
    'bell': '<path d="M12 2a1.5 1.5 0 0 1 1.5 1.5v.7A6 6 0 0 1 18 10v4l1.7 2.6a1 1 0 0 1-.8 1.4H5.1a1 1 0 0 1-.8-1.4L6 14v-4a6 6 0 0 1 4.5-5.8v-.7A1.5 1.5 0 0 1 12 2Zm-2.8 17h5.6a2.8 2.8 0 0 1-5.6 0Z"/>',
    'mail': '<path d="M4 5h16a2 2 0 0 1 2 2v.4l-10 6-10-6V7a2 2 0 0 1 2-2Zm-2 4.7 9.5 5.7a1 1 0 0 0 1 0L22 9.7V17a2 2 0 0 1-2 2H4a2 2 0 0 1-2-2V9.7Z"/>',
    'sms': '<path fill-rule="evenodd" d="M5 3h14a2 2 0 0 1 2 2v10a2 2 0 0 1-2 2H8.2L3 21.2V5a2 2 0 0 1 2-2Zm3 6.5a1.5 1.5 0 1 0 0 3 1.5 1.5 0 0 0 0-3Zm4 0a1.5 1.5 0 1 0 0 3 1.5 1.5 0 0 0 0-3Zm4 0a1.5 1.5 0 1 0 0 3 1.5 1.5 0 0 0 0-3Z"/>',
    'wa': '<path fill-rule="evenodd" d="M12 2a10 10 0 0 0-8.6 15.1L2 22l5-1.3A10 10 0 1 0 12 2Zm-3.3 5.3c.3 0 .6 0 .8.5l1 2.2c.1.3 0 .5-.1.7l-.7.8c-.2.2-.2.4 0 .7.6 1 1.4 1.8 2.4 2.4.3.2.5.2.7 0l.8-.9c.2-.2.4-.3.7-.2l2.2 1c.4.2.5.4.4.8-.2 1.2-1.2 2-2.4 2-3.9-.3-7.2-3.6-7.5-7.5 0-1.2.8-2.3 1.7-2.5Z"/>',
    'card': '<path fill-rule="evenodd" d="M4 4h16a2 2 0 0 1 2 2v2H2V6a2 2 0 0 1 2-2Zm-2 7h20v7a2 2 0 0 1-2 2H4a2 2 0 0 1-2-2v-7Zm3 4.5a1 1 0 0 0 0 2h4a1 1 0 1 0 0-2H5Z"/>',
    'check': '<path d="M12 2a10 10 0 1 1 0 20 10 10 0 0 1 0-20Zm4.7 6.3a1 1 0 0 0-1.4 0L10.5 13l-1.8-1.7a1 1 0 0 0-1.4 1.4l2.5 2.5a1 1 0 0 0 1.4 0l5.5-5.5a1 1 0 0 0 0-1.4Z"/>',
    'tag': '<path fill-rule="evenodd" d="M3 4a1 1 0 0 1 1-1h7.6a2 2 0 0 1 1.4.6l8.4 8.4a2 2 0 0 1 0 2.8l-6.6 6.6a2 2 0 0 1-2.8 0L3.6 13A2 2 0 0 1 3 11.6V4Zm4.5 2a1.5 1.5 0 1 0 0 3 1.5 1.5 0 0 0 0-3Z"/>',
    'globe': '<path fill-rule="evenodd" d="M12 2a10 10 0 1 1 0 20 10 10 0 0 1 0-20Zm-2 2.3A8 8 0 0 0 4.1 11h3.9c.1-2.5.8-4.9 2-6.7ZM4.1 13A8 8 0 0 0 10 19.7c-1.2-1.8-1.9-4.2-2-6.7H4.1Zm5.9 0c.2 2.6 1 4.8 2 6.3 1-1.5 1.8-3.7 2-6.3h-4Zm4-2c-.2-2.6-1-4.8-2-6.3-1 1.5-1.8 3.7-2 6.3h4Zm0 8.7a8 8 0 0 0 5.9-6.7H16c-.1 2.5-.8 4.9-2 6.7ZM19.9 11A8 8 0 0 0 14 4.3c1.2 1.8 1.9 4.2 2 6.7h3.9Z"/>',
}

def glyph(name, px, color='currentColor'):
    return f'<svg width="{px}" height="{px}" viewBox="0 0 24 24" fill="{color}" aria-hidden="true">{G[name]}</svg>'

def svg_file(path, px):
    """Inline a full-colour SVG file (brand marks, logos) at a square size."""
    s = open(path).read()
    s = re.sub(r'<metadata>.*?</metadata>', '', s, flags=re.S).replace('<?xml version="1.0" encoding="UTF-8"?>', '')
    s = re.sub(r'(<svg[^>]*?)\swidth="[^"]*"', r'\1', s, count=1)
    s = re.sub(r'(<svg[^>]*?)\sheight="[^"]*"', r'\1', s, count=1)
    return s.replace('<svg', f'<svg width="{px}" height="{px}"', 1)

# Official FluentBooking marks (Brand Assets, Updated Logo 2025). These files are the only FluentBooking logo
# and icon a graphic may show. Never redraw, retype or approximate a mark; if a needed mark is not here, stop and
# ask the user for the file.
BRAND_FILES = {
    'icon': 'fluentbooking_primary_icon', 'icon-secondary': 'fluentbooking_secondary_icon',
    'icon-dark': 'fluentbooking_monotone_dark_icon', 'icon-light': 'fluentbooking_monotone_light_icon',
    'logo': 'fluentbooking_primary_logo', 'logo-secondary': 'fluentbooking_secondary_logo',
    'logo-dark': 'fluentbooking_monotone_dark_logo', 'logo-light': 'fluentbooking_monotone_light_logo',
}

def _brand_path(variant):
    if variant not in BRAND_FILES:
        raise ValueError(f'No official FluentBooking mark called {variant!r}. Ask the user for the file instead of drawing one.')
    path = os.path.join(ASSETS, 'brand', BRAND_FILES[variant] + '.svg')
    if not os.path.exists(path):
        raise FileNotFoundError(f'{path} is missing. Ask the user for the official file.')
    return path

def brand(variant='icon', px=40):
    """Official FluentBooking icon (square-ish, 286x300), px = height."""
    s = open(_brand_path(variant)).read()
    s = re.sub(r'(<svg[^>]*?)\swidth="[^"]*"', r'\1', s, count=1)
    s = re.sub(r'(<svg[^>]*?)\sheight="[^"]*"', r'\1', s, count=1)
    return s.replace('<svg', f'<svg height="{px}" width="{round(px*286/300)}" aria-label="FluentBooking"', 1)

def brand_logo(variant='logo', height=40):
    """Official FluentBooking logo (icon plus wordmark, 318x59). Primary on light grounds."""
    s = open(_brand_path(variant)).read()
    s = re.sub(r'(<svg[^>]*?)\swidth="[^"]*"', r'\1', s, count=1)
    s = re.sub(r'(<svg[^>]*?)\sheight="[^"]*"', r'\1', s, count=1)
    return s.replace('<svg', f'<svg height="{height}" width="{round(height*318/59)}" role="img" aria-label="FluentBooking"', 1)

def logo(name, px):
    return svg_file(os.path.join(ASSETS, 'logos', name + '.svg'), px)

# ---------------------------------------------------------------- small parts
def pos(x, y, html, w=None, z=None):
    ws = f' width: {w}px;' if w else ''
    zs = f' z-index: {z};' if z is not None else ''
    return f'<div style="position: absolute; left: {x}px; top: {y}px;{ws}{zs}">{html}</div>'

def badge(text, fg, bg, size=10):
    return f'<span style="{JOST}; font-size: {size}px; font-weight: 600; color: {fg}; background: {bg}; padding: 3px 9px; border-radius: 999px; white-space: nowrap; line-height: 1.3">{text}</span>'

def status(name, size=10):
    fg, bg = STATUS[name]; return badge(name, fg, bg, size)

SHOW_PRO = False  # PRO badges are off unless the request asks for them: set kit.SHOW_PRO = True

def pro(size=9):
    """Pro marker for features the brain records in FluentBooking Pro. Draws nothing unless SHOW_PRO is True."""
    if not SHOW_PRO:
        return ''
    return f'<span style="{JOST}; font-size: {size}px; font-weight: 700; letter-spacing: 0.06em; color: #FFFFFF; background: {INDIGO}; padding: 2px 7px; border-radius: 999px; white-space: nowrap">PRO</span>'

MERGE = {}  # hole name -> literal merge tag; write_board/write_preview fill them in

def merge(tag, size=10.5):
    """A real FluentBooking merge tag, shown as a chip. Only tags listed in product-facts.md.
    Curly braces would be read as canvas holes, so the tag renders through a renderVals() value."""
    key = 'mt_' + re.sub(r'[^a-z0-9]+', '_', tag.lower()).strip('_')
    MERGE[key] = tag
    return f'<span style="{INT}; font-size: {size}px; font-weight: 500; color: {BLUE_DEEP}; background: {BLUE_TINT}; padding: 1px 6px; border-radius: 6px; white-space: nowrap">{{{{{key}}}}}</span>'

def tile(name, bg, px=34, gpx=None, fg='#FFFFFF', r=10):
    g = gpx or round(px * 0.55)
    return (f'<span style="width: {px}px; height: {px}px; flex-shrink: 0; border-radius: {r}px; background: {bg}; color: {fg}; '
            f'display: flex; align-items: center; justify-content: center">{glyph(name, g)}</span>')

def ring(name, px=44, color=BLUE_LINE):
    """Round outlined badge used on dashed connectors (channel or integration marker)."""
    return (f'<span style="width: {px}px; height: {px}px; box-sizing: border-box; border-radius: 999px; background: #FFFFFF; border: 2px solid {color}; '
            f'color: {BLUE}; display: flex; align-items: center; justify-content: center">{glyph(name, round(px*0.48))}</span>')

def avatar(initials, bg=PEACH, fg='#5A3A2A', px=36):
    """Invented person, drawn as initials. No photos of real people."""
    return (f'<span style="width: {px}px; height: {px}px; flex-shrink: 0; border-radius: 999px; background: {bg}; color: {fg}; display: flex; '
            f'align-items: center; justify-content: center; {JOST}; font-size: {round(px*0.36)}px; font-weight: 600">{initials}</span>')

def toggle(on=True, s=1.0):
    w, h = round(30*s), round(17*s); d = h - 4
    return (f'<span style="width: {w}px; height: {h}px; box-sizing: border-box; border-radius: 999px; background: {BLUE_LINE if on else "#D5D9E0"}; '
            f'display: flex; align-items: center; padding: 2px; justify-content: {"flex-end" if on else "flex-start"}; flex-shrink: 0">'
            f'<span style="width: {d}px; height: {d}px; border-radius: 999px; background: #FFFFFF"></span></span>')

def card(x, y, w, inner, h=None, pad='14px 16px', r=16, outline=True, shadow=CARD_SHADOW, bg='#FFFFFF', z=None):
    hs = f' height: {h}px;' if h else ''
    ol = f'border: 2px solid {BLUE_LINE};' if outline else 'border: 1px solid #ECEEF2;'
    zs = f' z-index: {z};' if z is not None else ''
    return (f'<div style="position: absolute; left: {x}px; top: {y}px; width: {w}px;{hs}{zs} box-sizing: border-box; background: {bg}; {ol} '
            f'border-radius: {r}px; padding: {pad}; {shadow}; overflow: hidden; {JOST}; color: {INK}">{inner}</div>')

def brand_tile(x, y, px=64):
    """FluentBooking icon on a white tile with the blue outline, overlapping a corner."""
    return (f'<div style="position: absolute; left: {x}px; top: {y}px; width: {px}px; height: {px}px; box-sizing: border-box; background: #FFFFFF; '
            f'border: 2px solid {BLUE_LINE}; border-radius: {round(px*0.26)}px; display: flex; align-items: center; justify-content: center; {FLOAT_SHADOW}">'
            f'{brand("icon", round(px*0.56))}</div>')

def dash_curve(x1, y1, x2, y2, color=BLUE_LINE, bend=0.5, w=None, h=None, z=None):
    """Dashed curved connector drawn in an SVG covering the board. Pass the board size as w, h."""
    w = w or max(x1, x2) + 20; h = h or max(y1, y2) + 20
    cx = x1 + (x2 - x1) * bend
    zs = f' z-index: {z};' if z is not None else ''
    return (f'<svg style="position: absolute; left: 0; top: 0; overflow: visible;{zs}" width="{w}" height="{h}" aria-hidden="true">'
            f'<path d="M{x1} {y1} C {cx} {y1}, {cx} {y2}, {x2} {y2}" fill="none" stroke="{color}" stroke-width="2.5" stroke-dasharray="7 7" stroke-linecap="round"/></svg>')

def blob(x, y, w, h, color, r=None, z=None, solid=0.5):
    """Soft background shape in a second palette colour that fades out to nothing at its edge (no hard rounded
    outline). solid = how much of the radius stays full colour before the fade starts. r is kept for old calls."""
    zs = f' z-index: {z};' if z is not None else ''
    return (f'<div data-deco="1" style="position: absolute; left: {x}px; top: {y}px; width: {w}px; height: {h}px; '
            f'background: radial-gradient(closest-side, {color} 0%, {color} {round(solid*100)}%, transparent 100%);{zs}"></div>')

def sparkle(x, y, px=28, color=INK):
    """Four-point star. Milestone and celebration social posts only; never as filler in a scene."""
    return (f'<svg style="position: absolute; left: {x}px; top: {y}px" width="{px}" height="{px}" viewBox="0 0 24 24" aria-hidden="true">'
            f'<path d="M12 0c.6 6.4 5.6 11.4 12 12-6.4.6-11.4 5.6-12 12-.6-6.4-5.6-11.4-12-12C6.4 11.4 11.4 6.4 12 0Z" fill="{color}"/></svg>')

# ---------------------------------------------------------------- booking page (the main anchor)
DAYS_MO = ['MO', 'TU', 'WE', 'TH', 'FR', 'SA', 'SU']

def month_grid(w, month='October', year='2028', first=6, days=31, selected=3, available=(), s=1.0):
    """Month grid as on the booking page. first = column of day 1 (0 = Monday). available = days with open slots."""
    cell = (w - 6*6*s) / 7
    head = ''.join(f'<span style="width: {cell:.1f}px; text-align: center; font-size: {11*s:.1f}px; font-weight: 500; color: {SLATE}">{d}</span>' for d in DAYS_MO)
    cells = [''] * first + list(range(1, days + 1))
    while len(cells) % 7: cells.append('')
    rows = ''
    for r in range(len(cells) // 7):
        row = ''
        for c in cells[r*7:(r+1)*7]:
            if c == '':
                row += f'<span style="width: {cell:.1f}px; height: {cell*0.86:.1f}px"></span>'; continue
            if c == selected:
                st = f'background: {BLUE_BRIGHT}; color: #FFFFFF; font-weight: 600'
            elif c in available:
                st = f'background: {CELL}; color: {INK}; font-weight: 500'
            else:
                st = f'background: transparent; color: #B3B9C6; font-weight: 400'
            dot = (f'<span style="position: absolute; bottom: {4*s:.0f}px; width: {4*s:.1f}px; height: {4*s:.1f}px; border-radius: 9px; background: #FFFFFF"></span>' if c == selected else '')
            row += (f'<span style="position: relative; width: {cell:.1f}px; height: {cell*0.86:.1f}px; border-radius: {7*s:.0f}px; display: flex; align-items: center; '
                    f'justify-content: center; font-size: {12.5*s:.1f}px; {st}">{c}{dot}</span>')
        rows += f'<div style="display: flex; gap: {6*s:.0f}px">{row}</div>'
    return (f'<div style="width: {w}px; display: flex; flex-direction: column; gap: {6*s:.0f}px; {JOST}; color: {INK}">'
            f'<div style="font-size: {16*s:.1f}px; font-weight: 600; margin-bottom: {4*s:.0f}px">{month} <span style="color: {MUTED}; font-weight: 500">{year}</span></div>'
            f'<div style="display: flex; gap: {6*s:.0f}px; margin-bottom: {2*s:.0f}px">{head}</div>{rows}</div>')

def slot_list(w, date_label, slots, s=1.0):
    """Time slots for the picked day. slots: list of (time, spots_text, selected)."""
    items = ''
    for t, spots, sel in slots:
        if sel:
            items += (f'<div style="display: flex; height: {38*s:.0f}px; border-radius: {8*s:.0f}px; overflow: hidden; border: 1.5px solid {BLUE_BRIGHT}">'
                      f'<span style="flex: 1; display: flex; align-items: center; padding-left: {12*s:.0f}px; font-size: {12.5*s:.1f}px; font-weight: 600; color: {BLUE_DEEP}; background: {BLUE_WASH}">{t}</span>'
                      f'<span style="width: 44%; display: flex; align-items: center; justify-content: center; background: {BLUE_DEEP}; color: #FFFFFF; font-size: {12*s:.1f}px; font-weight: 600">Next</span></div>')
        else:
            items += (f'<div style="display: flex; justify-content: space-between; align-items: center; height: {38*s:.0f}px; box-sizing: border-box; padding: 0 {12*s:.0f}px; '
                      f'border-radius: {8*s:.0f}px; border: 1px solid {LINE}; font-size: {12.5*s:.1f}px">'
                      f'<span style="font-weight: 500; color: {INK}">{t}</span><span style="font-size: {10.5*s:.1f}px; color: {SLATE}">{spots}</span></div>')
    return (f'<div style="width: {w}px; display: flex; flex-direction: column; gap: {7*s:.0f}px; {JOST}">'
            f'<div style="font-size: {12.5*s:.1f}px; font-weight: 600; color: {INK}; margin-bottom: {2*s:.0f}px">{date_label}</div>{items}</div>')

def host_panel(w, host, initials, event, duration, location, loc_icon='pin', av_bg=PEACH, s=1.0, extra=''):
    row = lambda g, t: (f'<div style="display: flex; align-items: center; gap: {6*s:.0f}px; font-size: {11.5*s:.1f}px; color: {SLATE}">'
                        f'<span style="color: {SLATE}; display: flex">{glyph(g, round(14*s))}</span>{t}</div>')
    return (f'<div style="width: {w}px; display: flex; flex-direction: column; gap: {7*s:.0f}px; {JOST}; color: {INK}">'
            f'{avatar(initials, av_bg, px=round(52*s))}'
            f'<span style="font-size: {12*s:.1f}px; color: {SLATE}; margin-top: {2*s:.0f}px">{host}</span>'
            f'<span style="font-size: {19*s:.1f}px; font-weight: 600; line-height: 1.15">{event}</span>'
            f'{row("clock", duration)}{row(loc_icon, location)}{extra}</div>')

def booking_page(x, y, w, h, host='Maya Ortiz', initials='MO', event='Morning Flow Class', duration='60 Min',
                 location='In Person (Organizer Address)', loc_icon='pin', month='October', year='2028', first=6, selected=3,
                 available=(3, 4, 5, 10, 11, 12, 17, 18, 19, 24, 25, 26), date_label='Tue, October 3',
                 slots=(('7:00 AM', '4 spots left', False), ('8:30 AM', '2 spots left', True), ('6:00 PM', '9 spots left', False)),
                 timezone='Asia/Dhaka', s=1.0, z=None, show_slots=True, description=''):
    """The public booking page: host panel, month grid with timezone, slots for the picked day.
    Pass h=None so the card is sized to its content: a recreated screen never carries padded white space."""
    pad = 22*s
    hp = 150*s
    gw = 290*s
    tz = (f'<div style="margin-top: {14*s:.0f}px; display: flex; flex-direction: column; gap: {5*s:.0f}px">'
          f'<span style="font-size: {11*s:.1f}px; font-weight: 500; color: {SLATE}">Time Zone</span>'
          f'<span style="display: flex; align-items: center; gap: {6*s:.0f}px; height: {32*s:.0f}px; box-sizing: border-box; padding: 0 {10*s:.0f}px; border: 1px solid {LINE}; '
          f'border-radius: {8*s:.0f}px; font-size: {11.5*s:.1f}px; color: {INK}"><span style="color: {SLATE}; display: flex">{glyph("globe", round(13*s))}</span>{timezone}</span></div>')
    grid = f'<div style="display: flex; flex-direction: column">{month_grid(gw, month, year, first, 31, selected, available, s)}{tz}</div>'
    sl = slot_list(round(170*s), date_label, slots, s) if show_slots else ''
    desc = (f'<span style="margin-top: {6*s:.0f}px; font-size: {11.5*s:.1f}px; line-height: 1.5; color: {SLATE}">{description}</span>' if description else '')
    inner = (f'<div style="display: flex; gap: {26*s:.0f}px; align-items: flex-start">'
             f'{host_panel(hp, host, initials, event, duration, location, loc_icon, s=s, extra=desc)}'
             f'<div style="width: 1px; align-self: stretch; background: {LINE}"></div>{grid}{sl}</div>')
    return card(x, y, w, inner, h=h, pad=f'{pad:.0f}px', r=round(22*s), z=z)

# ---------------------------------------------------------------- event types
TYPE_ICON = {'One-to-One': ('user', 'user'), 'Group': ('user', 'users'), 'Round Robin': ('rotate', 'user'), 'Collective': ('users', 'user')}

def type_mark(kind, px=14, color=SLATE):
    a, b = TYPE_ICON[kind]
    return (f'<span style="display: inline-flex; align-items: center; gap: 2px; color: {color}">{glyph(a, px)}'
            f'<svg width="{px}" height="{px}" viewBox="0 0 24 24" aria-hidden="true"><path d="M5 12h12m-4-4 4 4-4 4" fill="none" stroke="{color}" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"/></svg>'
            f'{glyph(b, px)}</span>')

def event_card(x, y, w, name, dot, duration, kind, location, loc_icon='pin', is_pro=False, s=1.0, z=None):
    """Event type card as on Calendars: colour dot, name, duration, meeting type, location."""
    meta = lambda inner: f'<span style="display: flex; align-items: center; gap: {5*s:.0f}px; font-size: {11.5*s:.1f}px; color: {SLATE}; white-space: nowrap">{inner}</span>'
    inner = (f'<div style="display: flex; align-items: center; gap: {9*s:.0f}px">'
             f'<span style="width: {11*s:.0f}px; height: {11*s:.0f}px; border-radius: 99px; background: {dot}; flex-shrink: 0"></span>'
             f'<span style="flex: 1; font-size: {16*s:.1f}px; font-weight: 600; white-space: nowrap">{name}</span>{pro() if is_pro else ""}'
             f'<span style="color: {MUTED}; font-size: {16*s:.0f}px; letter-spacing: 1px">···</span></div>'
             f'<div style="display: flex; gap: {14*s:.0f}px; margin-top: {10*s:.0f}px; padding-bottom: {12*s:.0f}px; border-bottom: 1px solid {LINE}">'
             f'{meta(glyph("clock", round(14*s)) + duration)}{meta(type_mark(kind, round(13*s)) + kind)}{meta(glyph(loc_icon, round(14*s)) + location)}</div>'
             f'<div style="display: flex; justify-content: space-between; margin-top: {11*s:.0f}px">'
             f'<span style="font-size: {11.5*s:.1f}px; font-weight: 500; color: {BLUE_DEEP}; background: {BLUE_WASH}; padding: {6*s:.0f}px {12*s:.0f}px; border-radius: {8*s:.0f}px">Copy Link</span>'
             f'<span style="font-size: {11.5*s:.1f}px; font-weight: 500; color: {INK}; border: 1px solid {LINE}; padding: {5*s:.0f}px {12*s:.0f}px; border-radius: {8*s:.0f}px">Edit</span></div>')
    return card(x, y, w, inner, pad=f'{15*s:.0f}px {17*s:.0f}px', r=round(16*s), z=z)

def type_chooser(x, y, w, kinds=(('Round Robin', 'One rotating host with One invitee', True), ('Collective', 'Multiple hosts with One invitee', True)), s=1.0, z=None):
    """Rows from the Add Team dialog (team types are Pro). Each row is its own floating card."""
    rows = ''
    for k, line, is_pro in kinds:
        rows += (f'<div style="display: flex; align-items: center; gap: {12*s:.0f}px; padding: {12*s:.0f}px {14*s:.0f}px; border: 2px solid {BLUE_LINE}; border-radius: {14*s:.0f}px; background: #FFFFFF; {FLOAT_SHADOW}">'
                 f'{type_mark(k, round(15*s), INK)}<div style="flex: 1; display: flex; flex-direction: column; gap: {2*s:.0f}px">'
                 f'<span style="display: flex; align-items: center; gap: {6*s:.0f}px; font-size: {14*s:.1f}px; font-weight: 600">{k}{pro() if is_pro else ""}</span>'
                 f'<span style="font-size: {10.5*s:.1f}px; color: {SLATE}">{line}</span></div>'
                 f'<span style="color: {INK}; font-size: {15*s:.0f}px">→</span></div>')
    zs = f' z-index: {z};' if z is not None else ''
    return f'<div style="position: absolute; left: {x}px; top: {y}px; width: {w}px;{zs} display: flex; flex-direction: column; gap: {10*s:.0f}px; {JOST}; color: {INK}">{rows}</div>'

# ---------------------------------------------------------------- notifications and reminders
def notif_list(x, y, w, rows, title='Notification Settings', s=1.0, z=None, button=True):
    """Email Notification list. rows: (label, on). Labels must be real ones from product-facts.md."""
    r = ''
    for label, on in rows:
        r += (f'<div style="display: flex; align-items: center; gap: {10*s:.0f}px; padding: {10*s:.0f}px 0; border-bottom: 1px solid {LINE}">'
              f'<span style="flex: 1; font-size: {12.5*s:.1f}px; color: {INK}; white-space: nowrap">{label}</span>'
              f'<span style="font-size: {11*s:.1f}px; color: {INK}; border: 1px solid {LINE}; padding: {3*s:.0f}px {10*s:.0f}px; border-radius: {7*s:.0f}px">Edit</span>{toggle(on, s)}</div>')
    btn = (f'<div style="display: flex; justify-content: flex-end; margin-top: {12*s:.0f}px"><span style="font-size: {12*s:.1f}px; font-weight: 500; color: #FFFFFF; '
           f'background: {BLUE_LINE}; padding: {7*s:.0f}px {14*s:.0f}px; border-radius: {8*s:.0f}px">Save Changes</span></div>') if button else ''
    inner = f'<div style="font-size: {14*s:.1f}px; font-weight: 600; padding-bottom: {6*s:.0f}px; border-bottom: 1px solid {LINE}">{title}</div>{r}{btn}'
    return card(x, y, w, inner, pad=f'{14*s:.0f}px {18*s:.0f}px', r=round(16*s), z=z)

def reminder_card(x, y, w, initials, headline, when_line, av_bg=AQUA, s=1.0, z=None):
    """A sent reminder, as the illustrations show it: avatar, headline, When block."""
    inner = (f'<div style="display: flex; gap: {14*s:.0f}px; align-items: flex-start">{avatar(initials, av_bg, "#0E4F43", round(46*s))}'
             f'<div style="display: flex; flex-direction: column; gap: {7*s:.0f}px; min-width: 0">'
             f'<span style="font-size: {15*s:.1f}px; font-weight: 600; line-height: 1.25">{headline}</span>'
             f'<span style="font-size: {13*s:.1f}px; font-weight: 600; margin-top: {2*s:.0f}px">When</span>'
             f'<span style="font-size: {11.5*s:.1f}px; color: {SLATE}; line-height: 1.4">{when_line}</span></div></div>')
    return card(x, y, w, inner, pad=f'{16*s:.0f}px {18*s:.0f}px', r=round(18*s), shadow=FLOAT_SHADOW, z=z)

def timing_chip(x, y, w, value='15', unit='Minutes Before', s=1.0, z=None):
    inner = (f'<div style="font-size: {13*s:.1f}px; font-weight: 600; margin-bottom: {8*s:.0f}px">Timing</div>'
             f'<div style="display: flex; border: 1px solid {LINE}; border-radius: {8*s:.0f}px; overflow: hidden; font-size: {13*s:.1f}px">'
             f'<span style="width: 34%; text-align: center; padding: {8*s:.0f}px 0; border-right: 1px solid {LINE}">{value}</span>'
             f'<span style="flex: 1; padding: {8*s:.0f}px {12*s:.0f}px; background: {CELL}; display: flex; justify-content: space-between">{unit}<span style="color: {MUTED}">⌄</span></span></div>')
    return card(x, y, w, inner, pad=f'{12*s:.0f}px {14*s:.0f}px', r=round(14*s), z=z)

def booking_thread(lead='15 minutes', reminder_at='8:15 AM', name='Lena', event='Morning Flow Class', host='Maya',
                   when='Tue, October 3 at 8:30 AM', link='stillpoint.yoga/r/8K2'):
    """A believable message thread for a phone: the confirmation the day before, the client's reply, then the
    reminder with its reschedule link. Keeps the reminder time consistent with the lead time."""
    return [('time', 'Yesterday 6:02 PM'),
            ('in', f'Your {event} with {host} is booked for {when}. See you at the studio!'),
            ('out', 'Thank you, see you there!'),
            ('time', f'Today {reminder_at}'),
            ('in', f'Hi {name}, your {event} with {host} starts in {lead}.'),
            ('in', f'Need a different time? Reschedule here: <span style="color: {BLUE_DEEP}">{link}</span>')]

def phone(x, y, w, h, ch='wa', sender='Stillpoint Yoga', sender_initial='S', messages=None, s=1.0, z=None):
    """Phone with an SMS or WhatsApp notification sent through Twilio (Pro). messages: ('time', text), ('in', html)
    for the business, ('out', html) for the client; a plain string counts as 'in'. Fill the screen with a believable
    thread (booking_thread()) so no blank screen shows; the thread is anchored to the bottom like a real chat."""
    wa = ch == 'wa'
    screen = '#EFE9DF' if wa else '#FFFFFF'
    chip = badge('WhatsApp', '#0B4627', '#E0FAEC', round(9*s)) if wa else badge('SMS', BLUE_DEEP, BLUE_TINT, round(9*s))
    items = [m if isinstance(m, tuple) else ('in', m) for m in (messages or booking_thread())]
    bub = ''
    for kind, m in items:
        if kind == 'time':
            bub += f'<span style="align-self: center; font-size: {9.5*s:.1f}px; color: {MUTED}; margin: {3*s:.0f}px 0">{m}</span>'
        elif kind == 'out':
            bub += (f'<div style="align-self: flex-end; max-width: 80%; background: {"#D3F5CE" if wa else BLUE_LINE}; color: {INK if wa else "#FFFFFF"}; '
                    f'border-radius: {14*s:.0f}px {14*s:.0f}px {4*s:.0f}px {14*s:.0f}px; padding: {8*s:.0f}px {11*s:.0f}px; font-size: {11*s:.1f}px; line-height: 1.45">{m}</div>')
        else:
            bub += (f'<div style="align-self: flex-start; max-width: 86%; background: {"#FFFFFF" if wa else CELL}; border-radius: {14*s:.0f}px {14*s:.0f}px {14*s:.0f}px {4*s:.0f}px; '
                    f'padding: {9*s:.0f}px {11*s:.0f}px; font-size: {11*s:.1f}px; line-height: 1.45; color: {INK}; box-shadow: 0 1px 2px rgba(0,0,0,0.06)">{m}</div>')
    zs = f' z-index: {z};' if z is not None else ''
    return (f'<div style="position: absolute; left: {x}px; top: {y}px; width: {w}px; height: {h}px;{zs} box-sizing: border-box; background: #14203F; border-radius: {32*s:.0f}px; '
            f'padding: {7*s:.0f}px; {FLOAT_SHADOW}; {JOST}">'
            f'<div style="height: 100%; border-radius: {26*s:.0f}px; background: {screen}; overflow: hidden; display: flex; flex-direction: column">'
            f'<div style="display: flex; justify-content: center; padding-top: {7*s:.0f}px"><span style="width: {58*s:.0f}px; height: {15*s:.0f}px; border-radius: 99px; background: #14203F"></span></div>'
            f'<div style="display: flex; align-items: center; gap: {8*s:.0f}px; padding: {9*s:.0f}px {12*s:.0f}px; background: #FFFFFF; border-bottom: 1px solid {LINE}">'
            f'{avatar(sender_initial, "#2F5D50", "#FFFFFF", round(28*s))}<span style="flex: 1; font-size: {12.5*s:.1f}px; font-weight: 600; color: {INK}">{sender}</span>{chip}</div>'
            f'<div style="flex: 1; display: flex; flex-direction: column; gap: {7*s:.0f}px; padding: {12*s:.0f}px {10*s:.0f}px">{bub}</div></div></div>')

# ---------------------------------------------------------------- after the booking
def activity_timeline(x, y, w, rows, title='Meeting Activities', s=1.0, z=None):
    """Booking detail timeline. rows: (glyph, tile colour, title, line, time). Titles follow the real log lines."""
    r = ''
    n = len(rows)
    for i, (g, col, t, line, when) in enumerate(rows):
        rail = (f'<span style="position: absolute; left: {15*s:.0f}px; top: {34*s:.0f}px; bottom: -{4*s:.0f}px; border-left: 2px dashed {BLUE_TINT}"></span>' if i < n - 1 else '')
        r += (f'<div style="position: relative; display: flex; gap: {12*s:.0f}px; padding-bottom: {14*s:.0f}px">{rail}{tile(g, col, round(32*s), r=round(9*s))}'
              f'<div style="flex: 1; display: flex; flex-direction: column; gap: {2*s:.0f}px; min-width: 0">'
              f'<span style="font-size: {13*s:.1f}px; font-weight: 600; line-height: 1.25">{t}</span>'
              f'<span style="font-size: {11*s:.1f}px; color: {SLATE}; line-height: 1.35">{line}</span></div>'
              f'<span style="font-size: {10.5*s:.1f}px; color: {MUTED}; white-space: nowrap">{when}</span></div>')
    inner = f'<div style="font-size: {15*s:.1f}px; font-weight: 600; margin-bottom: {14*s:.0f}px">{title}</div>{r}'
    return card(x, y, w, inner, pad=f'{16*s:.0f}px {18*s:.0f}px {4*s:.0f}px', r=round(18*s), z=z)

def booking_timeline(x, y, rows, card_w=330, gap=22, node=44, line_color=BLUE_LINE, s=1.0):
    """A visual timeline of what happens after a booking: a dashed rail with round nodes, each node
    joined to its own outlined card. rows: (node_html_or_glyph, node_colour, title, line, time, badge_html).
    A glyph name draws a solid round node; pass ready HTML (an avatar) for the first node.
    Returns (html, list of card boxes as (left, top, right, bottom)) so connectors can attach."""
    out, boxes = [], []
    n = round(node*s); cy = y; heights = []
    for nd, col, title, line, when, bdg in rows:
        h = round((66 if line else 46) * s); heights.append(h)
    total = sum(heights) + gap*s*(len(rows)-1)
    rail_x = x + n/2
    out.append(f'<div style="position: absolute; left: {rail_x-1:.0f}px; top: {y + heights[0]/2:.0f}px; height: {total - heights[0]/2 - heights[-1]/2:.0f}px; border-left: 2.5px dashed {line_color}"></div>')
    for (nd, col, title, line, when, bdg), h in zip(rows, heights):
        ny = cy + h/2 - n/2
        if nd in G:
            nh = (f'<span style="width: {n}px; height: {n}px; box-sizing: border-box; border-radius: 999px; background: {col}; color: #FFFFFF; border: 3px solid #FFFFFF; '
                  f'display: flex; align-items: center; justify-content: center; box-shadow: 0 6px 14px rgba(27,72,188,0.20)">{glyph(nd, round(n*0.45))}</span>')
        else:
            nh = nd
        out.append(pos(x, round(ny), nh, z=2))
        cx = x + n + round(16*s)
        out.append(f'<div style="position: absolute; left: {cx - round(16*s)}px; top: {cy + h/2 - 1:.0f}px; width: {round(16*s)}px; border-top: 2.5px dashed {line_color}"></div>')
        sub = f'<span style="font-size: {11*s:.1f}px; color: {SLATE}; line-height: 1.35">{line}</span>' if line else ''
        inner = (f'<div style="display: flex; align-items: center; gap: {10*s:.0f}px; height: 100%">'
                 f'<div style="flex: 1; min-width: 0; display: flex; flex-direction: column; gap: {3*s:.0f}px">'
                 f'<span style="display: flex; align-items: center; gap: {7*s:.0f}px; font-size: {13*s:.1f}px; font-weight: 600; line-height: 1.25">{title}{bdg}</span>{sub}</div>'
                 f'<span style="font-size: {10.5*s:.1f}px; color: {MUTED}; white-space: nowrap; align-self: flex-start; margin-top: {2*s:.0f}px">{when}</span></div>')
        out.append(card(cx, round(cy), card_w, inner, h=h, pad=f'{11*s:.0f}px {14*s:.0f}px', r=round(14*s), z=2))
        boxes.append((cx, round(cy), cx + card_w, round(cy + h)))
        cy += h + gap*s
    return ''.join(out), boxes

def crm_profile(x, y, w, name, initials, stat=('Email: 12', 'Open: 9', 'Click: 4'), tags=('Discovery Call', 'Northbeam Leads'), av_bg=PEACH, s=1.0, z=None):
    """FluentCRM Profile card as it appears on a booking. FluentCRM is a separate product."""
    st = ''.join(f'<span style="flex: 1; text-align: center; padding: {5*s:.0f}px 0; font-size: {10.5*s:.1f}px; color: {SLATE}; border-left: {"1px solid " + LINE if i else "none"}">{t}</span>' for i, t in enumerate(stat))
    tg = ''.join(f'<span style="font-size: {10.5*s:.1f}px; color: {BLUE_DEEP}; background: {BLUE_WASH}; padding: {3*s:.0f}px {9*s:.0f}px; border-radius: 99px">{t}</span>' for t in tags)
    inner = (f'<div style="display: flex; align-items: center; gap: {6*s:.0f}px; font-size: {12*s:.1f}px; font-weight: 600; color: {BLUE_DEEP}; margin-bottom: {12*s:.0f}px">'
             f'{logo("fluentcrm-icon", round(16*s))}FluentCRM Profile</div>'
             f'<div style="display: flex; flex-direction: column; align-items: center; gap: {5*s:.0f}px">{avatar(initials, av_bg, px=round(56*s))}'
             f'<span style="font-size: {15*s:.1f}px; font-weight: 600; margin-top: {3*s:.0f}px">{name}</span>{status("Subscribed", round(9.5*s))}</div>'
             f'<div style="display: flex; border: 1px solid {LINE}; border-radius: {7*s:.0f}px; margin: {12*s:.0f}px 0 {10*s:.0f}px">{st}</div>'
             f'<div style="display: flex; flex-wrap: wrap; gap: {5*s:.0f}px">{tg}</div>')
    return card(x, y, w, inner, pad=f'{13*s:.0f}px {14*s:.0f}px', r=round(18*s), shadow=FLOAT_SHADOW, z=z)

# ---------------------------------------------------------------- payments (Pro)
def payment_card(x, y, w, item='Physio Session', price='$80.00', coupon=('SPRING10', '-$8.00'), total='$72.00', method='Stripe', s=1.0, z=None):
    """Payment Summary on the booking form. Payment methods and coupons are Pro."""
    row = lambda a, b, st='': (f'<div style="display: flex; justify-content: space-between; padding: {9*s:.0f}px {12*s:.0f}px; font-size: {13*s:.1f}px; {st}">'
                               f'<span>{a}</span><span>{b}</span></div>')
    cp = ''
    if coupon:
        cp = (f'<div style="display: flex; justify-content: space-between; align-items: center; padding: {9*s:.0f}px {12*s:.0f}px; font-size: {12.5*s:.1f}px">'
              f'<span style="display: flex; align-items: center; gap: {6*s:.0f}px; color: {SLATE}"><span style="color: {BLUE}; display: flex">{glyph("tag", round(14*s))}</span>Coupon '
              f'<span style="font-weight: 600; color: {BLUE_DEEP}; background: {BLUE_WASH}; padding: {2*s:.0f}px {8*s:.0f}px; border-radius: 6px">{coupon[0]}</span></span>'
              f'<span style="color: #0B6B3A; font-weight: 600">{coupon[1]}</span></div>')
    inner = (f'<div style="display: flex; align-items: center; justify-content: space-between; margin-bottom: {12*s:.0f}px">'
             f'<span style="font-size: {16*s:.1f}px; font-weight: 600; color: {BLUE_DEEP}">Payment Summary</span>{pro()}</div>'
             f'<div style="border-radius: {10*s:.0f}px; overflow: hidden; border: 1px solid {LINE}">'
             f'{row("Item", "Price", f"background: {BLUE_TINT}; font-weight: 600; color: {INK}")}'
             f'{row(item, price, f"color: {INK}")}{cp}'
             f'{row("Total", total, f"background: {CELL}; font-weight: 700; color: {INK}; border-top: 1px solid {LINE}")}</div>'
             f'<div style="margin-top: {14*s:.0f}px; display: flex; align-items: center; justify-content: center; gap: {8*s:.0f}px; height: {42*s:.0f}px; border-radius: {10*s:.0f}px; '
             f'background: {BLUE_DEEP}; color: #FFFFFF; font-size: {13.5*s:.1f}px; font-weight: 600">{glyph("card", round(16*s))}Pay {total} with {method}</div>')
    return card(x, y, w, inner, pad=f'{16*s:.0f}px {18*s:.0f}px', r=round(18*s), z=z)

def details_form(x, y, w, name='Lena Park', email='lena.park@example.com', about='First class, keen to work on flexibility', s=1.0, z=None):
    """The booking form step after a slot is picked, using the real system questions."""
    field = lambda label, val, tall=False: (f'<div style="display: flex; flex-direction: column; gap: {5*s:.0f}px">'
        f'<span style="font-size: {11.5*s:.1f}px; font-weight: 500; color: {INK}">{label}</span>'
        f'<span style="min-height: {(52 if tall else 32)*s:.0f}px; box-sizing: border-box; padding: {8*s:.0f}px {10*s:.0f}px; border: 1px solid {LINE}; border-radius: {8*s:.0f}px; '
        f'font-size: {11.5*s:.1f}px; color: {SLATE}; line-height: 1.35">{val}</span></div>')
    inner = (f'<div style="font-size: {15*s:.1f}px; font-weight: 600; color: {BLUE_DEEP}; margin-bottom: {10*s:.0f}px">Enter Details</div>'
             f'<div style="display: flex; flex-direction: column; gap: {9*s:.0f}px">{field("Your Name *", name)}{field("Your Email *", email)}'
             f'{field("What is this meeting about?", about, True)}</div>')
    return card(x, y, w, inner, pad=f'{14*s:.0f}px {16*s:.0f}px', r=round(16*s), shadow=FLOAT_SHADOW, z=z)

def confirm_card(x, y, w, event, host, when, location, state='Scheduled', s=1.0, z=None, extra=''):
    """Booking confirmation summary with a real booking status."""
    row = lambda g, t: (f'<div style="display: flex; align-items: center; gap: {8*s:.0f}px; font-size: {12*s:.1f}px; color: {SLATE}">'
                        f'<span style="display: flex; color: {BLUE}">{glyph(g, round(15*s))}</span>{t}</div>')
    inner = (f'<div style="display: flex; align-items: center; gap: {10*s:.0f}px; margin-bottom: {10*s:.0f}px">'
             f'<span style="color: #1FA463; display: flex">{glyph("check", round(26*s))}</span>'
             f'<span style="flex: 1; font-size: {15*s:.1f}px; font-weight: 600">{event}</span>{status(state, round(10*s))}</div>'
             f'<div style="display: flex; flex-direction: column; gap: {7*s:.0f}px">{row("user", host)}{row("calendar", when)}{row("pin", location)}{extra}</div>')
    return card(x, y, w, inner, pad=f'{14*s:.0f}px {16*s:.0f}px', r=round(16*s), shadow=FLOAT_SHADOW, z=z)

# ---------------------------------------------------------------- board files
FONTS_LINK = ('<link rel="preconnect" href="https://fonts.googleapis.com">\n'
              '<link href="https://fonts.googleapis.com/css2?family=Inter:wght@400;500;600;700&amp;family=Jost:wght@400;500;600;700&amp;display=swap" rel="stylesheet">')

def board(w, h, inner, radius=32):
    """Root of a scene. Background is the {{ground}} tweak; radius 0 for full-bleed covers."""
    return (f'<div style="width: {w}px; height: {h}px; position: relative; overflow: hidden; border-radius: {radius}px; background: {{{{ground}}}}; {JOST}; color: {INK}">\n{inner}\n</div>')

def write_board(path, w, h, root_html, title, ground=SKY, options=GROUNDS):
    """Write a .dc.html board for the Design canvas with one colour tweak (ground)."""
    opts = json.dumps(list(options)).replace(' ', '')
    extra = ''.join(f", {k}: {json.dumps(v)}" for k, v in MERGE.items() if '{{' + k + '}}' in root_html)
    doc = f'''<!doctype html>
<html lang="en">
<head>
<meta charset="utf-8">
<title>{title}</title>
<script src="./support.js"></script>
</head>
<body>
<x-dc>
<helmet>
{FONTS_LINK}
<style>
body{{margin:0}}
</style>
</helmet>
{root_html}
</x-dc>
<script type="text/x-dc" data-dc-script data-props='{{"ground":{{"editor":"color","default":"{ground}","options":{opts}}},"$preview":{{"width":{w},"height":{h}}}}}'>
class Component extends DCLogic {{
renderVals() {{ return {{ ground: this.props.ground ?? '{ground}'{extra} }}; }}
}}
</script>
</body>
</html>
'''
    open(path, 'w').write(doc)
    return path

def write_preview(path, root_html, ground=SKY, page_bg='#FFFFFF'):
    """Plain HTML copy for the render check, with the tweak filled in. Fonts are added by render.py."""
    body = root_html.replace('{{ground}}', ground)
    for k, v in MERGE.items():
        body = body.replace('{{' + k + '}}', v)
    open(path, 'w').write(f'<!doctype html><html><head><meta charset="utf-8"><style>/*FONTS*/body{{margin:0;background:{page_bg}}}</style></head><body>{body}</body></html>')
    return path

# ---------------------------------------------------------------- layout helpers for covers, social and headers
def panel(x, y, w, h, ground, inner, radius=40):
    """A rounded pastel panel that clips its scene (blog covers, social, web heroes). Children use panel coordinates."""
    return (f'<div style="position: absolute; left: {x}px; top: {y}px; width: {w}px; height: {h}px; border-radius: {radius}px; '
            f'background: {ground}; overflow: hidden">{inner}</div>')

def lockup(x, y, height=40, variant='logo'):
    """The official FluentBooking logo file, placed at x, y. Never a typed or redrawn version."""
    return f'<div style="position: absolute; left: {x}px; top: {y}px; display: flex">{brand_logo(variant, height)}</div>'

def eyebrow(text, fg=BLUE_DEEP, bg=BLUE_TINT, size=13):
    return (f'<span style="align-self: flex-start; {JOST}; font-size: {size}px; font-weight: 600; letter-spacing: 0.1em; color: {fg}; '
            f'background: {bg}; padding: {round(size*0.55)}px {round(size*1.1)}px; border-radius: 999px">{text}</span>')

def copy_block(x, y, w, eyebrow_text, headline, line, h_size=50, l_size=20, color=INK, sub=SLATE, gap=18):
    return (f'<div style="position: absolute; left: {x}px; top: {y}px; width: {w}px; display: flex; flex-direction: column; gap: {gap}px; {JOST}">'
            + (eyebrow(eyebrow_text, size=round(h_size*0.26)) if eyebrow_text else '')
            + f'<span style="font-size: {h_size}px; line-height: 1.08; font-weight: 600; letter-spacing: -0.015em; color: {color}">{headline}</span>'
            + (f'<span style="font-size: {l_size}px; line-height: 1.45; color: {sub}">{line}</span>' if line else '') + '</div>')

def grid_card(x, y, w, month='October', year='2028', first=6, selected=3, available=(3, 4, 5, 10, 11, 12, 17, 18, 19, 24, 25, 26),
              s=1.0, z=None, title=None):
    """The month grid as a whole component card. Use it when the full booking page does not fit: rebuild the screen
    from whole parts (grid card, slot card, form) instead of slicing the page."""
    pad = round(16*s)
    head = (f'<div style="font-size: {12*s:.1f}px; font-weight: 500; color: {SLATE}; margin-bottom: {8*s:.0f}px">{title}</div>' if title else '')
    inner = head + month_grid(w - 2*pad - 4, month, year, first, 31, selected, available, s)
    return card(x, y, w, inner, pad=f'{pad}px', r=round(18*s), z=z)

def slots_card(x, y, w, date_label, slots, s=1.0, z=None):
    """The slot column as a whole component card."""
    pad = round(14*s)
    return card(x, y, w, slot_list(w - 2*pad - 4, date_label, slots, s), pad=f'{pad}px', r=round(16*s), shadow=FLOAT_SHADOW, z=z)

# ---------------------------------------------------------------- feature card parts
TYPE_LINE = {'One-to-One': 'One host with One invitee', 'Group': 'One host with Group of invitees',
             'Round Robin': 'One rotating host with One invitee', 'Collective': 'Multiple hosts with One invitee'}

def type_rows(x, y, w, kinds=('One-to-One', 'Group', 'Round Robin', 'Collective'), selected='Round Robin', s=1.0, z=None, gap=10):
    """The four meeting types as floating rows, labels and lines exactly as the product's dialogs word them.
    The selected row gets the bright outline and the wash fill."""
    rows = ''
    for k in kinds:
        on = k == selected
        rows += (f'<div style="display: flex; align-items: center; gap: {12*s:.0f}px; padding: {11*s:.0f}px {13*s:.0f}px; '
                 f'border: {2.5 if on else 2}px solid {BLUE_BRIGHT if on else BLUE_LINE}; border-radius: {14*s:.0f}px; background: {BLUE_WASH if on else "#FFFFFF"}; {CARD_SHADOW}">'
                 f'{type_mark(k, round(15*s), BLUE_DEEP if on else INK)}<div style="flex: 1; display: flex; flex-direction: column; gap: {2*s:.0f}px">'
                 f'<span style="font-size: {14*s:.1f}px; font-weight: 600; color: {BLUE_DEEP if on else INK}">{k}</span>'
                 f'<span style="font-size: {10.5*s:.1f}px; color: {SLATE}">{TYPE_LINE[k]}</span></div>'
                 f'<span style="color: {INK}; font-size: {15*s:.0f}px">→</span></div>')
    zs = f' z-index: {z};' if z is not None else ''
    return f'<div style="position: absolute; left: {x}px; top: {y}px; width: {w}px;{zs} display: flex; flex-direction: column; gap: {gap*s:.0f}px; {JOST}; color: {INK}">{rows}</div>'

def team_card(x, y, w, team='Northbeam Sales', kind='Round Robin', hosts=(('RM', 'Ravi Menon', PEACH), ('LP', 'Lena Park', AQUA), ('TW', 'Tomas Weber', BLUE_TINT)), s=1.0, z=None):
    """A team calendar as on Calendars › Teams: name, meeting type, its hosts."""
    rows = ''.join(f'<div style="display: flex; align-items: center; gap: {9*s:.0f}px; padding: {7*s:.0f}px 0; border-top: 1px solid {LINE}">'
                   f'{avatar(i, bg, "#3A2E22", round(28*s))}<span style="font-size: {12.5*s:.1f}px; font-weight: 500">{n}</span></div>' for i, n, bg in hosts)
    inner = (f'<div style="display: flex; align-items: center; gap: {8*s:.0f}px; margin-bottom: {4*s:.0f}px">{tile("users", BLUE_DEEP, round(30*s), r=round(9*s))}'
             f'<div style="display: flex; flex-direction: column"><span style="font-size: {14*s:.1f}px; font-weight: 600">{team}</span>'
             f'<span style="font-size: {10.5*s:.1f}px; color: {SLATE}">Team · {len(hosts)} hosts</span></div></div>'
             f'<div style="display: flex; align-items: center; gap: {6*s:.0f}px; margin: {6*s:.0f}px 0 {8*s:.0f}px; font-size: {11*s:.1f}px; color: {BLUE_DEEP}">'
             f'{type_mark(kind, round(13*s), BLUE_DEEP)}{kind}</div>{rows}')
    return card(x, y, w, inner, pad=f'{13*s:.0f}px {15*s:.0f}px {6*s:.0f}px', r=round(16*s), z=z)

def integrations_card(x, y, w, items=(('fluentcrm-icon', 'FluentCRM'), ('fluent-forms', 'Fluent Forms'), ('fluent-boards', 'Fluent Boards')), title='Recommended Plugins and Addons', s=1.0, z=None):
    """The Fluent integrations as listed in Settings › Advanced Modules. Avoid in marketing scenes: the System Enabled badge is a configuration label, not a benefit; show what the integration does instead (automation_flow)."""
    rows = ''.join(f'<div style="display: flex; align-items: center; gap: {10*s:.0f}px; padding: {9*s:.0f}px 0; border-top: 1px solid {LINE}">'
                   f'<span style="width: {32*s:.0f}px; height: {32*s:.0f}px; border-radius: {9*s:.0f}px; border: 1px solid {LINE}; display: flex; align-items: center; justify-content: center; flex-shrink: 0">{logo(lg, round(20*s))}</span>'
                   f'<span style="flex: 1; font-size: {13*s:.1f}px; font-weight: 600">{nm}</span>{badge("System Enabled", "#0B4627", "#E0FAEC", round(9.5*s))}</div>' for lg, nm in items)
    inner = f'<div style="font-size: {12.5*s:.1f}px; font-weight: 600; color: {BLUE_DEEP}; margin-bottom: {8*s:.0f}px">{title}</div>{rows}'
    return card(x, y, w, inner, pad=f'{13*s:.0f}px {15*s:.0f}px {5*s:.0f}px', r=round(16*s), z=z)

def booked_pill(x, y, name, initials, event, state='Scheduled', s=1.0, z=None, av_bg=PEACH):
    zs = f' z-index: {z};' if z is not None else ''
    return (f'<div style="position: absolute; left: {x}px; top: {y}px;{zs} display: inline-flex; align-items: center; gap: {9*s:.0f}px; background: #FFFFFF; border: 2px solid {BLUE_LINE}; '
            f'border-radius: 999px; padding: {5*s:.0f}px {13*s:.0f}px {5*s:.0f}px {5*s:.0f}px; {CARD_SHADOW}; {JOST}; white-space: nowrap">'
            f'{avatar(initials, av_bg, px=round(30*s))}<span style="font-size: {12.5*s:.1f}px; font-weight: 600; color: {INK}">{name} booked {event}</span>{status(state, round(10*s))}</div>')


def logo_node(name, px=40):
    """Round white timeline node holding a Fluent product's own logo file (from assets/logos)."""
    return (f'<span style="width: {px}px; height: {px}px; box-sizing: border-box; border-radius: 999px; background: #FFFFFF; border: 2px solid {BLUE_LINE}; '
            f'display: flex; align-items: center; justify-content: center; box-shadow: 0 6px 14px rgba(27,72,188,0.18)">{logo(name, round(px*0.5))}</span>')

# ---------------------------------------------------------------- automation (as in the FluentBooking website illustrations)
def flow_step(icon_html, title, block, s=1.0, highlight=False):
    """One automation block: icon, a descriptive step name, and under it the real FluentCRM block it uses."""
    return (f'<div style="display: flex; align-items: center; gap: {11*s:.0f}px; background: #FFFFFF; border: {2 if highlight else 1.5}px solid {BLUE_LINE if highlight else "#D9DEE7"}; '
            f'border-radius: {10*s:.0f}px; padding: {9*s:.0f}px {13*s:.0f}px; {JOST}">'
            f'<span style="width: {30*s:.0f}px; height: {30*s:.0f}px; flex-shrink: 0; display: flex; align-items: center; justify-content: center; color: {BLUE_DEEP}">{icon_html}</span>'
            f'<div style="display: flex; flex-direction: column; gap: {2*s:.0f}px; min-width: 0">'
            f'<span style="font-size: {14*s:.1f}px; font-weight: 600; color: {BLUE_DEEP}; white-space: nowrap">{title}</span>'
            f'<span style="font-size: {10.5*s:.1f}px; color: {SLATE}; white-space: nowrap">{block}</span></div></div>')

def flow_plus(s=1.0):
    d = round(20*s)
    return (f'<div style="display: flex; flex-direction: column; align-items: center">'
            f'<span style="width: 0; height: {9*s:.0f}px; border-left: 1.5px solid #C9D1DE"></span>'
            f'<span style="width: {d}px; height: {d}px; box-sizing: border-box; border-radius: 999px; border: 1.5px solid #C9D1DE; background: #FFFFFF; color: {SLATE}; '
            f'display: flex; align-items: center; justify-content: center; font-size: {13*s:.0f}px; line-height: 1">+</span>'
            f'<span style="width: 0; height: {9*s:.0f}px; border-left: 1.5px solid #C9D1DE"></span></div>')

def automation_flow(x, y, w, steps, s=1.0, z=None, pad=16):
    """A FluentCRM automation on a white outlined panel, as the FluentBooking website draws it: stacked blocks joined
    by thin lines with + circles. steps: (icon_html, step name, real block label). Block labels must exist in the
    FluentCRM product brain (triggers such as New Booking come from FluentBooking)."""
    body = ''
    for i, (ic, t, b) in enumerate(steps):
        if i: body += flow_plus(s)
        body += flow_step(ic, t, b, s, highlight=(i == 0))
    return card(x, y, w, f'<div style="display: flex; flex-direction: column">{body}</div>', pad=f'{pad*s:.0f}px', r=round(18*s), z=z)

def form_card(x, y, w, title='Book a Discovery Call', fields=(('Your Name', 'Priya Shah'), ('Your Email', 'priya.shah@example.com')),
              slot='Wed, October 4 · 3:00 PM', s=1.0, z=None):
    """A Fluent Forms form with a FluentBooking booking field, as on the Fluent Forms integration illustration."""
    f = ''.join(f'<div style="display: flex; flex-direction: column; gap: {4*s:.0f}px"><span style="font-size: {11*s:.1f}px; font-weight: 500">{lab}</span>'
                f'<span style="padding: {7*s:.0f}px {9*s:.0f}px; border: 1px solid {LINE}; border-radius: {7*s:.0f}px; font-size: {11*s:.1f}px; color: {SLATE}">{val}</span></div>' for lab, val in fields)
    inner = (f'<div style="display: flex; align-items: center; gap: {8*s:.0f}px; margin-bottom: {10*s:.0f}px">{logo("fluent-forms", round(20*s))}'
             f'<span style="font-size: {13.5*s:.1f}px; font-weight: 600; color: {BLUE_DEEP}">{title}</span></div>'
             f'<div style="display: flex; flex-direction: column; gap: {8*s:.0f}px">{f}'
             f'<div style="display: flex; flex-direction: column; gap: {4*s:.0f}px"><span style="font-size: {11*s:.1f}px; font-weight: 500">Booking</span>'
             f'<span style="display: flex; align-items: center; gap: {6*s:.0f}px; padding: {7*s:.0f}px {9*s:.0f}px; border: 1.5px solid {BLUE_BRIGHT}; background: {BLUE_WASH}; border-radius: {7*s:.0f}px; '
             f'font-size: {11*s:.1f}px; font-weight: 600; color: {BLUE_DEEP}">{glyph("calendar", round(13*s))}{slot}</span></div>'
             f'<span style="margin-top: {2*s:.0f}px; text-align: center; padding: {8*s:.0f}px; border-radius: {8*s:.0f}px; background: {BLUE_DEEP}; color: #FFFFFF; font-size: {12*s:.1f}px; font-weight: 600">Submit</span></div>')
    return card(x, y, w, inner, pad=f'{14*s:.0f}px {15*s:.0f}px', r=round(16*s), z=z)

# ---------------------------------------------------------------- web page pieces
def button(text, primary=True, size=16):
    if primary:
        st = f'background: {BLUE_DEEP}; color: #FFFFFF; border: 2px solid {BLUE_DEEP}'
    else:
        st = f'background: #FFFFFF; color: {BLUE_DEEP}; border: 2px solid {BLUE_LINE}'
    return (f'<span style="display: inline-flex; align-items: center; {JOST}; font-size: {size}px; font-weight: 600; {st}; '
            f'padding: {round(size*0.8)}px {round(size*1.5)}px; border-radius: {round(size*0.65)}px; white-space: nowrap">{text}</span>')

def nav_bar(x, y, w, links=('Features', 'Integrations', 'Pricing', 'Docs'), cta='Get FluentBooking', logo_h=34):
    items = ''.join(f'<span style="font-size: 16px; font-weight: 500; color: {INK}">{l}</span>' for l in links)
    return (f'<div style="position: absolute; left: {x}px; top: {y}px; width: {w}px; display: flex; align-items: center; justify-content: space-between; {JOST}">'
            f'{brand_logo("logo", logo_h)}<div style="display: flex; align-items: center; gap: 36px">{items}{button(cta, True, 15)}</div></div>')
