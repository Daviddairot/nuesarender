from django.shortcuts import render, redirect
from .models import President, UserProfile, Vice_President, General_Secretary, Financial_Secretary, Social_Director, Technical_Director, Sports_Director, Public_Relations_Officer, Treasurer, Welfare_Director,assistant_general_secretary, assistant_social_director, P_R_O1, P_R_O2
from django.contrib.auth.decorators import login_required



def index(request):
    return render(request, 'index.html')

def close(request):
    return render(request, 'close.html')

def next_page(request):
    return render(request, 'next_page.html')

def vote(request):
    presidents = President.objects.all()
    vice_presidents = Vice_President.objects.all()
    general_secretaries = General_Secretary.objects.all()
    welfare_directors = Welfare_Director.objects.all()
    financial_secretaries = Financial_Secretary.objects.all()
    social_directors = Social_Director.objects.all()
    technical_directors = Technical_Director.objects.all()
    sports_directors = Sports_Director.objects.all()
    public_relations_officers = Public_Relations_Officer.objects.all()
    treasurers = Treasurer.objects.all()
    pro1s = P_R_O1.objects.all()
    pro2s = P_R_O2.objects.all()
    assistant_general_secretaries = assistant_general_secretary.objects.all()
    assistant_social_directors = assistant_social_director.objects.all()

    # Render the template with candidates for each position
    return render(request, 'vote.html', {
        'presidents': presidents,
        'vice_presidents': vice_presidents,
        'general_secretaries': general_secretaries,
        'welfare_directors': welfare_directors,
        'financial_secretaries': financial_secretaries,
        'social_directors': social_directors,
        'technical_directors': technical_directors,
        'sports_directors': sports_directors,
        'public_relations_officers': public_relations_officers,
        'treasurers': treasurers,
        'pro1s': pro1s,
        'pro2s': pro2s,
        'assistant_general_secretaries': assistant_general_secretaries,
        'assistant_social_directors': assistant_social_directors,
    })


def login_view(request):
    if request.method == 'POST':
        matric_number = request.POST.get('matric_number', '').strip()

        # Debugging: Print the matric number
        print("Matric Number:", matric_number)

        # Custom condition for allowed values
        allowed_values = ['301', '302','303', '304','305','306', '307']
        if any(value in matric_number for value in allowed_values):
            # Set the matric_number in the session
            request.session['matric_number'] = matric_number

            # Check if the user has a UserProfile instance
            try:
                user_profile = UserProfile.objects.get(matric_number=matric_number)
            except UserProfile.DoesNotExist:
                user_profile = UserProfile.objects.create(matric_number=matric_number, has_voted=False)

            # Check if the user has already voted
            if user_profile.has_voted:
                return redirect('close')  # Redirect to the end page if the user has already voted

            # Redirect to the voting page
            return redirect('vote')

        else:
            feedback_message = "You are not authorized to log in with this matric number."
            return render(request, 'next_page.html', {'feedback_message': feedback_message})

    return render(request, 'next_page.html')


