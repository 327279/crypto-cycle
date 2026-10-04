"""
Generate Ultra High Resolution (2400x1260 @2x Retina) Twitter/X Card.
High definition, crystal clear typography, gorgeous glowing curve, perfectly spaced badges.
No white circles, no artifacts, pixel-perfect contrast.
"""
from PIL import Image, ImageDraw, ImageFont

# 2x High Resolution Canvas
w2, h2 = 2400, 1260
base = Image.new("RGBA", (w2, h2), (7, 9, 15, 255))
draw = ImageDraw.Draw(base)

# Load fonts with safe fallbacks (at 2x scale)
def load_font(paths, size):
    for p in paths:
        try:
            return ImageFont.truetype(p, size)
        except:
            continue
    return ImageFont.load_default()

font_title = load_font(["C:/Windows/Fonts/segoeuib.ttf", "C:/Windows/Fonts/arialbd.ttf"], 60)
font_subtitle = load_font(["C:/Windows/Fonts/segoeui.ttf", "C:/Windows/Fonts/arial.ttf"], 28)
font_badge = load_font(["C:/Windows/Fonts/consola.ttf", "C:/Windows/Fonts/segoeuib.ttf"], 22)
font_callout_title = load_font(["C:/Windows/Fonts/segoeuib.ttf", "C:/Windows/Fonts/arialbd.ttf"], 26)
font_callout_sub = load_font(["C:/Windows/Fonts/segoeui.ttf", "C:/Windows/Fonts/arial.ttf"], 21)
font_axis = load_font(["C:/Windows/Fonts/consola.ttf", "C:/Windows/Fonts/arial.ttf"], 21)
font_brand = load_font(["C:/Windows/Fonts/consola.ttf", "C:/Windows/Fonts/segoeuib.ttf"], 26)

# 1. Background Grid Lines (Clean and subtle)
grid_col = (255, 255, 255, 14)
for x in range(120, w2 - 80, 150):
    draw.line([(x, 240), (x, h2 - 130)], fill=grid_col, width=2)
for y in range(300, h2 - 130, 110):
    draw.line([(100, y), (w2 - 80, y)], fill=grid_col, width=2)

# Outer Card Border Frame
draw.rectangle([(28, 28), (w2 - 28, h2 - 28)], outline=(255, 255, 255, 28), width=2)

# 2. Header Area
# Kicker badge pill
draw.rounded_rectangle([(100, 56), (360, 102)], radius=8, fill=(16, 185, 129, 30), outline=(16, 185, 129, 140), width=2)
draw.ellipse([(124, 73), (136, 85)], fill=(16, 185, 129, 255))
draw.text((152, 66), "MARKET PSYCHOLOGY", font=font_badge, fill=(16, 185, 129, 255))

# Main Title
draw.text((100, 120), "THE CRYPTO MARKET CYCLE", font=font_title, fill=(248, 250, 252, 255))

# Subtitle
draw.text((100, 192), "How 95% of retail buys the hype, holds down -90%, sells break-even, and misses the pump.", font=font_subtitle, fill=(148, 163, 184, 255))

# Live site URL pill on top right
draw.rounded_rectangle([(w2 - 520, 72), (w2 - 100, 132)], radius=10, fill=(15, 20, 32, 245), outline=(16, 185, 129, 130), width=2)
draw.text((w2 - 490, 86), "crypto-cycles.vercel.app", font=font_brand, fill=(16, 185, 129, 255))

# 3. Break-Even Reference Line ($100 Level)
be_y = 600
for x in range(100, w2 - 80, 28):
    draw.line([(x, be_y), (x + 14, be_y)], fill=(249, 115, 22, 120), width=2)

# Entry Level badge on left
draw.rounded_rectangle([(100, be_y - 24), (360, be_y + 24)], radius=8, fill=(13, 16, 26, 255), outline=(249, 115, 22, 180), width=2)
draw.text((120, be_y - 14), "ENTRY LEVEL ($100)", font=font_badge, fill=(249, 115, 22, 255))

# 4. Draw Smooth Market Curve
def bezier_point(p0, p1, p2, p3, t):
    x = (1-t)**3 * p0[0] + 3*(1-t)**2 * t * p1[0] + 3*(1-t) * t**2 * p2[0] + t**3 * p3[0]
    y = (1-t)**3 * p0[1] + 3*(1-t)**2 * t * p1[1] + 3*(1-t) * t**2 * p2[1] + t**3 * p3[1]
    return (x, y)

curve_sections = [
    # 1. Smart money accumulation
    ((120, 980), (240, 980), (360, 970), (480, 940), (16, 185, 129)),
    # 2. Breakout
    ((480, 940), (580, 920), (680, 800), (790, 680), (16, 185, 129)),
    # 3. Markup to Entry ($100)
    ((790, 680), (850, 600), (910, 600), (960, 600), (168, 85, 247)),
    # 4. Hype pump to top
    ((960, 600), (1010, 480), (1050, 370), (1120, 350), (249, 115, 22)),
    # 5. Retracement dip
    ((1120, 350), (1170, 350), (1230, 540), (1300, 640), (239, 68, 68)),
    # 6. Dead cat bounce
    ((1300, 640), (1350, 620), (1400, 570), (1450, 570), (239, 68, 68)),
    # 7. Capitulation bleed to -90% floor
    ((1450, 570), (1500, 580), (1570, 940), (1650, 990), (239, 68, 68)),
    # 8. Smart money re-accumulates floor
    ((1650, 990), (1710, 990), (1770, 990), (1830, 990), (16, 185, 129)),
    # 9. Recovery to Break-even
    ((1830, 990), (1900, 990), (1960, 760), (2020, 600), (16, 185, 129)),
    # 10. Moonshot beyond break-even
    ((2020, 600), (2070, 460), (2140, 320), (2240, 270), (251, 191, 36)),
]

