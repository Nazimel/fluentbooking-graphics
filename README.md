# FluentBooking Graphics

Makes FluentBooking marketing graphics in the website illustration style: hero images, feature cards, blog covers, social visuals and email headers.

**Status: draft v0.1, not locked.** The colours, the font (Jost) and the format recipes are under test. Tested formats: 720×600 hero, 290×400 and 522×400 feature cards, 1200×628 blog cover, 1080×1080 and 1080×1350 social posts, 1080×1920 story, 1440×780 web hero, 1200×628 integration graphic and 600×200 email header.

## Install

In Claude (claude.ai, the desktop app or Cowork): **Customize > Plugins > Add > Add marketplace**, enter the repository once it is published (for example `Nazimel/fluentbooking-graphics`), then install **fluentbooking-graphics**. Or upload the packaged `.plugin` file.

In Claude Code:

```
/plugin marketplace add Nazimel/fluentbooking-graphics
/plugin install fluentbooking-graphics@fluentbooking-graphics
```

## How to use
Ask in plain language, for example:
- "Make a hero image for the Round Robin scheduling page."
- "Social visual for appointment reminders by WhatsApp. Headline: Fewer no-shows, every week."
- "Blog cover for: How to take payments for appointments in WordPress."

Say the size and where it goes if you know them; otherwise 720×600 is used and named in the reply.

You get PNG files at 2× resolution, plus an editable board (on your Design canvas when available) where you can change text and the ground colour.

## What it relies on
- **FluentBooking Product Brain plugin:** every setting, notification, status, location, merge tag and integration in a graphic is checked against it, and Pro features are noted in the reply; PRO badges appear only when asked for.
- Everything else is bundled: the brand guide, product facts, story recipes, tokens, the official FluentBooking logos and icons (Updated Logo 2025), Fluent family logos, the drawing kit, a render check and five test cards.

## Rules it follows
- Real features only, with descriptive names that map to them. No "No Show" status badge.
- Fictional sample brands (Stillpoint Yoga, Northbeam Consulting, Larkfield Clinic) and invented people drawn as initials.
- White cards with a 2px blue outline (#4587EC) on one pastel ground; brand blue #2653C7.
- Illustrations are always paired with copy. No mid-sentence dashes in copy.

## Still needed before locking
- The real font name from the designer (Jost is a visual match).
- FluentBooking's own UI icon set (the kit uses generic glyphs inside UI recreations until then).
- Confirmation that the Fluent family logos in assets/logos are the Updated Logo 2025 versions.
- Partner logo files (Google Calendar, Zoom, Stripe and others).

## Version
0.4.1 · Brand guide draft v0.1. Raise `version` in `.claude-plugin/plugin.json` and `marketplace.json` on every release. Send changes to Nazir.
