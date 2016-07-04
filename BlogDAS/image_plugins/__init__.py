from django.core.mail import send_mail


def make_jpeg_image_plugin():
    send_mail('Subject here',
              'text',
              'from@example.com',
              ['ruyther@me.com'],
              fail_silently=False,
              )


def make_png_image_plugin():
    return "This would return the PNG image plugin"
