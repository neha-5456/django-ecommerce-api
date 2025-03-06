# utils.py
from django.utils.html import format_html

def display_image(obj, field_name='image', width=50, height=50, border_radius=5):
    image = getattr(obj, field_name, None)
    if image and getattr(image, 'url', None):
        return format_html(
            '<img src="{}" width="{}" height="{}" style="border-radius:{}px;" />',
            image.url, width, height, border_radius
        )
    return "No Image"
