"""Feature card pairs (290x400 collapsed, 522x400 expanded) for four feature pages.

Run:  python3 feature_cards.py OUTDIR
Collapsed cards keep the top 48px clear for the label pill. Expanded cards keep the top 48px and the lower-left
236x110 clear for the page's headline and line, and switch to a different pastel ground. Every label is from
product-facts.md; sample brands are fictional.
"""
import os, sys
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from kit import *

out = sys.argv[1] if len(sys.argv) > 1 else '.'
os.makedirs(out, exist_ok=True)

def save(name, w, h, inner, ground, title):
    root = board(w, h, inner, 28)
    write_board(f'{out}/{name}.dc.html', w, h, root, title, ground=ground)
    write_preview(f'{out}/{name}.preview.html', root, ground=ground, page_bg='#16244F')

PAY_EXTRA = lambda s: (f'<div style="display: flex; align-items: center; gap: {8*s:.0f}px; font-size: {12*s:.1f}px; color: {SLATE}">'
                       f'<span style="display: flex; color: {BLUE}">{glyph("card", round(15*s))}</span>Payment {status("Paid", round(10*s))}</div>')

# ---------------------------------------------------------------- 1) Meeting Types
# Collapsed (sky): the four meeting types, Round Robin selected, centred in the area below the label pill.
scene = blob(120, 180, 320, 320, '#C7DEFA') + type_rows(16, 92, 258, s=0.92)
save('fc-meeting-types-290x400', 290, 400, scene, SKY, 'Meeting Types, feature card 290×400')
# Expanded (peach): the team behind the Round Robin on the left, the types on the right, joined by a dashed line.
scene = (blob(240, 60, 380, 380, BLUE_TINT)
         + team_card(24, 72, 200, s=0.86, z=2)
         + dash_curve(224, 122, 262, 240, w=522, h=400, z=1)
         + type_rows(262, 75, 236, s=0.92, z=3, gap=12))
save('fc-meeting-types-522x400', 522, 400, scene, PEACH, 'Meeting Types, feature card 522×400')

# ---------------------------------------------------------------- 2) Paid Bookings
# Collapsed (mint): the Payment Summary with a Black Friday coupon, paid with Stripe.
pay = dict(item='Physio Session', price='$80.00', coupon=('BFRIDAY30', '-$24.00'), total='$56.00', method='Stripe')
scene = blob(-90, 200, 340, 340, AQUA) + payment_card(18, 113, 254, s=0.78, **pay)
save('fc-paid-bookings-290x400', 290, 400, scene, MINT, 'Paid Bookings, feature card 290×400')
# Expanded (butter): the paid booking confirmed on the left, the Payment Summary on the right.
scene = (blob(230, 40, 380, 380, '#FFEC99')
         + confirm_card(24, 99, 206, 'Physio Session', 'Dr. Amara Cole', 'Fri, November 24, 10:30 AM', 'Larkfield Clinic', s=0.8, z=2, extra=PAY_EXTRA(0.8))
         + payment_card(250, 89, 248, s=0.95, z=3, **pay))
save('fc-paid-bookings-522x400', 522, 400, scene, BUTTER, 'Paid Bookings, feature card 522×400')

# ---------------------------------------------------------------- 3) Reminders
sms = booking_thread('1 hour', '7:30 AM')
# On the collapsed card the email reminder overlaps the phone's lower half, so the phone shows the text reminder
# itself and its reschedule link above the overlap.
sms_short = [('time', 'Today 7:30 AM'), ('in', 'Hi Lena, your Morning Flow Class with Maya starts in 1 hour.'),
             ('in', f'Need a different time? Reschedule here: <span style="color: {BLUE_DEEP}">stillpoint.yoga/r/8K2</span>')]
# Collapsed (butter): a text reminder on the phone with its reschedule link, the email reminder overlapping below.
scene = (blob(60, 120, 360, 360, BLUE_TINT)
         + phone(45, 58, 200, 420, 'sms', messages=sms_short, s=0.86, z=1)
         + reminder_card(18, 270, 254, 'LP', 'Reminder: Morning Flow Class starts in 1 hour', 'Tue, October 3, 8:30 AM (Asia/Dhaka)', s=0.8, z=3))
save('fc-reminders-290x400', 290, 400, scene, BUTTER, 'Reminders, feature card 290×400')
# Expanded (sky): which emails go out on the left, the text reminder on the phone on the right.
rows = [('Booking Confirmation Email to Attendee', True), ('Configure Meeting Reminder to Attendee', True)]
scene = (blob(250, 80, 380, 380, '#C7DEFA')
         + notif_list(24, 94, 248, rows, s=0.74, z=2)
         + phone(298, 52, 200, 420, 'sms', messages=sms, s=0.86, z=3))
save('fc-reminders-522x400', 522, 400, scene, SKY, 'Reminders, feature card 522×400')

# ---------------------------------------------------------------- 4) Booking Automation
# Drawn as a FluentCRM automation in the FluentBooking website style (white panel, stacked blocks, + connectors),
# because the copy is about follow-ups that run on their own. Each step has a descriptive name over its real block:
# New Booking is FluentBooking's trigger in FluentCRM; Apply Tag and Send Custom Email are FluentCRM
# blocks; Create Task is Fluent Boards' FluentCRM action.
auto_steps = lambda s: [
    (brand('icon', round(24*s)), 'Discovery Call Booked', 'New Booking (FluentBooking)'),
    (glyph('tag', round(20*s)), 'Tag as New Client', 'Apply Tag'),
    (glyph('mail', round(20*s)), 'Send Welcome Email', 'Send Custom Email'),
    (logo('fluent-boards', round(22*s)), 'Prepare Call Notes', 'Create Task (Fluent Boards)')]
# Collapsed (aqua): the automation alone, centred below the label pill.
scene = blob(80, 140, 360, 360, AQUA) + automation_flow(28, 72, 234, auto_steps(0.78), s=0.78)
save('fc-booking-automation-290x400', 290, 400, scene, AQUA_BG, 'Booking Automation, feature card 290×400')
# Expanded (mint): the Fluent Forms booking form that starts it on the left, the automation on the right.
scene = (blob(240, 40, 380, 380, AQUA)
         + form_card(24, 76, 206, s=0.8, z=2)
         + dash_curve(230, 118, 262, 118, w=522, h=400, z=1)
         + automation_flow(262, 70, 236, auto_steps(0.8), s=0.8, z=3))
save('fc-booking-automation-522x400', 522, 400, scene, MINT, 'Booking Automation, feature card 522×400')
print('ok')
