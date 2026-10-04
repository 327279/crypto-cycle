"""
Generate official 1200x630 Twitter/X OpenGraph Card Image
Clean, professional fintech dark theme, zero emojis.
"""
from PIL import Image, ImageDraw, ImageFont
import math

width, height = 1200, 630
img = Image.new("RGBA", (width, height), (9, 10, 15, 255))
draw = ImageDraw.Draw(img)

# Background subtle grid
grid_color = (255, 255, 255, 12)
for x in range(80, width - 80, 80):
    draw.line([(x, 60), (x, height - 60)], fill=grid_color, width=1)
for y in range(80, height - 60, 60):
    draw.line([(80, y), (width - 80, y)], fill=grid_color, width=1)

# Subtle background radial glow behind the peak and the moonshot
for r in range(160, 0, -8):
    alpha = int(18 * (1 - r / 160))
    draw.ellipse([460 - r, 160 - r, 460 + r, 160 + r], fill=(16, 185, 129, alpha))
    draw.ellipse([1080 - r, 110 - r, 1080 + r, 110 + r], fill=(251, 191, 36, alpha))

# Try loading standard Windows fonts
try:
    font_title = ImageFont.truetype("C:/Windows/Fonts/segoeuib.ttf", 34)
    font_sub = ImageFont.truetype("C:/Windows/Fonts/segoeui.ttf", 18)
    font_label = ImageFont.truetype("C:/Windows/Fonts/segoeuib.ttf", 15)
    font_sublabel = ImageFont.truetype("C:/Windows/Fonts/segoeui.ttf", 12)
    font_mono = ImageFont.truetype("C:/Windows/Fonts/consola.ttf", 13)
except:
    font_title = ImageFont.load_default()
    font_sub = ImageFont.load_default()
    font_label = ImageFont.load_default()
    font_sublabel = ImageFont.load_default()
    font_mono = ImageFont.load_default()

# Header
draw.text((80, 36), "THE CRYPTO MARKET CYCLE", font=font_title, fill=(243, 244, 246, 255))
draw.text((80, 78), "How Retail Becomes Exit Liquidity  |  An Interactive Psychological Breakdown", font=font_sub, fill=(148, 163, 184, 255))

# Break-even line at Y=260
break_even_y = 260
for x in range(100, 1100, 12):
    draw.line([(x, break_even_y), (x + 6, break_even_y)], fill=(249, 115, 22, 130), width=2)

draw.rectangle([(860, break_even_y - 12), (1070, break_even_y + 12)], fill=(18, 21, 31, 240), outline=(249, 115, 22, 180), width=1)
draw.text((875, break_even_y - 8), "YOUR ENTRY LEVEL ($100)", font=font_mono, fill=(249, 115, 22, 255))

# Curve Points Calculation (smooth cubic bezier interpolation)
# Stages:
# 1: Accumulate (100, 480) -> (200, 475)
# 2: Breakout (200, 475) -> (310, 400)
# 3: KOLs & Entry (310, 400) -> (420, 260)
# 4: FOMO Peak (420, 260) -> (510, 150)
# 5: Healthy Retrace (510, 150) -> (600, 320)
# 6: Dead Cat Bounce (600, 320) -> (670, 280)
# 7: Bleed -90% (670, 280) -> (780, 490)
# 8: Smart Money Accumulates (780, 490) -> (870, 490)
# 9: Fundamentals Bring It Back (870, 490) -> (970, 260)
# 10: Sell at Breakeven & Moonshot (970, 260) -> (1100, 95)

def bezier_point(p0, p1, p2, p3, t):
    x = (1-t)**3 * p0[0] + 3*(1-t)**2 * t * p1[0] + 3*(1-t) * t**2 * p2[0] + t**3 * p3[0]
    y = (1-t)**3 * p0[1] + 3*(1-t)**2 * t * p1[1] + 3*(1-t) * t**2 * p2[1] + t**3 * p3[1]
    return (x, y)

