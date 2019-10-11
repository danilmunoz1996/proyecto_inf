def base_template_name_context_processor(request):
    # Use request.user.is_authenticated() if using Django < 2.0
    if request.user.is_authenticated:
        base_template_name = 'base_loggeado.html'
    else:
        base_template_name = 'base.html'

    return {
        'base_template_name': base_template_name,
    }