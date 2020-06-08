'''
@Author: Whzcorcd
@Date: 2020-06-08 09:15:49
@LastEditors: Wzhcorcd
@LastEditTime: 2020-06-08 14:15:18
@Description: file content
'''
# coding: utf-8

import json

import requests
from sentry.plugins.bases.notify import NotificationPlugin

import sentry_wechat
from .forms import WechatOptions

Wechat_API = "https://qyapi.weixin.qq.com/cgi-bin/webhook/send?key={key}"


class WechatPlugin(NotificationPlugin):
    """
    Sentry extension to Share information to Wechat Work.
    """
    author = 'whzcorcd'
    author_url = 'https://github.com/corcd/sentry-wechat'
    version = sentry_wechat.VERSION
    description = 'Share information to Wechat Work.'
    resource_links = [
        ('Source', 'https://github.com/corcd/sentry-wechat'),
        ('Bug Tracker', 'https://github.com/corcd/sentry-wechat/issues'),
        ('README', 'https://github.com/corcd/sentry-wechat/blob/master/README.md'),
    ]

    slug = 'Wechat Wrok'
    title = 'Wechat Wrok'
    conf_key = slug
    conf_title = title
    project_conf_form = WechatOptions

    def is_configured(self, project):
        """
        Check if plugin is configured.
        """
        return bool(self.get_option('key', project))

    def notify_users(self, group, event, *args, **kwargs):
        self.post_process(group, event, *args, **kwargs)

    def post_process(self, group, event, *args, **kwargs):
        """
        Process error.
        """
        if not self.is_configured(group.project):
            return

        if group.is_ignored():
            return

        key = self.get_option('key', group.project)
        send_url = Wechat_API.format(key=key)
        title = u"New alert from {}".format(event.project.slug)

        data = {
            "msgtype": "markdown",
            "markdown": {
                "content": u"#### {title} \n > {message} [href]({url})".format(
                    title=title,
                    message=event.title or event.message,
                    url=u"{}events/{}/".format(
                        group.get_absolute_url(), event.event_id),
                )
            }
        }
        requests.post(
            url=send_url,
            headers={"Content-Type": "application/json"},
            data=json.dumps(data).encode("utf-8")
        )
