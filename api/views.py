import json

import requests
from django.http import HttpResponse
from django.views.generic import View

BASE_URL = "https://jsonplaceholder.typicode.com/{}"

""" Create your views here. """


class TopPostView(View):

    def get(self, request):
        try:
            posts = requests.get(BASE_URL.format("posts")).json() or []
            comments = requests.get(BASE_URL.format("comments")).json() or []

            posts = sorted(
                [
                    {
                        "post_id": post['id'],
                        "post_title": post['title'],
                        "post_body": post['body'],
                        "total_number_of_comments": len([c for c in comments if c['postId'] == post['id']])
                    } for post in posts
                ],
                key=lambda p: p['total_number_of_comments']
            )

            # from highest to lowest
            posts.reverse()
            return http_reply({"posts": posts[:10]})

        except Exception as e:
            print('Oopsi...', e.args)

        return http_reply({"posts": []})


class FilterSearchView(View):

    def get(self, request):
        try:
            field = request.GET.get('field', '')
            value = request.GET.get('value', '')

            if not (field and value):
                return http_reply({"comments": []})

            comments = requests.get(BASE_URL.format("comments")).json() or []
            c_keys = comments[0].keys()

            if field in c_keys:
                comments = [comment for comment in comments if str(comment[field]).lower() == str(value).lower()]
                return http_reply({"comments": comments})

            return http_reply({"comments": []})

        except Exception as e:
            print('Oopsi...', e.args)

        return http_reply({"comments": []})


def http_reply(data):
    return HttpResponse(
        json.dumps(data),
        content_type='application/json'
    )
