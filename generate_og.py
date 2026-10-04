"""
Generate official 1200x630 Twitter/X Post Card Image
Includes the visual curve chart AND the clear cycle stages printed directly on the card photo,
designed to attract maximum engagement on X feeds. Clean fintech dark theme, zero emojis.
"""
from PIL import Image, ImageDraw, ImageFont

width, height = 1200, 630
img = Image.new("RGBA", (width, height), (9, 10, 15, 255))
draw = ImageDraw.Draw(img)

# Try loading standard Windows fonts
try:
    font_brand = ImageFont.truetype("C:/Windows/Fonts/segoeuib.ttf", 26)
    font_badge = ImageFont.truetype("C:/Windows/Fonts/consola.ttf", 12)
    font_stage_title = ImageFont.truetype("C:/Windows/Fonts/segoeuib.ttf", 15)
    font_stage_desc = ImageFont.truetype("C:/Windows/Fonts/segoeui.ttf", 12)
    font_label = ImageFont.truetype("C:/Windows/Fonts/segoeuib.ttf", 13)
    font_mono = ImageFont.truetype("C:/Windows/Fonts/consola.ttf", 11)
    font_hero = ImageFont.truetype("C:/Windows/Fonts/segoeuib.ttf", 18)
except:
    font_brand = ImageFont.load_default()
    font_badge = ImageFont.load_default()
    font_stage_title = ImageFont.load_default()
    font_stage_desc = ImageFont.load_default()
    font_label = ImageFont.load_default()
    font_mono = ImageFont.load_default()
    font_hero = ImageFont.load_default()

# Background grid lines (right chart section)
grid_color = (255, 255, 255, 10)
for x in range(460, width - 40, 60):
    draw.line([(x, 60), (x, height - 70)], fill=grid_color, width=1)
for y in range(80, height - 70, 50):
    draw.line([(440, y), (width - 40, y)], fill=grid_color, width=1)

# Subtle background glow behind peak and moonshot
for r in range(140, 0, -8):
    alpha = int(14 * (1 - r / 140))
    draw.ellipse([720 - r, 150 - r, 720 + r, 150 + r], fill=(16, 185, 129, alpha))
    draw.ellipse([1120 - r, 100 - r, 1120 + r, 100 + r], fill=(251, 191, 36, alpha))

# --- LEFT PANEL: The Written Post Lines on the Card ---
draw.rectangle([(30, 24), (430, height - 24)], fill=(14, 17, 26, 245), outline=(255, 255, 255, 25), width=1)

# Top badge
draw.rectangle([(48, 40), (195, 62)], fill=(16, 185, 129, 25), outline=(16, 185, 129, 120), width=1)
draw.text((58, 44), "THE CRYPTO CYCLE", font=font_badge, fill=(16, 185, 129, 255))

draw.text((48, 72), "How Retail Becomes", font=font_brand, fill=(243, 244, 246, 255))
draw.text((48, 104), "Exit Liquidity", font=font_brand, fill=(249, 115, 22, 255))

# The written stages along the card photo
stages_text = [
    ("1. Accumulation", "Smart money buys low in silence", (16, 185, 129)),
    ("2. Breakout", "Early technical traders step in", (16, 185, 129)),
    ("3. KOL Hype", "Influencers shill, you buy at $100", (168, 85, 247)),
    ("4. Retail FOMO", "Newbies buy top, whales exit", (249, 115, 22)),
    ("5. Retracement", "'Just a healthy dip' - you hold", (239, 68, 68)),
    ("6. Dead Cat Bounce", "Relief rally fails, you stay trapped", (148, 163, 184)),
    ("7. Max Pain Bleed", "You hold down -90% in despair", (239, 68, 68)),
    ("8. Re-Accumulation", "Smart money buys the bottom floor", (16, 185, 129)),
    ("9. Fundamental Recovery", "Real protocol growth recovers to $100", (16, 185, 129)),
    ("10. Break-Even Exit", "You sell flat... then it pumps to ATH!", (251, 191, 36)),
]

y_pos = 146
for title, desc, col in stages_text:
    draw.ellipse([(48, y_pos + 4), (54, y_pos + 10)], fill=col)
    draw.text((62, y_pos), title, font=font_stage_title, fill=col)
    draw.text((62, y_pos + 17), desc, font=font_stage_desc, fill=(148, 163, 184, 255))
    y_pos += 38

# Left panel footer link
draw.line([(48, height - 64), (410, height - 64)], fill=(255, 255, 255, 20), width=1)
draw.text((48, height - 52), "LIVE INTERACTIVE ENGINE: 327279.github.io/crypto-cycle", font=font_mono, fill=(148, 163, 184, 255))


