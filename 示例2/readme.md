# User 

`AuthenticationForm `  (used by login() view)

`PasswordResetForm` (used bypassword_reset() view)

`SetPasswordForm` (used by password_reset_confirm() view)

`PasswordChangeForm` (used by password_change() view)



`UserCreationForm`
`UserChangeForm`
`AdminPasswordChangeForm`

`login()` (registration/login.html)
`logout()` (registration/logged_out.html) -> redirect_to_login()
`logout_then_login() `

## 两个步骤修改密码

It has `two views` for `changing passwords`:
### `password_change()` 
- (registration/password_change_form.html)
### `password_change_done()` 
- (registration/password_change_done.html)

## 四个步骤重置密码

And finally, `four views` are provided to `reset passwords`:

### `password_reset()`

- registration/password_reset_form.html
- registration/password_reset_email.html
- registration/password_reset_subject.txt
###  `password_reset_done()`
- registration/password_reset_done.html
###` password_reset_confirm()`
- registration/password_reset_confirm.html
### `password_reset_complete()`
- registration/password_reset_complete.html

## 在`settings.py`设置
djang 默认的用户url设置都在`django.contrib.auth.urls`中，一般不直接修改源码,而是修改配置文件
```python
# settings.py
... ...
from django.core.urlresolvers import reverse_lazy

LOGIN_REDIRECT_URL = '/home'
LOGIN_URL = reverse_lazy('dj-auth:login')
LOGOUT_URL = reverse_lazy('dj-auth:logout')
PASSWORD_RESET_TIMEOUT_DAYS = 7
```

完整的示例:https://github.com/macropin/django-registration

# Permission

# Group



