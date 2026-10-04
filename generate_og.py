"""
Generate high-impact, professional 1200x630 Twitter/X Post Card Image.
Design: Clean fintech dark theme, glowing market curve with clear psychological callout badges.
Optimized for virality and high engagement on X feeds.
"""
from PIL import Image, ImageDraw, ImageFont

width, height = 1200, 630
base = Image.new("RGBA", (width, height), (8, 10, 16, 255))

# Load fonts with safe fallbacks
def load_font(paths, size):
    for p in paths:
        try:
            return ImageFont.truetype(p, size)
        except:
            continue
    return ImageFont.load_default()

font_title = load_font(["C:/Windows/Fonts/segoeuib.ttf", "C:/Windows/Fonts/arialbd.ttf"], 28)
font_subtitle = load_font(["C:/Windows/Fonts/segoeui.ttf", "C:/Windows/Fonts/arial.ttf"], 14)
font_badge = load_font(["C:/Windows/Fonts/consola.ttf", "C:/Windows/Fonts/segoeuib.ttf"], 11)
font_callout_title = load_font(["C:/Windows/Fonts/segoeuib.ttf", "C:/Windows/Fonts/arialbd.ttf"], 13)
font_callout_sub = load_font(["C:/Windows/Fonts/segoeui.ttf", "C:/Windows/Fonts/arial.ttf"], 11)
font_axis = load_font(["C:/Windows/Fonts/consola.ttf", "C:/Windows/Fonts/arial.ttf"], 11)
font_brand = load_font(["C:/Windows/Fonts/consola.ttf", "C:/Windows/Fonts/segoeuib.ttf"], 14)

draw = ImageDraw.Draw(base)

# 1. Background Grid Lines
grid_col = (255, 255, 255, 12)
for x in range(60, width - 40, 75):
    draw.line([(x, 130), (x, height - 65)], fill=grid_col, width=1)
for y in range(160, height - 65, 55):
    draw.line([(50, y), (width - 40, y)], fill=grid_col, width=1)

# Outer Card Accent Border
draw.rectangle([(14, 14), (width - 14, height - 14)], outline=(255, 255, 255, 25), width=1)

# 2. Header Area
# Kicker badge
draw.rounded_rectangle([(60, 26), (195, 50)], radius=4, fill=(16, 185, 129, 30), outline=(16, 185, 129, 130), width=1)
draw.ellipse([(72, 35), (78, 41)], fill=(16, 185, 129, 255))
draw.text((86, 31), "MARKET CYCLE", font=font_badge, fill=(16, 185, 129, 255))

# Main Title
draw.text((60, 58), "THE CRYPTO MARKET CYCLE", font=font_title, fill=(245, 246, 250, 255))

# Subtitle
draw.text((60, 96), "How retail buys the hype, holds down -90%, sells break-even, and misses the pump.", font=font_subtitle, fill=(156, 163, 175, 255))

# Live site URL pill badge on top right
draw.rounded_rectangle([(width - 280, 36), (width - 60, 68)], radius=5, fill=(14, 18, 28, 245), outline=(16, 185, 129, 110), width=1)
draw.text((width - 262, 43), "crypto-cycles.vercel.app", font=font_brand, fill=(16, 185, 129, 255))

# 3. Break-Even Reference Line ($100 level)
be_y = 300
for x in range(50, width - 40, 14):
    draw.line([(x, be_y), (x + 7, be_y)], fill=(249, 115, 22, 110), width=1)

# Entry Level badge on left
draw.rounded_rectangle([(50, be_y - 12), (190, be_y + 12)], radius=4, fill=(12, 15, 24, 255), outline=(249, 115, 22, 180), width=1)
draw.text((62, be_y - 8), "ENTRY LEVEL ($100)", font=font_badge, fill=(249, 115, 22, 255))

# 4. Draw Smooth Market Curve
def bezier_point(p0, p1, p2, p3, t):
    x = (1-t)**3 * p0[0] + 3*(1-t)**2 * t * p1[0] + 3*(1-t) * t**2 * p2[0] + t**3 * p3[0]
    y = (1-t)**3 * p0[1] + 3*(1-t)**2 * t * p1[1] + 3*(1-t) * t**2 * p2[1] + t**3 * p3[1]
    return (x, y)

