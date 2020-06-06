import requests
from django.http import Http404
import json
from django.conf import settings
from markdown import Markdown
from io import StringIO


def get_root(extracted, subdomain):
    if extracted.suffix:
        return f"http://{subdomain}.{extracted.domain}.{extracted.suffix}"
    else:
        return f"http://{subdomain}.{extracted.domain}:8000"


def get_base_root(extracted):
    if extracted.suffix:
        return f"https://{extracted.domain}.{extracted.suffix}"
    else:
        return f"http://{extracted.domain}:8000"


def get_nav(all_posts):
    return list(filter(lambda post: post.is_page, all_posts))


def get_posts(all_posts):
    return list(filter(lambda post: not post.is_page, all_posts))


def get_post(all_posts, slug):
    try:
        return list(filter(lambda post: post.slug == slug, all_posts))[0]
    except IndexError:
        raise Http404("No Post matches the given query.")


def is_protected(subdomain):
    protected_subdomains = [
        'login',
        'www',
        'api',
        'signup',
        'signin',
        'profile',
        'register',
        'post',
        'http',
        'https',
        'account',
        'router',
        'settings',
    ]

    return subdomain in protected_subdomains


def add_new_domain(domain):
    url = "https://api.heroku.com/apps/stormy-island-54830/domains"
    print(domain," about to add")

    payload = {
        "hostname": domain
    }

    headers = {
        'content-type': "application/json",
        'accept': "application/vnd.heroku+json; version=3",
        'authorization': f'Bearer {settings.HEROKU_BEARER_TOKEN}',
    }

    response = requests.request(
        "POST", url, data=json.dumps(payload), headers=headers)

    print(response.text," Add")

    return id


def delete_domain(domain):
    url = f"https://api.heroku.com/apps/stormy-island-54830/domains/{domain}"

    payload = {
        "hostname": domain
    }

    headers = {
        'content-type': "application/json",
        'accept': "application/vnd.heroku+json; version=3",
        'authorization': f'Bearer {settings.HEROKU_BEARER_TOKEN}',
    }

    response = requests.request(
        "DELETE", url, data=json.dumps(payload), headers=headers)

    print(response.text)


def unmark_element(element, stream=None):
    if stream is None:
        stream = StringIO()
    if element.text:
        stream.write(element.text)
    for sub in element:
        unmark_element(sub, stream)
    if element.tail:
        stream.write(element.tail)
    return stream.getvalue()


# patching Markdown
Markdown.output_formats["plain"] = unmark_element
__md = Markdown(output_format="plain")
__md.stripTopLevelTags = False


def unmark(text):
    return __md.convert(text)
