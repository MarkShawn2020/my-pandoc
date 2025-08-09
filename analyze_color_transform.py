#!/usr/bin/env python3
"""
Analyze the color transformation between original and rendered colors
"""

def hex_to_rgb(hex_color):
    """Convert hex to RGB"""
    hex_color = hex_color.lstrip('#')
    return tuple(int(hex_color[i:i+2], 16) for i in (0, 2, 4))

def rgb_to_hex(rgb):
    """Convert RGB to hex"""
    return '{:02X}{:02X}{:02X}'.format(*rgb)

def analyze_transform(original_hex, rendered_hex):
    """Analyze the transformation between two colors"""
    orig_rgb = hex_to_rgb(original_hex)
    rend_rgb = hex_to_rgb(rendered_hex)
    
    print(f"Original: {original_hex} -> RGB{orig_rgb}")
    print(f"Rendered: {rendered_hex} -> RGB{rend_rgb}")
    print()
    
    # Calculate ratios
    ratios = []
    for i, (o, r) in enumerate(zip(orig_rgb, rend_rgb)):
        ratio = r / o if o != 0 else 0
        ratios.append(ratio)
        channel = ['R', 'G', 'B'][i]
        print(f"{channel}: {o} -> {r} (ratio: {ratio:.4f}, diff: {r-o})")
    
    print()
    print(f"Average ratio: {sum(ratios)/3:.4f}")
    
    # Test if it's a simple darkening
    darkening_factor = sum(ratios) / 3
    print(f"\nIf uniform darkening at {darkening_factor:.4f}:")
    predicted_rgb = tuple(int(c * darkening_factor) for c in orig_rgb)
    predicted_hex = rgb_to_hex(predicted_rgb)
    print(f"Predicted: #{predicted_hex} -> RGB{predicted_rgb}")
    
    # Check if it's actually what we got
    if predicted_hex == rendered_hex.lstrip('#'):
        print("✅ This is uniform darkening!")
    else:
        print("❌ Not uniform darkening, more complex transformation")
        
        # Test if it's a blend with white (opacity effect)
        print("\nTesting blend with white at various opacities:")
        for opacity in [0.9, 0.85, 0.8, 0.75, 0.7]:
            blended_rgb = tuple(int(c * opacity + 255 * (1 - opacity)) for c in orig_rgb)
            blended_hex = rgb_to_hex(blended_rgb)
            match = "✅" if blended_hex == rendered_hex.lstrip('#') else ""
            print(f"  Opacity {opacity:.2f}: #{blended_hex} {match}")
    
    return darkening_factor

# Test with the known case
print("=" * 50)
print("Known case: B55F3F -> A2593B")
print("=" * 50)
factor = analyze_transform("#B55F3F", "#A2593B")

print("\n" + "=" * 50)
print("Testing other predefined theme colors")
print("=" * 50)

# Test with other theme colors to see if the same factor applies
test_colors = {
    "blue": "1E88E5",
    "red": "E53935",
    "green": "43A047",
    "purple": "5D1EB1",
}

for name, color in test_colors.items():
    print(f"\n{name.upper()} theme: #{color}")
    orig_rgb = hex_to_rgb(color)
    # Apply the same darkening factor
    predicted_rgb = tuple(int(c * factor) for c in orig_rgb)
    predicted_hex = rgb_to_hex(predicted_rgb)
    print(f"If same factor ({factor:.4f}): #{predicted_hex}")