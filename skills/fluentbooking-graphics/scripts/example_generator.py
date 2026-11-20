"""Worked example: the five draft test cards, one per story type, at the 720x600 hero size.

Run:  python3 example_generator.py OUTDIR
Writes .dc.html boards and preview HTML into OUTDIR; render each preview with render.py.
Copy the closest scene as the starting point for a new request.

Sample brands are fictional: Stillpoint Yoga (host Maya Ortiz), Northbeam Consulting (team: Ravi Menon,
Lena Park, Tomas Weber), Larkfield Clinic (Dr. Amara Cole). Every product label is from product-facts.md.
"""
import os, sys
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from kit import *

out = sys.argv[1] if len(sys.argv) > 1 else '.'
os.makedirs(out, exist_ok=True)
W, H = 720, 600

def save(name, inner, ground, title):
    root = board(W, H, inner)
    write_board(f'{out}/{name}.dc.html', W, H, root, title, ground=ground)
    write_preview(f'{out}/{name}.preview.html', root, ground=ground, page_bg='#16244F')

# 1) THE BOOKING PAGE (sky): booking page anchor bleeding right and bottom. Its empty lower areas are covered by
#    overlays, never left blank: the details form over the slot column, the confirmation card over the host panel.
scene = (blob(-90, 360, 300, 300, BLUE_TINT)
         + booking_page(24, 40, 760, None, s=0.94, z=1,
                        description='A gentle 60 minute flow for every level. Mats and blocks are ready at the studio.',
                        slots=(('7:00 AM', '4 spots left', False), ('8:30 AM', '2 spots left', True), ('10:00 AM', '6 spots left', False),
                               ('12:30 PM', '3 spots left', False), ('6:00 PM', '9 spots left', False), ('7:30 PM', '5 spots left', False)))
         + details_form(446, 300, 256, z=3)
         + confirm_card(28, 366, 330, 'Morning Flow Class', 'Maya Ortiz, Stillpoint Yoga', 'Tue, October 3, 8:30 AM', 'In Person (Organizer Address)', z=4))
save('01-booking-page', scene, SKY, 'FluentBooking test card 1: the booking page')

# 2) EVENT TYPES (peach): stacked event cards, Round Robin and Collective chooser as the support card.
scene = (blob(470, -120, 380, 380, '#FFD3C4')
         + event_card(36, 60, 400, 'Discovery Call', BLUE_BRIGHT, '30 Min', 'Round Robin', 'Google Meet', 'video', is_pro=True, z=2)
         + event_card(36, 222, 400, 'Strategy Workshop', INDIGO, '90 Min', 'Collective', 'Zoom Video', 'video', is_pro=True, z=3)
         + event_card(36, 384, 400, 'Team Q&amp;A Session', '#1FA463', '60 Min', 'Group', 'Online Meeting', 'globe', z=4)
         + dash_curve(436, 110, 470, 236, w=W, h=H)
         + type_chooser(452, 236, 254, s=0.95, z=5))
save('02-event-types', scene, PEACH, 'FluentBooking test card 2: event types')

# 3) BEFORE THE MEETING (butter): notification list anchor, the sent reminder and a WhatsApp reminder on a phone.
#    No Timing card: the reminder headline already says when it goes out, and a third support card adds nothing.
rows = [('Booking Confirmation Email to Attendee', True), ('Configure Meeting Reminder to Attendee', True),
        ('Booking Rescheduled by Organizer (email to Attendee)', True), ('Booking Cancelled by Organizer (email to Attendee)', False)]
wa = booking_thread('15 minutes', '8:15 AM')
scene = (blob(-80, 380, 320, 300, '#FFF2B8', '46% 54% 50% 50%')
         + notif_list(30, 52, 440, rows, z=1)
         + reminder_card(46, 352, 360, 'LP', 'Reminder: Morning Flow Class starts in 15 minutes',
                         'Tue, October 3, 8:30 AM to 9:30 AM (Asia/Dhaka)', z=3)
         + phone(490, 150, 200, 480, 'wa', messages=wa, s=0.9, z=2))
save('03-before-the-meeting', scene, BUTTER, 'FluentBooking test card 3: reminders before the meeting')

# 4) AFTER THE BOOKING (aqua): a visual timeline of what happened after Priya booked, node by node, with the
#    FluentCRM Profile it ends on. Titles follow the real Meeting Activities log lines.
tl, boxes = booking_timeline(36, 70, [
    (avatar('PS', PEACH, px=48), None, 'Discovery Call booked', 'Priya Shah, Wed, October 4, 3:00 PM', '9:02 AM', status('Scheduled', 9.5)),
    ('mail', BLUE_LINE, 'Booking scheduled email sent to guest', '', '9:02 AM', ''),
    ('mail', BLUE_DEEP, 'Booking scheduled email sent to host', '', '9:02 AM', ''),
    ('calendar', '#1FA463', 'Google Calendar event created', 'Ravi Menon, Northbeam Consulting', '9:02 AM', ''),
    ('users', INDIGO, 'FluentCRM Integration Feed', 'Contact has been updated in FluentCRM', '9:03 AM', '')], card_w=350, gap=26, s=1.08)
l, t, r, b = boxes[-1]
scene = (blob(520, -140, 340, 340, AQUA)
         + tl
         + dash_curve(r, (t + b)//2, 478, 400, w=W, h=H)
         + crm_profile(478, 230, 230, 'Priya Shah', 'PS', tags=('Discovery Call', 'Northbeam Leads'), z=3))
save('04-after-the-booking', scene, AQUA_BG, 'FluentBooking test card 4: after the booking')

# 5) GETTING PAID (mint): the booking page sized to its content (no tall empty panel), the Payment Summary
#    overlapping its host panel, and the confirmation card with the Paid status over the space under the grid.
scene = (blob(-110, -110, 300, 300, '#D3F7C6')
         + booking_page(206, 36, 500, None, s=0.92, host='Dr. Amara Cole', initials='AC', event='Physio Session', duration='45 Min',
                        location='Larkfield Clinic', month='October', year='2028', first=6, selected=12, date_label='Thu, October 12',
                        show_slots=False, z=1)
         + payment_card(30, 214, 330, z=3)
         + confirm_card(392, 354, 304, 'Physio Session', 'Dr. Amara Cole', 'Thu, October 12, 10:30 AM', 'Larkfield Clinic', z=4,
                        extra=f'<div style="display: flex; align-items: center; gap: 8px; font-size: 12px; color: {SLATE}"><span style="display: flex; color: {BLUE}">{glyph("card", 15)}</span>Payment {status("Paid", 10)}</div>'))
save('05-getting-paid', scene, MINT, 'FluentBooking test card 5: getting paid')
print('ok')
