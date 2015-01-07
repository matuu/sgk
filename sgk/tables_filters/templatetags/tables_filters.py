from django import template

register = template.Library()


def render_table_filtered(context, table_data=None, filter_data=None, can_add_new=True):
    if table_data is not None:
        filter_qs = table_data
    else:
        filter_qs = context["filter_qs"]
    if filter_data is not None:
        filter1 = filter_data
    else:
        filter1 = context["filter"]
    actions = context["actions"]
    request = context["request"]
    return {'filter': filter1,
            'filter_qs': filter_qs,
            'actions': actions,
            'request': request,
            'model_prefix': filter_qs.Meta.model.__name__.lower(),
            'can_add_new': can_add_new
            }

# Register the custom tag as an inclusion tag with takes_context=True.
register.inclusion_tag('tables_filters/tables_filters.html',
                       takes_context=True)(render_table_filtered)


@register.assignment_tag
def get_nearby_page(page):
    """
    Return a range of pages number nearby to current page.
    """
    current = page.number
    page_range = page.paginator.page_range
    total_pages = len(page_range)
    if(total_pages < 6):
        return page_range
    else:
        if not page.has_previous() or current - 1 == 1:
            return page_range[:5]
        elif not page.has_next() or current + 1 == total_pages:
            return page_range[-5:]
        else:
            aux_range = page_range[current - 3:-(total_pages - (current + 2))]
            if aux_range:
                return aux_range
        # It should never passed by here
        return None
