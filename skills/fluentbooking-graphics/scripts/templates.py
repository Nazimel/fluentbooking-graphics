"""More template tests: 1440 web hero, 1080x1350 portrait social, 1080x1920 story, 1200x628 integration graphic.

Run:  python3 templates.py OUTDIR
"""
import os, sys
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from kit import *

out = sys.argv[1] if len(sys.argv) > 1 else '.'
os.makedirs(out, exist_ok=True)

def save(name, w, h, inner, ground, title, radius=0):
    root = board(w, h, inner, radius)
    write_board(f'{out}/{name}.dc.html', w, h, root, title, ground=ground)
    write_preview(f'{out}/{name}.preview.html', root, ground=ground, page_bg='#16244F')

SLOTS = (('7:00 AM', '4 spots left', False), ('8:30 AM', '2 spots left', True), ('10:00 AM', '6 spots left', False),
         ('12:30 PM', '3 spots left', False), ('6:00 PM', '9 spots left', False), ('7:30 PM', '5 spots left', False))
DESC = 'A gentle 60 minute flow for every level. Mats and blocks are ready at the studio.'

# 1) Web hero 1440x780 (sky): nav, copy and buttons left, the booking page right with the details form and the
#    confirmation overlapping its lower edge. 64px page margins.
scene = (blob(820, -160, 760, 760, '#C7DEFA') + blob(-200, 520, 560, 480, BLUE_TINT)
         + nav_bar(64, 40, 1312)
         + copy_block(64, 236, 584, 'APPOINTMENT SCHEDULING FOR WORDPRESS', 'Your calendar fills itself,<br>on your own site',
                      'Share one booking page, let clients pick a time that suits them, and get reminders, payments and follow-ups handled for every booking.',
                      h_size=48, l_size=20, gap=22)
         + pos(64, 548, f'<div style="display: flex; gap: 14px">{button("Get FluentBooking", True, 17)}{button("See all features", False, 17)}</div>')
         + booking_page(668, 150, 708, None, s=0.96, description=DESC, slots=SLOTS, z=1)
         + details_form(1092, 484, 284, s=0.95, z=3)
         + confirm_card(640, 560, 370, 'Morning Flow Class', 'Maya Ortiz, Stillpoint Yoga', 'Tue, October 3, 8:30 AM', 'In Person (Organizer Address)', s=1.0, z=4))
save('web-hero-1440x780', 1440, 780, scene, SKY, 'FluentBooking web hero, 1440×780')

# 2) Portrait social 1080x1350 (peach): logo and badge, headline and line, then the team and the four meeting types.
scene = (blob(380, 520, 900, 900, BLUE_TINT) + blob(-260, 1000, 640, 560, '#FFD3C4')
         + lockup(72, 72, 42) + pos(808, 80, eyebrow('MEETING TYPES', bg='#FFFFFF', size=14))
         + copy_block(72, 172, 860, '', 'One booking page for<br>every kind of meeting',
                      'Run one-to-one calls and group classes, or share calls across your team with round robin and collective scheduling.',
                      h_size=72, l_size=26)
         + team_card(72, 672, 356, s=1.85, z=2)
         + dash_curve(428, 790, 456, 920, w=1080, h=1350, z=1)
         + type_rows(456, 472, 552, s=2.3, z=3, gap=20))
save('social-meeting-types-1080x1350', 1080, 1350, scene, PEACH, 'FluentBooking portrait social, 1080×1350')

# 3) Story 1080x1920 (mint): keep the top 250 and bottom 250 clear of key content for the app's own overlays,
#    and centre the whole stack in the space between them.
#    Logo, headline and line, then the booking page whole and the Payment Summary overlapping its lower edge.
pay = dict(item='Physio Session', price='$80.00', coupon=('BFRIDAY30', '-$24.00'), total='$56.00', method='Stripe')
scene = (blob(300, 700, 1000, 1000, AQUA) + blob(-300, 1300, 700, 700, '#D3F7C6')
         + lockup(72, 312, 46)
         + copy_block(72, 412, 936, '', 'Get paid the moment<br>clients book',
                      'Add a price to any appointment, accept coupons and take payment at checkout on your own WordPress site.',
                      h_size=72, l_size=28)
         + booking_page(72, 717, 936, None, s=1.27, host='Dr. Amara Cole', initials='AC', event='Physio Session', duration='45 Min',
                        location='Larkfield Clinic', first=6, selected=24, date_label='Fri, November 24', show_slots=True,
                        slots=(('9:00 AM', '1 spot left', False), ('10:30 AM', '1 spot left', True), ('12:00 PM', '1 spot left', False), ('1:30 PM', '1 spot left', False), ('3:00 PM', '1 spot left', False), ('4:30 PM', '1 spot left', False)),
                        month='November', available=(1, 2, 3, 6, 7, 8, 9, 10, 13, 14, 15, 16, 17, 20, 21, 22, 24, 27, 28, 29, 30),
                        description='A one to one session to assess and treat sports and joint pain.', z=1)
         + payment_card(72, 1173, 540, s=1.55, z=3, **pay)
         + confirm_card(636, 1267, 372, 'Physio Session', 'Dr. Amara Cole', 'Fri, November 24, 10:30 AM', 'Larkfield Clinic', s=1.45, z=4,
                        extra=f'<div style="display: flex; align-items: center; gap: 10px; font-size: 17px; color: {SLATE}"><span style="display: flex; color: {BLUE}">{glyph("card", 22)}</span>Payment {status("Paid", 14)}</div>'))
save('story-paid-bookings-1080x1920', 1080, 1920, scene, MINT, 'FluentBooking story, 1080×1920')

# 4) Integration graphic 1200x628 (aqua): both official marks, headline, and the automation that connects them.
auto = [(brand('icon', 22), 'Discovery Call Booked', 'New Booking (FluentBooking)'),
        (glyph('tag', 19), 'Tag as New Client', 'Apply Tag'),
        (glyph('mail', 19), 'Send Welcome Email', 'Send Custom Email'),
        (glyph('clock', 19), 'Wait 2 Days', 'Wait X Days/Hours'),
        (glyph('mail', 19), 'Send Follow-up Email', 'Send Custom Email')]
scene = (blob(640, -180, 720, 720, AQUA) + blob(-160, 420, 420, 380, BLUE_TINT)
         + pos(64, 64, f'<div style="display: flex; align-items: center; gap: 16px">{brand_logo("logo", 34)}'
                       f'<span style="{JOST}; font-size: 26px; color: {SLATE}">+</span>{logo("fluentcrm-icon", 38)}'
                       f'<span style="{JOST}; font-size: 26px; font-weight: 600; color: {INK}">FluentCRM</span></div>')
         + copy_block(64, 190, 470, 'INTEGRATION', 'Every booking becomes a contact you can follow up',
                      'New bookings land in FluentCRM with the right tags, and your welcome emails start on their own.', h_size=46)
         + automation_flow(584, 64, 300, auto, s=1.05, z=2)
         + crm_profile(906, 200, 230, 'Priya Shah', 'PS', stat=('Email: 1', 'Open: 1', 'Click: 0'), tags=('New Client', 'Discovery Call'), s=0.95, z=3))
save('integration-fluentcrm-1200x628', 1200, 628, scene, AQUA_BG, 'FluentBooking + FluentCRM integration, 1200×628')
print('ok')
