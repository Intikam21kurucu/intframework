from PIL import Image

# ASCII karakterlerini tanımlayın
ascii_chars = "@%#*+=-:. "

def rgb_to_hex(rgb):
    return '#{:02x}{:02x}{:02x}'.format(*rgb)

def image_to_colored_ascii(image_path):
    # Resmi yükleyin
    img = Image.open(image_path)
    # Resmi ASCII sanatının boyutlarına göre yeniden boyutlandırın
    img = img.resize((80, 60))
    # ASCII sanatını oluşturun
    ascii_art = ""
    for y in range(img.height):
        for x in range(img.width):
            # Pikselin RGB değerini alın
            rgb = img.getpixel((x, y))
            # RGB değerini hex renk koduna dönüştürün
            hex_color = rgb_to_hex(rgb)
            # Pikselin parlaklık değerini alın
            brightness = sum(rgb) // 3
            # Parlaklık değerine göre bir ASCII karakteri seçin
            char = ascii_chars[brightness // (255 // len(ascii_chars))]
            # ASCII sanatına renkli karakter ekleyin
            ascii_art += f"<span style='color:{hex_color}'>{char}</span>"
        ascii_art += "\n"
    return ascii_art

# Fonksiyonu kullanarak renkli ASCII sanatını oluşturun
colored_ascii_art = image_to_colored_ascii("İNTİKAM11CONSOLEİMG_20240522_165446_0000.png")
print(colored_ascii_art)
