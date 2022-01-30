from django import template
from django.utils.safestring import mark_safe

register = template.Library()


@register.simple_tag()
def project_card(project):
    """ Return a project html card """
    card = f'''
        <div class="card mt-3">
            <div class="card-body">
                <a href="/project/{project.id}/">{project}#{project.id}</a>
            </div>
        </div>
    '''
    return mark_safe(card)
