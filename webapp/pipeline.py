from social_core.pipeline.partial import partial
from django.shortcuts import render, redirect
from Accounts.models import *

@partial
def require_infos(strategy, details, user=None, is_new=False, *args, **kwargs):
        current_partial = kwargs.get('current_partial')

        if is_new:
            print(details['email'])
            return redirect(
                '/register?partial_token={0}'.format(current_partial.token)
            )
        else:
            return redirect(
                '/social-auth?partial_token={0}'.format(current_partial.token)
            )
