from django.shortcuts import render
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
# Create your views here.

def test(request):
	return render_to_response('login.html', {
		'current_user': request.user,
		}, context_instance=RequestContext(request))

def register(request):
	email = request.POST['inputEmail']
	password = request.POST['inputPassword']
	serial = request.POST['inputSerialNumber']
	user = authenticate(username=email, password=password, serial=serial)
	if user is not None:
		user = User(email=email, username=email, password=password)
		user.save()
		user = authenticate(username=email, password=password)
		login(request, user)
	else:
		login(request, user)
	return HttpResponseRedirect(reverse('phLow.views.index', args=()))

def auth_login(request):
	email = request.POST['inputEmail']
	password = request.POST['inputPass']
	user = authenticate(username=email, password=password)
	if user is not None:
		if user.is_active:
			login(request, user)
		else:
			pass
		return HttpResponseRedirect('/somethingforthislater/')
	else:
		return HttpResponseRedirect('/somethingforthiswithsignup/')
	return HttpResponseRedirect(reverse('phLow.views.test', args=()))

def admin_login(request):
	if (request.POST['inputUser'] == "admin" and request.POST['inputPass'] == 'ecs199'):
		return render_to_response('admin_login.html', {
			'current_user': request.user,
			}, context_instance=RequestContext(request))
	else:
		return HttpResponseRedirect(reverse('phLow.views.index', args=()))

@login_required
def user_view(request):
	current_user = request.user
	user_garden = Garden.objects.filter(passed=False).filter(user_id=current_user.id).order_by('date')
	return render_to_response('user_view.html', {
		'current_user': request.user,
		'garden': user_garden,
		}, context_instance=RequestContext(request))

def Register(request):
	template_name='GuardN/product.html'
	context = []
	if request.method == 'POST':
		print request.GET
		form = ProjectForm(request.POST)
		context['form'] = form
		print request.POST
		print form.is_valid()
		print form.errors
		if form.is_valid():
			serial_number= form.cleaned_data.get('serial_number')
			email = form.cleaned_data.get('email')
			password = form.cleaned_data.get('password')
		print serial_number, email
		client = Client(serial_number, email, password)
		client.save()
	else:
		context['form'] = ProjectForm()
	return render(request, template_name, context)

	

