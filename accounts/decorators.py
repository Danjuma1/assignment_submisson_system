from django.core.exceptions import PermissionDenied


def user_is_student(function):
    """
    :param function:
    :return: USER PERMISSION WITH STUDENT ROLE
    """
    def wrap(request, *args, **kwargs):
        user = request.user
        if user.role == 'student':
            return function(request, *args, **kwargs)
        else:
            raise PermissionDenied

    return wrap


def user_is_lecturer(function):
    """
    :param function:
    :return: USER PERMISSION WITH LECTURER ROLE
    """
    def wrap(request, *args, **kwargs):
        user = request.user
        if user.role == 'lecturer':
            return function(request, *args, **kwargs)
        else:
            raise PermissionDenied

    return wrap