subtotal=123
igv=0.18
def obtenerIGVconSubtotal(subtotal):
    return subtotal*igv
def obtenerTotalconSubtotal(subtotal):
    return subtotal*(1+0.18)
def obtenerSubtotalconTotal(total):
    return total/(1+igv)
def obtenerIGVconTotal(total):
    return total-obetenerTotalconSubtotal(total)
