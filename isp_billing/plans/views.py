from django.shortcuts import render, redirect, get_object_or_404
from .models import Plan
from .forms import PlanForm

def plan_list(request):
    plans = Plan.objects.all()
    return render(request, 'plans/plan_list.html', {'plans': plans})

def plan_detail(request, pk):
    plan = get_object_or_404(Plan, pk=pk)
    return render(request, 'plans/plan_detail.html', {'plan': plan})

def plan_create(request):
    if request.method == 'POST':
        form = PlanForm(request.POST)
        if form.is_valid():
            plan = form.save()
            return redirect('plan_detail', pk=plan.pk)
    else:
        form = PlanForm()
    return render(request, 'plans/plan_form.html', {'form': form})

def plan_update(request, pk):
    plan = get_object_or_404(Plan, pk=pk)
    if request.method == 'POST':
        form = PlanForm(request.POST, instance=plan)
        if form.is_valid():
            plan = form.save()
            return redirect('plan_detail', pk=plan.pk)
    else:
        form = PlanForm(instance=plan)
    return render(request, 'plans/plan_form.html', {'form': form})

def plan_delete(request, pk):
    plan = get_object_or_404(Plan, pk=pk)
    plan.delete()
    return redirect('plan_list')
