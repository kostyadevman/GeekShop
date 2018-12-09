from django.contrib.auth.decorators import user_passes_test
from authapp.models import ShopUser
from django.shortcuts import get_object_or_404, render
from mainapp.models import Product, ProductCategory
from django.shortcuts import HttpResponseRedirect, reverse
from adminapp.forms import ShopUserAdminEditForm
from authapp.forms import ShopUserRegisterForm


@user_passes_test(lambda u: u.is_staff)
def users(request):
    context = {
        'title': 'админка/пользователи',
        'objects': ShopUser.objects.order_by('-is_active', 'username')
    }
    return  render(request, 'adminapp/users.html', context)

@user_passes_test(lambda u: u.is_staff)
def user_create(request):
    if request.method == 'POST':
        form = ShopUserRegisterForm(request.POST, request.FILES)

        if form.is_valid():
            form.save()
            return HttpResponseRedirect(reverse('admin:users'))
    else:
        form = ShopUserRegisterForm()
    return render(request, 'adminapp/user_update.html', {
        'title': 'пользователи/новый пользователь',
        'edit_form': form
    })

@user_passes_test(lambda u: u.is_staff)
def user_update(request, pk):

    user = get_object_or_404(ShopUser, pk=pk)
    if request.method == 'POST':
        edit_form = ShopUserAdminEditForm(request.POST, request.FILES, instance=request.user)
        if edit_form.is_valid():
            edit_form.save()
            return HttpResponseRedirect(reverse('admin:users', args=(pk,)))
    else:
        edit_form = ShopUserAdminEditForm(instance=user)

    return render(request, 'adminapp/user_update.html', {
        'title': 'пользователи/редакторование',
        'edit_form': edit_form
    })

@user_passes_test(lambda u: u.is_staff)
def user_delete(request, pk):
    user = get_object_or_404(ShopUser, pk=pk)

    if request.method == 'POST':
        user.is_active = False
        user.save()

        return HttpResponseRedirect(reverse('admin:users'))

    return render(request, 'adminapp/user_delete.html', {
        'title': 'пользователи/удалить',
        'user': user
    })

@user_passes_test(lambda u: u.is_staff)
def categories(request):

    return render(request, 'adminapp/categories.html', {
        'title': 'админка/категории',
        'objects': ProductCategory.objects.order_by('name')
    })


def category_create(request):
    pass


def category_update(request, pk):
    pass


def category_delete(request, pk):
    pass

@user_passes_test(lambda u: u.is_staff)
def products(request, pk):
    category = get_object_or_404(ProductCategory, pk=pk)
    products = Product.objects.filter(category__pk=pk).order_by('name')
    return render(request, 'adminapp/products.html', {
        'title': 'админка/продукт',
        'category': category,
        'objects': products
    })


def product_create(request, pk):
    pass


def product_read(request, pk):
    pass


def product_update(request, pk):
    pass


def product_delete(request, pk):
    pass
