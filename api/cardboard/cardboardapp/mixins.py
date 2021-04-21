from django.contrib.auth.mixins import UserPassesTestMixin


class OnlyYouMixin(UserPassesTestMixin):
    raise_exception = True # 制限に引っかかった場合に例外を発生させる

    def test_func(self): # TrueかFalseを返す
        user = self.request.user # ユーザーのインスタンス
        return user.pk == self.kwargs['pk'] # ユーザーのPKとページのPKを比較