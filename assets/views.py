import uuid

from django.shortcuts import render
# assets/views.py

from django.shortcuts import render, redirect
from .forms import AssetForm

from assets.Asset import Asset

def assets_choose(request):
    if request.method == 'POST':
        form = AssetForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('asset_saved') # Замените на нужное представление после сохранения
    else:
        form = AssetForm()

    return render(request, 'assets/assets_choose.html', {'form': form})

def asset_saved(request):
    return render(request, 'assets/asset_saved.html')

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







