# FluentBooking brand guide (draft v0.1, not locked)

The brand and asset system for **FluentBooking** by WPManageNinja: appointment scheduling that runs on your own WordPress site. Every graphic this plugin makes follows it. Nothing here is final until the team has tested it on real requests.

**Positioning (draft):** scheduling that runs on your own WordPress site and keeps working after someone books. The booking page fills your calendar, and the reminders, the payment and the CRM record follow on their own.

**Sources:** a full walkthrough of the FluentBooking admin on the team's local site (dashboard, calendars, the eleven event settings tabs, bookings and booking detail, availability, teams, global settings, integrations, modules, MCP) and the public booking page; every feature checked against the FluentBooking Product Brain (2.4.0); colours sampled from the FluentBooking logo and 19 website illustrations; the illustration font matched by eye against those illustrations. Live campaign pages were deliberately not used as a style source.

## What FluentBooking is, in five stories
1. **The booking page:** host panel, month grid, time zone and slots for the picked day. This is the anchor of the brand.
2. **Event types:** One-to-One, Group Event, Round Robin and Collective (the last two need a team, which is Pro), plus one-off events (Pro) and recurring events.
3. **Before the meeting:** the email notification list, reminders with their timing, and SMS or WhatsApp through Twilio (Pro).
4. **After the booking:** the Meeting Activities timeline on a booking (emails sent, calendar event created, FluentCRM feed) and the FluentCRM Profile card.
5. **Getting paid:** payment items, checkout, coupons and payment statuses (payments and coupons are Pro).

## How FluentBooking differs from FluentCRM visually
FluentCRM's anchor is the automation flow on lavender, where things happen after a contact exists. FluentBooking's anchor is the booking itself on cobalt blue and soft pastel grounds: a calendar, a slot, an event card. Never use FluentCRM lavender, purple or flow blocks as FluentBooking's own look; FluentCRM appears only as its icon and its Profile card.

## Brand personality
Organised, friendly, calm and dependable: a calendar that is never double booked. **Never** corporate, cluttered, gradient-noisy, cartoonish or stock-photo heavy.

## The rules
1. **Lead with the booking.** Every scene centres on one moment around a booking: picking a slot, choosing a meeting type, the reminder that goes out, what happens after, or the payment. Never a dashboard of numbers alone.
2. **Real structure, polished presentation.** Keep what makes a screen true to the product: its layout, its labels, its statuses. Refine the presentation freely: white cards with the blue outline, dashed connectors, overlaps, crops and bleeds. Never invent a feature, a screen or a setting the product does not have.
3. **Descriptive names, real capabilities.** Name events and steps for what they do in the story ("Discovery Call", "Morning Flow Class", "Reminder: Morning Flow Class starts in 15 minutes"). Every setting, notification, status, location, merge tag and integration shown must exist in `product-facts.md`, which is checked against the FluentBooking Product Brain. When a fact is missing from that file, ask the brain before drawing it.
4. **Know what is Pro, badge it only when asked.** Graphics carry no `PRO` badge unless the request asks for one (`kit.SHOW_PRO = True`). Still know which features are Pro, so you can mention them in the reply and in any copy that makes a free claim. The brain records these as implemented in FluentBooking Pro: Round Robin, Collective, teams, one-off events, Google Meet, MS Teams, Zoom, remote calendar sync, payments, coupons, WooCommerce, Twilio SMS and WhatsApp, webhooks. The brain does not make licensing claims, so confirm against the pricing page before a launch.
5. **Fictional brands and invented people only.** House samples: **Stillpoint Yoga** (host Maya Ortiz, attendee Lena Park), **Northbeam Consulting** (team Ravi Menon, Lena Park, Tomas Weber; lead Priya Shah) and **Larkfield Clinic** (Dr. Amara Cole). People appear as initials avatars until an approved set of illustrated or licensed avatars exists. Never use a real person's photo, name or email, and never a celebrity face.
6. **Sample data is consistent.** Dates match their weekdays (October 2028 starts on a Sunday, so day 1 sits in the SU column and October 3 is a Tuesday), times match durations, the time zone is shown, and totals add up (a $80.00 session with SPRING10 at minus $8.00 totals $72.00).
7. **One anchor per layout, no blank calendars.** One anchor object and at most two support cards. Empty areas of a booking page or calendar are covered with overlay cards rather than left blank (see `story-types.md`).
8. **Illustrations pair with copy.** Website illustrations always sit beside website copy; on social graphics an illustration is never posted alone, it sits with a headline and at least one supporting line.

