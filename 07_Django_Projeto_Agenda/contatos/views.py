from django.shortcuts import render, get_object_or_404, redirect
from django.core.paginator import Paginator
from django.http import Http404
from .models import Contato
from django.db.models import Q, Value
from django.db.models.functions import Concat
from django.contrib import messages


def index(request):
    contatos = Contato.objects.order_by('id').filter(
        mostrar=True
    )
    paginator = Paginator(contatos, 10)

    page = request.GET.get('p')
    contatos = paginator.get_page(page)

    return render(request, 'contatos/index.html', {
        'contatos': contatos
    })


def ver_contato(request, contato_id):
    """try:
        contato = Contato.objects.get(id=contato_id)
        return render(request, 'contatos/ver_contato.html', {
            'contato': contato
        })
    except Contato.DoesNotExist as e:
        raise Http404()"""
    # contato = Contato.objects.get(id=contato_id)
    contato = get_object_or_404(Contato, id=contato_id)

    if not contato.mostrar:
        raise Http404()

    return render(request, 'contatos/ver_contato.html', {
        'contato': contato
    })


def busca(request):
    termo = request.GET.get('termo')
    if termo is None or not termo:
        messages.add_message(
            request,
            messages.ERROR,
            'Campo de busca não pode ser vazio'
        )
        return redirect('index')
    campos = Concat('nome', Value(' '), 'sobrenome')

    """contatos = Contato.objects.order_by('id').filter(
        Q(nome__icontains=termo) | Q(sobrenome__icontains=termo),
        mostrar=True
    )"""
    contatos = Contato.objects.annotate(
        nome_completo=campos
    ).filter(
        Q(nome_completo__icontains=termo) | Q(telefone__icontains=termo)
    )
    if contatos:
        if len(contatos) == 1:
            messages.add_message(
                request,
                messages.SUCCESS,
                f'foram encotrado {len(contatos)} contato'
            )
        else:
            messages.add_message(
                request,
                messages.SUCCESS,
                f'foram encotrados {len(contatos)} contatos'
            )
    else:
        messages.add_message(
            request,
            messages.WARNING,
            'Nenhum contato encontrado'
        )

    paginator = Paginator(contatos, 10)

    page = request.GET.get('p')
    contatos = paginator.get_page(page)

    return render(request, 'contatos/busca.html', {
        'contatos': contatos
    })
