from django.shortcuts import render, redirect
from store.models import Product, Review
from django.db.models import Q
from django.contrib import messages


def home(request):
    popular_products = Product.objects.all().filter(available=True).order_by('-created')[:10]
    reviews = None
    for product in popular_products:
        reviews = Review.objects.filter(product_id=product.id, status=True)

    context = {
        'popular_products': popular_products,
        'reviews': reviews,
        'page_title': 'کالاهای پرطرفدار',
        'meta_title': 'KodeShop - فروشگاه آنلاین ابزار و تجهیزات کشاورزی',
        'meta_description': 'خرید آنلاین ابزار کشاورزی، کود، سم و تجهیزات کشاورزی با بهترین قیمت و کیفیت. ارسال سریع به سراسر کشور',
        'meta_keywords': 'ابزار کشاورزی, کود کشاورزی, سم کشاورزی, تجهیزات کشاورزی, خرید آنلاین',
    }
    return render(request, 'index.html', context)


def search(request):
    try:
        if request.method == 'POST':
            search_text = request.POST['search_text'].lower()
            desired_products = Product.objects.filter(Q(name__icontains=search_text) | Q(name_fa__icontains=search_text))
            reviews = None
            for pdt in desired_products:
                reviews = Review.objects.filter(product_id=pdt.id, status=True)

            context = {
                'popular_products': desired_products,
                'reviews': reviews,
                'page_title': 'نتایج جستجو',
                'meta_description': f'نتایج جستجو برای "{search_text}" در فروشگاه ابزار کشاورزی',
            }
            return render(request, 'index.html', context)
    except:
        messages.error(request, "مشکلی در روند جستجو اتفاق افتاد. لطفا دوباره تلاش کنید.")
        return redirect(request.META.get('HTTP_REFERER'))


def about_us(request):
    context = {
        'page_title': 'درباره ما',
        'meta_description': 'آشنایی با فروشگاه آنلاین ابزار و تجهیزات کشاورزی KodeShop',
    }
    return render(request, 'us/about.html', context)

from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from django.core.files.storage import default_storage

@csrf_exempt
def upload_video(request):
    if request.method == 'POST' and request.FILES.get('upload'):
        video = request.FILES['upload']
        save_path = default_storage.save(f'videos/{video.name}', video)
        video_url = default_storage.url(save_path)
        return JsonResponse({'url': video_url})
    return JsonResponse({'error': 'Invalid request'}, status=400)