# --- RIGHT PANEL: Visual Market Curve ---
# Break-even line at Y=250
break_even_y = 250
for x in range(450, 1160, 12):
    draw.line([(x, break_even_y), (x + 6, break_even_y)], fill=(249, 115, 22, 120), width=2)

draw.rectangle([(450, break_even_y - 10), (590, break_even_y + 10)], fill=(9, 10, 15, 240), outline=(249, 115, 22, 160), width=1)
draw.text((460, break_even_y - 7), "ENTRY LEVEL ($100)", font=font_mono, fill=(249, 115, 22, 255))

# Curve Bezier Segments
def bezier_point(p0, p1, p2, p3, t):
    x = (1-t)**3 * p0[0] + 3*(1-t)**2 * t * p1[0] + 3*(1-t) * t**2 * p2[0] + t**3 * p3[0]
    y = (1-t)**3 * p0[1] + 3*(1-t)**2 * t * p1[1] + 3*(1-t) * t**2 * p2[1] + t**3 * p3[1]
    return (x, y)

curve_segments = [
    # Accumulation
    ((460, 480), (490, 480), (520, 475), (550, 465), (16, 185, 129)),
    # Breakout
    ((550, 465), (580, 455), (610, 410), (640, 350), (16, 185, 129)),
    # Markup to entry
    ((640, 350), (665, 300), (690, 260), (715, 250), (16, 185, 129)),
    # Peak FOMO
    ((715, 250), (740, 200), (765, 120), (790, 115), (16, 185, 129)),
    # Drop
    ((790, 115), (810, 115), (835, 230), (860, 290), (239, 68, 68)),
    # Dead cat
    ((860, 290), (880, 280), (895, 245), (915, 245), (239, 68, 68)),
    # Bleed -90%
    ((915, 245), (935, 250), (965, 440), (1000, 485), (239, 68, 68)),
    # Floor
    ((1000, 485), (1020, 485), (1040, 485), (1060, 485), (16, 185, 129)),
    # Phoenix Rebirth
    ((1060, 485), (1085, 485), (1105, 360), (1125, 250), (16, 185, 129)),
    # Moonshot past breakeven
    ((1125, 250), (1145, 170), (1165, 90), (1180, 65), (251, 191, 36)),
]

for p0, p1, p2, p3, base_col in curve_segments:
    pts = [bezier_point(p0, p1, p2, p3, i / 30.0) for i in range(31)]
    # Glow
    for i in range(len(pts) - 1):
        draw.line([pts[i], pts[i+1]], fill=(base_col[0], base_col[1], base_col[2], 50), width=9)
    # Core
    for i in range(len(pts) - 1):
        draw.line([pts[i], pts[i+1]], fill=(base_col[0], base_col[1], base_col[2], 255), width=3)

# Key Visual Callouts on Curve
chart_callouts = [
    (500, 478, "Smart money accumulates", (16, 185, 129), (500, 505), "center"),
    (715, 250, "You buy in ($100)", (249, 115, 22), (640, 225), "right"),
    (790, 115, "Retail FOMO at top", (249, 115, 22), (790, 85), "center"),
    (860, 290, "Healthy retrace?", (239, 68, 68), (875, 295), "left"),
    (1000, 485, "Down 90% capitulation", (239, 68, 68), (960, 515), "right"),
    (1060, 485, "Smart money re-buys", (16, 185, 129), (1075, 515), "left"),
    (1125, 250, "You sell at break-even", (249, 115, 22), (1110, 280), "right"),
    (1180, 65, "Pumps to ATH!", (251, 191, 36), (1170, 40), "right"),
]

for cx, cy, label, col, (lx, ly), align in chart_callouts:
    draw.ellipse([cx - 6, cy - 6, cx + 6, cy + 6], fill=(9, 10, 15, 255), outline=col, width=2)
    draw.ellipse([cx - 3, cy - 3, cx + 3, cy + 3], fill=col)

    bbox = font_label.getbbox(label)
    w = bbox[2] - bbox[0]
    if align == "center":
        pos_x = lx - w // 2
    elif align == "right":
        pos_x = lx - w
    else:
        pos_x = lx
    draw.text((pos_x, ly), label, font=font_label, fill=(243, 244, 246, 255))

# Right top title
draw.text((450, 36), "MARKET PSYCHOLOGY CURVE", font=font_hero, fill=(243, 244, 246, 255))

img.save("og-image.png", "PNG")
print("Saved enhanced og-image.png successfully")
