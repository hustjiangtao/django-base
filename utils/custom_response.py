# -*- coding: utf-8 -*-
# -*- author: Jiangtao -*-

from rest_framework import renderers


class JSONRenderer(renderers.JSONRenderer):

    def render(self, data, accepted_media_type=None, renderer_context=None):
        request = renderer_context['request']
        # 在此处修改data
        if 'code' not in data:
            data = {
                'code': 200,
                'message': 'ok',
                'data': data
            }
        return super().render(data, accepted_media_type=accepted_media_type, renderer_context=renderer_context)


class BrowsableAPIRenderer(renderers.BrowsableAPIRenderer):

    def get_content(self, renderer, data,
                    accepted_media_type, renderer_context):
        request = renderer_context['request']
        # 在此处修改data
        return super().get_content(renderer, data,
                                   accepted_media_type, renderer_context)