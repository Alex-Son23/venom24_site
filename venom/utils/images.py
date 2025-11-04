from io import BytesIO
from PIL import Image
from django.core.files.uploadedfile import InMemoryUploadedFile


def compress_image(django_file, max_size_kb=500, max_side=2400):
    """
    Принимает django File/ImageField file и возвращает InMemoryUploadedFile
    уже сжатый под JPEG.
    """
    if not django_file:
        return django_file

    # Иногда приходит уже не файл, а строка пути — такое пропускаем
    if not hasattr(django_file, "file") and not hasattr(django_file, "read"):
        return django_file

    img = Image.open(django_file)

    # JPEG без альфы
    if img.mode in ("RGBA", "P"):
        img = img.convert("RGB")

    # ограничим физический размер
    if max(img.size) > max_side:
        img.thumbnail((max_side, max_side))

    quality = 85

    def make_buf(q):
        buf = BytesIO()
        img.save(buf, format="JPEG", quality=q, optimize=True)
        buf.seek(0)
        return buf

    buf = make_buf(quality)
    size_kb = buf.getbuffer().nbytes / 1024

    while size_kb > max_size_kb and quality > 20:
        quality -= 5
        buf = make_buf(quality)
        size_kb = buf.getbuffer().nbytes / 1024

    new_file = InMemoryUploadedFile(
        buf,
        field_name="ImageField",
        name=django_file.name.rsplit(".", 1)[0] + ".jpg",
        content_type="image/jpeg",
        size=buf.getbuffer().nbytes,
        charset=None,
    )
    return new_file