segments = [
    # (p0, p1, p2, p3, color)
    ((100, 485), (140, 485), (170, 480), (210, 475), (16, 185, 129)),       # 1
    ((210, 475), (250, 470), (280, 435), (320, 390), (16, 185, 129)),       # 2
    ((320, 390), (355, 345), (390, 280), (420, 260), (16, 185, 129)),       # 3
    ((420, 260), (450, 210), (475, 150), (510, 150), (16, 185, 129)),       # 4
    ((510, 150), (540, 150), (570, 250), (600, 330), (239, 68, 68)),        # 5
    ((600, 330), (625, 320), (645, 275), (670, 275), (239, 68, 68)),        # 6
    ((670, 275), (695, 285), (730, 450), (780, 490), (239, 68, 68)),        # 7
    ((780, 490), (810, 490), (840, 490), (870, 490), (16, 185, 129)),       # 8
    ((870, 490), (910, 490), (940, 370), (970, 260), (16, 185, 129)),       # 9
    ((970, 260), (1010, 180), (1050, 110), (1100, 95), (251, 191, 36)),     # 10
]

for p0, p1, p2, p3, base_color in segments:
    pts = [bezier_point(p0, p1, p2, p3, i / 40.0) for i in range(41)]
    # Glow layer
    glow_color = (base_color[0], base_color[1], base_color[2], 50)
    for i in range(len(pts) - 1):
        draw.line([pts[i], pts[i+1]], fill=glow_color, width=10)
    # Core line
    core_color = (base_color[0], base_color[1], base_color[2], 255)
    for i in range(len(pts) - 1):
        draw.line([pts[i], pts[i+1]], fill=core_color, width=4)

# Milestone Points & Labels
milestones = [
    (140, 485, "1. Smart money accumulates", "Quiet accumulation", (16, 185, 129), (140, 520), "center"),
    (320, 390, "2. Breakout", "Early technical longs", (16, 185, 129), (240, 375), "right"),
    (375, 315, "3. KOLs start shilling", "Influencers hype 100x", (168, 85, 247), (275, 305), "right"),
    (420, 260, "YOU BUY IN", "Entry Price: $100.00", (249, 115, 22), (370, 235), "right"),
    (510, 150, "4. Retail FOMO at top", "Smart money exits", (249, 115, 22), (510, 115), "center"),
    (600, 330, "5. 'Healthy retracement'", "Dip buyers trapped", (239, 68, 68), (620, 335), "left"),
    (670, 275, "6. Dead cat bounce", "Relief rally fails", (148, 163, 184), (685, 265), "left"),
    (780, 490, "7. You hold, down 90%", "Max pain bleed", (239, 68, 68), (730, 440), "right"),
    (850, 490, "8. Smart money buys again", "Quiet floor accumulation", (16, 185, 129), (850, 520), "center"),
    (930, 370, "9. Fundamentals recover", "Organic protocol growth", (16, 185, 129), (940, 390), "left"),
    (970, 260, "10. You sell at break-even", "Exit flat with zero profit", (249, 115, 22), (970, 290), "center"),
    (1100, 95, "Pumps without you", "New All-Time High", (251, 191, 36), (1090, 60), "right")
]

for mx, my, title, sub, col, (tx, ty), align in milestones:
    # Outer ring
    draw.ellipse([mx - 7, my - 7, mx + 7, my + 7], fill=(9, 10, 15, 255), outline=col, width=2)
    draw.ellipse([mx - 4, my - 4, mx + 4, my + 4], fill=col)

    # Calculate text positioning
    bbox_t = font_label.getbbox(title)
    w_t = bbox_t[2] - bbox_t[0]
    bbox_s = font_sublabel.getbbox(sub)
    w_s = bbox_s[2] - bbox_s[0]

    if align == "center":
        pos_tx = tx - w_t // 2
        pos_sx = tx - w_s // 2
    elif align == "right":
        pos_tx = tx - w_t
        pos_sx = tx - w_s
    else:
        pos_tx = tx
        pos_sx = tx

    draw.text((pos_tx, ty), title, font=font_label, fill=(243, 244, 246, 255))
    draw.text((pos_sx, ty + 18), sub, font=font_sublabel, fill=(148, 163, 184, 255))

# Footer bar
draw.line([(80, 575), (width - 80, 575)], fill=(255, 255, 255, 25), width=1)
draw.text((80, 588), "LIVE INTERACTIVE ENGINE: 327279.github.io/crypto-cycle", font=font_mono, fill=(148, 163, 184, 255))
draw.text((width - 80, 588), "DO YOUR OWN RESEARCH  |  NOT FINANCIAL ADVICE", font=font_mono, fill=(100, 116, 139, 255), anchor="ra")

img.save("og-image.png", "PNG")
print("Saved og-image.png successfully")