def vote_submit(request):
    if request.method == 'POST':
        # Get the selected candidates' IDs from the submitted form
        president_id = request.POST.get('president')
        vice_president_id = request.POST.get('vice_president')
        general_secretary_id = request.POST.get('general_secretaries')
        welfare_director_id = request.POST.get('welfare_director')
        financial_secretary_id = request.POST.get('financial_secretary')
        social_director_id = request.POST.get('social_director')
        technical_director_id = request.POST.get('technical_director')
        sports_director_id = request.POST.get('sports_director')
        public_relations_officer_id = request.POST.get('public_relations_officer')
        treasurer_id = request.POST.get('treasurer')
        PRO1id = request.POST.get('pro1')
        PRO2id = request.POST.get('pro2')
        assistant_general_secretary_id = request.POST.get('assistant_general_secretary')
        assistant_social_director_id = request.POST.get('assistant_social_director')

        # Check if any position was left unvoted (you may want to customize this part)

        if not president_id or not vice_president_id or not general_secretary_id \
                or not welfare_director_id or not financial_secretary_id \
                or not social_director_id or not technical_director_id \
                or not sports_director_id or not public_relations_officer_id \
                or not treasurer_id or not assistant_general_secretary_id \
                or not assistant_social_director_id or not PRO1id or not PRO2id:
            return redirect('vote')

        # Record the votes in your models (you may want to handle this based on your models)
        president = President.objects.get(pk=president_id)
        president.votes += 1
        president.save()

        vice_president = Vice_President.objects.get(pk=vice_president_id)
        vice_president.votes += 1
        vice_president.save()

        general_secretary = General_Secretary.objects.get(pk=general_secretary_id)
        general_secretary.votes += 1
        general_secretary.save()

        welfare_director = Welfare_Director.objects.get(pk=welfare_director_id)
        welfare_director.votes += 1
        welfare_director.save()

        financial_secretary = Financial_Secretary.objects.get(pk=financial_secretary_id)
        financial_secretary.votes += 1
        financial_secretary.save()

        social_director = Social_Director.objects.get(pk=social_director_id)
        social_director.votes += 1
        social_director.save()

        technical_director = Technical_Director.objects.get(pk=technical_director_id)
        technical_director.votes += 1
        technical_director.save()

        sports_director = Sports_Director.objects.get(pk=sports_director_id)
        sports_director.votes += 1
        sports_director.save()

        public_relations_officer = Public_Relations_Officer.objects.get(pk=public_relations_officer_id)
        public_relations_officer.votes += 1
        public_relations_officer.save()

        treasurer = Treasurer.objects.get(pk=treasurer_id)
        treasurer.votes += 1
        treasurer.save()

        PRO1 = P_R_O1.objects.get(pk=PRO1id)
        PRO1.votes += 1
        PRO1.save()

        PRO2 = P_R_O2.objects.get(pk=PRO2id)
        PRO2.votes += 1
        PRO2.save()

        assistantgeneralsecretary = assistant_general_secretary.objects.get(pk=assistant_general_secretary_id)
        assistantgeneralsecretary.votes += 1
        assistantgeneralsecretary.save()

        assistantsocialdirector  = assistant_social_director.objects.get(pk=assistant_social_director_id)
        assistantsocialdirector.votes += 1
        assistantsocialdirector.save()

        user_profile = UserProfile.objects.get(matric_number=request.session.get('matric_number'))
        user_profile.has_voted = True
        user_profile.save()
        

        # Mark the user as voted in the UserProfile

        president_candidates = President.objects.values('name', 'votes')
        vice_president_candidates = Vice_President.objects.values('name', 'votes')
        general_secretary_candidates = General_Secretary.objects.values('name', 'votes')
        welfare_director_candidates = Welfare_Director.objects.values('name', 'votes')
        financial_secretary_candidates = Financial_Secretary.objects.values('name', 'votes')
        social_director_candidates = Social_Director.objects.values('name', 'votes')
        technical_director_candidates = Technical_Director.objects.values('name', 'votes')
        sports_director_candidates = Sports_Director.objects.values('name', 'votes')
        public_relations_officer_candidates = Public_Relations_Officer.objects.values('name', 'votes')
        treasurer_candidates = Treasurer.objects.values('name', 'votes')
        assistant_general_secretary_candidates = assistant_general_secretary.objects.values('name', 'votes')
        assistant_social_director_candidates = assistant_social_director.objects.values('name', 'votes')
        pro1_candidates = P_R_O1.objects.values('name', 'votes')
        pro2_candidates = P_R_O2.objects.values('name', 'votes')

        return render(request, 'end.html', {
            'president_candidates': president_candidates,
            'vice_president_candidates': vice_president_candidates,
            'general_secretary_candidates': general_secretary_candidates,
            'welfare_director_candidates': welfare_director_candidates,
            'financial_secretary_candidates': financial_secretary_candidates,
            'social_director_candidates': social_director_candidates,
            'technical_director_candidates': technical_director_candidates,
            'sports_director_candidates': sports_director_candidates,
            'public_relations_officer_candidates': public_relations_officer_candidates,
            'treasurer_candidates': treasurer_candidates,
            'assistant_general_secretary_candidates': assistant_general_secretary_candidates,
            'assistant_social_director_candidates': assistant_social_director_candidates,
            'pro1_candidates': pro1_candidates,
            'pro2_candidates': pro2_candidates,
        })
    
        
    # If the request method is not POST, handle it accordingly (redirect or render a different page)
    return redirect('end')  

def end(request):
        president_candidates = President.objects.values('name', 'votes')
        vice_president_candidates = Vice_President.objects.values('name', 'votes')
        general_secretary_candidates = General_Secretary.objects.values('name', 'votes')
        welfare_director_candidates = Welfare_Director.objects.values('name', 'votes')
        financial_secretary_candidates = Financial_Secretary.objects.values('name', 'votes')
        social_director_candidates = Social_Director.objects.values('name', 'votes')
        technical_director_candidates = Technical_Director.objects.values('name', 'votes')
        sports_director_candidates = Sports_Director.objects.values('name', 'votes')
        public_relations_officer_candidates = Public_Relations_Officer.objects.values('name', 'votes')
        treasurer_candidates = Treasurer.objects.values('name', 'votes')
        assistant_general_secretary_candidates = assistant_general_secretary.objects.values('name', 'votes')
        assistant_social_director_candidates = assistant_social_director.objects.values('name', 'votes')
        pro1_candidates = P_R_O1.objects.values('name', 'votes')
        pro2_candidates = P_R_O2.objects.values('name', 'votes')

        return render(request, 'end.html', {
            'president_candidates': president_candidates,
            'vice_president_candidates': vice_president_candidates,
            'general_secretary_candidates': general_secretary_candidates,
            'welfare_director_candidates': welfare_director_candidates,
            'financial_secretary_candidates': financial_secretary_candidates,
            'social_director_candidates': social_director_candidates,
            'technical_director_candidates': technical_director_candidates,
            'sports_director_candidates': sports_director_candidates,
            'public_relations_officer_candidates': public_relations_officer_candidates,
            'treasurer_candidates': treasurer_candidates,
            'assistant_general_secretary_candidates': assistant_general_secretary_candidates,
            'assistant_social_director_candidates': assistant_social_director_candidates,
            'pro1_candidates': pro1_candidates,
            'pro2_candidates': pro2_candidates,
        })