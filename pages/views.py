from django.shortcuts import render, redirect
from pages.models import Category, Subcategory, Question, Option, QuizAttempt
from users.models import Profile, StudentStats
from django.http import JsonResponse
import random
from django.core.exceptions import ObjectDoesNotExist
from django.db.models import Q
from django.contrib import messages
from django.core.mail import send_mail
from django.template.loader import render_to_string
from django.utils.html import strip_tags
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User



@login_required(login_url='loginUser')
def dashboard(request, category_id):
    # categories = Category.objects.prefetch_related('subcategory_set', 'question_set__option_set').all()
    categories = Category.objects.filter(is_active=True, created_by=request.user).prefetch_related('subcategory_set', 'question_set__option_set')
    user = request.user
    attempted_subcategories = QuizAttempt.objects.filter(user=user, subcategory__category_id=category_id).values_list('subcategory', flat=True)
    subcategories = Subcategory.objects.filter(category_id=category_id).exclude(pk__in=attempted_subcategories)
    for category in categories:
        category.attempted_subcategories = QuizAttempt.objects.filter(user=user, subcategory__category=category).values_list('subcategory', flat=True)

    context = {
        'categories': categories,
        'subcategories': subcategories,
        'category_id': category_id,

    }
    return render(request, 'pages/dashboard.html', context)

@login_required(login_url='loginUser')
def index(request, category, subcategory, user_id):
    user_id =StudentStats.objects.filter(user_id=user_id)
    if request.user.is_authenticated:
        user_id = request.user.id
        has_examed = StudentStats.objects.filter(subcategory=subcategory, user_id = user_id)
        if has_examed:
            messages.error(request, 'You already took the Exam!')
            categories = Category.objects.filter(is_active=True).prefetch_related('subcategory_set', 'question_set__option_set')
            subcategories = Subcategory.objects.all()
            studstats = StudentStats.objects.all()
            context = {
                'categories': categories,
                'studstats':studstats,
                'subcategories':subcategories
            }
            return render(request, 'users/profiles.html', context)
    questions = list(Question.objects.filter(category=category, subcategory=subcategory))

    random.shuffle(questions)
    random_questions = questions[:10]  # Change the number (10) to the desired number of random questions to display

    context = {
        'questions': random_questions,
        'category': category,
        'subcategory': subcategory,
    }
    return render(request, 'pages/index.html', context)

@login_required(login_url='loginUser')
def submit_quiz(request):
    if request.method == 'POST':
        # Process submitted answers and calculate the score
        score = 0
        answers = []
        total_questions = 0

        total_questions_str = request.POST.get('total_questions')
        total_questions = int(total_questions_str)

        for question_id in request.POST.keys():
            if question_id.startswith('q'):
                selected_option_id = request.POST.get(question_id)
                try:
                    question = Question.objects.get(id=question_id[1:])
                    selected_option = Option.objects.get(id=selected_option_id)
                except ObjectDoesNotExist:
                    # Handle the case when the Question or Option object does not exist
                    # You can display an error message or handle it based on your requirements
                    question = None
                    selected_option = None

                if question and selected_option and selected_option.is_correct:
                    score += 1

                answers.append({
                    'question': question.text if question else 'N/A',
                    'selected_option': selected_option.text if selected_option else 'N/A',
                    'is_correct': selected_option.is_correct if selected_option else False,
                    'explanation': question.explanation if question else 'N/A'
                })

        # Calculate the score percentage
        score_percentage = round((score / total_questions) * 100, 2)

        # Save the results in the database
        user_id = request.user.id
        category_id = request.POST.get('category')
        subcategory_id=request.POST.get('subcategory')
        score = score
        total_questions = total_questions
        score_percentage = score_percentage
        # Retrieve User object
        user = User.objects.get(pk=user_id)
        # If category and subcategory are optional, handle the possibility of them being None
        category = None
        if category_id:
            category = Category.objects.get(pk=category_id)

        subcategory = None
        if subcategory_id:
            subcategory = Subcategory.objects.get(pk=subcategory_id)


        # Create or update the StudentStats object
        student_stats = StudentStats.objects.create(
                    user=user,
                    name=user.profile.name,
                    category=category,
                    subcategory=subcategory,
                    score=score,
                    total_questions=total_questions,
                    score_percentage=score_percentage,
                )
        quiz_attempt = QuizAttempt.objects.create(
            user=user,
            subcategory=subcategory,
        )


        context = {
            'score': score,
            'total_questions': total_questions,
            'answers': answers,
            'score_percentage': score_percentage,
            'user': request.user,

        }
        # Render the HTML template with context
        html_message = render_to_string('pages/emailtemplate.html', context)

        # Optionally, you can strip HTML tags for a plain text alternative
        plain_message = strip_tags(html_message)

        # Sending email
        send_mail(
            'QuizApp Result',
            html_message,  # Plain text version of the email
            'balaydalakay@gmail.com',  # From email address
            ['christopheranchetaece@gmail.com'],  # To email address(es)
            html_message=html_message,  # HTML version of the email
        )
        
        messages.success(request, 'Thank you for taking the quiz! Result has been sent to your Teacher')
        return render(request, 'pages/result.html', context)

    else:
        return redirect('index')


@login_required(login_url='loginUser')
def result(request, score, total_questions, correct_answers):
    context = {
        'score': score,
        'total_questions': total_questions,
        'correct_answers': correct_answers,
        'user': request.user,
    }

    
    return render(request, 'pages/result.html', context)

def check_attempt(request):
    if request.method == 'POST' and request.is_ajax():
        category_id = request.POST.get('category_id')
        subcategory_id = request.POST.get('subcategory_id')
        user = request.user

        # Check if QuizAttempt exists for the user and subject
        attempt_exists = QuizAttempt.objects.filter(
            user=user,
            category_id=category_id,
            subcategory_id=subcategory_id
        ).exists()

        return JsonResponse({'exists': attempt_exists})

    # Return a 404 if accessed via GET or non-ajax request
    return JsonResponse({'error': 'Method not allowed'}, status=404)