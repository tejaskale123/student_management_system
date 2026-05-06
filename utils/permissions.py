def is_admin(user):
    return (
        user.is_superuser or
        user.is_staff or
        user.groups.filter(name__iexact='Admin').exists()
    )

def is_teacher(user):
    return user.groups.filter(
        name__iexact='Teacher'
    ).exists()
