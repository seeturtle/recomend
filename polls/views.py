from .forms import *
from .models import *
from django.shortcuts import render, redirect, get_object_or_404


def detail(request, question_id):
    question = get_object_or_404(Question, pk=question_id)

    comments = Comment.objects.filter(
        target_question_id=question_id, reply_to_id__isnull=True)

    commentForm = CommentForm

    recommend_form = RecommendForm(request.POST or None, request.FILES or None)

    if request.method == 'POST' and recommend_form.is_valid():
        # おすすめ投稿処理
        recommend = recommend_form.save(commit=False)
        recommend.user = request.user
        recommend.question = question
        recommend.save()
        return redirect('polls:detail', question_id=question.id)

    context = {
        'question': question,
        'recommend_form': recommend_form,
        'comments': comments,
        'commentForm': commentForm
    }

    return render(request, 'polls/detail.html', context)


def post(request):
    # debug
    m = "initial"

    tag_form = TagForm
    if request.method == "POST":
        question_form = QuestionForm(request.POST)

        tag_form = TagForm(request.POST)
        if question_form.is_valid() and tag_form.is_valid():
            question = question_form.save(commit=False)
            question.user = request.user
            question.save()
            tag_form.save()
            m = "success"
        else:
            m = "failes"

    else:
        question_form = QuestionForm

    return render(request, 'polls/post.html', {'form': question_form, 'tag': tag_form, 'm': m})


def comment(request):
    if request.method == "POST":
        commentForm = CommentForm(request.POST)

        if commentForm.is_valid():

            comment = commentForm.save(commit=False)
            comment.user = request.user
            comment.target_question_id = request.POST["question_id"]

            # コメントに対するコメント時
            if "reply_to_id" in request.POST:
                comment.reply_to_id = request.POST["reply_to_id"]
            comment.save()

        # TODO
        # target_recommend_id時のコメント
    return redirect('polls:detail', question_id=request.POST["question_id"])
