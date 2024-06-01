from globetrotter.settings import SESSION_IDLE_TIMEOUT
from django.contrib.auth import logout
import datetime

class SessionIdleTimeout:
    def process_request(self, request):
        if request.user.is_authenticated():
            current_datetime = datetime.datetime.now()
            if ('inactive_time' in request.session):
                last = (current_datetime - request.session['inactivie_time']).seconds
                if last > SESSION_IDLE_TIMEOUT:
                    logout(request, 'login.html')
                else:
                    request.session['inactive_time'] = current_datetime
            return None