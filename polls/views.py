from django.shortcuts import render,  redirect, get_object_or_404
from .models import *
from .forms import *


def detail(request, question_id):
    question = get_object_or_404(Question, pk=question_id)

    comments = Comment.objects.filter(
        target_question_id=question_id, reply_to_id__isnull=True)

    commentForm = CommentForm
    return render(request, 'polls/detail.html', {'question': question, 'comments': comments, 'commentForm': commentForm})


def post(request):
    # debug
    m = "initial"

    tagForm = TagForm
    if request.method == "POST":
        questionForm = QuestionForm(request.POST)

        tagForm = TagForm(request.POST)
        if questionForm.is_valid() and tagForm.is_valid():
            question = questionForm.save(commit=False)
            question.user = request.user
            question.save()
            tagForm.save()
            m = "success"
        else:
            m = "failes"

    else:
        questionForm = QuestionForm

    return render(request, 'polls/post.html', {'form': questionForm, 'tag': tagForm, 'm': m})


def comment(request):

    if request.method == "POST":
        commentForm = CommentForm(request.POST)

        if commentForm.is_valid():

            comment = commentForm.save(commit=False)
            comment.user = request.user
            comment.target_question_id = request.POST["question_id"]

            # コメントに対するコメント時
            if request.POST["reply_to_id"]:
                comment.reply_to_id = request.POST["reply_to_id"]
            comment.save()

        # TODO
        # target_recommend_id時のコメント

    return redirect('polls:detail', question_id=request.POST["question_id"])
