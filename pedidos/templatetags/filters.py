from django import template
from pedidos.models import ImageBurguer

register = template.Library()

@register.filter(name='image_load')
def image_load(product):
    imagem = ImageBurguer.objects.filter(lanche=product).first()
    return imagem.foto.url