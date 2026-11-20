# Format recipes (draft v0.1)

Sizes the user names always win; with no size, use the default here and say so in the reply. Every recipe below has a tested example in `examples/` built by `scripts/example_generator.py` (stories) or `scripts/format_examples.py` (formats). Copy the closest one.

## Hero image beside page copy: 720×600 (default, tested)
- **Use:** the visual half of a two-column page hero; headline and paragraph stay in the page HTML.
- **All formats:** the pastel ground fills the whole canvas, combined with one or two large soft shapes in a second palette colour that fade out at their edges, sit partly behind the scene and bleed off an edge. Never sit the scene in an inset panel on white.
- **Ground:** one pastel ground, radius 32. No safe zones.
- **Scene:** one story from `story-types.md`. Examples: `examples/0*-*`.

## Feature card, collapsed: 290×400 (tested)
- **Ground:** Sky, radius 28. Top 48px clear for the label pill.
- **Scene:** the booking page never fits whole at this size, so rebuild it from components: `grid_card()` at s 0.8 (16,58, width 250) with the event and host as its title, `slots_card()` at s 0.78 for the picked day overlapping its lower right, 8px or more inside the bottom edge. No connector across the grid: the overlap already reads as the next step.
- **Example:** `examples/fc-booking-290x400`.

## Feature card, expanded: 522×400 (tested)
- **Ground:** a different pastel from the collapsed card (Peach when the collapsed card is Sky), so the hover change reads at a glance. Never a dark or saturated ground.
- **Safe zones:** top 48px; lower-left 236×110 clear for page copy. Keep the anchor's bottom above y 290 on the left.
- **Scene:** the same story with its context: `booking_page()` at s 0.6 from x 24, `details_form()` at s ≈ 0.72 overlapping its right half and running into the lower right.
- **Example:** `examples/fc-booking-522x400`.

## Feature card pairs for feature pages (tested: Meeting Types, Paid Bookings, Reminders, Booking Automation)
- Built by `scripts/feature_cards.py`; one story per pair, told the same way in both sizes.
- **Collapsed 290×400:** one anchor (or anchor plus one support card) centred in the area below the 48px label zone, so the gap under the zone equals the gap at the bottom. Anchors that work at this width: `type_rows()`, `payment_card()` at s ≈ 0.78, `phone()` with a `reminder_card()` overlapping its lower half, `automation_flow()` with four blocks at s ≈ 0.78 (five blocks do not fit; drop a Wait step first).
- **Expanded 522×400:** a different pastel from the collapsed card. Context card on the left (x 24, about 210 wide, kept above y 290 and centred in that column), anchor on the right (x ≈ 250, 24px from the right edge) running down close to the bottom so the right half has no dead space. The lower-left 236×110 stays clear for the page's headline and line.
- Check both with `render.py --margins`: equal left and right, and equal space above (below the label zone) and below.

## Blog cover: 1200×628 (tested)
- **Ground:** one pastel, full bleed (radius 0). The colour fills the whole cover: no white frame and no inset panel. The official primary logo with `lockup(64, 64, 36)`. Margins 64px on all four sides.
- **Copy:** `copy_block()` at 64,198, width ≈ 468 (no orphan words): eyebrow pill, Jost 600 50px headline (two lines at most; shorten long titles to their promise), one 20px line in slate.
- **Scene:** directly on the ground in the right half, sized to fill it: the anchor whole at s ≈ 0.9 (x ≈ 634, right edge at 1136), two support cards overlapping its lower half and running into the space between copy and anchor. Support cards may cover the anchor but never each other's values.
- **Example:** `examples/blog-cover-payments-1200x628`.

## Social post: 1080×1080 (tested), 1080×1350 (tested), 1080×1920 story (tested)
- **Ground:** one pastel, full bleed, with no white frame or inset panel. 72px edge padding. Eyebrow pills on the ground use a white fill.
- **Top:** the official primary logo with `lockup(72, 72, 42)` and an eyebrow pill top right.
- **Copy:** Jost 600 64px headline, width ≤ 780 so it breaks into two balanced lines with no orphan word; a 24px supporting line.
- **Scene:** directly on the ground from y ≈ 470, story at s ≈ 1.3, the phone or anchor bleeding off the bottom right. Never post an illustration without the copy.
- **Example:** `examples/social-reminders-1080x1080`.
- **1080×1350:** the same stack with more room: a 72px headline, the scene starting about 56px under the copy (y ≈ 472) and scaled up (rows at s ≈ 2.3) so it reaches 72px from the bottom. Example: `examples/social-meeting-types-1080x1350`.
- **1080×1920 story:** keep the top 250 and bottom 250 clear of key content (the app's own profile bar and reply field). The copy and scene stack is centred between the safe zones with about 56px between copy and scene: logo at y ≈ 312, 72px headline in two lines, then the scene: a whole booking page (slots shown, s ≈ 1.27, so its card has no empty white) with two support cards overlapping its lower edge, ending about 290 from the bottom. Example: `examples/story-paid-bookings-1080x1920`.

## Email header: 600×200 (tested)
- **Ground:** Sky, radius 0. the official primary logo with `lockup(36, 36, 28)`; headline Jost 600 28px and a 15px line at 36,92 (text 14px or larger).
- **Scene:** one whole small card: `slots_card()` at s 0.76 with three slots at x 380, fully inside the header.
- **Example:** `examples/email-header-600x200`.

## Web hero: 1440×780 (tested)
- **Ground:** Sky full bleed, two faded shapes. 64px side margins, nav (`nav_bar()`) at y 40 with the official logo.
- **Copy:** `copy_block()` at 64,236, width ≈ 584: eyebrow, Jost 600 48px headline in two balanced lines (break by hand with `<br>` if needed), a 20px paragraph; `button()` pair under it (primary `blue-deep`, secondary outlined) with at least 24px clear above.
- **Scene:** `booking_page()` at s ≈ 0.96 from x 668 so it ends at 1376, `details_form()` overlapping its lower right and `confirm_card()` its lower left.
- **Example:** `examples/web-hero-1440x780`.

## Integration graphic: 1200×628 (tested with FluentCRM)
- **Top-left:** the official FluentBooking logo, a "+", and the partner's own official mark and name. Never draw a partner mark; ask for the file if it is not bundled.
- **Copy:** eyebrow INTEGRATION, Jost 600 46px headline, one line.
- **Scene:** what the integration does, drawn as the product's real flow (for FluentCRM, an `automation_flow()` of New Booking (FluentBooking), Apply Tag, Send Custom Email, Wait X Days/Hours) with the result card beside it (`crm_profile()`), 64px margins.
- **Example:** `examples/integration-fluentcrm-1200x628`.

## What the test runs taught (apply to every format)
- Balance the composition: on every edge where nothing bleeds, the outer margin is equal on opposite sides (left equals right, top equals bottom, measured below any label-pill safe zone). Check with `python3 scripts/render.py --margins preview.html W H`, which ignores the decorative shapes, and adjust positions or scale until the numbers match. Covers and headers use 64px all round at 1200 wide, 72px on social, 36px or the card's own gap on a 600×200 header.
- Headlines: check the render for orphan words and narrow the copy width until lines balance.
- After the scene is placed, look for any empty patch bigger than about a fifth of the canvas or panel and close it by scaling or moving cards.
- Recreated screens are sized to their content (`h=None`); overlays cover their lower edge rather than padding.
- Never slice a component to make it fit; scale it, or rebuild the screen from whole components.
