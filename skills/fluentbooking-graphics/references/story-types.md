# Story types and composition (draft v0.1)

Five stories cover what FluentBooking does. Each has one anchor object built on a real screen, at most two support cards, a default ground and a kit recipe. The test cards in `examples/` show one of each at 720×600.

| # | Story | Anchor | Support cards (pick up to two) | Ground | Example |
|---|---|---|---|---|---|
| 1 | The booking page | `booking_page()` bleeding right and bottom | `details_form()` over the slot column, `confirm_card()` with a booking status over the host panel | Sky | `01-booking-page` |
| 2 | Event types | stacked `event_card()`s | `type_chooser()` (Round Robin, Collective, PRO), a dashed curve from the card to the chooser | Peach | `02-event-types` |
| 3 | Before the meeting | `notif_list()` with real labels | `reminder_card()`, `phone()` with an SMS or WhatsApp reminder (PRO) | Butter | `03-before-the-meeting` |
| 4 | After the booking | `booking_timeline()`: a dashed rail with round nodes and one card per step, starting with who booked | `crm_profile()` joined to the last step by a dashed curve | Aqua | `04-after-the-booking` |
| 5 | Getting paid | `payment_card()` with a coupon (PRO) | `booking_page()` behind it with slots hidden, `confirm_card()` with the Paid payment status over its empty lower right | Mint | `05-getting-paid` |

## Layering
Ground → one or two large shapes in a second palette colour (no decorative sparkles) → anchor (z 1) → connectors → support cards (z 3 to 5) → brand tile. Never more than three card layers deep.

## No blank calendars
A booking page, month grid or any anchor card must never show a large empty area (more than about a quarter of what is visible). Cover that space with overlay support cards: the details form over the slot column, a confirmation card over the host panel or under the time zone, a reminder, a status pill. Overlays sit on top of the anchor with the blue outline and floating shadow, so the empty part of the calendar is what they hide. Crop or shorten the anchor only when no fitting overlay exists.

## No dead space anywhere
The same goes for the whole scene. Size cards, and recreated screens above all, to their content rather than to a fixed height (a real screen has no padded white space inside it, so pass `h=None` to `booking_page()` and give it real content such as the event description and a full slot list), and check the render for any empty patch of ground or card bigger than about a fifth of the canvas that is not a deliberate breathing margin. Fix it by moving or scaling the cards, letting a support card overlap the anchor, or tightening the anchor; never leave it.

## Crop with intent
A crop has to read as a decision, never as a screen that did not fit.
- Bleed only a trailing edge where the content obviously continues (the end of a slot list, the right side of a phone, a list that runs on). Never slice through a calendar's columns, a label, a button or a line of text.
- When the full booking page does not fit, rebuild it from whole components instead of slicing it: `grid_card()` for the month, `slots_card()` for the picked day, `details_form()`, `confirm_card()`. Arrange them so they tell the step (pick a day, pick a time, enter details), joined by a dashed line only where it runs over open ground, never across a grid or text.
- Scale a screen down until it fits whole before cropping it at all; a recreated page that fits inside its panel beats a cut one.

## Spacing between cards
Cards either breathe or overlap on purpose. Keep at least 16px (24px on wide cards) between cards that sit side by side, or overlap them by 40px or more with one clearly on top. Never let two cards touch, overlap by a sliver or sit a few pixels apart. Check with `python3 scripts/render.py --gaps preview.html W H`.

## Copy to scene spacing
The scene starts close to the copy above it: about 56px at 1080 wide (40 to 64px at other sizes, scaled with the canvas). Never leave a band of empty ground between the text and the cards; scale the scene up or move the copy instead. When the canvas is tall (portrait, story), grow the scene to fill the height, or centre the whole copy and scene stack in the safe area.

## Bleed and safe zones
- The anchor may bleed off the right and bottom edges only. Support cards stay at least 8px inside every edge.
- Nothing important under another card: event names, statuses and PRO badges stay visible.
- Feature cards (290×400, 522×400) keep the top 48px clear for the page's label pill, and wide cards keep the lower-left ~45% × 30% clear for page copy.

## Scale
Scale the whole scene with the `s` argument, never a single label. Hero 720×600: s 0.94 to 1.05. Feature card 290×400: s 0.55 to 0.65 with the booking page cropped to the grid and slots. Blog cover panel 576 wide: s 0.75 to 0.85. Social 1080: s 1.3 to 1.5. Minimum text is 9px at the final size.

## Content rules
- One story per graphic; a collapsed and expanded card pair tell the same story.
- Dates, weekdays, durations, time zones and totals agree (see brand-guide rule 6).
- Automation versus timeline: anything that is set up to run on its own (follow-ups, tagging, tasks after a booking) is drawn as a FluentCRM automation with `automation_flow()`, in the FluentBooking website style: a white outlined panel of stacked blocks joined by thin lines with + circles, each block a descriptive step name over its real block label (trigger New Booking (FluentBooking); actions such as Apply Tag, Send Custom Email, Wait X Days/Hours, Create Task (Fluent Boards)). Check every block label in the FluentCRM product brain. `booking_timeline()` is only for a log of what already happened on one booking (Meeting Activities).
- Show the copy's promise, not the setup screen behind it. If the copy names outcomes (tag new clients, start follow-up emails, pass work to the team), draw those outcomes as the steps of an automation, rather than a settings list of the plugins involved.
- No blank screens: a phone always shows a believable thread that fills its screen (`booking_thread()`: the confirmation the day before, the client's reply, then the reminder with its reschedule link), anchored to the bottom like a real chat. When a card overlaps the phone, keep the key messages above the overlap.
- Every support card must add something the others do not.
- Every badge, chip and status must say something the reader cares about in this story (Scheduled, Paid, a tag the automation applied). Drop admin labels that only describe configuration, such as "System Enabled". Do not add a card that repeats what the anchor or another card already shows (for example a Timing card next to a reminder that already says "starts in 15 minutes"). `timing_chip()` is for scenes about setting up the reminder, where it replaces the sent reminder.
- Reminder copy and any Timing setting agree ("15 Minutes Before" with "starts in 15 minutes").
- No PRO badges unless the request asks for them; when asked, the badge sits next to the Pro thing itself, never floating loose.
