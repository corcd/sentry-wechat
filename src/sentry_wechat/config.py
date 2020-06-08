'''
@Author: Whzcorcd
@Date: 2020-06-08 09:17:33
@LastEditors: Wzhcorcd
@LastEditTime: 2020-06-08 09:48:19
@Description: file content
'''
# coding: utf-8

from django import forms


class WechatOptions(forms.Form):
    key = forms.CharField(
        max_length=255,
        help_text='Wechat Wrok robot webhook key'
    )