curve_sections = [
    # 1. Smart money accumulation
    ((60, 490), (120, 490), (180, 485), (240, 470), (16, 185, 129)),
    # 2. Breakout
    ((240, 470), (290, 460), (340, 400), (395, 340), (16, 185, 129)),
    # 3. Markup to Entry ($100)
    ((395, 340), (425, 300), (455, 300), (480, 300), (168, 85, 247)),
    # 4. Hype pump to top
    ((480, 300), (505, 240), (525, 185), (560, 175), (249, 115, 22)),
    # 5. Retracement dip
    ((560, 175), (585, 175), (615, 270), (650, 320), (239, 68, 68)),
    # 6. Dead cat bounce
    ((650, 320), (675, 310), (700, 285), (725, 285), (239, 68, 68)),
    # 7. Capitulation bleed to -90% floor
    ((725, 285), (750, 290), (785, 470), (825, 495), (239, 68, 68)),
    # 8. Smart money re-accumulates floor
    ((825, 495), (855, 495), (885, 495), (915, 495), (16, 185, 129)),
    # 9. Recovery to Break-even
    ((915, 495), (950, 495), (980, 380), (1010, 300), (16, 185, 129)),
    # 10. Moonshot beyond break-even
    ((1010, 300), (1035, 230), (1070, 160), (1120, 135), (251, 191, 36)),
]

overlay = Image.new("RGBA", (width, height), (0, 0, 0, 0))
ov_draw = ImageDraw.Draw(overlay)

for p0, p1, p2, p3, col in curve_sections:
    pts = [bezier_point(p0, p1, p2, p3, i / 32.0) for i in range(33)]
    for i in range(len(pts) - 1):
        ov_draw.line([pts[i], pts[i+1]], fill=(col[0], col[1], col[2], 55), width=12)
    for i in range(len(pts) - 1):
        ov_draw.line([pts[i], pts[i+1]], fill=(col[0], col[1], col[2], 120), width=6)
    for i in range(len(pts) - 1):
        draw.line([pts[i], pts[i+1]], fill=(col[0], col[1], col[2], 255), width=3)

base = Image.alpha_composite(base, overlay)
draw = ImageDraw.Draw(base)

# 5. Callout Cards and Badges
callouts = [
    # (anchor_x, anchor_y, title, subtitle, color, box_x, box_y, align)
    (150, 488, "1. Smart Money Buys", "Quiet baseline accumulation", (16, 185, 129), 70, 520, "left"),
    (480, 300, "2. You Buy In ($100)", "KOLs shill & hype begins", (249, 115, 22), 365, 250, "right"),
    (560, 175, "3. Retail FOMO Top", "Whales exit into liquidity", (249, 115, 22), 560, 125, "center"),
    (725, 285, "4. Dead Cat Bounce", "Last exit chance (you hold)", (239, 68, 68), 740, 255, "left"),
    (825, 495, "5. Down -90% Panic", "You hold in pure silence", (239, 68, 68), 735, 520, "center"),
    (915, 495, "6. Smart Money Re-Buys", "Accumulating the floor", (16, 185, 129), 905, 520, "left"),
    (1010, 300, "7. You Sell at Break-Even", "Exit flat after 2 years", (249, 115, 22), 995, 335, "right"),
    (1120, 135, "8. Pumps to New ATH", "Moonshot without you!", (251, 191, 36), 1100, 92, "right"),
]

for cx, cy, title, sub, col, bx, by, align in callouts:
    draw.ellipse([cx - 8, cy - 8, cx + 8, cy + 8], fill=(8, 10, 16, 255), outline=col, width=2)
    draw.ellipse([cx - 4, cy - 4, cx + 4, cy + 4], fill=col)

    bbox1 = font_callout_title.getbbox(title)
    bbox2 = font_callout_sub.getbbox(sub)
    w = max(bbox1[2] - bbox1[0], bbox2[2] - bbox2[0]) + 20
    h = 36

    if align == "center":
        x0 = bx - w // 2
    elif align == "right":
        x0 = bx - w
    else:
        x0 = bx

    y0 = by
    draw.rounded_rectangle([(x0, y0), (x0 + w, y0 + h)], radius=6, fill=(12, 16, 26, 245), outline=(col[0], col[1], col[2], 160), width=1)
    draw.text((x0 + 10, y0 + 4), title, font=font_callout_title, fill=col)
    draw.text((x0 + 10, y0 + 19), sub, font=font_callout_sub, fill=(156, 163, 175, 255))

# 6. Bottom Status Footer
draw.line([(50, height - 48), (width - 40, height - 48)], fill=(255, 255, 255, 18), width=1)

# Evenly spaced phase sequence
phase_items = [
    ("ACCUMULATION", 60),
    ("MARKUP", 195),
    ("DISTRIBUTION", 295),
    ("CAPITULATION", 435),
    ("REBIRTH", 575),
]

for name, x in phase_items:
    draw.text((x, height - 38), name, font=font_axis, fill=(125, 135, 150, 255))
    if name != "REBIRTH":
        draw.text((x + 100, height - 38), "→", font=font_axis, fill=(80, 90, 105, 255))

draw.text((width - 250, height - 38), "SURVIVAL RULES INCLUDED", font=font_axis, fill=(156, 163, 175, 255))

# Save image as PNG
base.save("og-image.png", "PNG")
print("Saved polished og-image.png successfully (1200x630)")
