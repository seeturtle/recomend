from django.contrib import messages

from .forms import *
from .models import *
from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponseForbidden


def detail(request, question_id):
    question = get_object_or_404(Question, pk=question_id)

    comments = Comment.objects.filter(
        target_question_id=question_id, reply_to_id__isnull=True)

    comment_form = CommentForm

    recommend_form = RecommendForm(request.POST or None, request.FILES or None)

    if request.method == 'POST' and recommend_form.is_valid():
        # おすすめ投稿処理
        if question.user == request.user:
            messages.error(request, '自分の質問には投稿できません')
            return redirect('polls:detail', question_id=question.id)
        recommend = recommend_form.save(commit=False)
        recommend.user = request.user
        recommend.question = question
        recommend.save()
        return redirect('polls:detail', question_id=question.id)

    context = {
        'question': question,
        'recommend_form': recommend_form,
        'comments': comments,
        'comment_form': comment_form,
        'best_recommend': question.recommend_set.filter(is_best=True).first(),
        'recommends': question.recommend_set.filter(is_best=False),
        'all_tags': list(map(lambda tag: tag.name, Tag.objects.all())),
    }

    return render(request, 'polls/detail.html', context)


def set_best_recommend(request, question_id, recommend_id):
    question = get_object_or_404(Question, pk=question_id)
    if question.user != request.user:
        return HttpResponseForbidden()

    best_recommend = get_object_or_404(Recommend, pk=recommend_id)

    if request.method == 'POST':
        old_best_recommend = Recommend.objects.filter(is_best=True).first()
        if old_best_recommend:
            old_best_recommend.is_best = False
            old_best_recommend.save()
        best_recommend.is_best = True
        best_recommend.save()

    return redirect('polls:detail', question_id=question_id)


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


def add_tag(request, question_id):
    """
    タグの追加
    質問とタグを関連付ける
    同じ名前のタグがない場合は新規作成
    """
    question = get_object_or_404(Question, pk=question_id)
    if question.user != request.user:
        messages.error(request, 'タグ追加は質問者のみ可能です')
        return redirect('polls:detail', question_id=question_id)
    tag, created = Tag.objects.get_or_create(name=request.POST.get('tag_name'))
    if tag not in question.tags.all():
        question.tags.add(tag)

    return redirect('polls:detail', question_id=question_id)


def delete_tag(request, question_id, tag_id):
    """
    タグの削除
    質問とタグの関連を削除する
    タグと関連する質問がない場合はタグ自体を削除
    """
    tag = get_object_or_404(Tag, pk=tag_id)
    question = get_object_or_404(Question, pk=question_id)
    if question.user != request.user:
        messages.error(request, 'タグ削除は質問者のみ可能です')
        return redirect('polls:detail', question_id=question_id)
    question.tags.remove(tag)
    if not tag.question_set.exists():
        tag.delete()

    return redirect('polls:detail', question_id=question_id)