## Content fundamentals
- **Voice:** helpful and outcome-led. Lead with what the reader gets ("Your calendar fills itself"), then how.
- **Person:** second person. "We" only on community, milestone and release posts.
- **Casing:** sentence case for headlines and body; ALL CAPS only for pill badges and eyebrows.
- **Length:** headlines up to 8 words per line, 2 lines on social and 3 on web; body 2 to 4 lines.
- **House style:** no dash in the middle of a sentence for an aside (use commas or a new sentence); connected sentences rather than choppy fragments; never "leverage, unlock, empower, streamline, game-changer, elevate, harness, robust, seamless, cutting-edge, landscape, paradigm shift, delve, deep dive, at the end of the day, it's worth noting".
- **Proofread product words:** the reference illustrations contain typos ("Patments", "Summery", "Doller", "Chet") and mismatched years; new work must not repeat them.

## Colour (draft, sampled)
- **Brand blue:** `blue` #2653C7 (the logo), `blue-deep` #1B48BC (slot text, primary buttons, headings on cards), `blue-bright` #006BFF (selected day, active dot, one highlight per scene).
- **Blue support:** `blue-line` #4587EC (2px card outlines, toggles, dashed connectors), `blue-tint` #DBE9FC (table headers, merge-tag chips, soft buttons), `blue-wash` #EEF2FC (selected slot, soft fills).
- **Accent:** `indigo` #4428BF for one accent shape per scene and the PRO badge.
- **Grounds (one per scene):** Sky #E1F1FF (default), Peach #FFE8E1, Mint #E9FFE1, Butter #FFFCE1, Aqua #E1FFF8. FluentBooking never uses dark or saturated backgrounds: brand blue, blue-deep and indigo are for buttons, selected states and accents, never a ground, including hover and expanded states.
- **Decorative accents:** Aqua strong #B1FDEB, Sun #F4CF45, Orange #FF9900. Combine colours as the website illustrations do: the ground plus one or two large soft shapes in a second palette colour, each a radial glow that fades out at its edge (never a hard rounded outline), (a blue tint circle on butter or peach, an aqua circle on mint, a deeper sky circle on sky), placed partly behind the anchor and bleeding off an edge so the whole background is used. No sparkles or stars as decoration; a sparkle appears only on milestone or celebration social posts.
- **Neutrals:** ink #1D2432, slate #5B6478, muted #8E96A8 (unavailable days, timestamps), line #E5E7EB, cell #F4F5F7 (available day cells).
- **Booking statuses (text/background):** Scheduled #0B4A8B/#E1F1FF, Rescheduled #5B3A00/#FFF4D6, Completed #0B4627/#E0FAEC, Pending #624C18/#FFFAEB, Cancelled #681219/#FFEBEC, Rejected #3A3F4B/#EEF0F3. Payment Paid uses the Completed pair.

## Type (draft)
- **Jost** for illustrations, headlines and copy: card titles 600, labels 500, body 400. Matched by eye against the website illustrations; confirm the real font with the designer before locking.
- **Inter** only for literal product UI and merge-tag chips.

## Shape, space, depth
- **Radii:** scene ground 32px (40px above 1000px wide), booking page 22px, cards 16 to 18px, slot rows and buttons 8px, pills for badges.
- **Outline:** 2px `blue-line` on every floating white card; this outline is the signature of the style.
- **Shadows:** blue-tinted, `0 14px 32px rgba(27,72,188,.14)` for cards and `.20` for floating cards.
- **Connectors:** 2.5px dashed `blue-line` curves with round outlined badges where a channel or integration joins.

## Imagery and layout
- Product UI rebuilt in markup, presented as white outlined cards on a pastel ground. No stock photos, no real people, no 3D.
- The anchor bleeds off the right and/or bottom edge; support cards overlap its lower left; the FluentBooking icon tile may sit on a corner.
- The pastel ground fills the whole canvas on every format, covers and social included. Never place the scene in an inset panel on a white page.
- The official primary logo top-left when the layout carries one. Web heroes and blog covers: copy left, scene right, both on the same ground. Social: logo and badge top, headline, then the scene bleeding off the bottom-right.

## Iconography
- **Logo and icon:** only the official files in `assets/brand/` (see `logos.md`). Never a typed, redrawn or approximated mark; if a needed mark is missing, ask the user for it before building.
- **UI glyphs:** the kit holds a small set of generic solid glyphs (calendar, clock, pin, video, user, users, rotate, bell, mail, sms, wa, card, check, tag, globe) for icons inside recreated UI. They are not FluentBooking's own UI icons; replace them as soon as the official icon files are supplied, and never present them as a brand mark. Never mix two icon sets in one graphic.
- Meeting types use the product's own notation: a person, an arrow, then a person or group.
- Partner logos (Google Calendar, Zoom, Stripe and others) are not bundled; ask the user for official files, and until then show names as text only. Never redraw a mark.

## Formats
Hero image 720×600 (default) · feature cards 290×400 and 522×400 · blog cover 1200×628 · social 1080×1080, 1080×1350, 1080×1920 · web hero 1440 wide. Recipes are in `formats.md`.
