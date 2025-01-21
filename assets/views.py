import uuid

from django.contrib.auth.mixins import LoginRequiredMixin


from django.shortcuts import render, redirect
from .forms import AssetForm


from .models import DefaultAssetType, Asset
from django.views.generic import ListView
from django.contrib.auth.decorators import login_required

@login_required
def assets_choose(request):
    if request.method == 'POST':
        form = AssetForm(request.POST, user=request.user)  # Передаем пользователя в форму
        if form.is_valid():
            new_asset_type = form.cleaned_data.get('new_asset_type')
            if new_asset_type:
                asset_type = DefaultAssetType.objects.get_or_create(default_asset_type=new_asset_type)
                asset = form.save(commit=False)
                asset.default_asset_type = asset_type
                asset.save()
            else:
                asset = form.save()

            return redirect('asset_saved')
    else:
        form = AssetForm(user=request.user)  # Передаем пользователя в форму

    return render(request, 'assets/assets_choose.html', {'form': form})
def asset_saved(request):
    return render(request, 'assets/asset_saved.html')

class CompanyAssetsView(LoginRequiredMixin, ListView):
    model = Asset
    template_name = 'accounts/company_assets.html'
    context_object_name = 'assets'

    def get_queryset(self):
        # Получаем ID компании из URL и извлекаем ее активы
        company_id = self.kwargs['company_id']
        return Asset.objects.filter(company_id=company_id)









