"""Format test set: the same kit across the untested sizes.

Run:  python3 format_examples.py OUTDIR
Writes .dc.html boards and preview HTML; render each preview with render.py at the size in the file name.
"""
import os, sys
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from kit import *

out = sys.argv[1] if len(sys.argv) > 1 else '.'
os.makedirs(out, exist_ok=True)

def save(name, w, h, inner, ground, title, radius=32, options=GROUNDS):
    root = board(w, h, inner, radius)
    write_board(f'{out}/{name}.dc.html', w, h, root, title, ground=ground, options=options)
    write_preview(f'{out}/{name}.preview.html', root, ground=ground, page_bg='#16244F')

SLOTS6 = (('7:00 AM', '4 spots left', False), ('8:30 AM', '2 spots left', True), ('10:00 AM', '6 spots left', False),
          ('12:30 PM', '3 spots left', False), ('6:00 PM', '9 spots left', False), ('7:30 PM', '5 spots left', False))
DESC = 'A gentle 60 minute flow for every level. Mats and blocks are ready at the studio.'

# 1) Feature card, collapsed 290x400 (sky). Top 48px clear for the page's label pill. The full booking page does
#    not fit at this size, so the screen is rebuilt from whole components instead of being sliced: the month grid
#    as its own card, and the slot card for the picked day overlapping it.
scene = (blob(110, 140, 320, 320, '#C7DEFA') + grid_card(15, 58, 250, selected=3, s=0.8, z=1, title='Morning Flow Class · Maya Ortiz')
         + slots_card(99, 235, 176, 'Tue, October 3', SLOTS6[:3], s=0.78, z=3))
save('fc-booking-290x400', 290, 400, scene, SKY, 'FluentBooking feature card, collapsed, 290×400', radius=28)

# 2) Feature card, expanded 522x400 (peach: a different pastel from the collapsed card marks the hover state). Top 48px clear; lower-left ~236x110 clear for the page's copy.
s = 0.6
scene = (blob(280, 90, 380, 380, BLUE_TINT) + booking_page(24, 52, 620, None, s=s, slots=SLOTS6[:4], description=DESC, z=1)
         + details_form(262, 182, 236, s=0.72, z=3))
save('fc-booking-522x400', 522, 400, scene, PEACH, 'FluentBooking feature card, expanded, 522×400', radius=28)

# 3) Blog cover 1200x628: the pastel ground runs full bleed, with no white frame or inset panel. Copy left with the
#    official primary logo; the payment story sits directly on the ground at a size that fills the right half.
pay_extra = f'<div style="display: flex; align-items: center; gap: 7px; font-size: 12px; color: {SLATE}"><span style="display: flex; color: {BLUE}">{glyph("card", 15)}</span>Payment {status("Paid", 10)}</div>'
scene = (blob(720, -170, 640, 640, AQUA) + blob(-120, 460, 320, 320, '#D3F7C6')
         + lockup(64, 64, 36)
         + copy_block(64, 198, 468, 'PAYMENTS GUIDE', 'Take payments when clients book',
                      'Add a price to any appointment, accept coupons and get paid at checkout on your own WordPress site.')
         + booking_page(634, 64, 502, None, s=0.907, host='Dr. Amara Cole', initials='AC', event='Physio Session', duration='45 Min',
                        location='Larkfield Clinic', first=6, selected=12, date_label='Thu, October 12', show_slots=False,
                        description='A one to one session to assess and treat sports and joint pain.', z=1)
         + payment_card(550, 294, 313, s=0.946, z=3)
         + confirm_card(880, 376, 256, 'Physio Session', 'Dr. Amara Cole', 'Thu, October 12, 10:30 AM', 'Larkfield Clinic', s=0.965, z=4, extra=pay_extra))
save('blog-cover-payments-1200x628', 1200, 628, scene, MINT, 'FluentBooking blog cover, 1200×628', radius=0)

# 4) Social post 1080x1080: butter ground full bleed. Lockup and badge top, headline and line, then the scene directly
#    on the ground, bleeding off the bottom right.
rows = [('Booking Confirmation Email to Attendee', True), ('Configure Meeting Reminder to Attendee', True),
        ('Booking Rescheduled by Organizer (email to Attendee)', True)]
wa = booking_thread('15 minutes', '8:15 AM')
scene = (blob(440, 300, 960, 960, '#CFE2FB') + blob(-260, 640, 720, 640, '#FFEC99')
         + lockup(72, 72, 42)
         + pos(765, 80, eyebrow('APPOINTMENT REMINDERS', bg='#FFFFFF', size=14))
         + copy_block(72, 176, 780, '', 'Reminders that go out on their own',
                      'Confirmation and reminder emails send themselves, and WhatsApp or SMS reminders reach people where they read.',
                      h_size=64, l_size=24)
         + notif_list(72, 470, 590, rows, s=1.3, z=1)
         + reminder_card(112, 806, 530, 'LP', 'Reminder: Morning Flow Class starts in 15 minutes',
                         'Tue, October 3, 8:30 AM to 9:30 AM (Asia/Dhaka)', s=1.3, z=3)
         + phone(678, 500, 330, 640, 'wa', messages=wa, s=1.3, z=2))
save('social-reminders-1080x1080', 1080, 1080, scene, BUTTER, 'FluentBooking social post, 1080×1080', radius=0)

# 5) Email header 600x200 (sky). Lockup and short headline left, a slot list card bleeding off the right and bottom.
slots_card = slots_card(368, 27, 196, 'Tue, October 3', SLOTS6[:3], s=0.76, z=1)
scene = (blob(340, -70, 330, 330, '#C7DEFA')
         + lockup(36, 36, 28)
         + copy_block(36, 92, 310, '', 'Pick a time that suits you', 'Book your next class in a few clicks.', h_size=28, l_size=15, gap=8)
         + slots_card)
save('email-header-600x200', 600, 200, scene, SKY, 'FluentBooking email header, 600×200', radius=0)
print('ok')
