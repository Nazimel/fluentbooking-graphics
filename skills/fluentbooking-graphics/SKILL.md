---
name: fluentbooking-graphics
description: This skill should be used when the user asks to design, make or build any FluentBooking graphic, such as a website feature card, hero image, page header, blog cover, social post visual, email header or integration graphic. Triggers include "make a FluentBooking graphic", "booking page illustration", "hero image for the FluentBooking page", "social visual for FluentBooking". It builds the graphic in FluentBooking's website illustration style, checks it by rendering, and delivers PNGs plus an editable board. DRAFT design system, not locked.
---

# FluentBooking graphics (draft v0.1)

Build FluentBooking marketing graphics in the brand's website illustration language: soft pastel grounds, white cards with a 2px blue outline, the public booking page with its month grid and slots, event cards, notification lists, reminders and phones, the booking activity timeline and the payment summary. Check every graphic by rendering it, then deliver it.

**This system is a draft.** Colours were sampled from the logo and website illustrations and the font (Jost) was matched by eye. Say so when a choice rests on a draft token, and collect feedback rather than treating anything as locked.

Everything needed is inside this skill folder:
- `references/brand-guide.md`: rules 1 to 8, colour, type, shape, house style. Read it first on every request.
- `references/product-facts.md`: every label a graphic may show, checked against the FluentBooking Product Brain, with Pro flags.
- `references/story-types.md`: the five stories, their anchors, support cards, layering, bleed and scale.
- `references/formats.md`: tested size recipes (720×600 hero default, feature cards, blog cover, social, email header).
- `references/tokens.json`: every token with a usage note.
- `assets/brand/` (official FluentBooking logos and icons, Updated Logo 2025), `assets/logos/` (Fluent family marks; confirm they are current). See `references/logos.md`.
- `scripts/kit.py` (drawing kit), `scripts/render.py` (render check), `scripts/example_generator.py` (the five story cards), `scripts/format_examples.py` (feature card pair, blog cover, social post, email header), `scripts/feature_cards.py` (feature card pairs for Meeting Types, Paid Bookings, Reminders, Booking Automation), `scripts/templates.py` (web hero, integration graphic, portrait social, story).
- `examples/`: the five story cards and the format tests as .dc.html boards and PNG renders. Open the closest one before building.

## Workflow

1. **Brief.** Establish size, placement (page section, blog, social, email), the story, and whether copy goes on the image or comes from the page. Use the default size in `formats.md` when none is given and say so. Ask only when the placement itself is unclear.

2. **Check the product facts.** Before drawing any setting, notification, status, location, merge tag or integration, find it in `product-facts.md`. If it is not there, ask the FluentBooking Product Brain (load its `fluentbooking-brain` skill). Note which features are Pro and mention them in the reply; draw no PRO badge unless the request asks for one (then set `kit.SHOW_PRO = True`). If the brain is unavailable, say so and keep to what `product-facts.md` lists. Never draw a "No Show" status badge: it is an event, not a status.

3. **Story.** Read the copy the graphic pairs with and draw what it promises: if it names outcomes, show those outcomes, not a settings screen. Pick one of the five stories in `story-types.md`, one anchor and at most two support cards. Name events descriptively ("Discovery Call", "Morning Flow Class"). Use a house sample brand (Stillpoint Yoga, Northbeam Consulting, Larkfield Clinic) or invent another fictional one. People are invented and drawn as initials avatars; never a real person, a celebrity face, or names and emails from a real site.

4. **Build.** Write one Python generator per request that imports the kit (`sys.path.insert(0, '<this skill>/scripts'); from kit import *`), composes absolutely positioned pieces inside `board()`, then calls `write_board()` for the editable .dc.html and `write_preview()` for the render check. Start from `scripts/example_generator.py`. Merge tags go through `merge()`, which keeps curly braces from being read as canvas holes.

5. **Render check (never skip).** Run `python3 scripts/render.py preview.html out.png W H`, open the PNG and look for blank calendar or card areas that need an overlay, clipped or overflowing text, hidden labels or PRO badges, collisions, empty dead areas, dates that do not match weekdays, and safe-zone breaks. Measure with `--measure`, run `--gaps` to catch cards that touch or overlap by a sliver, and run `--margins` to confirm the outer margins are equal left and right, top and bottom, wherever nothing bleeds. For several boards make a contact sheet with `--sheet`. Fix and re-render until clean.

6. **Deliver.**
   - Export PNGs at 2× (3× for a single small card) and send them to the user as files.
   - If a Design canvas is available, add the .dc.html boards to the user's FluentBooking canvas so they can edit text and the ground colour. Otherwise attach the .dc.html files with the PNGs.
   - Reply briefly: what was made, decisions to confirm (default size used, Pro features in the scene, sample data invented, draft tokens relied on), and one next step.

## Non-negotiables
- Logos and icons come only from the official files (`brand_logo()`, `lockup()`, `brand()`). Never type, redraw or approximate a mark. If a graphic needs a mark that is not bundled (a partner logo, a different product's current logo), stop and ask the user for the file before building.
- One anchor and at most two support cards, each adding something the others do not; the anchor bleeds right or bottom only; support cards stay 8px inside the edges.
- Crop with intent: never slice through a calendar, label, button or text; when a screen does not fit, rebuild it from whole components (`grid_card()`, `slots_card()`, forms) that tell the step.
- Overlapping cards may cover the anchor but never hide another card's prices, labels or values.
- Automations look like automations: anything set up to run on its own is an `automation_flow()` with real FluentCRM block labels, never a timeline; timelines are only for a log of what already happened.
- No blank phone screens: fill the phone with a believable thread (`booking_thread()`), with times that agree with the reminder lead time.
- Card spacing: at least 16px between side-by-side cards, or a deliberate overlap of 40px or more; never touching or a sliver.
- Copy and scene sit close: about 56px between the last line of copy and the scene at 1080 wide, never an empty band.
- Balanced margins: opposite outer margins match wherever nothing bleeds (check with `render.py --margins`).
- No dead space: size cards and recreated screens to their content (no padded white inside a UI), and fix any empty patch of ground or card bigger than about a fifth of the canvas.
- No blank calendars: empty areas of the booking page or any anchor are covered with overlay cards (details form, confirmation, reminder, status), never left as white space.
- Every floating white card has the 2px `blue-line` #4587EC outline and a blue-tinted shadow.
- One pastel ground per scene (Sky default), full bleed on every format with no inset panel on white, combined with one or two large soft shapes in a second palette colour behind the scene, faded out at their edges (`blob()` draws them as radial glows, never hard circles), so the background never reads as one flat colour. Never a dark or saturated background, hover states included. Never add a sparkle or star unless the piece celebrates a milestone.
- Sequences of events (what happens after a booking) are drawn as a visual timeline with `booking_timeline()`, not a list inside a card.
- Jost in illustrations and copy, Inter only for literal product UI and merge tag chips.
- Copy follows the house style: no mid-sentence dashes, connected sentences, none of the banned words.
- Illustrations are always paired with copy where they are published.
