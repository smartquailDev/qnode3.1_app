from .coti_cart import Coti_Cart


def coti_cart(request):
    return {'coti_cart': Coti_Cart(request)}
