# FluentBooking product facts for graphics (checked 2026-11-19)

Every label a graphic may show, checked against the **FluentBooking Product Brain** (FluentBooking and Pro 2.4.0, released 09 Sep 2026) and the admin on the team's local site. This is a convenience copy for drawing; the brain stays the source of truth. If something is not here, ask the brain before drawing it; if the brain answers UNKNOWN, leave it out.

**About Pro:** this table is for knowing, not for drawing; graphics show no PRO badge unless the request asks for one. The brain records which plugin implements a feature and deliberately makes no licensing claim. The `PRO` column below follows where the brain puts the feature (FluentBooking Pro) or a "(Pro)" label printed in the product itself. Confirm against the pricing page before launch copy.

## Event types (Calendars › New Event Type, Add Team)
| Label | What it is | PRO |
|---|---|---|
| One-to-One | One host with One invitee | |
| Group / Group Event | One host with Group of invitees | |
| Round Robin | One rotating host with One invitee (team) | PRO (teams) |
| Collective | Multiple hosts with One invitee (team) | PRO (teams) |
| One-off Event | Single event, from New › One-off Event | PRO (SingleEvent) |
| Recurring Event | Repeats every few Days, Weeks, Months or Years; "Require All Maximum Occurrences" | not stated |

## Event settings tabs
Event Details · Availability · Limits · Question Settings · Email Notification · SMS Notification · Recurring Settings · Advanced Settings · Payment Settings · Webhooks Feeds · Integrations

- **Durations:** 15, 30, 45, 60 Minutes, Custom; multi-duration options from 5 to 480 Minutes ("Allow attendee to select duration").
- **Buffer times:** No buffer time, 5 to 120 Minutes. **Slot intervals:** Use event length (default), 5 to 120 Minutes.
- **Limits:** Before Event, After Event, Minimum Notice, Time-slot intervals, Limit booking frequency, Limit total booking duration, Lock timezone on booking page.
- **Advanced Settings:** Booking Title, Submit Button Text, Redirect After Booking, Requires Confirmation, Allow Multiple Booking, Attendee Cannot Cancel, Attendee Cannot Reschedule, Landing Page Settings.

## Locations
In Person (Attendee Address) · In Person (Organizer Address) · Attendee Phone Number · Organizer Phone Number · Online Meeting · Custom · **Google Meet (Pro)** · **MS Teams (Pro)** · **Zoom Video (Pro)**

## Booking questions (field types)
Email, Text, Textarea, Number, Phone, Radio, Select, Multi Select, Checkbox, Checkbox Group, Date, File, Hidden, Terms & Conditions. System questions: Your Name, Your Email, What is this meeting about?, Additional Guests, Your Address, Reason for cancellation, Reason for reschedule.

## Email notifications (exact labels)
Booking Confirmation Email to Attendee · Booking Confirmation Email to Organizer (You) · Configure Meeting Reminder to Attendee · Configure Meeting Reminder to Organizer (You) · Booking Cancelled by Attendee (email to Organizer) · Booking Cancelled by Organizer (email to Attendee) · Booking Rescheduled by Attendee (email to Organizer) · Booking Rescheduled by Organizer (email to Attendee) · Booking Approval Request to Host (email to Organizer) · Booking Submission Confirmation (email to Attendee) · Booking Declined by Organizer (email to Attendee)

## SMS Notification (Twilio, PRO)
Receiver *, SMS Body, Timing, Save SMS. Send by SMS or WhatsApp; WhatsApp Number is optional in the Twilio settings.

## Statuses
- **Booking:** Scheduled, Rescheduled, Completed, Pending, Cancelled, Rejected.
- **No Show** fires an event other plugins (FluentCRM) can react to, but it is **not** a status a booking displays. Never draw a "No Show" status badge.
- **Payment:** Pending, Paid, Failed, Refunded, Partially Paid, Partially Refunded.
- **Bookings list tabs:** Upcoming, Completed, All, Recently Booked (period filter also has Pending, Cancelled).

## Merge tags (50 in total; the ones most useful in graphics)
`{{guest.first_name}}` `{{guest.full_name}}` `{{guest.email}}` `{{guest.timezone}}` `{{booking.event_name}}` `{{booking.full_start_end_guest_timezone}}` `{{booking.start_time_human_format}}` `{{booking.location_details_text}}` `{{host.name}}` `{{calendar.title}}` `{{add_booking_to_calendar}}` and the URL tags `##booking.reschedule_url##`, `##booking.cancelation_url##`. Use `merge()` in the kit; never invent a tag.

## Integrations and modules
| Item | Implemented in | PRO |
|---|---|---|
| FluentCRM, Fluent Forms, Fluent Boards, FluentCart, Elementor | FluentBooking | |
| Calendars (Google, Outlook, Apple, Nextcloud remote calendars) | FluentBooking Pro | PRO |
| Payment methods (Stripe, PayPal) | FluentBooking Pro | PRO |
| Coupon module | FluentBooking Pro | PRO |
| WooCommerce checkout | FluentBooking Pro | PRO |
| Twilio (SMS, WhatsApp) | FluentBooking Pro | PRO |
| Webhooks | FluentBooking Pro | PRO |
| Zoom | FluentBooking Pro | PRO |
| MCP server for AI agents (new in 2.4.0, 9 tools, 3 prompts) | both | |

FluentCRM integration feeds fire on Booking Confirmed, Booking Completed, Booking Cancelled, Booking Rescheduled and Booking Rejected.

## Booking detail (for "after the booking" scenes)
Invitees Information, Meeting Information, Internal Note, Notes (Private to your team), **Meeting Activities** with log lines such as "Booking scheduled email sent to guest", "Booking scheduled email sent to host", "Google Calendar event created" and "FluentCRM Integration Feed: Contact has been updated in FluentCRM", and the **CRM Profile** card (status, Emails, Opens, Clicks, tags) when FluentCRM is active.

## Not facts
Anything on a particular site (what is connected, saved settings, real bookings) is not a product fact. The local site's real names (Brady Sloan and others) must never appear in graphics.
