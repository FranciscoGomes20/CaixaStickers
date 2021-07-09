from django import template

register = template.Library()

@register.filter(name='addclassUsername')
def addclass(value):
    return value.as_widget(attrs={
        'class': 'input100', 
        'type': 'text', 
        'name': 'username', 
        'placeholder': 'User name'
    })

@register.filter(name='addclassPassword')
def addclass(value):
    return value.as_widget(attrs={
        'class': 'input100', 
        'type': 'password', 
        'name': 'pass', 
        'placeholder': 'Password'
    })
