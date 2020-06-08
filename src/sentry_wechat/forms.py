# coding: utf-8

from django import forms


class WechatOptions(forms.Form):
    key = forms.CharField(
        max_length=255,
        help_text='Wechat Wrok robot webhook key'
    )
