from django import template
from django.utils.safestring import mark_safe

register = template.Library()


@register.simple_tag()
def project_list(project):
    """ Return a project html card """
    card = f'''
        <li class="list-group-item d-flex justify-content-between align-items-start">
            <a href="/project/{project.id}/">{project}</a>
            <span class="text-muted">#{project.id}</span>
        </li>
    '''
    return mark_safe(card)