overlay = Image.new("RGBA", (w2, h2), (0, 0, 0, 0))
ov_draw = ImageDraw.Draw(overlay)

for p0, p1, p2, p3, col in curve_sections:
    pts = [bezier_point(p0, p1, p2, p3, i / 36.0) for i in range(37)]
    # Broad atmospheric glow
    for i in range(len(pts) - 1):
        ov_draw.line([pts[i], pts[i+1]], fill=(col[0], col[1], col[2], 45), width=24)
    # Intense mid glow
    for i in range(len(pts) - 1):
        ov_draw.line([pts[i], pts[i+1]], fill=(col[0], col[1], col[2], 100), width=12)
    # Core sharp curve
    for i in range(len(pts) - 1):
        draw.line([pts[i], pts[i+1]], fill=(col[0], col[1], col[2], 255), width=6)

base = Image.alpha_composite(base, overlay)
draw = ImageDraw.Draw(base)

# 5. Callout Cards and Badges (Clean, no overlap, crisp text)
callouts = [
    # (anchor_x, anchor_y, title, subtitle, color, box_x, box_y, align)
    (300, 976, "1. Smart Money Buys", "Quiet baseline accumulation", (16, 185, 129), 140, 1040, "left"),
    (960, 600, "2. You Buy In ($100)", "KOLs shill & hype begins", (249, 115, 22), 730, 500, "right"),
    (1120, 350, "3. Retail FOMO Top", "Whales exit into liquidity", (249, 115, 22), 1120, 250, "center"),
    (1450, 570, "4. Dead Cat Bounce", "Last exit chance (you hold)", (239, 68, 68), 1480, 510, "left"),
    (1650, 990, "5. Down -90% Panic", "You hold in pure silence", (239, 68, 68), 1470, 1040, "center"),
    (1830, 990, "6. Smart Money Re-Buys", "Accumulating the floor", (16, 185, 129), 1810, 1040, "left"),
    (2020, 600, "7. You Sell at Break-Even", "Exit flat after 2 years", (249, 115, 22), 1990, 670, "right"),
    (2240, 270, "8. Pumps to New ATH", "Moonshot without you!", (251, 191, 36), 2200, 180, "right"),
]

for cx, cy, title, sub, col, bx, by, align in callouts:
    # Anchor point dot
    draw.ellipse([cx - 16, cy - 16, cx + 16, cy + 16], fill=(7, 9, 15, 255), outline=col, width=4)
    draw.ellipse([cx - 8, cy - 8, cx + 8, cy + 8], fill=col)

    # Box dimension
    bbox1 = font_callout_title.getbbox(title)
    bbox2 = font_callout_sub.getbbox(sub)
    w = max(bbox1[2] - bbox1[0], bbox2[2] - bbox2[0]) + 36
    h = 72

    if align == "center":
        x0 = bx - w // 2
    elif align == "right":
        x0 = bx - w
    else:
        x0 = bx

    y0 = by
    # Clean frosted rounded card
    draw.rounded_rectangle([(x0, y0), (x0 + w, y0 + h)], radius=12, fill=(13, 17, 28, 248), outline=(col[0], col[1], col[2], 160), width=2)
    draw.text((x0 + 18, y0 + 8), title, font=font_callout_title, fill=col)
    draw.text((x0 + 18, y0 + 38), sub, font=font_callout_sub, fill=(156, 163, 175, 255))

# 6. Bottom Status Footer
draw.line([(100, h2 - 96), (w2 - 80, h2 - 96)], fill=(255, 255, 255, 20), width=2)

phases = [
    ("ACCUMULATION", 120),
    ("MARKUP", 380),
    ("DISTRIBUTION", 580),
    ("CAPITULATION", 860),
    ("REBIRTH", 1140),
]

for name, x in phases:
    draw.text((x, h2 - 76), name, font=font_axis, fill=(125, 135, 150, 255))
    if name != "REBIRTH":
        draw.text((x + 200, h2 - 76), "→", font=font_axis, fill=(80, 90, 105, 255))

draw.text((w2 - 500, h2 - 76), "SURVIVAL PLAYBOOK INSIDE", font=font_axis, fill=(156, 163, 175, 255))

# Resize down to standard 1200x630 using high-quality Lanczos resampling
# This produces anti-aliasing and sharpness
final_img = base.resize((1200, 630), Image.Resampling.LANCZOS)

# Save to all filenames
for filename in ["card-v3.png", "card-v2.png", "card.png", "og-image.png", "crypto-cycle-card.png"]:
    final_img.save(filename, "PNG")
    print(f"Saved {filename}")

print("All card images regenerated with 2x Lanczos supersampling successfully.")
