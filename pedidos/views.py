from django.shortcuts import render, redirect
from django.urls import reverse
from .models import Categorias, Lanches, Sobremesa, Bebidas, Acompanhamento, Extra, Pedido
from django.http import HttpResponse, JsonResponse
from datetime import datetime
from site_principal.models import Usuario
import json
from django.core.serializers import serialize


def pedidos(request):
    if request.method == 'GET':
        categorias = Categorias.objects.all()
        lanches = Lanches.objects.all()


        valores = Lanches.objects.filter(categoria_id=1).all()
        
        nome_categoria = Categorias.objects.get(id=1)
        categoria_get = request.GET.get('categoria_get')
        horario_funcionamento = datetime.now().time()

        if int(str(horario_funcionamento).split(':')[0]) <= 22:
            horario = 'aberto'
        if int(str(horario_funcionamento).split(':')[0]) > 22:
            horario = 'fechado'

        if categoria_get:
            
            valores = Lanches.objects.filter(categoria_id=categoria_get).all()
            nome_categoria = Categorias.objects.get(id=categoria_get)
            
        return render(request, 'pedidos.html', {'valores': valores,'nome_categoria':nome_categoria.nome, 'categorias': categorias, 'lanches':lanches, 'horario':horario})
    
    elif request.method == 'POST':

        burguer = request.POST.get('lanche')
        lanche = Lanches.objects.get(id=burguer)
        

        return redirect(f'contiunar_pedido/{lanche.id}')
    
def contiunar_pedido(request, id):
    sobremesa = Sobremesa.objects.all()
    bebidas = Bebidas.objects.all()
    acompanhamento = Acompanhamento.objects.all()
    extra = Extra.objects.all()
    lanche = Lanches.objects.get(id=id)
    estra_qtd = 5
    return render(request, 'continuar_pedidos.html', {'lanche':lanche, 'extras':extra,'estra_qtd':estra_qtd, 'acompanhamentos':acompanhamento, 'sobremesas':sobremesa, 'bebidas':bebidas})



def verificar_pedido(request):
    try:
        extra_id = request.POST.get('extra')
        lanche_id = request.POST.get('lanche')
        usuario = Usuario.objects.get(id=request.session['user'])
        extra = Extra.objects.get(id=int(extra_id))
        lanche = Lanches.objects.get(id=int(lanche_id))
        print(extra, lanche)
        pedido = Pedido.objects.filter(usuario_id=usuario).first()
        if pedido:
            #TODO: Colocar o lanche como finalizado ao perguntar se o usuario quer continuar fazendo pedidos
            print('caiu no pedido')
            if pedido.finalizado == 'NÃO':
                print('caiu no finalizado')
                
                qtd = pedido.quantidade_extra + 1
                print(qtd)
                pedido.quantidade_extra = int(qtd)

                valor = pedido.valor + extra.valor
                pedido.valor = valor
                pedido.save()

                
                print(pedido.valor)
                pedido = Pedido.objects.all()
                valor_json = json.loads(serialize('json', pedido))[0]['fields']['valor']
                qtd = json.loads(serialize('json', pedido))[0]['fields']['quantidade_extra']
                print(valor_json)


                return JsonResponse({'valor_json': valor_json, 'qtd':qtd})
        else:
            print('caiu no sem pedido')
            valor = lanche.valor + extra.valor
            
            pedido = Pedido(usuario= usuario, lanche=lanche, extra=extra,quantidade_extra=1, valor=float(valor))
            pedido.save()
            print(pedido.valor)
        return HttpResponse(f'{extra}')
    except:
        print('caiu no erro bd')

        # valor = lanche.valor + extra.valor
        
        # pedido = Pedido(usuario= usuario, lanche=lanche, extra=extra, valor=float(valor))
        # pedido.save()
        # print(pedido.valor)
        return HttpResponse(f'{extra}')
    
    #TODO: criar função que cadastra um pedido ao usuario assim que ele entra na parte de continuar pedido
    #TODO: colocar função de cancelar pedido e excluir o pedido do cliente

