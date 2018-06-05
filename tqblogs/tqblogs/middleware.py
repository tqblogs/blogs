
from django.utils.deprecation import MiddlewareMixin


# 获取真实ip地址
class  SetRemoteGetRealIp(MiddlewareMixin):

    def process_request(self, request):
        try:
            real_ip = request.META['HTTP_X_FORWARDED_FOR']
        except KeyError:
            pass
        else:
            real_ip = real_ip.split(",")[0]
            request.META['REMOTE_ADDR'] = real_ip