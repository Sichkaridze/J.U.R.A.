from task_manager.forms import SearchForm


class SearchMixin():
    QUERY_FIELDS = []

    def get_queryset(self):
        queryset = super().get_queryset()
        search_query = self.request.GET.get("query", "")
        search_field = self.request.GET.get("field", None)

        if search_field not in self.QUERY_FIELDS and self.QUERY_FIELDS:
            search_field = self.QUERY_FIELDS[0]

        if search_query:
            queryset = queryset.filter(**{f"{search_field}__icontains": search_query}).distinct()
        return queryset

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["search_form"] = SearchForm(self.request.GET)
        context["allowed_fields"] = self.QUERY_FIELDS
        return context
