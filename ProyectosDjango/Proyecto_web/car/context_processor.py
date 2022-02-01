def total_car_amount(request):
    total=0
    #if request.user.is_authenticated:
        #if 'car' in request.session:
    '''for key, value in request.session['car'].items():
        total=total+float(value['price'])'''

    return{'total_car_amount':total}
