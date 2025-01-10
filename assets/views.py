import uuid

from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import render
# assets/views.py

from django.shortcuts import render, redirect
from .forms import AssetForm

from assets.Asset import Asset
from .models import DefaultAssetType, DefaultAssetModel
from django.views.generic import ListView


def assets_choose(request):
    if request.method == 'POST':
        form = AssetForm(request.POST)
        if form.is_valid():
            # Получаем введенное значение нового типа актива
            new_asset_type = form.cleaned_data.get('new_asset_type')
            # Проверяем, если новое значение было введено
            if new_asset_type:
                # Создаем новый тип актива, если он не существует
                asset_type, created = DefaultAssetType.objects.get_or_create(default_asset_type=new_asset_type)
                # Создаем экземпляр модели актива
                asset = form.save(commit=False)
                asset.default_asset_type = asset_type  # Присваиваем новый тип актива
                asset.save()  # Сохраняем актив
            else:
                # Если новое значение не введено, просто сохраняем актив с выбранным типом
                asset = form.save()

            return redirect('asset_saved')  # Замените на нужное представление после сохранения
    else:
        form = AssetForm()

    return render(request, 'assets/assets_choose.html', {'form': form})

def asset_saved(request):
    return render(request, 'assets/asset_saved.html')

class CompanyAssetsView(LoginRequiredMixin, ListView):
    model = DefaultAssetModel
    template_name = 'accounts/company_assets.html'  # Создайте этот шаблон
    context_object_name = 'assets'

    def get_queryset(self):
        # Получаем ID компании из URL и извлекаем ее активы
        company_id = self.kwargs['company_id']
        return DefaultAssetModel.objects.filter(company_id=company_id)

""""def assets_choose(request):
    asset_types = Asset.AsseType.choices
    asset_values = Asset.AssetValue.choices
    asset_names = Asset.AssetName.choices


    context = {

        'asset_types': asset_types,
        'asset_values': asset_values,
        'asset_names': asset_names,
    }
    return render(request, 'assets/assets_choose.html',context)"""""
"""def asset_create(request):
    if request.method == 'POST':
        # Получаем данные из POST-запроса
        asset_name = request.POST.get('asset_name')
        asset_value = request.POST.get('asset_value')
        asset_type = request.POST.get('asset_type')

        # Создаем новый экземпляр Asset
        asset = Asset(
            asset_id=str(uuid.uuid4()),  # Генерируем уникальный идентификатор для актива
            asset_name=asset_name,
            asset_value=asset_value,
            asset_type=asset_type
        )
        # Сохраняем актив в базе данных
        asset.save()

        # Перенаправляем пользователя на другую страницу или отображаем сообщение об успехе
        return redirect('some_view_name')  # Замените на нужное представление

"""""







