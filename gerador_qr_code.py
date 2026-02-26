import qrcode

def create_qr_code(url):
    imagem = qrcode.make(url)
    return imagem


def save_image(image, file_destination):
    image.save(file_destination)